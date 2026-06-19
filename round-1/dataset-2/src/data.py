"""data.py -- entry point that BUILDS the synthetic QCN backbone dataset.

This dataset is PURELY SYNTHETIC (a controlled generator), exactly as mandated by the
artifact plan: its entire value is independently controlling structural parameters
(redundancy, hop-count, cyclomatic number, density, node count) with ground truth that
is exact and globally consistent BY CONSTRUCTION. There is therefore nothing to download
into ``temp/datasets/`` -- the networks are generated from concrete geometric models by
the ``qcn/`` package and ``method.py``.

Running this script standardizes every generated network into the aii ``exp_sel_data_out``
schema (one ROW = one example: ``input`` = NL realization, ``output`` = gold graph JSON
string, plus ``metadata_*`` fields), grouped into THREE datasets
(``synthetic_qcn_point``, ``synthetic_qcn_allen``, ``synthetic_qcn_rcc8``), and writes:

  * ``data_out/full_data_out_{1,2}.json``  -- the full corpus, split into <90 MB parts
    (the full ~153 MB single ``full_data_out.json`` exceeds the per-file publish limit,
    so it is split per the aii-file-size-limit procedure; concatenate the datasets with
    the same name across parts to reconstruct);
  * ``data_out/{mini,preview}_data_out_{1,2}.json`` and top-level
    ``mini_data_out.json`` / ``preview_data_out.json``  -- size-optimized variants;
  * ``results/dataset_metadata.json``  -- QA / provenance / dataset-card metadata.

Run:
    uv run data.py                 # full corpus (~35k networks; 500/cell primary, 300/cell secondary)
    uv run data.py --networks-primary 6 --networks-secondary 6 --tag pilot   # quick pilot
"""
from __future__ import annotations

import sys

from method import main

if __name__ == "__main__":
    # Default to the full corpus when no scale flags are supplied; otherwise honor CLI args.
    if not any(a.startswith("--networks-") for a in sys.argv[1:]):
        sys.argv += ["--networks-primary", "500", "--networks-secondary", "300", "--tag", "full"]
    main()
