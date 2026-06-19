#!/usr/bin/env python3
"""Dataset entrypoint.

Loads the six source corpora from temp/datasets/, standardizes them to the
exp_sel_data_out schema (one example per (corpus, document) row, grouped by dataset),
and writes data_out.json + full_data_out.json. The actual build logic lives in the
modular pipeline (common.py / builders.py / counts.py / build_dataset.py); this is a
thin entrypoint so `python data.py` (inside the uv venv) reproduces the dataset.

Run:
    uv venv .venv --python=3.12 && source .venv/bin/activate
    uv pip install loguru networkx lxml beautifulsoup4 nltk numpy pandas tqdm
    python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
    python data.py
Then generate mini/preview variants with the aii-json skill's format script.
"""

from build_dataset import main

if __name__ == "__main__":
    main()
