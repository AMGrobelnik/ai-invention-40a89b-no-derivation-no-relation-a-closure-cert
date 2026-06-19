#!/usr/bin/env python3
"""Emit mini_data_out.json (3 examples/dataset) and preview_data_out.json
(3 examples/dataset, all strings truncated to 200 chars) preserving the
exp_sel_data_out top-level {metadata, datasets} object shape.

(The aii-json format script assumes a top-level ARRAY; this schema is a
top-level OBJECT {datasets:[...]}, so we mini/preview per-dataset here.)"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
full = json.loads((ROOT / "full_data_out.json").read_text())


def truncate(o, n=200):
    if isinstance(o, str):
        return o[:n] + ("..." if len(o) > n else "")
    if isinstance(o, list):
        return [truncate(x, n) for x in o]
    if isinstance(o, dict):
        return {k: truncate(v, n) for k, v in o.items()}
    return o


def variant(truncate_strings, n):
    ds = []
    for d in full["datasets"]:
        exs = d["examples"][:n]
        if truncate_strings:
            exs = [truncate(e) for e in exs]
        ds.append({"dataset": d["dataset"], "examples": exs})
    return {"metadata": full["metadata"], "datasets": ds}


# mini = 3 examples/dataset (full rows); preview = 10 examples/dataset (strings truncated)
(ROOT / "mini_data_out.json").write_text(json.dumps(variant(False, 3), ensure_ascii=False, indent=1))
(ROOT / "preview_data_out.json").write_text(json.dumps(variant(True, 10), ensure_ascii=False, indent=1))
print("wrote mini_data_out.json (3/dataset) + preview_data_out.json (10/dataset)")
