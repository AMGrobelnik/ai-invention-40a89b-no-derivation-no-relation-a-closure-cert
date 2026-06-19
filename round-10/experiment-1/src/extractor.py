#!/usr/bin/env python3
"""iter-10 PRECISION-PRESERVING SUPERVISED located_in extractor.

This is the ONLY new modelling component of iter-10. It REPLACES the refuted prompt-only
LLM extraction (iter-9 PATH-2, whose recall was precision-bought: CI-lower-vs-recall slope
-0.30 located-in / -0.67 kinship) with a TRAINED, threshold-tunable, precision-preserving
binary located_in classifier over GOLD-MENTION ENTITY PAIRS. Because it works directly over
gold entity_ids there is NO grounding step and NO grounding loss; the extracted edges are
already keyed by entity_id and feed B.predict_symbolic unchanged.

The task: binary located_in(i,j) over ORDERED gold-entity pairs (i,j) that co-occur within a
W-sentence window. located_in(i,j) means "i is located in / part of / an administrative
subdivision of j". The engine seeds the converse (contains) itself, so we emit only
type='located_in' edges. At a threshold tau we keep candidates with calibrated
P(located_in) >= tau; directed 2-cycles on one unordered pair are resolved by keeping the
higher-probability direction (the certificate would otherwise see a conflicting both-ways
containment).

TWO interchangeable supervised families (both expose extract_supervised(ctx, tau)):
  (A) GBDTExtractor   -- calibrated LightGBM (fallback: GradientBoosting/LogReg) over ~30
                         engineered per-pair features. CPU, robust, isotonic-calibrated so a
                         threshold maps monotonically to precision. PRIMARY workhorse.
  (B) EncoderExtractor -- fine-tuned compact encoder (microsoft/deberta-v3-small, GPU) over the
                         minimal text window around the closest co-occurring mention pair with
                         entity markers [E1]..[/E1] / [E2]..[/E2]. A SECOND, independent
                         supervised family; agreement on the fork verdict across families is
                         stronger evidence than a single extractor.

Candidate enumeration is IDENTICAL at train and eval (build_doc_candidates). Labels (train):
pos = (i,j) is a gold atomic_edge (source=i,target=j); reverse and all other window pairs are
negative. Heavy class imbalance is handled by class weights, not by changing the eval-time
candidate set.
"""
from __future__ import annotations

import ctypes
import glob
import math
import re
import warnings
from collections import defaultdict
from pathlib import Path

import numpy as np
from loguru import logger

warnings.filterwarnings("ignore", message="X does not have valid feature names")


def _preload_libgomp():
    """LightGBM dlopens libgomp.so.1; preload it (RTLD_GLOBAL) from torch / scikit-learn / extra_libs
    so `import lightgbm` works WITHOUT a manual LD_LIBRARY_PATH (e.g. under `uv run method.py`)."""
    here = Path(__file__).resolve().parent
    pats = [str(here / ".venv/lib/python*/site-packages/torch/lib/libgomp-*.so*"),
            str(here / ".venv/lib/python*/site-packages/scikit_learn.libs/libgomp-*.so*"),
            str(here / "extra_libs/libgomp.so*")]
    for pat in pats:
        for cand in sorted(glob.glob(pat)):
            try:
                ctypes.CDLL(cand, mode=ctypes.RTLD_GLOBAL)
                return cand
            except OSError:
                continue
    return None


_preload_libgomp()

import readers_locatedin as R

# --------------------------------------------------------------------------- #
# Cue vocabularies (reused from the located-in reader's surface-synonym map)
# --------------------------------------------------------------------------- #
_LOCIN_CUES = sorted({k.lower() for k, v in R._SURF_SYN.items() if v == "located in" and len(k) >= 2},
                     key=len, reverse=True)
_CONTAINS_CUES = sorted({k.lower() for k, v in R._SURF_SYN.items() if v == "contains" and len(k) >= 2},
                        key=len, reverse=True)
_LOCIN_RE = [re.compile(r"\b" + re.escape(c) + r"\b") for c in _LOCIN_CUES]
_CONTAINS_RE = [re.compile(r"\b" + re.escape(c) + r"\b") for c in _CONTAINS_CUES]
_SENT_BOUND = re.compile(r"[.!?]+(?=\s|$)")
_TOKEN = re.compile(r"[A-Za-z0-9]+")

_ADMIN_ORD = {"city": 1.0, "town": 1.0, "region": 2.0, "province": 2.0, "state": 2.0,
              "country": 3.0, "other": 0.0, None: 0.0, "": 0.0}

# fixed feature order (stable X columns)
FEATURE_NAMES = [
    "min_sent_dist", "same_sent", "adjacent_sent", "char_gap_norm", "i_before_j",
    "locin_between", "contains_between", "locin_window", "contains_window",
    "dir_locin_support", "dir_contains_support",
    "paren_pattern", "comma_pattern",
    "admin_i", "admin_j", "admin_diff", "admin_i_known", "admin_j_known",
    "i_token_in_j", "j_token_in_i", "token_jaccard",
    "n_ment_i", "n_ment_j", "deg_i", "deg_j",
    "len_tok_i", "len_tok_j", "len_diff",
    "n_loc_nodes", "between_len_norm",
]
N_FEATURES = len(FEATURE_NAMES)


# --------------------------------------------------------------------------- #
# Sentence indexing
# --------------------------------------------------------------------------- #
def sentence_spans(text: str) -> list[tuple[int, int]]:
    """List of (start, end) char spans, one per sentence (regex on .!? + whitespace)."""
    spans = []
    start = 0
    for m in _SENT_BOUND.finditer(text or ""):
        end = m.end()
        if end > start:
            spans.append((start, end))
        start = end
    if start < len(text or ""):
        spans.append((start, len(text)))
    if not spans:
        spans = [(0, len(text or ""))]
    return spans


def _sent_of(offset: int, spans: list[tuple[int, int]]) -> int:
    for i, (a, b) in enumerate(spans):
        if a <= offset < b:
            return i
    if offset < spans[0][0]:
        return 0
    return len(spans) - 1


# --------------------------------------------------------------------------- #
# Candidate enumeration (IDENTICAL at train & eval)
# --------------------------------------------------------------------------- #
def _entity_mentions(ctx: dict, spans):
    """entity_id -> list of (cs, ce, sent_idx), only LOC nodes with >=1 valid mention span."""
    text = ctx["text"]
    gg = ctx["gg"]
    out = {}
    for n in gg["nodes"]:
        eid = n["entity_id"]
        ms = []
        for sp in n.get("mention_spans", []):
            try:
                cs, ce = int(sp[0]), int(sp[1])
            except (TypeError, ValueError, IndexError):
                continue
            if 0 <= cs < ce <= len(text):
                ms.append((cs, ce, _sent_of(cs, spans)))
        if not ms:
            # fall back to the surface's first occurrence so isolated nodes still enumerate
            s = n.get("surface")
            if s:
                idx = text.find(s)
                if idx >= 0:
                    ms.append((idx, idx + len(s), _sent_of(idx, spans)))
        if ms:
            out[eid] = ms
    return out


def _closest_pair(ms_i, ms_j):
    """Closest (mention_i, mention_j) by (sentence distance, char gap)."""
    best = None
    best_key = None
    for (ai, bi, si) in ms_i:
        for (aj, bj, sj) in ms_j:
            sd = abs(si - sj)
            gap = aj - bi if aj >= bi else (ai - bj if ai >= bj else 0)
            gap = abs(gap)
            key = (sd, gap)
            if best_key is None or key < best_key:
                best_key = key
                best = (ai, bi, si, aj, bj, sj, sd, gap)
    return best


def _cue_counts(window_text: str):
    lt = window_text.lower()
    nloc = sum(1 for rx in _LOCIN_RE if rx.search(lt))
    ncon = sum(1 for rx in _CONTAINS_RE if rx.search(lt))
    return nloc, ncon


def _tokens(s: str):
    return _TOKEN.findall((s or "").lower())


def build_doc_candidates(ctx: dict, window: int = 2, cap: int = 400) -> list[dict]:
    """Enumerate ordered gold-entity candidate pairs (i,j) whose mentions co-occur within
    `window` sentences. Returns deterministic list of {i, j, feat:np.array, sent_dist}.
    Cap by ascending min-sentence-distance (then by entity ids) so dense docs can't explode."""
    text = ctx["text"]
    spans = sentence_spans(text)
    ment = _entity_mentions(ctx, spans)
    ids = sorted(ment.keys())
    n_nodes = len(ids)
    # co-occurrence degree within window (undirected) for deg features
    deg = defaultdict(int)
    cooc_pairs = []
    for a_idx in range(n_nodes):
        for b_idx in range(a_idx + 1, n_nodes):
            i, j = ids[a_idx], ids[b_idx]
            cp = _closest_pair(ment[i], ment[j])
            if cp is None:
                continue
            if cp[6] <= window:
                deg[i] += 1
                deg[j] += 1
                cooc_pairs.append((i, j, cp))
    id2node = {n["entity_id"]: n for n in ctx["gg"]["nodes"]}
    cands = []
    for (i, j, cp) in cooc_pairs:
        for (a, b) in ((i, j), (j, i)):
            feat = _featurize_pair(text, spans, a, b, ment, deg, id2node, n_nodes,
                                   forced_cp=(cp if a == i else None))
            cands.append({"i": a, "j": b, "feat": feat, "sent_dist": cp[6]})
    # deterministic cap
    cands.sort(key=lambda c: (c["sent_dist"], str(c["i"]), str(c["j"])))
    if len(cands) > cap:
        cands = cands[:cap]
    return cands


def _featurize_pair(text, spans, i, j, ment, deg, id2node, n_nodes, forced_cp=None):
    """Build the ordered-pair feature vector for predicting located_in(i,j)."""
    ms_i, ms_j = ment[i], ment[j]
    cp = _closest_pair(ms_i, ms_j) if forced_cp is None else forced_cp
    ai, bi, si, aj, bj, sj, sd, gap = cp
    i_before = 1.0 if ai < aj else 0.0
    # between text (strictly between the two closest mentions) + sentence window
    lo_end = min(bi, bj)
    hi_start = max(ai, aj)
    between = text[lo_end:hi_start] if hi_start > lo_end else ""
    s_lo = min(si, sj)
    s_hi = max(si, sj)
    win_a = spans[s_lo][0]
    win_b = spans[min(s_hi, len(spans) - 1)][1]
    window_text = text[win_a:win_b]
    locb, conb = _cue_counts(between)
    locw, conw = _cue_counts(window_text)
    # direction-aware cue support for located_in(i,j):
    #  if i precedes j, a located_in cue between them ("i in j") supports located_in(i,j);
    #  if j precedes i, a contains cue ("j contains i") supports located_in(i,j).
    if i_before:
        dir_loc = float(locb)
        dir_con = float(conb)        # contains between (i before j) would support contains(i,j)=located_in(j,i)
    else:
        dir_loc = float(conb)
        dir_con = float(locb)
    paren = 1.0 if ("(" in between and gap <= 6) else 0.0
    comma = 1.0 if between.strip().startswith(",") else 0.0
    ni = id2node.get(i, {})
    nj = id2node.get(j, {})
    adi = _ADMIN_ORD.get(ni.get("admin_level"), 0.0)
    adj = _ADMIN_ORD.get(nj.get("admin_level"), 0.0)
    adi_known = 1.0 if ni.get("admin_level") in ("city", "town", "region", "province", "state", "country") else 0.0
    adj_known = 1.0 if nj.get("admin_level") in ("city", "town", "region", "province", "state", "country") else 0.0
    ti = set(_tokens(ni.get("surface", "")))
    tj = set(_tokens(nj.get("surface", "")))
    i_in_j = 1.0 if (ti and ti <= tj) else 0.0
    j_in_i = 1.0 if (tj and tj <= ti) else 0.0
    jac = (len(ti & tj) / len(ti | tj)) if (ti | tj) else 0.0
    feat = [
        float(sd),                                   # min_sent_dist
        1.0 if sd == 0 else 0.0,                     # same_sent
        1.0 if sd <= 1 else 0.0,                     # adjacent_sent
        min(1.0, gap / 200.0),                       # char_gap_norm
        i_before,                                    # i_before_j
        float(locb), float(conb), float(locw), float(conw),
        dir_loc, dir_con,
        paren, comma,
        adi, adj, adj - adi, adi_known, adj_known,
        i_in_j, j_in_i, jac,
        float(len(ms_i)), float(len(ms_j)),
        float(deg.get(i, 0)), float(deg.get(j, 0)),
        float(len(ti)), float(len(tj)), float(len(ti) - len(tj)),
        float(n_nodes), min(1.0, len(between) / 200.0),
    ]
    return np.asarray(feat, dtype=np.float32)


# --------------------------------------------------------------------------- #
# Training-data assembly (shared by both families)
# --------------------------------------------------------------------------- #
def _gold_pos_set(ctx: dict) -> set:
    """Directed gold located_in pairs (source,target) for this doc."""
    pos = set()
    for e in ctx["gg"].get("atomic_edges", []):
        if e.get("primitive") == "located_in":
            pos.add((e["source"], e["target"]))
    return pos


def assemble_training(contexts: dict, window: int = 2, cap: int = 400):
    """Build (X, y, groups, cand_meta) over all train docs. y[k]=1 iff candidate (i,j) is a
    directed gold located_in edge. groups = doc_id (for optional grouped CV)."""
    X, y, groups, meta = [], [], [], []
    n_pos = 0
    for did, ctx in contexts.items():
        pos = _gold_pos_set(ctx)
        cands = build_doc_candidates(ctx, window=window, cap=cap)
        for c in cands:
            lab = 1 if (c["i"], c["j"]) in pos else 0
            X.append(c["feat"])
            y.append(lab)
            groups.append(did)
            meta.append((did, c["i"], c["j"]))
            n_pos += lab
    if not X:
        return (np.zeros((0, N_FEATURES), np.float32), np.zeros((0,), int), [], [])
    X = np.vstack(X)
    y = np.asarray(y, dtype=int)
    logger.info(f"training candidates: {len(y)} pairs / {n_pos} positives "
                f"({100*n_pos/max(1,len(y)):.1f}%) over {len(set(groups))} docs")
    return X, y, groups, meta


# --------------------------------------------------------------------------- #
# (A) GBDT / logistic calibrated extractor
# --------------------------------------------------------------------------- #
class GBDTExtractor:
    """Calibrated supervised located_in classifier over engineered features."""

    def __init__(self, window: int = 2, cap: int = 400, seed: int = 20260618,
                 backend: str = "auto"):
        self.window = window
        self.cap = cap
        self.seed = seed
        self.backend = backend
        self.model = None
        self.calibrator = None      # IsotonicRegression mapping raw score -> P
        self.name = "gbdt"
        self.fit_stats = {}

    # ---- fit ----
    def fit(self, train_contexts: dict):
        from sklearn.isotonic import IsotonicRegression
        X, y, groups, _ = assemble_training(train_contexts, self.window, self.cap)
        if len(y) == 0 or y.sum() == 0:
            raise RuntimeError("no training positives assembled")
        # doc-fold split: SHA-based fold==0 -> calibration, else fit (doc-disjoint within train)
        import hashlib
        fold = np.array([int(hashlib.sha256(str(g).encode()).hexdigest(), 16) % 5 for g in groups])
        cal_mask = fold == 0
        fit_mask = ~cal_mask
        if fit_mask.sum() == 0 or cal_mask.sum() == 0 or y[fit_mask].sum() == 0:
            fit_mask = np.ones(len(y), bool); cal_mask = np.ones(len(y), bool)
        Xf, yf = X[fit_mask], y[fit_mask]
        pos_w = float((yf == 0).sum()) / max(1.0, float((yf == 1).sum()))
        backend = self._train_base(Xf, yf, pos_w)
        raw_cal = self._raw_score(X[cal_mask])
        iso = IsotonicRegression(out_of_bounds="clip", y_min=0.0, y_max=1.0)
        iso.fit(raw_cal, y[cal_mask])
        self.calibrator = iso
        self.fit_stats = {"backend": backend, "n_train_pairs": int(len(y)),
                          "n_positives": int(y.sum()), "n_fit": int(fit_mask.sum()),
                          "n_calib": int(cal_mask.sum()), "scale_pos_weight": round(pos_w, 2),
                          "window": self.window, "cap": self.cap, "n_features": N_FEATURES}
        logger.info(f"GBDTExtractor fit: {self.fit_stats}")
        return self

    def _train_base(self, X, y, pos_w):
        if self.backend in ("auto", "lightgbm"):
            try:
                import lightgbm as lgb
                self.model = lgb.LGBMClassifier(
                    n_estimators=400, learning_rate=0.05, num_leaves=31, max_depth=-1,
                    min_child_samples=20, subsample=0.8, subsample_freq=1, colsample_bytree=0.8,
                    reg_lambda=1.0, scale_pos_weight=pos_w, random_state=self.seed, n_jobs=4,
                    verbosity=-1)
                self.model.fit(X, y)
                self._kind = "lightgbm"
                return "lightgbm"
            except Exception as e:  # noqa: BLE001
                logger.warning(f"lightgbm unavailable/failed ({e}); falling back to GradientBoosting")
        from sklearn.ensemble import GradientBoostingClassifier
        # GB has no class weight -> pass sample_weight
        sw = np.where(y == 1, pos_w, 1.0)
        self.model = GradientBoostingClassifier(n_estimators=300, learning_rate=0.05,
                                                max_depth=3, subsample=0.8,
                                                random_state=self.seed)
        self.model.fit(X, y, sample_weight=sw)
        self._kind = "gradient_boosting"
        return "gradient_boosting"

    def _raw_score(self, X):
        if X.shape[0] == 0:
            return np.zeros((0,), float)
        return self.model.predict_proba(X)[:, 1]

    # ---- predict ----
    def predict_proba_doc(self, ctx: dict) -> dict:
        cands = build_doc_candidates(ctx, self.window, self.cap)
        if not cands:
            return {}
        X = np.vstack([c["feat"] for c in cands])
        raw = self._raw_score(X)
        p = self.calibrator.predict(raw) if self.calibrator is not None else raw
        return {(c["i"], c["j"]): float(pi) for c, pi in zip(cands, p)}

    def extract_supervised(self, ctx: dict, tau: float) -> list[dict]:
        return _edges_from_probs(self.predict_proba_doc(ctx), tau)

    def feature_importance(self):
        try:
            imp = getattr(self.model, "feature_importances_", None)
            if imp is None:
                return {}
            order = np.argsort(imp)[::-1]
            return {FEATURE_NAMES[k]: float(imp[k]) for k in order[:15]}
        except Exception:  # noqa: BLE001
            return {}


# --------------------------------------------------------------------------- #
# 2-cycle-safe edge emission (shared)
# --------------------------------------------------------------------------- #
def _edges_from_probs(probs: dict, tau: float) -> list[dict]:
    """Keep candidates with P>=tau; for a pair predicted both ways keep the higher-prob
    direction; emit entity-id located_in edges."""
    kept = {k: p for k, p in probs.items() if p >= tau}
    # resolve directed 2-cycles
    final = {}
    for (i, j), p in kept.items():
        key = frozenset((i, j))
        prev = final.get(key)
        if prev is None or p > prev[1]:
            final[key] = ((i, j), p)
    return [{"a": ij[0], "b": ij[1], "type": "located_in", "surface": "located in"}
            for ij, _p in final.values()]


# --------------------------------------------------------------------------- #
# (B) Fine-tuned compact encoder extractor (GPU; second supervised family)
# --------------------------------------------------------------------------- #
class EncoderExtractor:
    """Fine-tuned encoder over the marked text window of the closest co-occurring mention pair.
    Binary located_in(i,j); P(located_in) per ordered candidate. Independent of the GBDT family."""

    def __init__(self, model_name: str = "microsoft/deberta-v3-small", window: int = 2,
                 cap: int = 400, seed: int = 20260618, max_len: int = 128, epochs: int = 2,
                 batch_size: int = 64, lr: float = 2e-5, device: str | None = None,
                 max_fit_neg_ratio: float = 6.0):
        self.model_name = model_name
        self.window = window
        self.cap = cap
        self.seed = seed
        self.max_len = max_len
        self.epochs = epochs
        self.batch_size = batch_size
        self.lr = lr
        self.device = device
        self.max_fit_neg_ratio = max_fit_neg_ratio
        self.tokenizer = None
        self.model = None
        self.calibrator = None
        self.name = "encoder"
        self.fit_stats = {}

    # ---- marked-window text for an ordered pair ----
    def _pair_text(self, ctx, spans, i, j, ment) -> str:
        cp = _closest_pair(ment[i], ment[j])
        ai, bi, si, aj, bj, sj, sd, gap = cp
        text = ctx["text"]
        s_lo, s_hi = min(si, sj), max(si, sj)
        win_a = spans[s_lo][0]
        win_b = spans[min(s_hi, len(spans) - 1)][1]
        # insert markers around the two closest mentions (order by position)
        marks = sorted([(ai, bi, "E1"), (aj, bj, "E2")])
        out = []
        cur = win_a
        for (a, b, tag) in marks:
            a = max(a, win_a); b = min(b, win_b)
            if a < cur:
                continue
            out.append(text[cur:a])
            out.append(f"[{tag}] {text[a:b]} [/{tag}] ")
            cur = b
        out.append(text[cur:win_b])
        return "".join(out).strip()

    def _doc_pairs(self, ctx):
        spans = sentence_spans(ctx["text"])
        ment = _entity_mentions(ctx, spans)
        cands = build_doc_candidates(ctx, self.window, self.cap)
        texts = [self._pair_text(ctx, spans, c["i"], c["j"], ment) for c in cands]
        keys = [(c["i"], c["j"]) for c in cands]
        return keys, texts

    def fit(self, train_contexts: dict):
        import torch
        from sklearn.isotonic import IsotonicRegression
        from transformers import AutoModelForSequenceClassification, AutoTokenizer
        dev = self.device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.device = dev
        torch.manual_seed(self.seed)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, num_labels=2).to(dev)
        # assemble (text,label,doc)
        import hashlib
        texts, labels, docs = [], [], []
        for did, ctx in train_contexts.items():
            pos = _gold_pos_set(ctx)
            keys, txts = self._doc_pairs(ctx)
            for k, t in zip(keys, txts):
                texts.append(t); labels.append(1 if k in pos else 0); docs.append(did)
        if not texts or sum(labels) == 0:
            raise RuntimeError("encoder: no training positives")
        fold = np.array([int(hashlib.sha256(str(d).encode()).hexdigest(), 16) % 5 for d in docs])
        fit_mask = fold != 0
        cal_mask = fold == 0
        labels = np.asarray(labels, int)
        if fit_mask.sum() == 0 or cal_mask.sum() == 0 or labels[fit_mask].sum() == 0:
            fit_mask = np.ones(len(labels), bool); cal_mask = np.ones(len(labels), bool)
        # subsample fit-set negatives to bound encoder training time (keep ALL positives); the
        # calibration fold is left FULL so isotonic still maps to true precision on the natural mix.
        rng = np.random.default_rng(self.seed)
        fit_idx_all = np.where(fit_mask)[0]
        pos_idx = fit_idx_all[labels[fit_idx_all] == 1]
        neg_idx = fit_idx_all[labels[fit_idx_all] == 0]
        n_keep_neg = int(min(len(neg_idx), max(1, self.max_fit_neg_ratio * len(pos_idx))))
        neg_keep = rng.choice(neg_idx, size=n_keep_neg, replace=False) if len(neg_idx) > n_keep_neg else neg_idx
        fit_idx = np.concatenate([pos_idx, neg_keep])
        rng.shuffle(fit_idx)
        pos_w = float((labels[fit_idx] == 0).sum()) / max(1.0, float((labels[fit_idx] == 1).sum()))
        self._n_fit_used = int(len(fit_idx))
        self._train_loop(texts, labels, fit_idx, pos_w)
        raw_cal = self._raw_scores([texts[k] for k in np.where(cal_mask)[0]])
        iso = IsotonicRegression(out_of_bounds="clip", y_min=0.0, y_max=1.0)
        iso.fit(raw_cal, labels[cal_mask])
        self.calibrator = iso
        self.fit_stats = {"backend": self.model_name, "n_train_pairs": int(len(labels)),
                          "n_positives": int(labels.sum()), "n_fit_available": int(fit_mask.sum()),
                          "n_fit_used": int(self._n_fit_used), "n_calib": int(cal_mask.sum()),
                          "pos_weight": round(pos_w, 2), "epochs": self.epochs, "max_len": self.max_len,
                          "batch_size": self.batch_size, "max_fit_neg_ratio": self.max_fit_neg_ratio,
                          "device": dev}
        logger.info(f"EncoderExtractor fit: {self.fit_stats}")
        return self

    def _train_loop(self, texts, labels, fit_idx, pos_w):
        import time
        import torch
        from torch.utils.data import DataLoader, TensorDataset
        idx = np.asarray(fit_idx)
        enc = self.tokenizer([texts[k] for k in idx], truncation=True, max_length=self.max_len,
                             padding="max_length", return_tensors="pt")
        ds = TensorDataset(enc["input_ids"], enc["attention_mask"],
                           torch.tensor(labels[idx], dtype=torch.long))
        dl = DataLoader(ds, batch_size=self.batch_size, shuffle=True)
        opt = torch.optim.AdamW(self.model.parameters(), lr=self.lr)
        cw = torch.tensor([1.0, pos_w], dtype=torch.float32, device=self.device)
        lossf = torch.nn.CrossEntropyLoss(weight=cw)
        use_bf16 = (self.device == "cuda" and torch.cuda.is_bf16_supported())
        self.model.train()
        for ep in range(self.epochs):
            tot = 0.0; t0 = time.time()
            for ids, am, yb in dl:
                ids, am, yb = ids.to(self.device), am.to(self.device), yb.to(self.device)
                opt.zero_grad()
                if use_bf16:
                    with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
                        out = self.model(input_ids=ids, attention_mask=am).logits
                        loss = lossf(out, yb)
                else:
                    out = self.model(input_ids=ids, attention_mask=am).logits
                    loss = lossf(out, yb)
                loss.backward()
                opt.step()
                tot += float(loss.item())
            logger.info(f"  encoder epoch {ep+1}/{self.epochs} mean_loss={tot/max(1,len(dl)):.4f} "
                        f"({time.time()-t0:.0f}s, bf16={use_bf16}, n_steps={len(dl)})")

    def _raw_scores(self, texts):
        import torch
        if not texts:
            return np.zeros((0,), float)
        self.model.eval()
        use_bf16 = (self.device == "cuda" and torch.cuda.is_bf16_supported())
        out = []
        with torch.no_grad():
            for s in range(0, len(texts), 128):
                chunk = texts[s:s + 128]
                enc = self.tokenizer(chunk, truncation=True, max_length=self.max_len,
                                     padding=True, return_tensors="pt").to(self.device)
                if use_bf16:
                    with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
                        logits = self.model(**enc).logits
                else:
                    logits = self.model(**enc).logits
                p = torch.softmax(logits.float(), dim=-1)[:, 1].cpu().numpy()
                out.append(p)
        return np.concatenate(out) if out else np.zeros((0,), float)

    def predict_proba_doc(self, ctx: dict) -> dict:
        keys, texts = self._doc_pairs(ctx)
        if not keys:
            return {}
        raw = self._raw_scores(texts)
        p = self.calibrator.predict(raw) if self.calibrator is not None else raw
        return {k: float(pi) for k, pi in zip(keys, p)}

    def extract_supervised(self, ctx: dict, tau: float) -> list[dict]:
        return _edges_from_probs(self.predict_proba_doc(ctx), tau)
