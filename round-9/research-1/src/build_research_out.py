#!/usr/bin/env python3
"""Assemble research_out.json + research_report.md for iter-9 NOVELTY-MAJOR research.

Pure-web ($0) research. Closes the ACL-Knowledge-Extraction reviewer NOVELTY MAJOR
for the closure-certificate paper by pinning two literature clusters
(RE NO_RELATION/NA + hallucination-resistant RE; training-free structural / logical
premise verification + KG-triple hallucination detection), dropping the untenable
'absent-relation hallucination is not derivable a priori' assertion, and re-carving
a defensible two-part delta + ACL-KE-primary / NeSy-fallback venue framing.

All facts below were verified by direct web fetch + fetch_grep over the arXiv
abstract pages and PDFs (see SOURCES). Builds on iter-8 false-premise dossier
art_oUhZgMSjf7lm; reuses its keys verbatim.
"""
import json
import os

OUT_DIR = "/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_9/gen_art/gen_art_research_1"

# ---------------------------------------------------------------------------
# SOURCES (numbered; index matches in-text [n] citations in `answer`)
# ---------------------------------------------------------------------------
sources = [
    {"index": 1,
     "url": "https://arxiv.org/abs/2508.14391",
     "title": "Hallucination-Resistant Relation Extraction via Dependency-Aware Sentence Simplification and Two-tiered Hierarchical Refinement (DEPTH; Yang et al.)",
     "summary": "arXiv abstract page (v2, last revised 1 Feb 2026; v1 20 Aug 2025). Authors Yupei Yang, Fan Feng, Lin Yang, Wanxi Deng, Lin Qu, Biwei Huang, Shikui Tu, Lei Xu. cs.CL/cs.AI. Headline: Qwen2.5-14B over-predicts relations on 96.9% of NO-RELATION instances on SciERC; DEPTH = dependency-aware simplification + two-tiered hierarchical refinement + causality-driven RLHF reward model. 'Preprint. Under review.' (no published venue)."},
    {"index": 2,
     "url": "https://arxiv.org/pdf/2508.14391",
     "title": "DEPTH PDF (grepped) — 96.9% NO-RELATION over-prediction, 45/1475, v2 results, 8 benchmarks, RLHF/PPO",
     "summary": "fetch_grep extraction. VERBATIM: 'Qwen2.5-14B-Instruct incorrectly predicts a relation in 96.9% of NO-RELATION instances on SciERC, revealing a severe hallucination problem.' Also: 'correctly identifies NO-RELATION in only 45 out of 1,475 instances, misclassifying the remaining 1,430 as having some relation'; 'tendency to overpredict relations: even when no meaningful connection exists ... LLMs often hallucinate a spurious relation rather than outputting NO-RELATION'. v2 results: 'reduces the average hallucination rate to 7.9% while achieving a 9.3% improvement in average F1 ... over existing LLM-based extraction baselines' on EIGHT benchmarks (TACRED, TACREV, Re-TACRED, NYT11, SciERC, FOBIE, DDI, SemEval). Method: shortest-dependency-path Grounding + sentence-level Refinement + causality-driven reward model + PPO/RLHF fine-tuning (NOT training-free)."},
    {"index": 3,
     "url": "https://arxiv.org/abs/2408.13889",
     "title": "LLM with Relation Classifier for Document-Level Relation Extraction (Li et al.)",
     "summary": "arXiv abstract page (v2, 7 Dec 2024; v1 25 Aug 2024). Authors Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang. cs.CL. Identifies 'the dispersion of attention by LLMs due to entity pairs without relations' as the key cause of the DocRE LLM gap; introduces a classifier-LLM hybrid (classifier pre-selects candidate pairs with potential relations, LLM classifies only those). No authoritative published venue (arXiv preprint; Semantic Scholar's 'IEEE Transactions on Big Data' tag is unconfirmed)."},
    {"index": 4,
     "url": "https://arxiv.org/pdf/2408.13889",
     "title": "LLM+Relation-Classifier PDF (grepped) — attention-dispersion, NA framing, DocRED/Re-DocRED",
     "summary": "fetch_grep extraction. VERBATIM: 'identifying the dispersion of attention by LLMs due to entity pairs without relations as a key factor'. Figure 1: 'Statistics on the number of entity pairs in DocRED and Re-DocRED training set. NA: entity pairs that do not express any relation. Rel: entity pairs expressing relations.' Datasets = DocRED + Re-DocRED. Code: github.com/wisper12933/LMRC. Single-hop/schema-bound NA classification by trained pre-filter; not deductive/multi-hop, not gold-free."},
    {"index": 5,
     "url": "https://arxiv.org/abs/2511.08143",
     "title": "Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction (RelPrior; Pi et al.)",
     "summary": "arXiv abstract page (v1, 11 Nov 2025, 17 pages). Authors Qiankun Pi, Yepeng Sun, Jicang Lu, Qinlong Fan, Ningbo Huang, Shiyu Wang. cs.CL/cs.AI. Two challenges: (1) 'Numerous unrelated entity pairs introduce noise and interfere with the relation prediction for truly related entity pairs'; (2) relation labels beyond the predefined set are treated as errors. RelPrior uses a binary relation prior to filter irrelevant pairs + a predefined-relation prior to match entities. arXiv preprint (no published venue)."},
    {"index": 6,
     "url": "https://arxiv.org/pdf/2511.08143",
     "title": "RelPrior PDF (grepped) — 'unrelated entity pairs' filtering, binary-classifier prior, DocRED/Re-DocRED",
     "summary": "fetch_grep extraction. VERBATIM challenge (1): 'Numerous unrelated entity pairs introduce noise and interfere with the relation prediction for truly related entity pairs.' Method: 'fine-tuning a binary classification LLM that determines whether there is a relation between entity pairs' (Step1 unrelated-pair filter; Step2 relation-as-prior matching). Keywords: 'Document-level relation extraction; Unrelated entity pairs; Relation as a prior.' Datasets: 'document-level relation extraction public datasets DocRED and RE-DocRED.' Trained (fine-tuned classifier); single-hop NA filtering, not deductive multi-hop."},
    {"index": 7,
     "url": "https://arxiv.org/abs/2504.06438",
     "title": "Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning (Qin et al.)",
     "summary": "arXiv abstract page (v2, last revised 16 Feb 2026; v1 8 Apr 2025). Authors Yuehan Qin, Shawn Li, Yi Nian, Xinyan Velocity Yu, Yue Zhao, Xuezhe Ma. cs.CL/cs.AI. Comments field: 'TMLR 2026'. Transforms a query into a logical representation, then uses retrieval-augmented generation (RAG) to validate each premise against factual sources, and feeds verification into the prompt. 'does not require access to model logits or large-scale fine-tuning' — but DOES require external retrieval/KB. THE closest structural-premise-verification neighbor."},
    {"index": 8,
     "url": "https://arxiv.org/pdf/2504.06438",
     "title": "Premise Verification PDF (grepped) — logicalize+RAG-over-external-KG, no-logits/no-fine-tuning, TMLR 02/2026, KG-FPQ/CREAK",
     "summary": "fetch_grep extraction. Page header on every page: 'Published in Transactions on Machine Learning Research (02/2026)' (CONFIRMS TMLR 2026). VERBATIM method: 'Our method first transforms a user's query into a logical representation, then applies retrieval-augmented generation (RAG) to assess the validity of each premise using factual sources' and 'transform the user's query into a logical form ... employ retrieval-augmented generation (RAG) to check the accuracy of these statements against a knowledge graph.' VERBATIM cost claim: 'does not require access to model logits or large-scale fine-tuning'. Datasets: KG-FPQ (Zhu et al. 2024, from KoPL/Wikidata) + CREAK. EXTERNAL-KB/RAG, atomic-premise, world-fact check (NOT document-internal, NOT deductive-closure)."},
    {"index": 9,
     "url": "https://arxiv.org/abs/2407.10793",
     "title": "GraphEval: A Knowledge-Graph Based LLM Hallucination Evaluation Framework (Sansford et al.)",
     "summary": "arXiv abstract page (v1, 15 Jul 2024). Authors Hannah Sansford, Nicholas Richardson, Hermina Petric Maretic, Juba Nait Saada (Univ. of Bristol / Amazon Science). cs.CL/cs.AI/cs.LG. Comments: 'to be published at KiL'24: Workshop on Knowledge-infused Learning co-located with 30th ACM KDD Conference, August 26, 2024, Barcelona, Spain.' Builds a KG of (subject,predicate,object) triples from a response and feeds each triple to an NLI model to check consistency vs the provided context; GraphCorrect rectifies. FIRST AUTHOR = Sansford (NOT Wang — corrects the planner's tentative 'Wang2024GraphEval' key)."},
    {"index": 10,
     "url": "https://arxiv.org/pdf/2407.10793",
     "title": "GraphEval PDF (grepped) — triple-level NLI vs PROVIDED CONTEXT, balanced-accuracy gain, GraphCorrect, world-knowledge out-of-scope",
     "summary": "fetch_grep extraction. VERBATIM: 'identifies the specific triples in the KG that are prone to hallucinations'; 'using our approach in conjunction with state-of-the-art natural language inference (NLI) models leads to an improvement in balanced accuracy on various hallucination benchmarks, compared to using the raw NLI models'. Scope (VERBATIM): 'we focus on the problem of detecting hallucinations with respect to the provided context ... detecting hallucinations that have deviated from the LLM's original training data is out of the scope of this work'; binary classification, 0=consistent given provided context, 1=>=1 inconsistency. Faithfulness-vs-context NLI on single triples (NOT deductive, NOT a no-path certificate); needs a trained NLI model. GraphCorrect = KG-structure correction."},
    {"index": 11,
     "url": "https://openreview.net/group?id=KDD.org/2024/Workshop/KiL",
     "title": "KDD 2024 Workshop KiL (OpenReview) + CEUR-WS Vol-3894 — GraphEval venue confirmation",
     "summary": "OpenReview/CEUR confirm GraphEval venue: KiL 2024 (4th International Workshop on Knowledge-infused Learning, co-located with ACM SIGKDD/KDD 2024, 26 Aug 2024, Barcelona), 'KiL 2024 Oral', CEUR-WS Vol-3894; Amazon Science PDF cites 'Proceedings of the Fourth ACM SIGKDD Workshop on Knowledge-infused Learning', pages 20-31. Authoritative venue for the Sansford2024GraphEval BibTeX."},
    {"index": 12,
     "url": "https://aclanthology.org/2025.coling-main.698/",
     "title": "KG-FPQ: Evaluating Factuality Hallucination in LLMs with Knowledge Graph-based False Premise Questions (COLING 2025)",
     "summary": "Adjacency / triangulation. KG-FPQ = ~178k false-premise questions across three knowledge domains constructed by editing KG triples (KoPL/Wikidata). Confirms that the false-premise QA datasets the structural-verification cluster uses are SINGLE-TRIPLE-LEVEL (one edited subject-relation-object fact), not compositional/multi-hop derivation premises — reinforcing DELTA-1. This is the dataset Qin2026PremiseVerification [8] evaluates on."},
    {"index": 13,
     "url": "https://openreview.net/pdf?id=aolJqJ50ZA",
     "title": "Breadth probe — cross-document / multi-hop DocRE infers relations via reasoning paths (no deductive no-path abstention)",
     "summary": "Representative of the time-boxed breadth search ('document-level relation extraction deductive closure abstain'; 'transitive relation hallucination KG abstain'). Multi-hop / cross-document DocRE work (e.g. CodRED reasoning-path bridging, multi-hop evidence retrieval arXiv:2212.10786) uses reasoning paths to INFER present relations, not to issue a no-derivation-path certificate that ABSTAINS on absent relations. Confirms the deductive-multi-hop-NA (abstain-on-no-path) niche is unclaimed — strengthens DELTA-1/DELTA-2 novelty."},
    {"index": 14,
     "url": "https://www.paperdigest.org/2020/04/recent-papers-on-relation-extraction/",
     "title": "Li2024 venue cross-check — listed as arxiv-cs.CL 2024-08 (no authoritative published venue)",
     "summary": "Triangulation of the LLM+Relation-Classifier publication venue. PaperDigest and ResearchGate list arXiv:2408.13889 as 'arxiv-cs.CL, 2024-08' with no peer-reviewed venue; the Semantic Scholar 'IEEE Transactions on Big Data' association is uncorroborated. BibTeX therefore pins it as an arXiv preprint with a venue-unconfirmed note."},
]

# ---------------------------------------------------------------------------
# WORKSTREAM 1 — RE NO_RELATION / NA + hallucination-resistant RE
# ---------------------------------------------------------------------------
workstream_1 = [
    {
        "key": "Yang2025DEPTH",
        "role": "PRIMARY WS1 anchor — proves FACT A (LLMs over-predict / hallucinate relations on NO_RELATION pairs) is a KNOWN, quantified, single-hop RE phenomenon",
        "title": "Hallucination-Resistant Relation Extraction via Dependency-Aware Sentence Simplification and Two-tiered Hierarchical Refinement",
        "authors": "Yupei Yang, Fan Feng, Lin Yang, Wanxi Deng, Lin Qu, Biwei Huang, Shikui Tu, Lei Xu",
        "venue": "arXiv preprint 2508.14391 (cs.CL); v1 20 Aug 2025, v2 1 Feb 2026 ('Preprint. Under review.'). No peer-reviewed venue confirmed.",
        "ids": "arXiv:2508.14391; DOI 10.48550/arXiv.2508.14391",
        "na_framing": "Over-prediction of relations on NO-RELATION pairs is framed as a 'severe hallucination problem': LLMs 'hallucinate a spurious relation rather than outputting NO-RELATION' even when 'no meaningful connection exists between an entity pair'. This is a SINGLE-HOP, SENTENCE-LEVEL, fixed-schema decision over one candidate (head, tail) pair (SciERC label set USED-FOR / FEATURE-OF / ... / NO-RELATION).",
        "detection_method_type": "TRAINED. Two-stage pipeline: (1) Grounding module distils each sentence to the shortest dependency path (SDP) between the pair, converted to a natural-language structural cue; (2) Refinement module aggregates local predictions and revises them under sentence-level constraints. Reliability is further trained via a causality-driven reward model (causal factorization to resist reward hacking) + PPO/RLHF fine-tuning. NOT gold-free, NOT training-free, NOT schema-free.",
        "datasets": "Eight sentence/short-text RE benchmarks: TACRED, TACREV, Re-TACRED, NYT11 (news); SciERC, FOBIE (scientific); DDI (biomedical); SemEval (general). NO document-level / multi-hop benchmark.",
        "headline_findings": "VERBATIM: 'Qwen2.5-14B-Instruct incorrectly predicts a relation in 96.9% of NO-RELATION instances on SciERC, revealing a severe hallucination problem.' Table 1: correctly identifies NO-RELATION in only 45/1,475 instances (1,430 misclassified). v2 result: 'reduces the average hallucination rate to 7.9% while achieving a 9.3% improvement in average F1 score over existing LLM-based extraction baselines' across the eight benchmarks.",
        "verbatim_quotes": [
            "Qwen2.5-14B-Instruct incorrectly predicts a relation in 96.9% of NO-RELATION instances on SciERC, revealing a severe hallucination problem. (Abstract)",
            "even when no meaningful connection exists between an entity pair, LLMs often hallucinate a spurious relation rather than outputting NO-RELATION. ... Qwen2.5-14B-Instruct correctly identifies NO-RELATION in only 45 out of 1,475 instances, mis-classifying the remaining 1,430 as having some relation (see Table 1). (Sec. Introduction)",
            "Experiments on eight well-established benchmarks demonstrate that DEPTH reduces the average hallucination rate to 7.9% while achieving a 9.3% improvement in average F1 score over existing LLM-based extraction baselines. (Abstract, v2)"
        ],
        "why_it_is_the_RE_NA_foil": "It is the strongest, most-quantified statement that confident absent-relation fabrication is REAL and EXPECTED at the single-hop level. We therefore CITE it to DROP the untenable 'not derivable a priori' assertion, and contrast on setting (its NO-RELATION is one fixed-schema label for one mention/pair; ours is a compositional 'no derivation path between X and Y' over MULTIPLE composed edges) and method (it FIXES extraction via SDP grounding + RLHF; we DETECT via gold-free/training-free deductive closure, no fine-tuning).",
        "version_note": "CORRECTION to planner pin: planner cited v1 numbers (7.0% hallucination / 17.2% F1 / six benchmarks) and a 'DEPTH:'-prefixed title. The CURRENT v2 (1 Feb 2026) reports 7.9% / 9.3% over EIGHT benchmarks, and the v2 title has no 'DEPTH:' prefix (DEPTH is the framework name introduced in the abstract). Use the v2 numbers; the 96.9% SciERC over-prediction quote is unchanged and verbatim."
    },
    {
        "key": "Li2024RelClassifier",
        "role": "WS1 document-level NA foil — attributes the DocRE LLM gap to entity pairs WITHOUT relations and pre-filters with a trained classifier",
        "title": "LLM with Relation Classifier for Document-Level Relation Extraction",
        "authors": "Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang",
        "venue": "arXiv preprint 2408.13889 (cs.CL); v1 25 Aug 2024, v2 7 Dec 2024. No peer-reviewed venue authoritatively confirmed (Semantic Scholar's 'IEEE Transactions on Big Data' tag uncorroborated; PaperDigest/ResearchGate list it as arxiv-cs.CL).",
        "ids": "arXiv:2408.13889; DOI 10.48550/arXiv.2408.13889; code github.com/wisper12933/LMRC",
        "na_framing": "Diagnoses the DocRE LLM gap as 'the dispersion of attention by LLMs due to entity pairs without relations'. Defines NA explicitly: 'NA: entity pairs that do not express any relation. Rel: entity pairs expressing relations.' The 'candidate space' is dominated by NA pairs (class imbalance). Still SINGLE-HOP per pair and bound to the DocRED relation SCHEMA.",
        "detection_method_type": "TRAINED classifier-LLM hybrid: a relation classifier pre-selects entity-pair candidates 'that exhibit potential relations', and only those are fed to the LLM for final classification, focusing attention away from no-relation pairs. NOT gold-free, NOT training-free; it solves NA by FILTERING, not by a deductive abstention certificate.",
        "datasets": "Document-level RE benchmarks DocRED and Re-DocRED (Figure 1 reports NA vs Rel entity-pair statistics on both training sets).",
        "headline_findings": "The classifier-LLM method 'significantly outperforms recent LLM-based DocRE models and narrows the performance gap with state-of-the-art BERT-based models', by directing LLM attention to relation-expressing pairs.",
        "verbatim_quotes": [
            "identifying the dispersion of attention by LLMs due to entity pairs without relations as a key factor. (Abstract)",
            "NA: entity pairs that do not express any relation. Rel: entity pairs expressing relations. (Figure 1 caption)",
            "begins with a classifier designed to select entity pair candidates that exhibit potential relations and then feed them to LLM for final relation classification. (Abstract)"
        ],
        "why_it_is_the_RE_NA_foil": "It is the document-level instance of the NA problem and the closest in SETTING (DocRED/Re-DocRED, the same corpora our located-in/kinship work uses). But its NA is still a per-pair, schema-bound classification handled by a TRAINED pre-filter; it never asks whether a MULTI-HOP DERIVATION PATH exists and never abstains by deduction. Our certificate is gold-free, training-free, schema-free, and compositional."
    },
    {
        "key": "Pi2025RelPrior",
        "role": "WS1 newest document-level NA foil — 'unrelated entity pairs introduce noise', filtered by a binary relation prior",
        "title": "Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction",
        "authors": "Qiankun Pi, Yepeng Sun, Jicang Lu, Qinlong Fan, Ningbo Huang, Shiyu Wang",
        "venue": "arXiv preprint 2511.08143 (cs.CL); v1 11 Nov 2025 (17 pages). No peer-reviewed venue confirmed.",
        "ids": "arXiv:2511.08143; DOI 10.48550/arXiv.2511.08143",
        "na_framing": "Challenge (1): 'Numerous unrelated entity pairs introduce noise and interfere with the relation prediction for truly related entity pairs.' Challenge (2): valid relations outside the predefined schema are treated as errors. Both are single-hop, schema-bound concerns over the entity-pair candidate set.",
        "detection_method_type": "TRAINED. RelPrior fine-tunes a binary-classification LLM as a PRIOR to decide whether two entities are correlated (Step 1: filter unrelated pairs / reduce noise) and uses a predefined-relation prior to match entities for triple extraction (Step 2). NOT gold-free, NOT training-free; NA is handled by binary FILTERING, not deductive abstention.",
        "datasets": "Two document-level RE benchmarks: DocRED and Re-DocRED ('document-level relation extraction public datasets DocRED and RE-DocRED').",
        "headline_findings": "'Extensive experiments on two benchmarks demonstrate that RelPrior achieves state-of-the-art performance, surpassing existing LLM-based methods.' Binary relation prior reduces prediction noise from unrelated pairs; predefined-relation prior avoids misjudgement from strict labeling.",
        "verbatim_quotes": [
            "Numerous unrelated entity pairs introduce noise and interfere with the relation prediction for truly related entity pairs. (Abstract, challenge 1)",
            "RelPrior utilizes binary relation as a prior to extract and determine whether two entities are correlated, thereby filtering out irrelevant entity pairs and reducing prediction noise. (Abstract)",
            "we propose fine-tuning a binary classification LLM that determines whether there is a relation between entity pairs. (Sec. Method)"
        ],
        "why_it_is_the_RE_NA_foil": "Most recent (Nov 2025) confirmation that 'unrelated entity pairs' / NA handling is an active DocRE concern solved by a TRAINED binary filter. Same DocRED/Re-DocRED setting as ours, same single-hop schema-bound NA decision, same training requirement — the exact contrast our gold-free/training-free compositional deductive certificate is positioned against."
    },
]

# ---------------------------------------------------------------------------
# WORKSTREAM 2 — training-free structural / logical premise verification
#                + KG-triple hallucination detection
# ---------------------------------------------------------------------------
ws2_papers = [
    {
        "key": "Qin2026PremiseVerification",
        "role": "CLOSEST METHOD NEIGHBOR — training-free, no-logits premise verification, BUT external-KB/RAG and atomic-premise",
        "title": "Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning",
        "authors": "Yuehan Qin, Shawn Li, Yi Nian, Xinyan Velocity Yu, Yue Zhao, Xuezhe Ma",
        "venue": "Transactions on Machine Learning Research (TMLR), 02/2026 (CONFIRMED: page header 'Published in Transactions on Machine Learning Research (02/2026)'; arXiv Comments field 'TMLR 2026').",
        "ids": "arXiv:2504.06438; DOI 10.48550/arXiv.2504.06438; v1 8 Apr 2025, v2 16 Feb 2026",
        "method": "(1) Transform the user's query into a LOGICAL representation/form highlighting key entities and relations; (2) apply retrieval-augmented generation (RAG) to assess the validity of EACH PREMISE against EXTERNAL FACTUAL SOURCES (a knowledge graph / factual corpus); (3) integrate the verification result into the LLM prompt to keep the final output factually consistent. Proactive (checks before generation).",
        "requires_external_KB": "YES — RAG over external factual sources / a knowledge graph (KG-FPQ is built from KoPL/Wikidata). The premise is checked against WORLD facts, not the input document.",
        "requires_training": "NO large-scale fine-tuning and NO access to model logits ('does not require access to model logits or large-scale fine-tuning'), but DOES require a retriever + external corpus/KG.",
        "granularity_logic": "ATOMIC premises of a single query (e.g. 'penicillin treats shellfish allergy'); a logical FORM is extracted but validity is decided by external-fact RETRIEVAL, not by iterated deductive closure over a composition table. Not compositional/multi-hop, not a no-derivation-path test.",
        "datasets": "KG-FPQ (Zhu et al. 2024; true/false-premise questions from the KoPL Wikidata subset) and CREAK (commonsense reasoning about entity knowledge).",
        "results": "Reduces hallucinations and improves factual accuracy without logits/fine-tuning; positioned as seamlessly integrable into existing LLM pipelines.",
        "verbatim_quotes": [
            "Our method first transforms a user's query into a logical representation, then applies retrieval-augmented generation (RAG) to assess the validity of each premise using factual sources. (Abstract)",
            "transform the user's query into a logical form that highlights key entities or relations. We then employ retrieval-augmented generation (RAG) to check the accuracy of these statements against a knowledge graph. (Sec. Method)",
            "does not require access to model logits or large-scale fine-tuning. (Abstract)"
        ],
        "why_it_is_the_method_foil": "It is the single closest method neighbor: training-free, logits-free premise verification via a logicalized query. The METHOD delta hinges entirely on its EXTERNAL-KB/RAG world-fact check vs our DOCUMENT-INTERNAL, no-external-KB, deductive-closure premise check, and on its ATOMIC premise vs our COMPOSITIONAL multi-edge derivation premise."
    },
    {
        "key": "Sansford2024GraphEval",
        "role": "KG-triple hallucination-detection foil — triple-level NLI vs PROVIDED CONTEXT (faithfulness, not deduction)",
        "title": "GraphEval: A Knowledge-Graph Based LLM Hallucination Evaluation Framework",
        "authors": "Hannah Sansford, Nicholas Richardson, Hermina Petric Maretic, Juba Nait Saada",
        "venue": "KiL 2024 — 4th International Workshop on Knowledge-infused Learning, co-located with ACM SIGKDD/KDD 2024 (26 Aug 2024, Barcelona); CEUR-WS Vol-3894; pages 20-31; 'KiL 2024 Oral'. (Univ. of Bristol / Amazon Science.)",
        "ids": "arXiv:2407.10793; DOI 10.48550/arXiv.2407.10793; OpenReview KDD.org/2024/Workshop/KiL",
        "method": "Extract a knowledge graph of (subject, predicate, object) triples from the LLM response, then feed EACH triple to a natural-language-inference (NLI) model to check consistency against the PROVIDED grounding CONTEXT; flags the specific triples prone to hallucination. GraphCorrect extends this to correct hallucinations by leveraging KG structure.",
        "requires_external_KB": "NO external world KB, but checks against the PROVIDED CONTEXT (in-prompt grounding) — explicitly NOT document-internal deductive composition, and explicitly NOT world-knowledge ('detecting hallucinations that have deviated from the LLM's original training data is out of the scope').",
        "requires_training": "YES — relies on a (state-of-the-art) trained NLI model as the per-triple consistency checker.",
        "granularity_logic": "SINGLE-TRIPLE faithfulness via NLI entailment/consistency (binary: 0 consistent given context / 1 contains >=1 inconsistency). No iterated closure, no composition table, no abstain-on-no-path; it cannot certify that NO derivation path exists between two entities.",
        "datasets": "Various hallucination benchmarks (faithfulness-vs-context, e.g. summarization-consistency style); improvement in balanced accuracy over raw NLI models.",
        "results": "Using GraphEval with SOTA NLI models improves balanced accuracy on hallucination benchmarks vs raw NLI; GraphCorrect rectifies the majority of hallucinations.",
        "verbatim_quotes": [
            "Our method identifies the specific triples in the KG that are prone to hallucinations. (Abstract)",
            "using our approach in conjunction with state-of-the-art natural language inference (NLI) models leads to an improvement in balanced accuracy on various hallucination benchmarks, compared to using the raw NLI models. (Abstract)",
            "we focus on the problem of detecting hallucinations with respect to the provided context ... detecting hallucinations that have deviated from the LLM's original training data is out of the scope of this work. (Sec. Problem setting)"
        ],
        "why_it_is_the_method_foil": "Represents the KG/triple-structural hallucination-detection family. It is STRUCTURAL and KG-based like ours, which makes the contrast sharp: GraphEval verifies single triples for FAITHFULNESS-to-context with a TRAINED NLI MODEL, whereas our certificate verifies a COMPOSITIONAL multi-edge premise by training-free, model-free symbolic deductive closure and abstains when no derivation path exists.",
        "key_correction": "Planner tentatively suggested key 'Wang2024GraphEval' and asked to verify the first author. First author is Hannah SANSFORD (not Wang); key set to Sansford2024GraphEval. This also avoids a collision/confusion with the inherited dossier key Wang2023 (self-consistency)."
    },
]

method_delta_table = {
    "axes": ["external KB / retrieval", "requires training / fine-tuning", "requires a trained model (NLI/classifier)",
             "granularity", "logic", "absent-relation handling", "operates on"],
    "rows": [
        {"method": "DEPTH [Yang2025DEPTH]",
         "external KB / retrieval": "No (uses dependency parse of the sentence)",
         "requires training / fine-tuning": "Yes (causality-driven reward model + PPO/RLHF)",
         "requires a trained model (NLI/classifier)": "Yes (fine-tuned LLM extractor + reward model)",
         "granularity": "single (head, tail) pair in one sentence",
         "logic": "learned extraction + refinement (no symbolic deduction)",
         "absent-relation handling": "predict NO-RELATION label after grounding+refinement",
         "operates on": "sentence-level RE (fixed schema)"},
        {"method": "LLM+Relation-Classifier [Li2024RelClassifier]",
         "external KB / retrieval": "No",
         "requires training / fine-tuning": "Yes (trained relation classifier pre-filter)",
         "requires a trained model (NLI/classifier)": "Yes (classifier)",
         "granularity": "single entity pair (document-level candidate)",
         "logic": "learned filtering (no deduction)",
         "absent-relation handling": "filter NA pairs out before LLM classification",
         "operates on": "document-level RE (DocRED/Re-DocRED, fixed schema)"},
        {"method": "RelPrior [Pi2025RelPrior]",
         "external KB / retrieval": "No",
         "requires training / fine-tuning": "Yes (fine-tuned binary-relation classifier as prior)",
         "requires a trained model (NLI/classifier)": "Yes (binary classifier)",
         "granularity": "single entity pair",
         "logic": "learned filtering + relation-as-prior matching (no deduction)",
         "absent-relation handling": "binary prior filters 'unrelated entity pairs'",
         "operates on": "document-level RE (DocRED/Re-DocRED, fixed schema)"},
        {"method": "Premise Verification [Qin2026PremiseVerification]",
         "external KB / retrieval": "YES (RAG over external factual sources / KG)",
         "requires training / fine-tuning": "No large-scale fine-tuning; no logits (but needs retriever+corpus)",
         "requires a trained model (NLI/classifier)": "No NLI, but a retriever + external KG",
         "granularity": "atomic premise of a single query",
         "logic": "logicalize query, then external-fact RETRIEVAL check (not iterated deduction)",
         "absent-relation handling": "flag query as false-premise if external facts contradict a premise",
         "operates on": "query-side world-fact premises (KG-FPQ/CREAK)"},
        {"method": "GraphEval [Sansford2024GraphEval]",
         "external KB / retrieval": "No external KB; checks vs PROVIDED CONTEXT",
         "requires training / fine-tuning": "Inference-time, but uses a trained NLI model",
         "requires a trained model (NLI/classifier)": "Yes (NLI model)",
         "granularity": "single response triple",
         "logic": "NLI entailment/consistency (no deduction, no closure)",
         "absent-relation handling": "none (faithfulness-to-context only; cannot certify no-path)",
         "operates on": "response triples vs grounding context"},
        {"method": "Closure certificate (OURS)",
         "external KB / retrieval": "NO external KB; document-internal only",
         "requires training / fine-tuning": "NO (training-free, model-free symbolic closure)",
         "requires a trained model (NLI/classifier)": "NO (exact composition table)",
         "granularity": "COMPOSITIONAL multi-edge relational premise ('a derivation path exists between X and Y')",
         "logic": "iterated DEDUCTIVE CLOSURE over an exact composition table",
         "absent-relation handling": "ABSTAIN when no derivation path exists (no-derivation certificate)",
         "operates on": "document-internal composed edges (kinship / located-in, multi-hop)"},
    ],
    "reading": "All five recognized methods either (a) require training (DEPTH, LLM+Classifier, RelPrior, GraphEval's NLI), (b) require an external KB/retriever (Premise Verification), or (c) operate at the atomic/single-pair/single-triple level (all of them). NONE issues a gold-free, training-free, no-external-KB, COMPOSITIONAL deductive 'no derivation path exists -> abstain' certificate. That cell is the method delta."
}

workstream_2 = {"papers": ws2_papers, "method_delta_table": method_delta_table}

# ---------------------------------------------------------------------------
# WORKSTREAM 3 — re-carved delta, drop-in related-work, novelty, venue framing
# ---------------------------------------------------------------------------
related_work_paragraph = (
    r"Confident \emph{absent}-relation fabrication is a documented relation-extraction (RE) "
    r"phenomenon: LLM extractors over-predict relations on entity pairs that bear none. "
    r"\citet{Yang2025DEPTH} measure a $96.9\%$ relation rate on \textsc{no-relation} pairs in "
    r"SciERC and counter it with dependency-aware sentence simplification, hierarchical "
    r"refinement, and a causality-driven RLHF reward model; \citet{Li2024RelClassifier} trace "
    r"the document-level LLM gap to ``the dispersion of attention by LLMs due to entity pairs "
    r"without relations'' and pre-filter candidate pairs with a trained classifier; "
    r"\citet{Pi2025RelPrior} likewise filter ``unrelated entity pairs [that] introduce noise'' "
    r"with a binary relation prior. All three, however, target a \emph{single-hop, schema-bound} "
    r"``no label for this pair'' decision solved by better extraction or filtering, not a verdict "
    r"over \emph{composed} edges. The closest structural detectors verify premises against "
    r"\emph{external} knowledge: \citet{Qin2026PremiseVerification} validate each premise of a "
    r"logicalized query by retrieval-augmented generation over factual sources, and "
    r"\citet{Sansford2024GraphEval} check response triples against the \emph{provided context} "
    r"with an NLI model---both atomic and dependent on an external KB, retriever, or trained "
    r"model. The unanswerable / false-premise line \citep{Hu2023,Kirichenko2025,Wen2024} "
    r"addresses sentence-level presuppositions with trained or prompt-based detectors. None of "
    r"these targets a \emph{compositional, multi-hop, document-internal} absent-relation "
    r"premise detected \emph{gold-free, training-free, and without any external KB} by deductive "
    r"closure---the gap this paper fills."
)

novelty_sentence = (
    r"Our contribution is two-fold: (i) a \emph{corpus-robust diagnostic} that confident "
    r"absent-relation fabrication---already documented at the single-hop level "
    r"\citep{Yang2025DEPTH}---becomes, at the compositional/multi-hop/document level, a "
    r"false-premise failure that transfers across readers and corpora and that neither the "
    r"confidence/uncertainty family nor a same-model query-side verifier filters; and (ii) a "
    r"\emph{gold-free, training-free, no-external-KB} structural detector---a no-derivation-path "
    r"closure certificate---evaluated head-to-head against these recognized methods. We claim "
    r"neither that the certificate mechanism is new (it inherits the standard neuro-symbolic "
    r"deduce-then-abstain premise) nor that the raw fabrication \emph{rate} is new "
    r"(\citet{Yang2025DEPTH} already show it single-hop); the novelty is the compositional, "
    r"document-internal reframing together with the gold-free/training-free structural detector "
    r"and its head-to-head evaluation against trained RE refiners, external-KB premise "
    r"verification, and NLI-vs-context triple checks."
)

two_part_delta = {
    "delta_1_setting": (
        r"\textbf{Setting.} We lift absent-relation detection from a single-hop, schema-bound "
        r"\textsc{no\_relation} classification \citep{Yang2025DEPTH,Li2024RelClassifier,Pi2025RelPrior} "
        r"and a sentence-level false premise \citep{Hu2023,Kim2023,Yu2023} to a "
        r"\emph{compositional, multi-hop, document-internal} absent-relation premise---the "
        r"structural claim that ``a derivation path exists between $X$ and $Y$.''"
    ),
    "delta_2_method": (
        r"\textbf{Method.} We detect it with a \emph{gold-free, training-free, no-external-KB} "
        r"deductive-closure certificate (no derivation path $\Rightarrow$ abstain), versus trained "
        r"RE refiners/classifiers \citep{Yang2025DEPTH,Li2024RelClassifier,Pi2025RelPrior}, "
        r"external-KB/RAG premise verification \citep{Qin2026PremiseVerification}, and "
        r"NLI-vs-context triple checks \citep{Sansford2024GraphEval}."
    ),
    "empirical_contrast": (
        "Beyond the setting/method deltas, the paper's own experiments supply the decisive "
        "empirical contrast (cited from the existing artifacts, not re-run here): the four "
        "dispersion/confidence signals AND a same-model query-side false-premise verifier (the "
        "iter-8 RELATEDNESS / SELF-VERIFICATION baselines) BOTH fail to filter the confident "
        "absent-relation fabrications at matched coverage, whereas the structural no-derivation "
        "certificate catches them on the non-structural-by-construction (mixed present / "
        "same-component-sibling-absent) regime. That is the head-to-head evidence an ACL-KE "
        "reviewer needs: the recognized confidence and query-side-verifier methods do not "
        "suffice, and the structural detector is what closes the gap."
    )
}

venue_positioning_recommendation = {
    "primary_ACL_KE": {
        "move_1_frame_against_RE_NA": (
            "Lead, in the Introduction (not just Related Work), by framing the contribution "
            "against the RE NO_RELATION / hallucination-resistant-RE literature: cite "
            "\\citet{Yang2025DEPTH} (96.9% NO-RELATION over-prediction on SciERC), "
            "\\citet{Li2024RelClassifier} (attention dispersion from no-relation pairs), and "
            "\\citet{Pi2025RelPrior} (unrelated-pair noise) so the ACL-KE reviewer immediately "
            "recognizes a familiar Knowledge-Extraction problem. State plainly that the raw "
            "fabrication RATE is known and EXPECTED at the single-hop level, then pivot: what is "
            "unaddressed is the COMPOSITIONAL, multi-hop, document-internal absent-relation "
            "premise and its gold-free/training-free detection."
        ),
        "move_2_KE_metrics_up_front": (
            "Put Knowledge-Extraction metrics first in the results: atomic fact-extraction "
            "precision/recall directly from the document, multi-hop fact-extraction / deduction "
            "accuracy, and NO_RELATION/NA handling expressed as confident-wrong rate on absent "
            "pairs AT MATCHED COVERAGE (a risk-coverage view). Explicitly connect the "
            "no-derivation certificate to deductive NA-detection for document-level/multi-hop RE "
            "so it reads as a KE capability, and report the head-to-head vs the trained RE "
            "refiner/classifier framing and the external-KB / NLI-triple detectors."
        ),
        "move_3_demote_relation_algebra": (
            "Keep the qualitative-reasoning / relation-algebra (composition-table) machinery as "
            "the METHOD section, framed as the deductive engine BEHIND NA detection, not as the "
            "headline. The headline is the KE deliverable: human-auditable trace-graphs of the "
            "derivation path (or its absence) that reduce confident absent-relation hallucination "
            "in document-level extraction."
        ),
    },
    "fallback_NeSy": {
        "framing": (
            "For a NeSy / neuro-symbolic-reasoning venue (or EMNLP), lead instead with the "
            "deduce-then-abstain certificate and the risk-coverage / selective-prediction story: "
            "the structural composition-closure mechanism, the soundness of 'no derivation path "
            "=> abstain', and the trace-graph as a certificate of the reasoning path. Demote the "
            "RE NO_RELATION/NA framing to motivation (one paragraph) and elevate the "
            "neuro-symbolic integration (LLM extraction + symbolic closure + LLM fuzzy "
            "unification for gaps) and the abstention guarantees."
        ),
        "why_KE_primary": (
            "ACL-KE is the better primary fit because (a) the empirical bite lands on DocRED/"
            "Re-DocRED-derived document-level extraction with KE metrics, exactly the RE-NA "
            "community's home turf; (b) the closest neighbors (DEPTH, LLM+Classifier, RelPrior) "
            "are KE papers, so engaging them head-to-head is most legible to a KE reviewer; and "
            "(c) the NeSy contribution (the certificate mechanism) is inherited, so leading with "
            "it would over-claim mechanism novelty, whereas leading with the KE diagnostic + "
            "head-to-head evaluation matches the honest novelty scope."
        ),
    }
}

workstream_3 = {
    "related_work_paragraph": related_work_paragraph,
    "novelty_sentence": novelty_sentence,
    "two_part_delta": two_part_delta,
    "venue_positioning_recommendation": venue_positioning_recommendation,
}

# ---------------------------------------------------------------------------
# BIBTEX BLOCK (5 NEW keys; hand-built from web-verified metadata)
# ---------------------------------------------------------------------------
bibtex_block = r"""% ===== NEW (iter-9): RE NO_RELATION/NA + hallucination-resistant RE cluster =====
% (verified via arXiv abstract pages + PDF fetch_grep; see sources [1]-[6],[14])

@misc{Yang2025DEPTH,
  author       = {Yupei Yang and Fan Feng and Lin Yang and Wanxi Deng and Lin Qu and Biwei Huang and Shikui Tu and Lei Xu},
  title        = {Hallucination-Resistant Relation Extraction via Dependency-Aware Sentence Simplification and Two-tiered Hierarchical Refinement},
  year         = {2026},
  eprint       = {2508.14391},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  doi          = {10.48550/arXiv.2508.14391},
  url          = {https://arxiv.org/abs/2508.14391},
  note         = {DEPTH framework; v1 Aug 2025, v2 Feb 2026; ``Preprint. Under review.''; venue unconfirmed (arXiv preprint). Reports Qwen2.5-14B over-predicts a relation on 96.9\% of NO-RELATION SciERC pairs}
}

@misc{Li2024RelClassifier,
  author       = {Xingzuo Li and Kehai Chen and Yunfei Long and Min Zhang},
  title        = {{LLM} with Relation Classifier for Document-Level Relation Extraction},
  year         = {2024},
  eprint       = {2408.13889},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  doi          = {10.48550/arXiv.2408.13889},
  url          = {https://arxiv.org/abs/2408.13889},
  note         = {arXiv preprint (v1 Aug 2024, v2 Dec 2024); code github.com/wisper12933/LMRC; venue unconfirmed (Semantic Scholar's ``IEEE Transactions on Big Data'' association is uncorroborated)}
}

@misc{Pi2025RelPrior,
  author       = {Qiankun Pi and Yepeng Sun and Jicang Lu and Qinlong Fan and Ningbo Huang and Shiyu Wang},
  title        = {Relation as a Prior: A Novel Paradigm for {LLM}-based Document-level Relation Extraction},
  year         = {2025},
  eprint       = {2511.08143},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  doi          = {10.48550/arXiv.2511.08143},
  url          = {https://arxiv.org/abs/2511.08143},
  note         = {RelPrior; arXiv preprint (v1 Nov 2025, 17 pp.); venue unconfirmed; evaluated on DocRED and Re-DocRED}
}

% ===== NEW (iter-9): training-free structural / logical premise verification
%                      + KG-triple hallucination detection cluster =====

@article{Qin2026PremiseVerification,
  author       = {Yuehan Qin and Shawn Li and Yi Nian and Xinyan Velocity Yu and Yue Zhao and Xuezhe Ma},
  title        = {Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning},
  journal      = {Transactions on Machine Learning Research (TMLR)},
  year         = {2026},
  eprint       = {2504.06438},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  doi          = {10.48550/arXiv.2504.06438},
  url          = {https://arxiv.org/abs/2504.06438},
  note         = {Published in TMLR 02/2026 (confirmed via page header and arXiv comments); logicalize query + RAG over external factual sources; ``does not require access to model logits or large-scale fine-tuning''}
}

@inproceedings{Sansford2024GraphEval,
  author       = {Hannah Sansford and Nicholas Richardson and Hermina Petric Maretic and Juba Nait Saada},
  title        = {{GraphEval}: A Knowledge-Graph Based {LLM} Hallucination Evaluation Framework},
  booktitle    = {Proceedings of the 4th International Workshop on Knowledge-infused Learning (KiL), co-located with the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)},
  year         = {2024},
  pages        = {20--31},
  address      = {Barcelona, Spain},
  publisher    = {CEUR-WS, Vol-3894},
  eprint       = {2407.10793},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  doi          = {10.48550/arXiv.2407.10793},
  url          = {https://arxiv.org/abs/2407.10793},
  note         = {KiL 2024 Oral; Univ. of Bristol / Amazon Science; per-triple NLI consistency vs provided context; first author Sansford (NOT Wang)}
}

% ===== REUSED from iter-8 dossier art_oUhZgMSjf7lm (DO NOT re-emit) =====
% Hu2023 (FalseQA), Kirichenko2025 (AbstentionBench), Wen2024 (TACL 2025 survey),
% Kim2023 ((QA)^2), Yu2023 (CREPE), Press2023 (self-ask), Weng2023 (self-verification),
% Deng2024 (self-align), Kadavath2022 (P(True)), Wang2023 (self-consistency).
% NOTE: the GraphEval key is Sansford2024GraphEval (NOT the planner's tentative
% 'Wang2024GraphEval') -- correct first author + avoids confusion with Wang2023.
"""

# ---------------------------------------------------------------------------
# ANSWER (numbered citations; narrates all 3 workstreams, the DROPPED assertion,
#         and the re-carved delta)
# ---------------------------------------------------------------------------
answer = r"""
This artifact closes the ACL Knowledge-Extraction (ACL-KE) reviewer's NOVELTY MAJOR for the
closure-certificate paper by engaging the two literature clusters a KE reviewer will demand,
dropping an untenable assertion, and re-carving a defensible two-part delta plus a venue framing.
It is pure $0 web research; all five new papers were verified by direct fetch + fetch_grep over
the arXiv abstract pages and PDFs. It builds on the iter-8 false-premise dossier and reuses its
keys verbatim (Hu2023, Kirichenko2025, Wen2024, Kim2023, Yu2023, Press2023, Weng2023, Deng2024,
Kadavath2022, Wang2023).

WORKSTREAM 1 - THE RE NO_RELATION/NA + HALLUCINATION-RESISTANT-RE CLUSTER (the KE reviewer's home
literature). The single most important move is to DROP the paper's untenable claim that confident
absent-relation hallucination is "not derivable a priori" / a fresh observation. It is not: the
relation-extraction community has already quantified LLMs OVER-PREDICTING relations on pairs that
bear none. DEPTH reports, verbatim, that "Qwen2.5-14B-Instruct incorrectly predicts a relation in
96.9% of NO-RELATION instances on SciERC, revealing a severe hallucination problem", and that the
model "correctly identifies NO-RELATION in only 45 out of 1,475 instances, mis-classifying the
remaining 1,430 as having some relation" [1,2]. (Correction to the planner's pinned numbers: the
CURRENT v2 of DEPTH, 1 Feb 2026, reports a 7.9% average hallucination rate and 9.3% F1 improvement
over EIGHT sentence-level RE benchmarks - TACRED, TACREV, Re-TACRED, NYT11, SciERC, FOBIE, DDI,
SemEval - not the v1 "7.0%/17.2%/six" figures; the 96.9% SciERC quote is unchanged [2].) The
document-level NA problem is just as established: Li et al. trace the DocRE LLM gap to "the
dispersion of attention by LLMs due to entity pairs without relations" and pre-filter candidates
with a trained classifier on DocRED/Re-DocRED [3,4], and the newest (Nov 2025) RelPrior filters
"unrelated entity pairs [that] introduce noise" with a fine-tuned binary relation prior, again on
DocRED/Re-DocRED [5,6]. So FACT A's raw fabrication RATE is EXPECTED, not our novelty. What this
cluster does NOT do, and what is ours, is sharp: every method detects "no relation from a FIXED
LABEL SCHEMA for a SINGLE mention/pair", solved by better extraction, refinement, or filtering
(DEPTH's dependency-aware grounding + RLHF [1,2]; a trained classifier pre-filter [3,4];
relation-as-prior filtering [5,6]); NONE issues a DEDUCTIVE "no DERIVATION PATH exists" certificate
over MULTIPLE COMPOSED edges, and none operates gold-free + training-free + schema-free at the
document-internal multi-hop level. A time-boxed breadth probe confirmed the deductive-multi-hop-NA
(abstain-on-no-path) niche is unclaimed: cross-document and multi-hop DocRE use reasoning paths to
INFER present relations, not to abstain on absent ones by deduction [13]. This is the WS1 half of
DELTA-1.

WORKSTREAM 2 - TRAINING-FREE STRUCTURAL / LOGICAL PREMISE VERIFICATION + KG-TRIPLE HALLUCINATION
DETECTION. The closest method neighbor is Premise Verification [7,8] (TMLR 2026, confirmed by the
"Published in Transactions on Machine Learning Research (02/2026)" page header [8]). It transforms a
query into a "logical representation", then uses retrieval-augmented generation "to assess the
validity of each premise using factual sources", and is explicitly training/logits-light ("does not
require access to model logits or large-scale fine-tuning") [7,8]. The method delta hinges on this:
it checks ATOMIC premises against EXTERNAL world facts (a KG / factual corpus; its datasets KG-FPQ
and CREAK are world-knowledge sets), whereas our certificate checks a COMPOSITIONAL, multi-edge
premise against the DOCUMENT-INTERNAL composition closure with NO external KB. The KG-triple family
is represented by GraphEval [9,10] (KiL 2024 @ ACM SIGKDD/KDD 2024, CEUR-WS Vol-3894 [11]; first
author SANSFORD, not Wang): it extracts response triples and feeds EACH to an NLI model to check
consistency "with respect to the provided context", explicitly scoping OUT world knowledge and
deduction [9,10]. So GraphEval is structural and KG-based like us, but it is a TRAINED-NLI,
single-triple, faithfulness-to-context check - it cannot certify that NO derivation path exists.
The method-delta table (workstream_2) lays this out on five axes (external KB, training, trained
model, granularity, logic): all five recognized methods either require training, require an external
KB/retriever, or operate atomically; the gold-free + training-free + no-external-KB + COMPOSITIONAL
deductive "no derivation path -> abstain" cell is empty - that is DELTA-2. The empirical contrast
completes it: the four dispersion/confidence signals AND a same-model query-side false-premise
verifier (the iter-8 baseline) BOTH fail to filter the confident absent-relation fabrications at
matched coverage, where the structural certificate succeeds (cited from the paper's own artifacts,
not recomputed here).

WORKSTREAM 3 - RE-CARVED DELTA, DROP-IN RELATED WORK, NOVELTY SENTENCE, VENUE FRAMING. DELTA-1
(setting): lift absent-relation detection from single-hop, schema-bound NO_RELATION classification
[1,3,5] and sentence-level false premise (FalseQA/(QA)^2/CREPE) to a compositional, multi-hop,
document-internal absent-relation premise - "a derivation path exists between X and Y". DELTA-2
(method): detect it with a gold-free, training-free, no-external-KB deductive-closure certificate
(no path => abstain), versus trained RE refiners/classifiers [1,3,5], external-KB/RAG premise
verification [7], and NLI-vs-context triple checks [9]. The sharpened novelty is honest and
two-fold: (i) a corpus-robust DIAGNOSTIC that confident absent-relation fabrication - documented
single-hop [1] - becomes, at the compositional/document level, a false-premise failure that
transfers across readers/corpora and that neither the confidence family nor a same-model query-side
verifier filters; plus (ii) a gold-free, training-free, no-external-KB STRUCTURAL detector evaluated
head-to-head against these recognized methods. We do NOT claim the certificate mechanism is new (it
inherits the standard neuro-symbolic deduce-then-abstain premise), nor that FACT A's rate is new
(DEPTH shows it single-hop [1]). The drop-in Related-Work paragraph, the novelty sentence, and the
two delta sentences are provided as LaTeX with real \cite keys in workstream_3. VENUE: lead for
ACL-KE - frame the contribution against the RE NA-problem literature already in the Introduction
(cite DEPTH and the DocRE-NA papers up front [1,3,5]), put KE metrics first (atomic-fact
precision/recall, multi-hop deduction accuracy, NO_RELATION/NA confident-wrong rate at coverage),
and keep the relation-algebra machinery as the deductive engine behind NA detection rather than the
headline; keep NeSy/EMNLP as the fallback (lead with deduce-then-abstain + risk-coverage, demote
RE-NA to motivation). ACL-KE is the better primary because the empirical bite lands on
DocRED/Re-DocRED-style document-level extraction with KE metrics, the closest neighbors are KE
papers, and the inherited NeSy mechanism should not be the headline.

BibTeX for all five new papers (verified; venues marked unconfirmed where not authoritatively
established) is in bibtex_block, with the dossier keys referenced as reused. KEY CORRECTION: the
GraphEval key is Sansford2024GraphEval (correct first author; avoids confusion with the inherited
Wang2023 self-consistency key), not the planner's tentative Wang2024GraphEval.
""".strip()

# ---------------------------------------------------------------------------
title = "Retiring the NOVELTY MAJOR: RE NO_RELATION/NA and training-free structural premise-verification literature, re-carved two-part delta, and ACL-KE venue framing for the closure-certificate paper"

summary = (
    "Pure-web ($0, no code) research that retires the ACL-Knowledge-Extraction reviewer's NOVELTY "
    "MAJOR for the closure-certificate paper (iter-9). It pins, with web-verified BibTeX, exact "
    "verbatim quotes, method-types, datasets and venues, the two literature clusters a KE reviewer "
    "demands. CLUSTER 1 (RE NO_RELATION/NA + hallucination-resistant RE): DEPTH [Yang2025DEPTH, "
    "arXiv:2508.14391] reports Qwen2.5-14B over-predicts a relation on 96.9% of NO-RELATION SciERC "
    "pairs (45/1,475 correct) and fixes it with dependency-aware grounding + RLHF (v2 numbers "
    "7.9%/9.3% over eight sentence-RE benchmarks -- a CORRECTION of the planner's v1 7.0%/17.2%/six "
    "pin); LLM+Relation-Classifier [Li2024RelClassifier, 2408.13889] blames 'attention dispersion "
    "due to entity pairs without relations' and pre-filters with a trained classifier on "
    "DocRED/Re-DocRED; RelPrior [Pi2025RelPrior, 2511.08143] filters 'unrelated entity pairs [that] "
    "introduce noise' with a fine-tuned binary prior. CLUSTER 2 (training-free structural/logical "
    "premise verification + KG-triple detection): Premise Verification [Qin2026PremiseVerification, "
    "2504.06438, TMLR 2026 CONFIRMED] logicalizes a query then RAG-validates each premise against "
    "EXTERNAL factual sources ('no logits / no large-scale fine-tuning'); GraphEval "
    "[Sansford2024GraphEval, 2407.10793, KiL@KDD 2024 -- first author Sansford, NOT the planner's "
    "tentative 'Wang2024GraphEval'] checks single response triples against the PROVIDED CONTEXT with "
    "a trained NLI model, explicitly out-of-scope for world knowledge/deduction. It DROPS the "
    "untenable 'absent-relation hallucination is not derivable a priori' assertion (DEPTH already "
    "quantifies single-hop over-prediction) and re-carves a defensible two-part delta -- SETTING "
    "(compositional, multi-hop, document-internal absent-relation premise vs single-hop/schema-bound "
    "NO_RELATION classification and sentence-level false premise) and METHOD (gold-free, "
    "training-free, no-external-KB deductive-closure certificate vs trained RE refiners/classifiers, "
    "external-KB/RAG premise checks, and NLI-vs-context triple checks) -- plus the empirical contrast "
    "that the confidence family AND a same-model query-side verifier both fail where the structural "
    "certificate succeeds. A breadth probe confirms the deductive-multi-hop-NA (abstain-on-no-path) "
    "niche is unclaimed. Deliverables: a drop-in Related-Work paragraph (~200 words, real \\cite "
    "keys folding both new clusters + inherited FalseQA/AbstentionBench/Wen2024), a sharpened "
    "one-sentence novelty statement, the re-carved DELTA-1/DELTA-2, a method-delta table on five "
    "axes, a verified BibTeX block for the five new keys (dossier keys reused verbatim), and a "
    "concrete ACL-KE-primary / NeSy-fallback venue recommendation. Feeds the iter-9 Related-Work, "
    "Introduction, and venue decision."
)

layman_summary = (
    "Web-only literature research that shows how the paper should position itself against existing "
    "relation-extraction and hallucination-detection work, so reviewers see a clear, defensible new "
    "contribution."
)

out = {
    "title": title,
    "layman_summary": layman_summary,
    "summary": summary,
    "answer": answer,
    "workstream_1": workstream_1,
    "workstream_2": workstream_2,
    "workstream_3": workstream_3,
    "bibtex_block": bibtex_block,
    "sources": sources,
    "follow_up_questions": [
        "DEPTH, LLM+Relation-Classifier, and RelPrior are all arXiv preprints (or near-press): "
        "should the camera-ready re-verify their venues at submission time, and does any of them "
        "land at ACL/EMNLP 2026 in a way that lets us cite a peer-reviewed venue instead of arXiv?",
        "Premise Verification (TMLR 2026) is the closest method neighbor and is itself training-free "
        "/ logits-free -- should we add it as a THIRD external-KB baseline (RAG premise check against "
        "a small Wikidata slice) to harden the 'no-external-KB' method delta, or does that exceed the "
        "$0/commodity-hardware and reproducibility constraints?",
        "KG-FPQ (COLING 2025) and the RE-NA datasets (SciERC, DocRED/Re-DocRED) are all single-edge; "
        "is there ANY published dataset of compositional/multi-hop FALSE relational premises we could "
        "cite or adapt, or is our document-internal closure corpus the first such evaluation -- which "
        "would further strengthen DELTA-1?",
    ],
}

os.makedirs(OUT_DIR, exist_ok=True)
out_path = os.path.join(OUT_DIR, "research_out.json")
with open(out_path, "w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("WROTE", out_path)
print("bytes:", os.path.getsize(out_path))
print("sources:", len(sources), "| ws1 papers:", len(workstream_1),
      "| ws2 papers:", len(workstream_2["papers"]))
print("answer chars:", len(answer), "| summary chars:", len(summary),
      "| title chars:", len(title))
