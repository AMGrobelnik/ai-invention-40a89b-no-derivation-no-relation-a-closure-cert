#!/usr/bin/env python3
"""iter-10 canonical entry point (`method.py`) for the S_supervised experiment.

This is the harness-expected `method.py`. The full implementation lives in `run_supervised.py`
(imported here); this wrapper makes a single `uv run method.py` (re)produce ALL deliverables --
method_out.json + full_/mini_/preview_method_out.json -- self-contained:

  * preloads libgomp.so.1 so LightGBM imports without a manual LD_LIBRARY_PATH;
  * IDEMPOTENT: if a valid method_out.json already exists it is REUSED and the variant files are
    refreshed (pass --force to regenerate from scratch). A fresh checkout with no outputs runs the
    full supervised pipeline (GBDT + fine-tuned deberta-v3-small over the natural Re-DocRED
    located-in corpus; competitors replayed byte-identical at $0 from the SHA-256 cache);
  * writes full/mini/preview variants in PURE PYTHON (no external service), matching the aii-json
    convention (full = identical; mini = first 3 examples per dataset; preview = mini with every
    string truncated to 200 chars).

The substantive method + baseline comparison (the precision-preserving supervised extractor vs the
frozen closure certificate vs the 6 confident-wrong competitors, the recall->net-utility frontier,
and the pre-registered fork verdict) is identical to `run_supervised.py`.
"""
from __future__ import annotations

import ctypes
import glob
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _preload_libgomp():
    pats = [str(HERE / ".venv/lib/python*/site-packages/torch/lib/libgomp-*.so*"),
            str(HERE / ".venv/lib/python*/site-packages/scikit_learn.libs/libgomp-*.so*"),
            str(HERE / "extra_libs/libgomp.so*")]
    for pat in pats:
        for cand in sorted(glob.glob(pat)):
            try:
                ctypes.CDLL(cand, mode=ctypes.RTLD_GLOBAL)
                return cand
            except OSError:
                continue
    return None


_preload_libgomp()

import run_supervised  # noqa: E402  (after libgomp preload)
from loguru import logger  # noqa: E402

OUT = HERE / "method_out.json"
FULL = HERE / "full_method_out.json"
MINI = HERE / "mini_method_out.json"
PREVIEW = HERE / "preview_method_out.json"


def _n_examples(obj: dict) -> int:
    return sum(len(d.get("examples", [])) for d in obj.get("datasets", []))


def _valid_output(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        obj = json.loads(path.read_text())
        return isinstance(obj, dict) and "metadata" in obj and "datasets" in obj and _n_examples(obj) >= 50
    except Exception:  # noqa: BLE001
        return False


def _truncate_strings(o, limit: int = 200):
    if isinstance(o, str):
        return o[:limit]
    if isinstance(o, list):
        return [_truncate_strings(x, limit) for x in o]
    if isinstance(o, dict):
        return {k: _truncate_strings(v, limit) for k, v in o.items()}
    return o


def _write_variants(obj: dict):
    """full = identical; mini = first 3 examples/dataset; preview = mini, strings truncated to 200."""
    FULL.write_text(json.dumps(obj, default=run_supervised._json_default))
    mini = {"metadata": obj.get("metadata", {}),
            "datasets": [{**d, "examples": d.get("examples", [])[:3]} for d in obj.get("datasets", [])]}
    MINI.write_text(json.dumps(mini, default=run_supervised._json_default))
    preview = _truncate_strings(json.loads(json.dumps(mini, default=run_supervised._json_default)), 200)
    PREVIEW.write_text(json.dumps(preview))
    logger.info(f"wrote variants: full={FULL.stat().st_size/1e6:.2f}MB mini={MINI.stat().st_size/1e3:.0f}KB "
                f"preview={PREVIEW.stat().st_size/1e3:.0f}KB")


def main():
    force = "--force" in sys.argv
    if force:
        sys.argv = [a for a in sys.argv if a != "--force"]
    # IDEMPOTENT fast path: a valid method_out.json already exists -> reuse, just refresh variants.
    if not force and _valid_output(OUT):
        obj = json.loads(OUT.read_text())
        logger.info(f"method_out.json present and valid ({_n_examples(obj)} examples); reusing "
                    f"(pass --force to regenerate the full pipeline).")
        _write_variants(obj)
        logger.info("DONE (reused existing output + refreshed full/mini/preview variants).")
        return obj
    # full pipeline (writes method_out.json), then variant files
    obj = run_supervised.main()
    if obj is None and OUT.exists():
        obj = json.loads(OUT.read_text())
    if obj is not None:
        _write_variants(obj)
    logger.info("DONE (ran full supervised pipeline + wrote full/mini/preview variants).")
    return obj


if __name__ == "__main__":
    main()
