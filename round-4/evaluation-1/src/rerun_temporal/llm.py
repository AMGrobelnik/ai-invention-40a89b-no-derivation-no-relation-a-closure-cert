#!/usr/bin/env python3
"""Async OpenRouter client: disk cache, hard cost-guard, concurrency, robust parsing.

* All calls go through OpenRouter `/chat/completions` (temperature 0, deterministic).
* Every (model, system, user) is sha256-keyed to a JSON file in ./cache/ -> reruns and
  duplicate prompts NEVER re-bill.
* A cumulative cost tracker aborts (BudgetExceeded) before the hard cap is crossed.
* Robust relation parsing maps synonyms to the coarse vocab; parse failures are treated
  as UNDERDETERMINED (universal) so they lower closure bite, not recall artificially.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import re
from pathlib import Path

import httpx
from loguru import logger

API_URL = "https://openrouter.ai/api/v1/chat/completions"

# synonym -> coarse vocab
_SYN = {
    "before": "before", "precedes": "before", "prior": "before", "earlier": "before",
    "b": "before", "preceding": "before",
    "after": "after", "follows": "after", "later": "after", "succeeds": "after",
    "a": "after", "following": "after",
    "includes": "includes", "contains": "includes", "encloses": "includes",
    "i": "includes", "include": "includes",
    "is_included": "is_included", "included": "is_included", "during": "is_included",
    "within": "is_included", "contained": "is_included", "ii": "is_included",
    "is included": "is_included", "is-included": "is_included",
    "simultaneous": "simultaneous", "equal": "simultaneous", "equals": "simultaneous",
    "same": "simultaneous", "coincides": "simultaneous", "concurrent": "simultaneous",
    "s": "simultaneous", "simultaneously": "simultaneous", "co-occurs": "simultaneous",
}
_UNDET = {"underdetermined", "undetermined", "vague", "unknown", "universal", "none",
          "any", "indeterminate", "all", "unclear", "ambiguous"}


class BudgetExceeded(Exception):
    pass


def parse_relations(content: str, vocab: list[str]):
    """Return (coarse_labels:list, underdetermined:bool, parse_fail:bool)."""
    if not content:
        return [], True, True
    txt = content.strip()
    # strip code fences
    txt = re.sub(r"^```(?:json)?|```$", "", txt, flags=re.M).strip()
    obj = None
    # try direct json, then first {...} block
    for cand in (txt, _first_json_block(txt)):
        if cand is None:
            continue
        try:
            obj = json.loads(cand)
            break
        except Exception:
            continue
    tokens = []
    underdet = False
    if isinstance(obj, dict):
        underdet = bool(obj.get("underdetermined", False))
        rels = obj.get("relations", obj.get("relation", []))
        tokens = _extract_tokens(rels)
    elif isinstance(obj, list):
        tokens = _extract_tokens(obj)
    else:
        # regex fallback: scan for known relation words
        low = txt.lower()
        for w in list(_SYN) + list(_UNDET):
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                tokens.append(w)
        if not tokens:
            return [], True, True

    coarse = []
    for t in tokens:
        tl = str(t).strip().lower().replace(" ", "_")
        if tl in _UNDET:
            underdet = True
            continue
        # try normalized + raw
        c = _SYN.get(tl) or _SYN.get(str(t).strip().lower())
        if c:
            coarse.append(c)
    # keep only vocab-relevant labels (includes/is_included allowed on POINT via mapping)
    coarse = [c for c in dict.fromkeys(coarse)]
    if underdet or not coarse:
        return coarse, True, False
    return coarse, False, False


def _extract_tokens(rels):
    out = []
    if isinstance(rels, str):
        return [rels]
    if isinstance(rels, list):
        for r in rels:
            if isinstance(r, str):
                out.append(r)
            elif isinstance(r, dict):
                for k in ("relation", "rel", "label", "type"):
                    if k in r:
                        out.append(r[k]); break
    elif isinstance(rels, dict):
        for k in ("relation", "rel", "label", "type"):
            if k in rels:
                out.append(rels[k])
    return out


def _first_json_block(txt: str):
    start = txt.find("{")
    if start < 0:
        return None
    depth = 0
    for i in range(start, len(txt)):
        if txt[i] == "{":
            depth += 1
        elif txt[i] == "}":
            depth -= 1
            if depth == 0:
                return txt[start:i + 1]
    return None


class OpenRouterClient:
    def __init__(self, api_key: str, model: str, fallbacks: list[str], cache_dir: Path,
                 temperature: float = 0.0, budget_hard: float = 9.0, budget_soft: float = 2.0,
                 concurrency: int = 12, max_tokens: int = 220, timeout: float = 90.0):
        self.api_key = api_key
        self.model = model
        self.fallbacks = list(fallbacks)
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.temperature = temperature
        self.budget_hard = budget_hard
        self.budget_soft = budget_soft
        self.concurrency = concurrency
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.cost = 0.0
        self.n_calls = 0
        self.n_cache_hits = 0
        self.n_parse_fail = 0
        self.n_errors = 0
        self.soft_warned = False
        self._active_model = model

    def _key(self, system: str, user: str) -> str:
        # max_tokens is part of the key: a reasoning model truncated at a low cap returns
        # EMPTY content; bumping the cap must NOT replay the poisoned low-cap cache entry.
        h = hashlib.sha256(
            f"{self._active_model}\x00{self.temperature}\x00{self.max_tokens}\x00{system}\x00{user}"
            .encode()).hexdigest()
        return h

    def _cache_path(self, key: str) -> Path:
        return self.cache_dir / f"{key}.json"

    _EV_N_MISS = 0  # EVAL-INJECT: class-level cache-miss counter (R1 $0 verification)

    def _read_cache(self, key: str):
        p = self._cache_path(key)
        if p.exists():
            try:
                return json.loads(p.read_text())
            except Exception:
                OpenRouterClient._EV_N_MISS += 1
                return None
        OpenRouterClient._EV_N_MISS += 1
        return None

    def _write_cache(self, key: str, payload: dict):
        try:
            self._cache_path(key).write_text(json.dumps(payload))
        except Exception as e:
            logger.warning(f"cache write failed: {e}")

    async def _post(self, client: httpx.AsyncClient, model: str, system: str, user: str):
        body = {
            "model": model,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }
        r = await client.post(API_URL, json=body,
                              headers={"Authorization": f"Bearer {self.api_key}",
                                       "Content-Type": "application/json"})
        r.raise_for_status()
        return r.json()

    async def call(self, client: httpx.AsyncClient, sem: asyncio.Semaphore,
                   system: str, user: str):
        """Return dict {content, cost, cached, model}. Raises BudgetExceeded if hard cap hit."""
        key = self._key(system, user)
        cached = self._read_cache(key)
        if cached is not None:
            self.n_cache_hits += 1
            cached = dict(cached); cached["cached"] = True
            return cached
        if self.cost >= self.budget_hard:
            raise BudgetExceeded(f"cumulative ${self.cost:.4f} >= hard cap ${self.budget_hard}")
        async with sem:
            if self.cost >= self.budget_hard:
                raise BudgetExceeded(f"cumulative ${self.cost:.4f} >= hard cap ${self.budget_hard}")
            models = [self._active_model] + [m for m in self.fallbacks if m != self._active_model]
            last_err = None
            for attempt, model in enumerate(_with_retries(models)):
                try:
                    data = await self._post(client, model, system, user)
                    content = data["choices"][0]["message"]["content"]
                    usage = data.get("usage", {}) or {}
                    cost = float(usage.get("cost", 0.0) or 0.0)
                    self.cost += cost
                    self.n_calls += 1
                    payload = {"content": content, "cost": cost, "cached": False, "model": model,
                               "usage": {"in": usage.get("prompt_tokens"), "out": usage.get("completion_tokens")}}
                    self._write_cache(key, payload)
                    if (not self.soft_warned) and self.cost >= self.budget_soft:
                        self.soft_warned = True
                        logger.warning(f"soft budget ${self.budget_soft} crossed (cost=${self.cost:.4f})")
                    return payload
                except httpx.HTTPStatusError as e:
                    last_err = e
                    code = e.response.status_code
                    if code in (429, 500, 502, 503, 524):
                        await asyncio.sleep(1.5 * (attempt + 1))
                        continue
                    # permanent error for this model -> try next model
                    logger.warning(f"model {model} HTTP {code}; trying next")
                    continue
                except Exception as e:
                    last_err = e
                    await asyncio.sleep(1.0 * (attempt + 1))
                    continue
            self.n_errors += 1
            logger.error(f"all model attempts failed: {last_err}")
            # treat as universal/underdetermined; do NOT cache (so a rerun can retry)
            return {"content": "", "cost": 0.0, "cached": False, "model": None, "error": str(last_err)}

    async def run_batch(self, items: list[dict]):
        """items: [{id, system, user}]. Returns {id: payload}. Stops issuing new calls on
        BudgetExceeded but returns whatever completed (cached results always available)."""
        sem = asyncio.Semaphore(self.concurrency)
        results: dict = {}
        limits = httpx.Limits(max_connections=self.concurrency + 4, max_keepalive_connections=self.concurrency + 4)
        async with httpx.AsyncClient(timeout=self.timeout, limits=limits) as client:
            async def one(it):
                try:
                    results[it["id"]] = await self.call(client, sem, it["system"], it["user"])
                except BudgetExceeded:
                    results.setdefault(it["id"], {"content": "", "cost": 0.0, "cached": False,
                                                  "model": None, "budget_skipped": True})
            # schedule sequentially-awarish so budget guard can stop the tail
            await asyncio.gather(*(one(it) for it in items))
        return results

    def stats(self) -> dict:
        return {"cumulative_usd": round(self.cost, 6), "n_llm_calls": self.n_calls,
                "n_cache_hits": self.n_cache_hits, "n_parse_fail": self.n_parse_fail,
                "n_errors": self.n_errors, "model": self.model, "fallbacks": self.fallbacks,
                "temperature": self.temperature, "budget_hard": self.budget_hard,
                "budget_soft": self.budget_soft}


def _with_retries(models: list[str], retries_per: int = 2):
    """Yield models with per-model retry slots (transient errors re-enter the same model)."""
    seq = []
    for m in models:
        for _ in range(retries_per):
            seq.append(m)
    return seq
