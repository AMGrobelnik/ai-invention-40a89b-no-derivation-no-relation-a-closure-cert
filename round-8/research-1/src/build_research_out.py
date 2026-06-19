#!/usr/bin/env python3
"""Build research_out.json + research_report.md for research_iter8_dir1.

Pure-web research artifact: reframe confident absent-relation hallucination as a
COMPOSITIONAL false-premise / unanswerable-question abstention failure, carve the
two-part novelty delta, and specify the mandatory query-side verifier baseline.

All facts below were verified against primary sources (arXiv, ACL Anthology, MIT
TACL, OpenReview) during this session. No fabrication.
"""
import json
import os

OUT_DIR = "/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_research_1"

# ---------------------------------------------------------------------------
# BIBTEX  (new entries verified this session + reused dossier keys)
# ---------------------------------------------------------------------------
BIBTEX_NEW = r"""
% ===== WORKSTREAM 1: false-premise / unanswerable literature (NEW, verified) =====

@inproceedings{Hu2023,
  author    = {Shengding Hu and Yifan Luo and Huadong Wang and Xingyi Cheng and Zhiyuan Liu and Maosong Sun},
  title     = {Won't Get Fooled Again: Answering Questions with False Premises},
  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), Volume 1: Long Papers},
  year      = {2023},
  month     = jul,
  address   = {Toronto, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {5626--5643},
  url       = {https://aclanthology.org/2023.acl-long.309/},
  doi       = {10.18653/v1/2023.acl-long.309},
  note      = {arXiv:2307.02394; FalseQA dataset, GitHub thunlp/FalseQA}
}

@inproceedings{Kirichenko2025,
  author    = {Polina Kirichenko and Mark Ibrahim and Kamalika Chaudhuri and Samuel J. Bell},
  title     = {{AbstentionBench}: Reasoning {LLMs} Fail on Unanswerable Questions},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track},
  year      = {2025},
  eprint    = {2506.09038},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  note      = {arXiv:2506.09038; NeurIPS 2025 D\&B; OpenReview OkHC30LLpO; GitHub facebookresearch/AbstentionBench}
}

% Wen2024: KEY REUSED FROM DOSSIER for downstream consistency, but venue/year/DOI
% CORRECTED to the authoritative TACL Volume 13 (2025) publication. The arXiv
% preprint (2407.18418) is dated July 2024; the journal version appeared in 2025.
@article{Wen2024,
  author  = {Bingbing Wen and Jihan Yao and Shangbin Feng and Chenjun Xu and Yulia Tsvetkov and Bill Howe and Lucy Lu Wang},
  title   = {Know Your Limits: A Survey of Abstention in Large Language Models},
  journal = {Transactions of the Association for Computational Linguistics (TACL)},
  volume  = {13},
  pages   = {529--556},
  year    = {2025},
  address = {Cambridge, MA},
  publisher = {MIT Press},
  doi     = {10.1162/tacl_a_00754},
  url     = {https://aclanthology.org/2025.tacl-1.26/},
  note    = {arXiv:2407.18418 (preprint Jul 2024); published TACL vol.~13, 2025, anthology 2025.tacl-1.26}
}

% ----- optional adjacency (sentence-level false-premise QA) -----

@inproceedings{Kim2023,
  author    = {Najoung Kim and Phu Mon Htut and Samuel R. Bowman and Jackson Petty},
  title     = {{(QA)\textsuperscript{2}}: Question Answering with Questionable Assumptions},
  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), Volume 1: Long Papers},
  year      = {2023},
  address   = {Toronto, Canada},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2023.acl-long.472/},
  doi       = {10.18653/v1/2023.acl-long.472},
  note      = {arXiv:2212.10003}
}

@inproceedings{Yu2023,
  author    = {Xinyan Velocity Yu and Sewon Min and Luke Zettlemoyer and Hannaneh Hajishirzi},
  title     = {{CREPE}: Open-Domain Question Answering with False Presuppositions},
  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), Volume 1: Long Papers},
  year      = {2023},
  address   = {Toronto, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {10457--10480},
  url       = {https://aclanthology.org/2023.acl-long.583/},
  doi       = {10.18653/v1/2023.acl-long.583},
  note      = {arXiv:2211.17257}
}

% ===== WORKSTREAM 3: query-side verifier method families (NEW, verified) =====

@inproceedings{Press2023,
  author    = {Ofir Press and Muru Zhang and Sewon Min and Ludwig Schmidt and Noah A. Smith and Mike Lewis},
  title     = {Measuring and Narrowing the Compositionality Gap in Language Models},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2023},
  year      = {2023},
  address   = {Singapore},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2023.findings-emnlp.378/},
  doi       = {10.18653/v1/2023.findings-emnlp.378},
  note      = {arXiv:2210.03350; introduces self-ask}
}

@inproceedings{Weng2023,
  author    = {Yixuan Weng and Minjun Zhu and Fei Xia and Bin Li and Shizhu He and Shengping Liu and Bin Sun and Kang Liu and Jun Zhao},
  title     = {Large Language Models are Better Reasoners with Self-Verification},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2023},
  year      = {2023},
  address   = {Singapore},
  publisher = {Association for Computational Linguistics},
  pages     = {2550--2575},
  url       = {https://aclanthology.org/2023.findings-emnlp.167/},
  doi       = {10.18653/v1/2023.findings-emnlp.167},
  note      = {arXiv:2212.09561}
}

@inproceedings{Deng2024,
  author    = {Yang Deng and Yong Zhao and Moxin Li and See-Kiong Ng and Tat-Seng Chua},
  title     = {Don't Just Say ``I don't know''! Self-aligning Large Language Models for Responding to Unknown Questions with Explanations},
  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year      = {2024},
  address   = {Miami, Florida, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {13652--13673},
  url       = {https://aclanthology.org/2024.emnlp-main.757/},
  doi       = {10.18653/v1/2024.emnlp-main.757},
  note      = {arXiv:2402.15062; the planner's working title ``Gotcha!'' is a mislabel -- canonical title is ``Don't Just Say `I don't know'!''}
}
""".strip()

# Reused dossier keys (verbatim) needed by Workstream 3 baseline design.
BIBTEX_REUSED = r"""
% ===== REUSED FROM DOSSIER art_dA_3iFe_7fn_ (verbatim keys; do NOT duplicate) =====

@article{Kadavath2022,
  author        = {Saurav Kadavath and Tom Conerly and Amanda Askell and Tom Henighan and Dawn Drain and Ethan Perez and Nicholas Schiefer and Zac Hatfield-Dodds and Nova DasSarma and Eli Tran-Johnson and others},
  title         = {Language Models (Mostly) Know What They Know},
  journal       = {arXiv preprint arXiv:2207.05221},
  year          = {2022},
  eprint        = {2207.05221},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL}
}

@inproceedings{Wang2023,
  author        = {Xuezhi Wang and Jason Wei and Dale Schuurmans and Quoc Le and Ed H. Chi and Sharan Narang and Aakanksha Chowdhery and Denny Zhou},
  title         = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
  booktitle     = {International Conference on Learning Representations (ICLR)},
  year          = {2023},
  eprint        = {2203.11171},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL}
}
""".strip()

BIBTEX_BLOCK = BIBTEX_NEW + "\n\n" + BIBTEX_REUSED

# ---------------------------------------------------------------------------
# WORKSTREAM 1 -- per-paper structured records
# ---------------------------------------------------------------------------
workstream_1 = [
    {
        "key": "Hu2023",
        "role": "REQUIRED 1a -- canonical sentence-level TRAINED false-premise detector (the method foil)",
        "title": "Won't Get Fooled Again: Answering Questions with False Premises",
        "authors": "Shengding Hu, Yifan Luo, Huadong Wang, Xingyi Cheng, Zhiyuan Liu, Maosong Sun",
        "venue": "ACL 2023 (Long Papers), Toronto",
        "ids": "anthology 2023.acl-long.309; arXiv:2307.02394; DOI 10.18653/v1/2023.acl-long.309; pages 5626-5643; GitHub thunlp/FalseQA",
        "framing_of_false_premise": (
            "Introduces 'False Premise Questions (FPQs)': questions that presuppose something untrue, "
            "so the presupposition must be rebutted rather than answered. The false premise is LOCAL to a "
            "single question/sentence (e.g. 'How many eyes does the sun have?' presupposes 'the sun can have "
            "eyes'). The paper explicitly notes such premises 'always violate human knowledge or logic and "
            "rarely appear in the natural text', i.e. they are SENTENCE-LEVEL, out-of-distribution, and "
            "non-compositional."),
        "detection_method": (
            "TRAINED / LEARNABLE classifier: fine-tune PLMs to DISCRIMINATE FPQs from true-premise questions "
            "(works on ~256 examples) and GENERATE explanations as rebuttals; a 'replay general questions "
            "during training' trick preserves performance on ordinary QA."),
        "method_type": "trained classifier (supervised fine-tuning) + generative rebuttal; NOT gold-free, NOT training-free",
        "headline_findings": (
            "FalseQA = 2365 human-written FPQs, each with an explanation of the false premise and a revised "
            "true-premise question (TPQ). (1) PLMs of different types/scales can distinguish FPQs from TPQs and "
            "a scaling effect holds; (2) PLMs generate reasonable false-premise explanations usable as rebuttals; "
            "(3) the number of FPQ examples needed is moderate -- 256 FPQs give >70% accuracy for >1B-param "
            "models, and in-context learning suffices for larger PLMs."),
        "verbatim_quotes": [
            "\"We annotate a FalseQA dataset containing 2365 human-written FPQs, with the corresponding "
            "explanations for the false premises and the revised true premise questions.\" (arXiv:2307.02394, abstract)",
            "\"PLMs are capable of discriminating FPQs by fine-tuning on moderate numbers (e.g., 256) of "
            "examples.\" (arXiv:2307.02394, abstract)",
            "\"Such false premises always violate human knowledge or logic and rarely appear in the natural "
            "text, thus leading to an out-of-distribution generalization gap for the PLMs.\" (arXiv:2307.02394, sec. 1)",
        ],
        "why_it_is_the_foil": (
            "FalseQA is THE canonical false-premise-detection paper, but (a) the false premise is sentence-level "
            "(a single questionable presupposition), not a multi-edge relational claim, and (b) detection is a "
            "TRAINED discriminator. Our certificate addresses a COMPOSITIONAL relational false premise ('a "
            "derivation path exists between X and Y') with a GOLD-FREE, TRAINING-FREE structural test -- the "
            "two axes on which we differ."),
    },
    {
        "key": "Kirichenko2025",
        "role": "REQUIRED 1b -- establishes false-premise/unanswerable abstention as OPEN; reasoning fine-tuning makes it WORSE",
        "title": "AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions",
        "authors": "Polina Kirichenko, Mark Ibrahim, Kamalika Chaudhuri, Samuel J. Bell (Meta/FAIR)",
        "venue": "NeurIPS 2025 Datasets & Benchmarks Track",
        "ids": "arXiv:2506.09038 (submitted 10 Jun 2025); OpenReview OkHC30LLpO; GitHub facebookresearch/AbstentionBench",
        "framing_of_false_premise": (
            "A large-scale abstention benchmark over 20 datasets spanning 6 scenarios -- 'questions with unknown "
            "answers, underspecification, FALSE PREMISES, subjective interpretations, and outdated information'. "
            "False premise is one of six first-class unanswerability scenarios. Abstention = refusing to answer "
            "definitively under uncertainty."),
        "detection_method": (
            "BENCHMARK + evaluation study (not a new detector): evaluates 20 frontier LLMs (open/closed, "
            "instruct vs reasoning) with an automatic, quality-verified LLM-judge of abstention behaviour; "
            "also probes a system-prompt mitigation."),
        "method_type": "benchmark-only / diagnostic evaluation; studies (and finds limits of) training- and prompt-based fixes",
        "headline_findings": (
            "Abstention is an UNSOLVED problem and scaling is of little use. CRITICALLY, reasoning fine-tuning "
            "DEGRADES abstention by 24% on average (even in math/science domains the reasoning models are trained "
            "on). A carefully crafted system prompt boosts abstention but 'does not resolve models' fundamental "
            "inability to reason about uncertainty'. Reasoning models 'often hallucinate missing context and "
            "provide definitive final answers even when their reasoning chains express uncertainty'."),
        "verbatim_quotes": [
            "\"...a large-scale benchmark for holistically evaluating abstention across 20 diverse datasets, "
            "including questions with unknown answers, underspecification, false premises, subjective "
            "interpretations, and outdated information.\" (arXiv:2506.09038, abstract)",
            "\"we find that reasoning fine-tuning degrades abstention (by 24% on average), even for math and "
            "science domains on which reasoning models are explicitly trained.\" (arXiv:2506.09038, abstract)",
            "\"often hallucinating missing context and providing definitive final answers even when their "
            "reasoning chains express uncertainty\" (arXiv:2506.09038, sec. 1)",
            "\"a carefully crafted system prompt can boost abstention in practice, [but] it does not resolve "
            "models' fundamental inability to reason about uncertainty.\" (arXiv:2506.09038, abstract)",
        ],
        "why_it_motivates_the_certificate": (
            "Establishes that confident false-premise/unanswerable abstention is open and unsolved AT FRONTIER "
            "SCALE, and -- decisively -- that the obvious fix (reasoning models / more training) makes it WORSE, "
            "with models committing definitive answers even while internally uncertain. This is precisely the "
            "confident-wrong regime a dispersion/confidence signal cannot catch, motivating a structural, "
            "training-free certificate."),
    },
    {
        "key": "Wen2024",
        "role": "REQUIRED 1c -- CORRECTS the dossier: a query-side ANSWERABILITY axis exists, independent of model confidence",
        "title": "Know Your Limits: A Survey of Abstention in Large Language Models",
        "authors": "Bingbing Wen, Jihan Yao, Shangbin Feng, Chenjun Xu, Yulia Tsvetkov, Bill Howe, Lucy Lu Wang",
        "venue": "TACL Volume 13 (2025), MIT Press, Cambridge MA",
        "ids": "anthology 2025.tacl-1.26; DOI 10.1162/tacl_a_00754; pages 529-556; arXiv:2407.18418 (preprint Jul 2024)",
        "dossier_correction": (
            "The prior dossier (art_dA_3iFe_7fn_) framed Wen2024 ONLY as the MODEL perspective -- 'abstain when "
            "confidence c(x,y) < threshold' -- and listed it among the confidence/calibration family. That is "
            "incomplete. The survey's central contribution is a framework with THREE perspectives, of which "
            "answerability is a SEPARATE axis from model confidence."),
        "three_perspective_framework": (
            "Refusal function r(x,y) is defined as a CONJUNCTION of three system-designer functions: query "
            "answerability a(x) in [0,1], model confidence c(x,y) in [0,1], and human-value alignment h(x,y) in "
            "[0,1]. The system abstains (r=1) if ANY of a(x), c(x,y), h(x,y) = 0. Crucially a(x) -- 'the degree "
            "to which an input x can be answered' -- is INDEPENDENT of the model's confidence c. The query "
            "perspective covers inputs that are ambiguous/incomplete, beyond what any human or model could know, "
            "or that have irrelevant/insufficient context. 'Input-processing' inference methods abstain based on "
            "query answerability, separate from confidence calibration."),
        "method_type": "survey/taxonomy (organizing framework); not a single detector",
        "headline_findings": (
            "Organizes the abstention literature by (i) three perspectives (query/model/human-values) and (ii) "
            "lifecycle stage (pretraining, alignment, inference; inference split into input-/in-/output-processing). "
            "Query-centric abstention datasets enumerated include SQuAD2, Natural Questions, MuSiQue (multi-hop, "
            "unanswerable via removed support paragraphs), CoQA, QuAC, AmbigQA, SelfAware, Known-Unknown -- "
            "answerability framed broadly (ambiguity, incompleteness, unknowable, insufficient context)."),
        "verbatim_quotes": [
            "\"we introduce a framework to analyze abstention capabilities from three perspectives that have "
            "typically been considered in isolation -- query answerability, the confidence of the model to answer "
            "the query, and alignment of query and responses with human values.\" (arXiv:2407.18418, sec. 1)",
            "\"The query perspective focuses on the nature of the input -- whether the query is ambiguous or "
            "incomplete ..., beyond what any human or model could possibly know ..., there is irrelevant or "
            "insufficient context to answer ...\" (arXiv:2407.18418, sec. 2)",
            "\"Query function a : X -> [0, 1]. a(x) represents the degree to which an input x can be answered.\" "
            "and \"r(x, y) = 1, if any of a(x); c(x, y); h(x, y) = 0\" (arXiv:2407.18418, sec. 2)",
            "\"From the query perspective in our proposed framework, LLMs can choose to abstain based on the "
            "query answerability.\" (arXiv:2407.18418, sec. 3.3.1, input-processing approaches)",
        ],
        "honest_scope_note": (
            "The survey's enumerated query-side datasets do NOT single out a COMPOSITIONAL multi-hop relational "
            "false premise as a studied category -- the closest is MuSiQue (multi-hop, made unanswerable by "
            "REMOVING a supporting paragraph, i.e. missing-evidence, not a false derivation-path premise). So "
            "Wen2024 supplies the AXIS (answerability is separate from confidence) but not the specific instance; "
            "this strengthens, rather than pre-empts, our delta."),
        "venue_year_reconciliation": (
            "RESOLVED. The dossier pinned 'TACL 2024' (the arXiv preprint year, 2407.18418, Jul 2024); the iter-8 "
            "objective says 'TACL 2025'. Authoritative ACL Anthology / MIT TACL record: published in TACL Volume "
            "13, YEAR 2025, pages 529-556, DOI 10.1162/tacl_a_00754, anthology id 2025.tacl-1.26. The iter-8 "
            "'TACL 2025' is CORRECT. BibTeX updated to year=2025 with a note that the preprint is dated 2024; "
            "the citation key 'Wen2024' is retained verbatim to avoid breaking downstream \\cite{Wen2024} "
            "references inherited from the dossier."),
    },
    {
        "key": "Kim2023",
        "role": "OPTIONAL 1d -- sentence-level questionable-assumption QA (sharpens the 'sentence-level' contrast)",
        "title": "(QA)^2: Question Answering with Questionable Assumptions",
        "authors": "Najoung Kim, Phu Mon Htut, Samuel R. Bowman, Jackson Petty",
        "venue": "ACL 2023 (Long Papers), Toronto",
        "ids": "anthology 2023.acl-long.472; arXiv:2212.10003; DOI 10.18653/v1/2023.acl-long.472",
        "one_line_framing": (
            "An open-domain evaluation set of NATURALLY OCCURRING search-engine queries that may or may not "
            "contain a questionable assumption; the questionable assumption is a SENTENCE-LEVEL presupposition "
            "local to one query (benchmark, not a new detector)."),
        "method_type": "benchmark / evaluation",
    },
    {
        "key": "Yu2023",
        "role": "OPTIONAL 1d -- natural-distribution false-presupposition QA (sentence-level, with baseline detectors)",
        "title": "CREPE: Open-Domain Question Answering with False Presuppositions",
        "authors": "Xinyan Velocity Yu, Sewon Min, Luke Zettlemoyer, Hannaneh Hajishirzi",
        "venue": "ACL 2023 (Long Papers), Toronto",
        "ids": "anthology 2023.acl-long.583; arXiv:2211.17257; DOI 10.18653/v1/2023.acl-long.583; pages 10457-10480",
        "one_line_framing": (
            "8,400 Reddit (information-seeking) questions with a NATURAL distribution of presupposition failures; "
            "25% of questions contain false presuppositions, annotated with the presupposition and its correction. "
            "Again the false presupposition is SENTENCE-LEVEL; the paper provides baseline detect-and-correct "
            "models."),
        "method_type": "benchmark + baseline detect/correct models",
        "verbatim_quote": (
            "\"We introduce CREPE, a QA dataset containing a natural distribution of presupposition failures from "
            "online information-seeking forums. We find that 25% of questions contain false presuppositions...\" "
            "(arXiv:2211.17257, abstract)"),
    },
    {
        "key": "Deng2024",
        "role": "OPTIONAL 1d -- self-alignment FINE-TUNING for unknown questions (reinforces 'trained method' contrast)",
        "title": "Don't Just Say \"I don't know\"! Self-aligning LLMs for Responding to Unknown Questions with Explanations",
        "authors": "Yang Deng, Yong Zhao, Moxin Li, See-Kiong Ng, Tat-Seng Chua",
        "venue": "EMNLP 2024 (Main), Miami",
        "ids": "anthology 2024.emnlp-main.757; arXiv:2402.15062; DOI 10.18653/v1/2024.emnlp-main.757; pages 13652-13673",
        "one_line_framing": (
            "A self-alignment method that fine-tunes the LLM on self-generated unknown-question data (two-stage "
            "class-aware self-augmentation + disparity-driven self-curation) to refuse AND explain unanswerable "
            "questions. A TRAINED detect-then-explain pattern."),
        "method_type": "trained (self-alignment fine-tuning)",
        "title_correction": (
            "The iter-8 planner referred to this as 'Gotcha! Don't trick me with unanswerable questions' at "
            "arXiv:2402.15062. That arXiv id resolves to the canonical title above ('Don't Just Say \"I don't "
            "know\"!'), published at EMNLP 2024. We cite the verified canonical title; treat 'Gotcha' as a "
            "working mislabel."),
    },
]

# ---------------------------------------------------------------------------
# WORKSTREAM 2 -- delta carving
# ---------------------------------------------------------------------------
related_work_paragraph = (
    "\\paragraph{Confident absent-relation hallucination as a compositional false premise.} "
    "Our failure mode is an instance of the false-premise / unanswerable-question problem, but at a "
    "level the existing literature does not reach. Work on false-premise QA detects a presupposition that "
    "is \\emph{local to a single question}: FalseQA \\cite{Hu2023} fine-tunes models to discriminate "
    "questions such as ``How many eyes does the sun have?'', while \\citet{Kim2023} and CREPE \\cite{Yu2023} "
    "collect naturally occurring queries whose single questionable assumption is to be flagged or corrected. "
    "AbstentionBench \\cite{Kirichenko2025} shows this family of unanswerable cases -- false premises among "
    "them -- is far from solved: across 20 frontier LLMs abstention is unreliable, and, strikingly, "
    "reasoning fine-tuning \\emph{degrades} abstention by 24\\% on average, with models ``providing definitive "
    "final answers even when their reasoning chains express uncertainty.'' The abstention survey of "
    "\\citet{Wen2024} makes the relevant distinction explicit: it organises abstention around a query "
    "\\emph{answerability} function $a(x)$ that is separate from model confidence $c(x,y)$, so that a system "
    "may abstain because the question itself is ill-posed, independent of how confident the model feels. "
    "What none of these works model is a \\emph{compositional, multi-hop relational} false premise -- the "
    "implicit assumption that \\emph{a derivation path exists between two entities}. When a reader is asked "
    "for the relation between two entities that are not connected in the document, the false premise is not "
    "a local presupposition but the structural claim that the underlying relation graph is connected. We "
    "place our no-derivation certificate in this answerability lineage \\cite{Wen2024,Hu2023,Kirichenko2025} "
    "and target exactly the compositional case it leaves open."
)

delta_statement = {
    "delta_1_setting": (
        "SETTING DELTA -- compositional / multi-hop relational false premise. Existing false-premise QA is "
        "SENTENCE-LEVEL: the false presupposition is local to one question (FalseQA's 'How many eyes does the "
        "sun have?' [Hu2023]; questionable assumptions [Kim2023]; CREPE's Reddit presuppositions [Yu2023]). "
        "Ours is the STRUCTURAL premise that a multi-edge derivation path exists between two entities in a "
        "document -- a compositional, relation-graph-level false premise. The multi-hop axis is recognized for "
        "ANSWERING (the 'compositionality gap', [Press2023]) and for missing-evidence unanswerability (MuSiQue, "
        "via [Wen2024]), but a compositional relational false premise as an abstention target is absent from "
        "that literature."),
    "delta_2_method": (
        "METHOD DELTA -- gold-free, training-free, STRUCTURAL detector. The recognized detectors for this "
        "failure mode are TRAINED (FalseQA fine-tunes a discriminator [Hu2023]; Self-Align fine-tunes on "
        "self-generated unknown-question data [Deng2024]) or PROMPT-BASED self-verification at the answer level. "
        "AbstentionBench [Kirichenko2025] further shows that adding training (reasoning fine-tuning) can HURT "
        "abstention. Our no-derivation certificate needs neither gold labels nor training: it abstains because, "
        "after composing per-edge reads through the exact relation algebra, NO derivation path supports the "
        "queried edge -- a structural, confidence-independent test of the false premise itself."),
    "one_line_each": [
        "DELTA-1 (setting): we lift false-premise abstention from a sentence-level presupposition to a "
        "compositional, multi-hop relational premise ('a derivation path between X and Y exists'), a regime "
        "absent from FalseQA/(QA)^2/CREPE [Hu2023,Kim2023,Yu2023].",
        "DELTA-2 (method): we detect that false premise with a gold-free, training-free STRUCTURAL certificate "
        "(no derivation path => abstain), versus the trained or prompt-based detectors that define prior work "
        "[Hu2023,Deng2024] -- and that training can even degrade [Kirichenko2025].",
    ],
}

novelty_sentence = (
    "Our contribution is a corpus-robust DIAGNOSTIC -- that confident, self-consistent absent-relation "
    "fabrication is a compositional false-premise failure that transfers across readers and corpora, "
    "accompanied by a measurable present-vs-absent capability gap on a non-by-construction mixed pool -- "
    "together with a gold-free, training-free STRUCTURAL detector (the no-derivation certificate) whose net "
    "selective-prediction utility, off the structural-by-construction stratum and at coverage matched to a "
    "query-side false-premise verifier, is the open question this work tests; we do NOT claim the certificate "
    "mechanism itself is new (it inherits the standard neuro-symbolic deduce-then-abstain premise), only its "
    "framing, its corpus-robust diagnostic, and its head-to-head evaluation against the recognized method for "
    "exactly this failure mode."
)

workstream_2 = {
    "related_work_paragraph": related_work_paragraph,
    "delta_statement": delta_statement,
    "novelty_sentence": novelty_sentence,
}

# ---------------------------------------------------------------------------
# WORKSTREAM 3 -- query-side verifier baseline design
# ---------------------------------------------------------------------------
method_survey = [
    {
        "family": "self-ask (compositional decomposition)",
        "key": "Press2023",
        "description": (
            "Press et al. measure a 'compositionality gap' (models answer sub-questions but not the multi-hop "
            "composition) and introduce self-ask: the model 'explicitly asks itself (and answers) follow-up "
            "questions before answering the initial question.'"),
        "abstention_signal_mapping": (
            "Decompose the relational query into the sub-edges that WOULD have to hold for a path to exist; if "
            "the model cannot produce a connected chain of supported sub-edges, the relatedness premise fails. "
            "Directly motivates a query-side relatedness/decomposition check; also the canonical citation for "
            "the multi-hop / compositional framing of our setting."),
        "verbatim_quote": (
            "\"We present a new method, self-ask ... the model explicitly asks itself (and answers) follow-up "
            "questions before answering the initial question.\" (arXiv:2210.03350, abstract)"),
    },
    {
        "family": "self-verification (backward answer checking)",
        "key": "Weng2023",
        "description": (
            "Weng et al. take a CoT conclusion as a condition and perform BACKWARD verification, yielding "
            "'interpretable answer validation scores' used to select among candidates."),
        "abstention_signal_mapping": (
            "Re-pose the committed relation as a claim to verify against the document; a NO verdict / low "
            "validation score flips a confident-wrong commit to abstain. This is the method family behind the "
            "self-verification verifier (3b-ii)."),
        "verbatim_quote": (
            "\"By performing a backward verification of the answers that LLM deduced for itself, we can obtain "
            "interpretable answer validation scores to select the candidate answer with the highest score.\" "
            "(arXiv:2212.09561, abstract)"),
    },
    {
        "family": "P(True) / P(IK) self-evaluation",
        "key": "Kadavath2022",
        "description": (
            "The model evaluates the probability that a proposed answer is true (P(True)) or that it knows the "
            "answer (P(IK)); reused from the dossier."),
        "abstention_signal_mapping": (
            "Apply P(True) to the RELATEDNESS proposition ('X and Y are related at all') and to the committed "
            "edge; threshold P(True) to abstain. Supplies the confidence read INSIDE the query-side verifier "
            "(distinct from using P(True) on the open-ended answer)."),
    },
    {
        "family": "self-consistency (vote margin)",
        "key": "Wang2023",
        "description": (
            "Majority vote over multiple sampled reasoning paths; agreement is the confidence signal. Reused "
            "from the dossier."),
        "abstention_signal_mapping": (
            "Sample the verification question k times; the agreement fraction on RELATED/UNRELATED (or YES/NO) "
            "is the abstain signal. Yields the stronger self-consistency variant of both verifiers."),
    },
    {
        "family": "verify-then-answer / detect-then-respond (unknown-question handling)",
        "key": "Deng2024 / Hu2023",
        "description": (
            "Two-step patterns that first DETECT unanswerability/false premise, then respond: FalseQA "
            "discriminate-then-rebut [Hu2023]; Self-Align detect-then-explain [Deng2024]. In prior work the "
            "detector is TRAINED."),
        "abstention_signal_mapping": (
            "Our baseline keeps the two-step shape but uses a PROMPT-BASED, zero-training detector on the same "
            "reader, so the comparison isolates the structural certificate against the recognized method WITHOUT "
            "conflating in the cost of fine-tuning."),
    },
]

relatedness_verifier_spec = {
    "name": "Query-side RELATEDNESS verifier (tests the false premise directly)",
    "what_it_tests": (
        "The PREMISE that a relation of the queried type exists between X and Y at all -- the compositional "
        "false premise itself, before any specific edge is committed."),
    "prompt_template_kinship": (
        "Document:\n{document}\n\n"
        "Question: Based ONLY on the document above, are {X} and {Y} related by a FAMILY/KINSHIP relationship "
        "of ANY kind -- directly or through a chain of stated relationships (parent, child, sibling, spouse, "
        "and their compositions such as grandparent, aunt/uncle, cousin)?\n"
        "First answer RELATED or UNRELATED. Then, on a new line, give your confidence as an integer 0-100.\n"
        "Respond EXACTLY in this format:\n"
        "ANSWER: <RELATED|UNRELATED>\n"
        "CONFIDENCE: <0-100>"),
    "prompt_template_containment": (
        "Document:\n{document}\n\n"
        "Question: Based ONLY on the document above, are {X} and {Y} related by GEOGRAPHIC / ADMINISTRATIVE "
        "CONTAINMENT of ANY kind -- directly or through a chain of stated relationships (located-in, part-of, "
        "capital-of, contains, and their compositions)?\n"
        "First answer RELATED or UNRELATED. Then, on a new line, give your confidence as an integer 0-100.\n"
        "Respond EXACTLY in this format:\n"
        "ANSWER: <RELATED|UNRELATED>\n"
        "CONFIDENCE: <0-100>"),
    "parse_and_abstain_rule": (
        "Parse ANSWER in {RELATED, UNRELATED} and CONFIDENCE in [0,100]. The verifier ABSTAINS (predicts 'no "
        "relation' / declines to commit a specific edge) iff ANSWER == UNRELATED OR CONFIDENCE < tau_rel. "
        "Otherwise it defers to the main pipeline's committed edge. On unparseable output, retry once at "
        "temperature 0; if still unparseable, count as ABSTAIN (conservative) and log."),
    "stronger_self_consistency_variant": (
        "Sample k=5 relatedness judgements at temperature 0.7; take the majority of ANSWER and the mean "
        "CONFIDENCE. Abstain iff majority == UNRELATED OR agreement_fraction < tau_sc OR mean CONFIDENCE < "
        "tau_rel. Grounds the relatedness signal in self-consistency [Wang2023]."),
    "grounding": "self-ask decomposition [Press2023]; P(True) on the relatedness proposition [Kadavath2022]; detect-then-respond [Hu2023,Deng2024].",
}

self_verification_spec = {
    "name": "Query-side SELF-VERIFICATION pass (flips confident-wrong commits)",
    "what_it_tests": (
        "Whether the SPECIFIC committed edge the raw reader produced is actually supported by the document "
        "(including edges derivable by chaining stated relationships). Applied to the SAME committed answer for "
        "an apples-to-apples comparison."),
    "prompt_template_kinship": (
        "Document:\n{document}\n\n"
        "A system answered that, according to the document, {X} is the {relation} of {Y}.\n"
        "Re-read the document and VERIFY this claim. Is it actually true -- based ONLY on the document, including "
        "facts derivable by chaining stated relationships -- that {X} is the {relation} of {Y}?\n"
        "Answer YES or NO. Then, on a new line, give your confidence as an integer 0-100.\n"
        "Respond EXACTLY in this format:\n"
        "VERDICT: <YES|NO>\n"
        "CONFIDENCE: <0-100>"),
    "prompt_template_containment": (
        "Document:\n{document}\n\n"
        "A system answered that, according to the document, {X} is {relation} {Y} (e.g. located in / part of).\n"
        "Re-read the document and VERIFY this claim. Is it actually true -- based ONLY on the document, including "
        "facts derivable by chaining stated containment relationships -- that {X} is {relation} {Y}?\n"
        "Answer YES or NO. Then, on a new line, give your confidence as an integer 0-100.\n"
        "Respond EXACTLY in this format:\n"
        "VERDICT: <YES|NO>\n"
        "CONFIDENCE: <0-100>"),
    "parse_and_abstain_rule": (
        "Parse VERDICT in {YES, NO} and CONFIDENCE in [0,100]. FLIP the committed answer to ABSTAIN iff "
        "VERDICT == NO OR CONFIDENCE < tau_ver. Otherwise keep the committed edge. Apply ONLY to queries where "
        "the raw reader committed a specific edge (abstained queries are untouched). On unparseable output, "
        "retry once at temperature 0; if still unparseable, keep the commit (do not silently abstain) and log."),
    "stronger_self_consistency_variant": (
        "Sample k=5 backward verifications at temperature 0.7; majority-vote VERDICT, mean CONFIDENCE. Flip to "
        "abstain iff majority == NO OR agreement_fraction < tau_sc OR mean CONFIDENCE < tau_ver. This is the "
        "self-consistency [Wang2023] strengthening of self-verification [Weng2023]."),
    "grounding": "self-verification / backward checking [Weng2023]; P(True) on the committed edge [Kadavath2022]; self-consistency [Wang2023].",
}

matched_coverage_recipe = {
    "coverage_object": (
        "The unit of analysis is SINGLE-RELATION RESOLUTION at the QUERY level (one (X, relation-type, Y) "
        "query), identical to the certificate's confident-wrong metric. Coverage = fraction of queries on which "
        "a method COMMITS a specific edge (1 - abstention rate). Risk = error rate among committed queries "
        "(equivalently, confident-wrong rate)."),
    "evaluation_pool": (
        "A SINGLE mixed pool combining PRESENT queries (a true edge exists) and SAME-COMPONENT-SIBLING-ABSENT "
        "queries (entities in the same connected component but with NO edge of the queried type -- the "
        "non-by-construction hard-absent stratum from iter-7). Report metrics on the whole pool and sliced by "
        "stratum (present / hard-absent), since the certificate's win, if any, concentrates on the absent slice."),
    "methods_compared": [
        "no-derivation certificate (structural; single operating point)",
        "4 dispersion / confidence signals from the dossier battery (verbalized confidence, self-consistency vote-margin, P(True), semantic-entropy-style) -- each swept over its threshold",
        "query-side RELATEDNESS verifier (sweep tau_rel and the RELATED/UNRELATED decision)",
        "query-side SELF-VERIFICATION verifier (sweep tau_ver; optional k=5 self-consistency variant)",
    ],
    "procedure": (
        "(1) For each thresholded method, sweep tau over [0,100] (and the discrete RELATED/UNRELATED or YES/NO "
        "decision) to trace the FULL risk-coverage curve. (2) The certificate is a single (coverage, risk) "
        "point. (3) To compare fairly, read every baseline AT THE CERTIFICATE'S COVERAGE: pick the tau that "
        "equalizes coverage with the certificate, then compare selective accuracy and confident-wrong rate at "
        "that matched coverage. (4) Also overlay all full curves and locate the certificate point relative to "
        "each baseline's frontier. (5) Report Holm-adjusted, document-clustered bootstrap (B=10000) confidence "
        "intervals on the confident-wrong REDUCTION (certificate vs each baseline) -- exactly the existing "
        "battery's statistics."),
    "primary_comparator": (
        "The query-side false-premise verifiers (relatedness + self-verification), NOT the dispersion signals, "
        "are the PRIMARY comparator: they are the recognized method for this specific failure mode, so the "
        "certificate's claim stands or falls against them."),
    "report_both_directions": (
        "Report present-slice and absent-slice separately. Expect the verifiers to do well on the absent slice "
        "(they are designed for it); the dispersion signals are expected to fail on confident-wrong absent "
        "fabrications (the dossier's argument)."),
}

credibility_bar = (
    "The certificate's claim for the absent-relation stratum is credible ONLY if, at coverage matched to the "
    "query-side false-premise verifier (relatedness + self-verification, the recognized method for this failure "
    "mode), the certificate MATCHES OR BEATS it on confident-wrong reduction with non-overlapping / Holm-"
    "adjusted doc-clustered bootstrap CIs. If the prompt-based query-side verifier already catches the "
    "fabrications as well as the certificate, that is an HONEST NEGATIVE -- the structural certificate is not "
    "needed for the absent stratum -- and must be reported as such (it would still leave the corpus-robust "
    "DIAGNOSTIC and the present-vs-absent capability gap as the contribution). A certificate WIN is meaningful "
    "only relative to this strong, recognized baseline, never relative to the dispersion signals alone."
)

operational_cautions = [
    "COST: each verifier adds 1-2 LLM calls per query (k=5 self-consistency variants add ~5x on the verified "
    "subset). Budget within the experiment's $10 cap; run the single-sample variants as primary and the k=5 "
    "self-consistency variants only on a subsample if cost-bound.",
    "UNIT-OF-ANALYSIS MATCH: score the verifier at the QUERY level (one (X, relation, Y)), identical to the "
    "certificate's confident-wrong metric, so risk-coverage points are directly comparable.",
    "APPLES-TO-APPLES: the self-verification pass MUST be applied to the SAME committed answer the raw reader "
    "produced (do not re-generate the answer); the relatedness verifier is independent of the committed edge "
    "and tests the premise.",
    "SAME READER: run both verifiers on the SAME reader model as the main pipeline (gemini + deepseek per the "
    "iter-8 plan), zero training, so the comparison isolates the structural certificate, not a stronger model.",
    "GOLD-READ CEILING: optionally run the verifiers on the gold-edge reading to separate verifier failure from "
    "extraction failure, mirroring the certificate's gold-read ceiling (iter-7 EXTRACTION-LIMITED-BOUNDARY).",
]

workstream_3 = {
    "method_survey": method_survey,
    "relatedness_verifier_spec": relatedness_verifier_spec,
    "self_verification_spec": self_verification_spec,
    "matched_coverage_recipe": matched_coverage_recipe,
    "credibility_bar": credibility_bar,
    "operational_cautions": operational_cautions,
}

# ---------------------------------------------------------------------------
# SOURCES
# ---------------------------------------------------------------------------
sources = [
    {"index": 1, "url": "https://arxiv.org/abs/2307.02394",
     "title": "Won't Get Fooled Again: Answering Questions with False Premises (Hu et al., 2023)",
     "summary": "FalseQA abstract: 2365 human-written false-premise questions (FPQs) + explanations + revised true-premise questions; PLMs discriminate FPQs by fine-tuning on ~256 examples; sentence-level, trained detector."},
    {"index": 2, "url": "https://aclanthology.org/2023.acl-long.309/",
     "title": "FalseQA -- ACL Anthology (2023.acl-long.309)",
     "summary": "Authoritative venue/pages: ACL 2023 Long Papers, Toronto, July 2023, pp. 5626-5643, DOI 10.18653/v1/2023.acl-long.309; full author list."},
    {"index": 3, "url": "https://arxiv.org/pdf/2307.02394",
     "title": "FalseQA PDF (grepped) -- FPQ definition + discriminate quote",
     "summary": "Exact FPQ definition ('How many eyes does the sun have?' presupposes 'the sun can have eyes'; 'always violate human knowledge or logic and rarely appear in the natural text') and the 256-example / >70% accuracy findings."},
    {"index": 4, "url": "https://arxiv.org/abs/2506.09038",
     "title": "AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions (Kirichenko et al., 2025)",
     "summary": "20 datasets / 6 scenarios incl. false premises; abstention unsolved; reasoning fine-tuning degrades abstention by 24%; system prompt helps but doesn't resolve fundamental inability to reason about uncertainty."},
    {"index": 5, "url": "https://arxiv.org/pdf/2506.09038",
     "title": "AbstentionBench PDF (grepped) -- 24% + scenario list + confident-wrong quote",
     "summary": "Verbatim: scenario list incl. 'false premises'; '24% on average' degradation; 'hallucinating missing context and providing definitive final answers even when their reasoning chains express uncertainty'."},
    {"index": 6, "url": "https://neurips.cc/virtual/2025/poster/121675",
     "title": "AbstentionBench -- NeurIPS 2025 poster page",
     "summary": "Confirms NeurIPS 2025 (Datasets & Benchmarks) venue for AbstentionBench; OpenReview id OkHC30LLpO."},
    {"index": 7, "url": "https://aclanthology.org/2025.tacl-1.26/",
     "title": "Know Your Limits: A Survey of Abstention in LLMs -- TACL Anthology (2025.tacl-1.26)",
     "summary": "Authoritative venue/year reconciliation: TACL Volume 13, YEAR 2025, pp. 529-556, Cambridge MA, MIT Press, DOI 10.1162/tacl_a_00754. Confirms iter-8 'TACL 2025' (not dossier's 'TACL 2024')."},
    {"index": 8, "url": "https://arxiv.org/pdf/2407.18418",
     "title": "Wen et al. 2024 survey PDF (grepped) -- query-side / answerability content",
     "summary": "Three-perspective framework (query answerability a(x), model confidence c(x,y), human values h(x,y)); r(x,y)=1 if any of a,c,h = 0; a(x) independent of confidence; corrects the dossier's confidence-only framing."},
    {"index": 9, "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00754/131566/Know-Your-Limits-A-Survey-of-Abstention-in-Large",
     "title": "Know Your Limits -- MIT TACL journal page (DOI 10.1162/tacl_a_00754)",
     "summary": "MIT Press TACL landing page; confirms the journal publication and DOI used in the corrected BibTeX."},
    {"index": 10, "url": "https://arxiv.org/abs/2210.03350",
     "title": "Measuring and Narrowing the Compositionality Gap (Press et al., self-ask)",
     "summary": "Introduces the 'compositionality gap' and self-ask (model asks itself follow-up questions before answering). Grounds the multi-hop framing and the relatedness-decomposition verifier."},
    {"index": 11, "url": "https://aclanthology.org/2023.findings-emnlp.378/",
     "title": "self-ask -- Findings of EMNLP 2023 (2023.findings-emnlp.378)",
     "summary": "Authoritative venue for Press et al.: Findings-EMNLP 2023, Singapore; used for the Press2023 BibTeX."},
    {"index": 12, "url": "https://arxiv.org/abs/2212.09561",
     "title": "Large Language Models are Better Reasoners with Self-Verification (Weng et al., 2023)",
     "summary": "Backward verification of CoT conclusions yields interpretable validation scores to select answers. Method family for the self-verification verifier."},
    {"index": 13, "url": "https://aclanthology.org/2023.findings-emnlp.167/",
     "title": "self-verification -- Findings of EMNLP 2023 (2023.findings-emnlp.167)",
     "summary": "Authoritative venue/pages (2550-2575) for Weng et al.; DOI 10.18653/v1/2023.findings-emnlp.167."},
    {"index": 14, "url": "https://aclanthology.org/2023.acl-long.472/",
     "title": "(QA)^2: Question Answering with Questionable Assumptions (Kim et al., ACL 2023)",
     "summary": "Authors Najoung Kim, Phu Mon Htut, Samuel R. Bowman, Jackson Petty; naturally occurring search queries with sentence-level questionable assumptions. Optional adjacency."},
    {"index": 15, "url": "https://arxiv.org/abs/2212.10003",
     "title": "(QA)^2 -- arXiv abstract",
     "summary": "Open-domain evaluation set of naturally occurring search-engine queries that may or may not contain questionable assumptions (sentence-level)."},
    {"index": 16, "url": "https://arxiv.org/pdf/2211.17257",
     "title": "CREPE: Open-Domain QA with False Presuppositions (Yu et al., 2023) PDF",
     "summary": "8,400 Reddit questions, natural distribution of presupposition failures; 25% contain false presuppositions; sentence-level; baseline detect/correct models. Optional adjacency."},
    {"index": 17, "url": "https://aclanthology.org/2023.acl-long.583/",
     "title": "CREPE -- ACL Anthology (2023.acl-long.583)",
     "summary": "Authoritative venue/pages: ACL 2023 Long, pp. 10457-10480; authors Xinyan Velocity Yu, Sewon Min, Luke Zettlemoyer, Hannaneh Hajishirzi."},
    {"index": 18, "url": "https://arxiv.org/abs/2402.15062",
     "title": "Don't Just Say \"I don't know\"! Self-aligning LLMs for Unknown Questions (Deng et al., 2024)",
     "summary": "Self-alignment FINE-TUNING for unknown questions with explanations (detect-then-explain, trained). arXiv id the planner labeled 'Gotcha'; canonical title corrected; EMNLP 2024 main (2024.emnlp-main.757)."},
    {"index": 19, "url": "https://arxiv.org/abs/2207.05221",
     "title": "Language Models (Mostly) Know What They Know (Kadavath et al., 2022) -- reused",
     "summary": "P(True)/P(IK) self-evaluation; reused dossier key for the confidence read inside the query-side verifiers."},
    {"index": 20, "url": "https://arxiv.org/abs/2203.11171",
     "title": "Self-Consistency Improves Chain of Thought Reasoning (Wang et al., 2023) -- reused",
     "summary": "Majority vote over sampled reasoning paths; reused dossier key for the k=5 self-consistency variants of both verifiers."},
]

# ---------------------------------------------------------------------------
# ANSWER (synthesis with numbered citations)
# ---------------------------------------------------------------------------
answer = (
"This artifact supplies the two contribution-defining moves the empirical/dataset artifacts cannot produce: "
"the LITERATURE half of the novelty reframe, and the design of the mandatory query-side false-premise "
"verifier baseline. Three workstreams.\n\n"

"(1) FALSE-PREMISE / UNANSWERABLE LITERATURE. Confident absent-relation hallucination is best positioned as a "
"COMPOSITIONAL instance of the false-premise / unanswerable-question abstention problem. FalseQA [1,2,3] is the "
"canonical anchor: it defines 'False Premise Questions' -- questions presupposing something untrue ('How many "
"eyes does the sun have?' presupposes 'the sun can have eyes') -- and detects them with a TRAINED discriminator "
"fine-tuned on ~256 examples, explicitly noting such premises 'rarely appear in the natural text' and are "
"SENTENCE-LEVEL [3]. AbstentionBench [4,5,6] establishes that this family (false premises among six "
"unanswerability scenarios over 20 datasets) is UNSOLVED at frontier scale, and -- decisively for our "
"motivation -- that reasoning fine-tuning DEGRADES abstention by 24% on average, with models 'providing "
"definitive final answers even when their reasoning chains express uncertainty' [5]: the obvious fix makes the "
"confident-wrong regime worse. Critically, the dossier's framing of Wen et al. as a mere confidence-threshold "
"survey is CORRECTED here: the survey's central framework organizes abstention around THREE perspectives -- "
"query answerability a(x), model confidence c(x,y), and human values h(x,y) -- with refusal r(x,y)=1 if ANY of "
"them is 0, and a(x) ('the degree to which an input x can be answered') is INDEPENDENT of confidence [7,8,9]. "
"That answerability axis is exactly where our certificate lives. We also reconcile the venue: Wen et al. is "
"authoritatively TACL Volume 13, YEAR 2025 (pp. 529-556, DOI 10.1162/tacl_a_00754) [7,9]; the dossier's 'TACL "
"2024' was the arXiv preprint year, and the iter-8 'TACL 2025' is correct -- we keep the key Wen2024 to "
"preserve downstream \\cite's but set year=2025. Optional adjacency confirms the SENTENCE-LEVEL character of "
"prior false-premise QA: (QA)^2 [14,15] and CREPE [16,17] (8,400 Reddit questions, 25% with false "
"presuppositions) collect single-question presuppositions, and Self-Align [18] is a TRAINED detect-then-explain "
"method.\n\n"

"(2) THE TWO-PART DELTA. DELTA-1 (setting): we lift false-premise abstention from a SENTENCE-LEVEL "
"presupposition [1,14,16] to a COMPOSITIONAL, multi-hop RELATIONAL premise -- the structural claim that 'a "
"derivation path exists between X and Y'. The multi-hop axis is recognized for ANSWERING (the 'compositionality "
"gap' [10,11]) and for missing-evidence unanswerability (MuSiQue, via [8]), but a compositional relational "
"false premise as an abstention TARGET is absent from that literature. DELTA-2 (method): we detect it with a "
"GOLD-FREE, TRAINING-FREE STRUCTURAL certificate (no derivation path => abstain), versus the TRAINED detectors "
"that define prior work (FalseQA fine-tuning [1]; Self-Align [18]) -- and AbstentionBench shows training can "
"even HURT [4]. The one-sentence novelty claim that survives iter-7's EXTRACTION-LIMITED boundary is honest: "
"the contribution is the corpus-robust DIAGNOSTIC (confident absent-relation fabrication is a compositional "
"false premise that transfers across readers/corpora, plus a present-vs-absent capability gap on a "
"non-by-construction mixed pool) PLUS a structural detector whose NET utility off the structural-by-construction "
"stratum is the open iter-8 test -- NOT a claim that the certificate mechanism itself is novel (it inherits the "
"standard neuro-symbolic deduce-then-abstain premise).\n\n"

"(3) QUERY-SIDE VERIFIER BASELINE. The hypothesis requires a query-side false-premise verifier the certificate "
"must MATCH OR BEAT at matched coverage, because that -- not the dispersion signals -- is the recognized method "
"for this failure mode. We ground it in self-ask decomposition [10], self-verification / backward checking "
"[12,13], P(True) self-evaluation [19], self-consistency [20], and the detect-then-respond pattern [1,18], then "
"specify TWO complementary prompt-based, zero-training verifiers run on the same reader: (i) a RELATEDNESS "
"verifier ('are X and Y related by <kinship|containment> at all?' -> RELATED/UNRELATED + confidence; abstain on "
"UNRELATED or confidence < tau) that tests the false premise directly, and (ii) a SELF-VERIFICATION pass on the "
"SAME committed answer ('verify: is X really the <relation> of Y?' -> YES/NO + confidence; flip confident-wrong "
"to abstain on NO or confidence < tau), each with a stronger k=5 self-consistency variant. Both are compared "
"against the certificate and the four dispersion signals at the SAME coverage object (single-relation "
"resolution) on the SAME mixed present / same-component-sibling-absent pool, with Holm-adjusted, doc-clustered "
"(B=10000) confident-wrong reductions and CIs -- exactly the existing battery. CREDIBILITY BAR: a certificate "
"win is meaningful only against this strong baseline; if the prompt-based verifier already catches the "
"fabrications as well, that is an HONEST NEGATIVE (structural certificate not needed for the absent stratum) "
"and must be reported, leaving the diagnostic + capability gap as the contribution."
)

summary = (
"Pure-web ($0) research that retires the LITERATURE half of the reviewer NOVELTY MAJOR and de-risks the new "
"mandatory query-side baseline for the closure-certificate paper (iter-8). (1) Pins the closest-neighbor "
"false-premise / unanswerable abstention literature with verified BibTeX, exact detection-method TYPES, and "
"verbatim quotes: FalseQA [Hu2023, ACL 2023, 2023.acl-long.309] = 2365 FPQs + a SENTENCE-LEVEL, TRAINED "
"discriminator (256 examples); AbstentionBench [Kirichenko2025, NeurIPS 2025 D&B, arXiv:2506.09038] = "
"false-premise abstention UNSOLVED at frontier scale and reasoning fine-tuning DEGRADES it 24%, models commit "
"definitive answers while internally uncertain; and a CORRECTION of the dossier's Wen2024 framing -- the survey "
"[Wen2024] is built on three perspectives (query answerability a(x) | model confidence c(x,y) | human values), "
"with a(x) INDEPENDENT of confidence, so answerability is a distinct axis, not confidence thresholding. Venue "
"reconciled: Wen2024 is authoritatively TACL Volume 13, 2025 (pp. 529-556, DOI 10.1162/tacl_a_00754); the "
"iter-8 'TACL 2025' is correct (dossier's '2024' = preprint year); key Wen2024 retained for downstream cites. "
"Optional adjacency ((QA)^2 [Kim2023], CREPE [Yu2023] 25%/8,400 Reddit Qs, Self-Align [Deng2024]) confirms "
"prior false-premise QA is sentence-level and/or trained. (2) Carves the two-part delta into a drop-in "
"Related-Work paragraph (real \\cite keys), a SETTING delta (compositional/multi-hop relational premise vs "
"sentence-level) + METHOD delta (gold-free, training-free STRUCTURAL detector vs trained/prompt detectors), and "
"one honest novelty sentence scoped to the corpus-robust diagnostic + capability gap (certificate mechanism = "
"inherited NeSy premise). (3) Specifies the mandatory query-side verifier baseline grounded in self-ask "
"[Press2023], self-verification [Weng2023], P(True) [Kadavath2022], self-consistency [Wang2023], and "
"detect-then-respond [Hu2023, Deng2024]: two cheap prompt-based verifiers (RELATEDNESS check + SELF-VERIFICATION "
"pass, each with a k=5 self-consistency variant), exact prompt templates for kinship and containment, "
"parse/abstain rules, and a matched-coverage thresholding recipe (same single-relation coverage object on the "
"mixed present/same-component-sibling-absent pool; Holm-adjusted doc-clustered B=10000 CIs). Credibility bar: "
"the certificate must match-or-beat the query-side verifier at matched coverage, else honest negative. Reuses "
"dossier BibTeX (Kadavath2022, Wang2023) verbatim. Feeds the iter-8 Related-Work and the experiment that "
"decides the diagnostic-vs-demonstrated-fix fork."
)

follow_up_questions = [
    "On the iter-7 same-component-sibling-absent pool, does the cheap prompt-based RELATEDNESS verifier already "
    "match the structural certificate's confident-wrong reduction at matched coverage -- i.e. is the certificate "
    "necessary for the absent stratum, or is the contribution the diagnostic + capability gap alone?",
    "Should the self-verification verifier use a SINGLE pass or the k=5 self-consistency variant as the headline "
    "baseline, given the $10 cap -- and does the self-consistency variant change the verdict on confident-wrong "
    "absent fabrications (where, by the dossier's argument, samples agree on the WRONG edge)?",
    "Does AbstentionBench's released code (facebookresearch/AbstentionBench) include a runnable false-premise "
    "abstention detector that could be added as a third, recognized baseline beyond our two prompt-based "
    "verifiers, to further harden the certificate comparison?",
    "Can we cite a paper that already treats MULTI-HOP / relational false premises specifically (beyond MuSiQue's "
    "removed-evidence unanswerability), or is the compositional-relational false-premise setting genuinely "
    "unclaimed -- which would strengthen DELTA-1?",
]

# ---------------------------------------------------------------------------
# ASSEMBLE
# ---------------------------------------------------------------------------
out = {
    "title": "Reframing confident absent-relation hallucination as a compositional false-premise abstention failure",
    "summary": summary,
    "answer": answer,
    "workstream_1": workstream_1,
    "workstream_2": workstream_2,
    "workstream_3": workstream_3,
    "bibtex_block": BIBTEX_BLOCK,
    "sources": sources,
    "follow_up_questions": follow_up_questions,
}

out_path = os.path.join(OUT_DIR, "research_out.json")
with open(out_path, "w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print("Wrote", out_path, os.path.getsize(out_path), "bytes")

# Quick sanity
assert "Wen2024" in BIBTEX_BLOCK and "year    = {2025}" in BIBTEX_BLOCK
assert "Hu2023" in BIBTEX_BLOCK and "Kirichenko2025" in BIBTEX_BLOCK
assert "Press2023" in BIBTEX_BLOCK and "Weng2023" in BIBTEX_BLOCK
print("Sanity OK")
