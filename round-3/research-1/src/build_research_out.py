#!/usr/bin/env python3
"""
build_research_out.py
Assembles research_out.json for the "Pin & Differentiate the 4 Closest Recent
Neuro-Symbolic Temporal / Abstention Neighbors" citation-verification artifact
(retires the iter-2 reviewer MINOR 'closest recent neighbors not cited').

All facts below were INDEPENDENTLY web-verified this run:
  P1 NeSTR  -> arXiv abstract page (https://arxiv.org/abs/2512.07218) + Semantic Scholar
  P2 TReMu  -> ACL Anthology page + .bib (2025.findings-acl.972) + arXiv 2502.01630 (id check)
  P3 Fan&Strube -> ACL Anthology page + .bib (2025.findings-emnlp.1010)
  P4 When Silence -> arXiv abstract page (https://arxiv.org/abs/2602.04755) + Semantic Scholar
No LLM API calls; cost = $0.
"""
import json, os

WS = "/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_research_1"

# ----------------------------------------------------------------------------
# Verified BibTeX (project key style = AuthorYYYY, matching references.bib:
#   Allen1983, Eirew2025, Kougia2024, Bajpai2025, Kim2025, Ghosh2024, Bajpai2024, Wei2024 ...)
# ----------------------------------------------------------------------------
BIB_LIANG = r"""@inproceedings{Liang2026,
  author        = {Feng Liang and Weixin Zeng and Runhao Zhao and Xiang Zhao},
  title         = {{NeSTR}: A Neuro-Symbolic Abductive Framework for Temporal Reasoning in Large Language Models},
  booktitle     = {Proceedings of the 40th {AAAI} Conference on Artificial Intelligence ({AAAI})},
  year          = {2026},
  eprint        = {2512.07218},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  doi           = {10.48550/arXiv.2512.07218},
  note          = {arXiv:2512.07218; accepted to AAAI 2026}
}"""

BIB_GE = r"""@inproceedings{Ge2025,
  author    = {Yubin Ge and Salvatore Romeo and Jason Cai and Raphael Shu and Yassine Benajiba and Monica Sunkara and Yi Zhang},
  title     = {{TR}e{M}u: Towards Neuro-Symbolic Temporal Reasoning for {LLM}-Agents with Memory in Multi-Session Dialogues},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
  month     = jul,
  year      = {2025},
  address   = {Vienna, Austria},
  publisher = {Association for Computational Linguistics},
  pages     = {18974--18988},
  url       = {https://aclanthology.org/2025.findings-acl.972/},
  doi       = {10.18653/v1/2025.findings-acl.972}
}"""

BIB_FAN = r"""@inproceedings{Fan2025,
  author    = {Yi Fan and Michael Strube},
  title     = {Consistent Discourse-level Temporal Relation Extraction Using Large Language Models},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},
  month     = nov,
  year      = {2025},
  address   = {Suzhou, China},
  publisher = {Association for Computational Linguistics},
  pages     = {18605--18622},
  url       = {https://aclanthology.org/2025.findings-emnlp.1010/},
  doi       = {10.18653/v1/2025.findings-emnlp.1010}
}"""

BIB_ZHOU = r"""@inproceedings{Zhou2026,
  author        = {Xinyu Zhou and Chang Jin and Carsten Eickhoff and Zhijiang Guo and Seyed Ali Bahrainian},
  title         = {When Silence Is Golden: Can {LLMs} Learn to Abstain in Temporal {QA} and Beyond?},
  booktitle     = {Proceedings of the International Conference on Learning Representations ({ICLR})},
  year          = {2026},
  eprint        = {2602.04755},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  doi           = {10.48550/arXiv.2602.04755},
  note          = {arXiv:2602.04755; accepted to ICLR 2026 (OpenReview PhUCxfS0yf)}
}"""

# ----------------------------------------------------------------------------
# Neighbor records
# ----------------------------------------------------------------------------
neighbors = [
  {
    "key": "Liang2026",
    "short_name": "NeSTR",
    "title": "NeSTR: A Neuro-Symbolic Abductive Framework for Temporal Reasoning in Large Language Models",
    "authors": ["Feng Liang", "Weixin Zeng", "Runhao Zhao", "Xiang Zhao"],
    "year": 2026,
    "venue": "AAAI 2026 (preprint arXiv:2512.07218, Dec 2025)",
    "arxiv_id": "2512.07218",
    "anthology_id": None,
    "doi": "10.48550/arXiv.2512.07218",
    "url": "https://arxiv.org/abs/2512.07218",
    "objective_summary": "Integrates structured symbolic temporal encoding with a hybrid reflective reasoner: it preserves explicit temporal relations symbolically, enforces logical consistency via verification, and corrects flawed inferences using ABDUCTIVE reflection, achieving strong zero-shot temporal QA without fine-tuning.",
    "output_contract": "generate-then-abductively-REPAIR a single revised, committed conclusion",
    "one_sentence_differentiation": "NeSTR's abductive-reflection loop repairs detected inconsistencies toward one revised, committed answer, whereas we PRESERVE the relation-algebra disjunction and ABSTAIN on closure-collapse via a gold-free per-edge certificate rather than repairing-to-commit.",
    "bibtex": BIB_LIANG,
  },
  {
    "key": "Ge2025",
    "short_name": "TReMu",
    "title": "TReMu: Towards Neuro-Symbolic Temporal Reasoning for LLM-Agents with Memory in Multi-Session Dialogues",
    "authors": ["Yubin Ge", "Salvatore Romeo", "Jason Cai", "Raphael Shu", "Yassine Benajiba", "Monica Sunkara", "Yi Zhang"],
    "year": 2025,
    "venue": "Findings of ACL 2025 (Vienna, Austria), pp. 18974-18988",
    "arxiv_id": "2502.01630",
    "anthology_id": "2025.findings-acl.972",
    "doi": "10.18653/v1/2025.findings-acl.972",
    "url": "https://aclanthology.org/2025.findings-acl.972/",
    "objective_summary": "A neuro-symbolic framework for temporal reasoning in MULTI-SESSION DIALOGUES: it builds time-aware memory by timeline-summarizing each session with inferred dates, then has the LLM generate PYTHON CODE to perform temporal calculations and select a single answer, lifting GPT-4o from 29.83 to 77.67 on its new multi-choice benchmark.",
    "output_contract": "CODE-GENERATION / single-answer COMMIT (in a dialogue-memory QA setting)",
    "one_sentence_differentiation": "TReMu commits to one computed answer via LLM-generated Python over summarized dialogue memory, whereas we operate on single short documents with an EXACT relation-algebra composition table + iterated path-consistency, preserving disjunction and abstaining rather than code-gen-and-commit.",
    "bibtex": BIB_GE,
  },
  {
    "key": "Fan2025",
    "short_name": "Consistent Discourse-level TRE",
    "title": "Consistent Discourse-level Temporal Relation Extraction Using Large Language Models",
    "authors": ["Yi Fan", "Michael Strube"],
    "year": 2025,
    "venue": "Findings of EMNLP 2025 (Suzhou, China), pp. 18605-18622",
    "arxiv_id": None,
    "anthology_id": "2025.findings-emnlp.1010",
    "doi": "10.18653/v1/2025.findings-emnlp.1010",
    "url": "https://aclanthology.org/2025.findings-emnlp.1010/",
    "objective_summary": "A three-step framework to improve LLM discourse-level temporal relation extraction: (1) context selection per event pair, (2) prompts inspired by Allen's interval algebra, and (3) reflection-based consistency learning, guiding the model toward a structured, CONSISTENT single-label extraction.",
    "output_contract": "F1-maximizing single-label COMMIT (the contract we directly invert)",
    "one_sentence_differentiation": "Fan & Strube enforce consistency + self-reflection to COMMIT to one F1-maximizing label per event pair, whereas we INVERT that objective -- keep the high-recall sound disjunction, narrow only by cross-path composition, and abstain when closure leaves more than one relation.",
    "bibtex": BIB_FAN,
  },
  {
    "key": "Zhou2026",
    "short_name": "When Silence Is Golden",
    "title": "When Silence Is Golden: Can LLMs Learn to Abstain in Temporal QA and Beyond?",
    "authors": ["Xinyu Zhou", "Chang Jin", "Carsten Eickhoff", "Zhijiang Guo", "Seyed Ali Bahrainian"],
    "year": 2026,
    "venue": "ICLR 2026 (preprint arXiv:2602.04755, Feb 2026; OpenReview PhUCxfS0yf)",
    "arxiv_id": "2602.04755",
    "anthology_id": None,
    "doi": "10.48550/arXiv.2602.04755",
    "url": "https://arxiv.org/abs/2602.04755",
    "objective_summary": "The first empirical study of TRAINING LLMs to abstain in temporal QA: it frames abstention as a teachable skill and couples Chain-of-Thought supervision with Reinforcement Learning guided by abstention-aware rewards, improving true-positive rate on unanswerable questions and surpassing GPT-4o on TimeQA.",
    "output_contract": "LEARNED-UNCERTAINTY (trained) ABSTENTION at the QA-answer level",
    "one_sentence_differentiation": "When Silence Is Golden TRAINS the abstention skill via CoT + RL abstention-aware rewards at the QA-answer level, whereas we abstain STRUCTURALLY and TRAINING-FREE because deductive path-consistency closure leaves the queried relation a disjunction -- a per-edge algebraic certificate, not a learned uncertainty score.",
    "bibtex": BIB_ZHOU,
  },
]

# ----------------------------------------------------------------------------
# Differentiation paragraph (drop-in for related work)
# ----------------------------------------------------------------------------
differentiation_paragraph = (
  "Our closest recent neighbors attack LLM temporal reasoning from three angles, none of which "
  "adopts our output contract. NeSTR [Liang2026] integrates symbolic temporal encoding with hybrid "
  "reflective reasoning, but its abductive-reflection loop repairs detected inconsistencies toward a "
  "single revised, COMMITTED conclusion rather than preserving the relation-algebra disjunction. "
  "TReMu [Ge2025] is likewise neuro-symbolic, yet it generates Python over timeline-summarized DIALOGUE "
  "memory to compute and commit to one answer, in a multi-session QA setting rather than single-document "
  "relation extraction. Fan and Strube's Consistent Discourse-level TRE [Fan2025] is the contract we most "
  "directly invert: it pairs Allen-algebra-inspired prompts with reflection-based consistency to COMMIT to "
  "a single F1-maximizing label per event pair, whereas we keep the high-recall sound disjunction, narrow "
  "it only by cross-path composition, and abstain when closure leaves more than one relation. When Silence "
  "Is Golden [Zhou2026] does target temporal abstention, but it TRAINS that skill via Chain-of-Thought "
  "supervision and reinforcement learning with abstention-aware rewards at the QA-answer level, in contrast "
  "to our structural, training-free, gold-free per-edge certificate that abstains precisely because "
  "deductive path-consistency closure leaves the queried relation under-determined. Across all four, the "
  "novel delta is the same: we (1) preserve a relation-algebra disjunction (inverting the single-label "
  "commit contract of [Fan2025] and the established Eirew/Kougia line), (2) issue a gold-free, training-free, "
  "per-edge closure CERTIFICATE that flags jointly-inconsistent reads without any reference graph, and "
  "(3) abstain on closure-COLLAPSE rather than committing (TReMu), repairing-to-commit (NeSTR), or learning "
  "to abstain (When Silence Is Golden)."
)

# ----------------------------------------------------------------------------
# Answer (synthesis prose with numbered citations)
# ----------------------------------------------------------------------------
answer = (
  "All four neighbor papers named in FIX 7 were INDEPENDENTLY re-verified this run and every candidate ID "
  "resolves to a real, correctly-titled paper; verified BibTeX is pinned for each in the project's AuthorYYYY "
  "key style. (P1) NeSTR -- 'NeSTR: A Neuro-Symbolic Abductive Framework for Temporal Reasoning in Large "
  "Language Models' by Feng Liang, Weixin Zeng, Runhao Zhao, Xiang Zhao, arXiv:2512.07218 (8 Dec 2025), "
  "accepted to AAAI 2026 [1, 8]. (P2) TReMu -- 'TReMu: Towards Neuro-Symbolic Temporal Reasoning for "
  "LLM-Agents with Memory in Multi-Session Dialogues' by Yubin Ge, Salvatore Romeo, Jason Cai, Raphael Shu, "
  "Yassine Benajiba, Monica Sunkara, Yi Zhang, Findings of ACL 2025, anthology 2025.findings-acl.972, "
  "pp. 18974-18988; the arXiv mirror is 2502.01630 and points to the same paper [3, 5, 6]. (P3) "
  "'Consistent Discourse-level Temporal Relation Extraction Using Large Language Models' by Yi Fan and "
  "Michael Strube, Findings of EMNLP 2025, anthology 2025.findings-emnlp.1010, pp. 18605-18622 [4, 7]. "
  "(P4) 'When Silence Is Golden: Can LLMs Learn to Abstain in Temporal QA and Beyond?' by Xinyu Zhou, "
  "Chang Jin, Carsten Eickhoff, Zhijiang Guo, Seyed Ali Bahrainian, arXiv:2602.04755 (4 Feb 2026), accepted "
  "to ICLR 2026 (OpenReview PhUCxfS0yf) [2, 8].\n\n"
  "Two corrections to the planner's pre-verification were found. First, the hypothesis short-name "
  "'Towards Neuro-Symbolic Temporal Reasoning for LLMs (Findings-ACL 2025)' is INCOMPLETE -- the real paper "
  "is TReMu (arXiv:2502.01630), and its setting is multi-session DIALOGUE temporal QA with LLM-generated "
  "Python over summarized memory, NOT single-document temporal relation extraction [3, 5]. Second, the "
  "page range the planner attached to TReMu (18605-18622) is actually P3's range; TReMu's correct pages are "
  "18974-18988 [6, 7]. NeSTR's full author list (Liang, Zeng, Zhao, Zhao) and P4's canonical arXiv spelling "
  "of the second author ('Chang Jin', not Semantic Scholar's disambiguated 'Changhong Jin') were also pinned "
  "from the primary pages [1, 2]. None of the four duplicates the iter-2 dossier's four temporal/logical-"
  "consistency citations (arXiv:2510.15513, 2502.11425, 2412.16100, 2409.14065), so the bundle is additive.\n\n"
  "Each neighbor is differentiated on the OUTPUT-CONTRACT axis. NeSTR generate-then-abductively-REPAIRs to a "
  "single committed conclusion [1]; TReMu does CODE-GEN-and-COMMIT over dialogue memory [3]; Consistent "
  "Discourse-level TRE COMMITS to one F1-maximizing consistent label per pair -- the exact contract we invert "
  "[4]; and When Silence Is Golden achieves LEARNED, TRAINED abstention at the QA-answer level [2]. Our "
  "contribution is the methodological opposite: a disjunction-preserving, abstain-on-collapse output contract "
  "backed by a gold-free, training-free, PER-EDGE closure certificate. The ready-to-drop differentiation "
  "paragraph is: \n\n\"" + differentiation_paragraph + "\"\n\n"
  "An adversarial novelty scout (three targeted queries on 'preserve relation-algebra disjunction' AND "
  "'abstain on path-consistency / closure collapse' over LLM-extracted temporal/spatial relations) surfaced "
  "NO exact-match competitor that performs BOTH of our distinctive moves [9, 10]; the queries returned only "
  "generic encyclopedic references. The two nearest extra neighbors seen in passing are real but do NOT match: "
  "GDLLM (arXiv:2508.20828, EMNLP Findings 2025) is a global-distance GAT+LLM event-TRE model that performs "
  "single-label hard classification (a commit contract, no disjunction/abstention) [9], and BeDiscovER "
  "(arXiv:2511.13095, EACL 2026) is a discourse-understanding BENCHMARK aggregating temporal-relation tasks, "
  "not a method [10]. Both are listed only as optional backups; the four named papers remain the deliverable. "
  "Confirming that no paper already preserves a relation-algebra disjunction and abstains on closure-collapse "
  "is itself a novelty-supporting result."
)

# ----------------------------------------------------------------------------
# Sources
# ----------------------------------------------------------------------------
sources = [
  {"index": 1, "url": "https://arxiv.org/abs/2512.07218",
   "title": "NeSTR: A Neuro-Symbolic Abductive Framework for Temporal Reasoning in Large Language Models (Liang et al., AAAI 2026)",
   "summary": "arXiv abstract page: verified title, authors (Feng Liang, Weixin Zeng, Runhao Zhao, Xiang Zhao), 8 Dec 2025 submission, cs.CL, 'Accepted by AAAI 2026', and the full abstract describing symbolic encoding + abductive reflection (generate-then-repair-to-commit)."},
  {"index": 2, "url": "https://arxiv.org/abs/2602.04755",
   "title": "When Silence Is Golden: Can LLMs Learn to Abstain in Temporal QA and Beyond? (Zhou et al., ICLR 2026)",
   "summary": "arXiv abstract page: verified title, 5-author list (Xinyu Zhou, Chang Jin, Carsten Eickhoff, Zhijiang Guo, Seyed Ali Bahrainian), Feb 2026 submission, 'Accepted to ICLR2026', and abstract describing trained abstention via CoT supervision + RL with abstention-aware rewards."},
  {"index": 3, "url": "https://aclanthology.org/2025.findings-acl.972/",
   "title": "TReMu: Towards Neuro-Symbolic Temporal Reasoning for LLM-Agents with Memory in Multi-Session Dialogues (Ge et al., Findings ACL 2025)",
   "summary": "ACL Anthology landing page: verified title, 7-author list, Findings of ACL 2025, anthology id 2025.findings-acl.972, pages 18974-18988, and abstract (timeline summarization + LLM-generated Python over dialogue memory, commit-to-answer)."},
  {"index": 4, "url": "https://aclanthology.org/2025.findings-emnlp.1010/",
   "title": "Consistent Discourse-level Temporal Relation Extraction Using Large Language Models (Fan & Strube, Findings EMNLP 2025)",
   "summary": "ACL Anthology landing page: verified title, authors Yi Fan and Michael Strube, Findings of EMNLP 2025, anthology id 2025.findings-emnlp.1010, pages 18605-18622, abstract (context selection + Allen-algebra prompts + reflection-based consistency -> single consistent label)."},
  {"index": 5, "url": "https://arxiv.org/abs/2502.01630",
   "title": "TReMu arXiv mirror (2502.01630) -- ID cross-check",
   "summary": "arXiv abstract page confirming arXiv:2502.01630 is the SAME TReMu paper (title + authors match the anthology entry); resolves the planner's incomplete short-name and confirms the dialogue-memory setting."},
  {"index": 6, "url": "https://aclanthology.org/2025.findings-acl.972.bib",
   "title": "ACL Anthology canonical BibTeX for TReMu",
   "summary": "Canonical .bib export (ge-etal-2025-tremu): exact author/title/booktitle/pages 18974-18988/doi 10.18653/v1/2025.findings-acl.972 -- source for the pinned BibTeX (re-keyed Ge2025 to match project style)."},
  {"index": 7, "url": "https://aclanthology.org/2025.findings-emnlp.1010.bib",
   "title": "ACL Anthology canonical BibTeX for Consistent Discourse-level TRE",
   "summary": "Canonical .bib export (fan-strube-2025-consistent): exact author/title/booktitle/pages 18605-18622/doi 10.18653/v1/2025.findings-emnlp.1010 -- source for the pinned BibTeX (re-keyed Fan2025)."},
  {"index": 8, "url": "https://www.semanticscholar.org/",
   "title": "Semantic Scholar batch BibTeX (NeSTR arXiv:2512.07218; When Silence arXiv:2602.04755)",
   "summary": "Semantic Scholar resolved both arXiv papers (2/2 found), supplying author lists and DOIs (10.48550/arXiv.2512.07218; 10.48550/arXiv.2602.04755); used to seed hand-finalized @inproceedings entries with the AAAI-2026 / ICLR-2026 venue notes."},
  {"index": 9, "url": "https://arxiv.org/abs/2508.20828",
   "title": "GDLLM: A Global Distance-aware Modeling Approach Based on LLMs for Event Temporal Relation Extraction (EMNLP Findings 2025)",
   "summary": "Adversarial-scout near-neighbor: GAT distance-aware + LLM probability distributions for event-TRE; performs single-label (hard) classification -- a commit contract with no disjunction/abstention, so it does NOT match our distinctive moves. Optional backup only."},
  {"index": 10, "url": "https://arxiv.org/abs/2511.13095",
   "title": "BeDiscovER: The Benchmark of Discourse Understanding in the Era of Reasoning Language Models (EACL 2026)",
   "summary": "Adversarial-scout near-neighbor: a 52-dataset discourse-understanding BENCHMARK (incl. temporal relation extraction), not a reasoning method; no relation-algebra disjunction or closure-abstention. Optional backup only."},
  {"index": 11, "url": "file:///ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_research_1/research_out.json",
   "title": "Iter-2 Local-Reader/Prolog-Discharge/CLUTRR dossier (art_Dm5vYXmD1R8h) -- internal dependency",
   "summary": "Source of (a) the four consistency citations NOT to be duplicated here (2510.15513 / 2502.11425 / 2412.16100 / 2409.14065) and (b) the project's crisp novelty statement: disjunction-preserving abstain-on-collapse output contract + gold-free per-edge closure certificate + redundancy-as-coding-rate, NOT the algebra."},
]

# ----------------------------------------------------------------------------
# Assemble
# ----------------------------------------------------------------------------
out = {
  "title": "Pinned & Differentiated 4 Closest Recent Neuro-Symbolic Temporal / Abstention Neighbors (NeSTR, TReMu, Fan&Strube, When Silence Is Golden)",
  "summary": (
    "Citation-verification bundle retiring the iter-2 reviewer MINOR 'closest recent neighbors not cited'. "
    "Independently re-verified and BibTeX-pinned four 2025-2026 neighbors -- NeSTR (Liang2026, AAAI 2026, "
    "arXiv:2512.07218; generate-then-abductively-REPAIR), TReMu (Ge2025, Findings-ACL 2025, 2025.findings-acl.972, "
    "arXiv:2502.01630; neuro-symbolic CODE-GEN/COMMIT over dialogue memory), Consistent Discourse-level TRE "
    "(Fan2025, Findings-EMNLP 2025, 2025.findings-emnlp.1010; single-label F1 COMMIT we invert), and When Silence "
    "Is Golden (Zhou2026, ICLR 2026, arXiv:2602.04755; LEARNED/TRAINED abstention). Provides per-paper "
    "objective_summary, output_contract, one_sentence_differentiation, verified BibTeX in AuthorYYYY project key "
    "style, a drop-in differentiation_paragraph, two ID corrections (TReMu full name/setting; TReMu pages "
    "18974-18988 not 18605-18622), and an adversarial novelty-scout result confirming NO exact-match competitor "
    "preserves a relation-algebra disjunction AND abstains on closure-collapse (near-but-non-matching GDLLM "
    "2508.20828 and BeDiscovER 2511.13095 noted). $0, pure-web, ready for GEN_PAPER_TEXT related work."
  ),
  "answer": answer,
  "neighbors": neighbors,
  "differentiation_paragraph": differentiation_paragraph,
  "id_corrections": [
    "Hypothesis short-name 'Towards Neuro-Symbolic Temporal Reasoning for LLMs (Findings-ACL 2025)' = TReMu, arXiv:2502.01630, Findings-ACL 2025 (2025.findings-acl.972); its setting is multi-session DIALOGUE temporal QA with LLM-generated Python over summarized memory, NOT single-document TRE.",
    "TReMu page range correction: the planner's 18605-18622 belongs to P3 (Fan & Strube); TReMu's correct pages are 18974-18988 (ACL Anthology canonical .bib).",
    "NeSTR authors pinned from the arXiv page: Feng Liang, Weixin Zeng, Runhao Zhao, Xiang Zhao (planner did not list authors).",
    "When Silence Is Golden second author canonical spelling is 'Chang Jin' per the arXiv author page (Semantic Scholar's disambiguated 'Changhong Jin' was NOT used).",
  ],
  "no_closer_competitor_found": True,
  "novelty_scout_note": (
    "Three targeted queries combining 'preserve relation-algebra disjunction' with 'abstain on path-consistency / "
    "closure collapse' over LLM-extracted temporal/spatial relations returned no exact-match competitor (only "
    "encyclopedic references). Nearest extras GDLLM (arXiv:2508.20828, EMNLP Findings 2025; single-label hard "
    "classification ETRE) and BeDiscovER (arXiv:2511.13095, EACL 2026; discourse benchmark, not a method) are real "
    "but do NOT perform our distinctive disjunction-preserving abstain-on-collapse moves. Confirming no such "
    "competitor exists is itself novelty-supporting."
  ),
  "optional_backups": [
    {"key": "Mu2025gdllm", "title": "GDLLM: A Global Distance-aware Modeling Approach Based on Large Language Models for Event Temporal Relation Extraction",
     "arxiv_id": "2508.20828", "venue": "Findings of EMNLP 2025", "url": "https://arxiv.org/abs/2508.20828",
     "why_not_a_match": "Single-label hard-classification event-TRE (GAT distance features + LLM prob. distributions); a commit contract with no relation-algebra disjunction and no abstention."},
    {"key": "Li2026bediscover", "title": "BeDiscovER: The Benchmark of Discourse Understanding in the Era of Reasoning Language Models",
     "arxiv_id": "2511.13095", "venue": "EACL 2026 (2026.eacl-long.207)", "url": "https://arxiv.org/abs/2511.13095",
     "why_not_a_match": "A 52-dataset discourse-understanding BENCHMARK (includes temporal relation extraction), not a reasoning method; no disjunction-preservation or closure-abstention."},
  ],
  "iter2_dossier_citations_not_duplicated": ["2510.15513", "2502.11425", "2412.16100", "2409.14065"],
  "iter2_dossier_citation_titles": {
    "2510.15513": "Temporal Referential Consistency: Do LLMs Favor Sequences Over Absolute Time References? (Bajpai & Chakraborty, EMNLP 2025)",
    "2502.11425": "Counterfactual-Consistency Prompting for Relative Temporal Understanding in LLMs (Kim & Hwang, ACL 2025)",
    "2412.16100": "Logical Consistency of Large Language Models in Fact-checking (Ghosh et al., ICLR 2025)",
    "2409.14065": "Temporally Consistent Factuality Probing for LLMs (Bajpai et al., EMNLP 2024)",
  },
  "bibtex_block": "\n\n".join([BIB_LIANG, BIB_GE, BIB_FAN, BIB_ZHOU]),
  "sources": sources,
  "follow_up_questions": [
    "Should the related-work paragraph also explicitly contrast our gold-free per-edge closure CERTIFICATE against the established single-label commit line (Eirew2025 ILP-commit, Kougia2024), to make the 'output-contract inversion' framing span both the new neighbors and the prior baselines in one sweep?",
    "Does NeSTR's 'verification' step compute any algebraic consistency check (e.g., interval-algebra composition) that we should cite as the closest mechanistic precedent, even though it repairs-to-commit rather than abstains -- and is its code/benchmark public enough to run as an additional matched baseline?",
    "Should GDLLM (2508.20828) be promoted from optional backup to a cited single-label-commit ETRE baseline given it is an EMNLP-2025 LLM-based event-TRE method directly in our task family, or kept out to avoid padding the four-paper deliverable?",
  ],
}

os.makedirs(WS, exist_ok=True)
path = os.path.join(WS, "research_out.json")
with open(path, "w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print("WROTE", path, os.path.getsize(path), "bytes")
print("neighbors:", len(out["neighbors"]), "| sources:", len(out["sources"]))
# quick BibTeX brace-balance sanity check
for b in [BIB_LIANG, BIB_GE, BIB_FAN, BIB_ZHOU]:
    key = b.split("{",1)[1].split(",",1)[0]
    assert b.count("{") == b.count("}"), f"brace imbalance in {key}"
    print("  bibtex OK, balanced braces:", key)
