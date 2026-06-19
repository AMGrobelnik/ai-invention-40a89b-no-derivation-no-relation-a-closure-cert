# /// script
# requires-python = ">=3.10"
# dependencies = ["huggingface_hub"]
# ///
"""Canonical entry point for the Natural-Text Absent-Relation Kinship Corpus.

`uv run data.py` does the whole pipeline end-to-end:
  1. ensure the raw Re-DocRED + DocRED json files are in temp/datasets/ (download if absent);
  2. build the per-document gold graphs (detok.py char offsets + kinship.py closure engine)
     for the TWO best datasets -- 're-docred' (primary) and 'docred' (secondary slice);
  3. standardize to the exp_sel_data_out schema -- ONE ROW PER DOCUMENT, grouped by dataset
     ({datasets:[{dataset, examples:[{input, output, metadata_*}, ...]}, ...]}), attach
     top-level metadata (composition table verbatim, provenance, QA, char-len distribution);
  4. write full_data_out.json + mini_/preview_ variants.

Each example = one Wikipedia document (input=detokenized prose, output=json.dumps(gold_graph)).
$0 LLM spend (pure deterministic data construction; deterministic cue check passes 100%, so
the optional small-LLM cue judge is skipped).
"""
from __future__ import annotations
import gzip, os, shutil, sys

WORK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, WORK)
DST = os.path.join(WORK, "temp", "datasets")

# raw source files needed in temp/datasets/ : (HF repo, repo path, local basename)
SOURCES = [
    ("tonytan48/Re-DocRED", "train_revised.json", "train_revised.json"),
    ("tonytan48/Re-DocRED", "dev_revised.json", "dev_revised.json"),
    ("tonytan48/Re-DocRED", "test_revised.json", "test_revised.json"),
    ("thunlp/docred", "data/train_annotated.json.gz", "train_annotated.json"),
    ("thunlp/docred", "data/dev.json.gz", "dev.json"),
    ("thunlp/docred", "data/rel_info.json.gz", "rel_info.json"),
]


def ensure_downloads():
    os.makedirs(DST, exist_ok=True)
    missing = [(r, p, b) for (r, p, b) in SOURCES if not os.path.exists(os.path.join(DST, b))]
    if not missing:
        print(f"[data] all {len(SOURCES)} raw files present in {DST}")
        return
    from huggingface_hub import hf_hub_download
    for repo, path, base in missing:
        src = hf_hub_download(repo, path, repo_type="dataset")
        out = os.path.join(DST, base)
        if path.endswith(".gz"):
            with gzip.open(src, "rb") as f:
                open(out, "wb").write(f.read())
        else:
            shutil.copy(src, out)
        print(f"[data] downloaded {repo}/{path} -> {out} ({os.path.getsize(out)/1e6:.1f} MB)")


def main():
    ensure_downloads()
    import assemble                       # imports build -> detok, kinship (all local, stdlib)
    sz = assemble.main()
    print(f"[data] DONE -- full_data_out.json ({sz:.1f} MB) + mini_/preview_ variants written.")


if __name__ == "__main__":
    main()
