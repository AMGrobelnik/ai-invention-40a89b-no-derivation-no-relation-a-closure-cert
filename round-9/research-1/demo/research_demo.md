# Retire NOVELTY MAJOR: RE NO_RELATION lit + structural premise-verification + ACL-KE venue

## Summary

Pure-web ($0, no code) research that retires the ACL-Knowledge-Extraction reviewer's NOVELTY MAJOR for the closure-certificate paper (iter-9). It pins, with web-verified BibTeX, exact verbatim quotes, method-types, datasets and venues, the two literature clusters a KE reviewer demands. CLUSTER 1 (RE NO_RELATION/NA + hallucination-resistant RE): DEPTH [Yang2025DEPTH, arXiv:2508.14391] reports Qwen2.5-14B over-predicts a relation on 96.9% of NO-RELATION SciERC pairs (45/1,475 correct) and fixes it with dependency-aware grounding + RLHF (v2 numbers 7.9%/9.3% over eight sentence-RE benchmarks -- a CORRECTION of the planner's v1 7.0%/17.2%/six pin); LLM+Relation-Classifier [Li2024RelClassifier, 2408.13889] blames 'attention dispersion due to entity pairs without relations' and pre-filters with a trained classifier on DocRED/Re-DocRED; RelPrior [Pi2025RelPrior, 2511.08143] filters 'unrelated entity pairs [that] introduce noise' with a fine-tuned binary prior. CLUSTER 2 (training-free structural/logical premise verification + KG-triple detection): Premise Verification [Qin2026PremiseVerification, 2504.06438, TMLR 2026 CONFIRMED] logicalizes a query then RAG-validates each premise against EXTERNAL factual sources ('no logits / no large-scale fine-tuning'); GraphEval [Sansford2024GraphEval, 2407.10793, KiL@KDD 2024 -- first author Sansford, NOT the planner's tentative 'Wang2024GraphEval'] checks single response triples against the PROVIDED CONTEXT with a trained NLI model, explicitly out-of-scope for world knowledge/deduction. It DROPS the untenable 'absent-relation hallucination is not derivable a priori' assertion (DEPTH already quantifies single-hop over-prediction) and re-carves a defensible two-part delta -- SETTING (compositional, multi-hop, document-internal absent-relation premise vs single-hop/schema-bound NO_RELATION classification and sentence-level false premise) and METHOD (gold-free, training-free, no-external-KB deductive-closure certificate vs trained RE refiners/classifiers, external-KB/RAG premise checks, and NLI-vs-context triple checks) -- plus the empirical contrast that the confidence family AND a same-model query-side verifier both fail where the structural certificate succeeds. A breadth probe confirms the deductive-multi-hop-NA (abstain-on-no-path) niche is unclaimed. Deliverables: a drop-in Related-Work paragraph (~200 words, real \cite keys folding both new clusters + inherited FalseQA/AbstentionBench/Wen2024), a sharpened one-sentence novelty statement, the re-carved DELTA-1/DELTA-2, a method-delta table on five axes, a verified BibTeX block for the five new keys (dossier keys reused verbatim), and a concrete ACL-KE-primary / NeSy-fallback venue recommendation. Feeds the iter-9 Related-Work, Introduction, and venue decision.

## Research Findings

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

## Sources

[1] [Hallucination-Resistant Relation Extraction via Dependency-Aware Sentence Simplification and Two-tiered Hierarchical Refinement (DEPTH; Yang et al.)](https://arxiv.org/abs/2508.14391) — arXiv abstract page (v2, last revised 1 Feb 2026; v1 20 Aug 2025). Authors Yupei Yang, Fan Feng, Lin Yang, Wanxi Deng, Lin Qu, Biwei Huang, Shikui Tu, Lei Xu. cs.CL/cs.AI. Headline: Qwen2.5-14B over-predicts relations on 96.9% of NO-RELATION instances on SciERC; DEPTH = dependency-aware simplification + two-tiered hierarchical refinement + causality-driven RLHF reward model. 'Preprint. Under review.' (no published venue).

[2] [DEPTH PDF (grepped) — 96.9% NO-RELATION over-prediction, 45/1475, v2 results, 8 benchmarks, RLHF/PPO](https://arxiv.org/pdf/2508.14391) — fetch_grep extraction. VERBATIM: 'Qwen2.5-14B-Instruct incorrectly predicts a relation in 96.9% of NO-RELATION instances on SciERC, revealing a severe hallucination problem.' Also: 'correctly identifies NO-RELATION in only 45 out of 1,475 instances, misclassifying the remaining 1,430 as having some relation'; 'tendency to overpredict relations: even when no meaningful connection exists ... LLMs often hallucinate a spurious relation rather than outputting NO-RELATION'. v2 results: 'reduces the average hallucination rate to 7.9% while achieving a 9.3% improvement in average F1 ... over existing LLM-based extraction baselines' on EIGHT benchmarks (TACRED, TACREV, Re-TACRED, NYT11, SciERC, FOBIE, DDI, SemEval). Method: shortest-dependency-path Grounding + sentence-level Refinement + causality-driven reward model + PPO/RLHF fine-tuning (NOT training-free).

[3] [LLM with Relation Classifier for Document-Level Relation Extraction (Li et al.)](https://arxiv.org/abs/2408.13889) — arXiv abstract page (v2, 7 Dec 2024; v1 25 Aug 2024). Authors Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang. cs.CL. Identifies 'the dispersion of attention by LLMs due to entity pairs without relations' as the key cause of the DocRE LLM gap; introduces a classifier-LLM hybrid (classifier pre-selects candidate pairs with potential relations, LLM classifies only those). No authoritative published venue (arXiv preprint; Semantic Scholar's 'IEEE Transactions on Big Data' tag is unconfirmed).

[4] [LLM+Relation-Classifier PDF (grepped) — attention-dispersion, NA framing, DocRED/Re-DocRED](https://arxiv.org/pdf/2408.13889) — fetch_grep extraction. VERBATIM: 'identifying the dispersion of attention by LLMs due to entity pairs without relations as a key factor'. Figure 1: 'Statistics on the number of entity pairs in DocRED and Re-DocRED training set. NA: entity pairs that do not express any relation. Rel: entity pairs expressing relations.' Datasets = DocRED + Re-DocRED. Code: github.com/wisper12933/LMRC. Single-hop/schema-bound NA classification by trained pre-filter; not deductive/multi-hop, not gold-free.

[5] [Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction (RelPrior; Pi et al.)](https://arxiv.org/abs/2511.08143) — arXiv abstract page (v1, 11 Nov 2025, 17 pages). Authors Qiankun Pi, Yepeng Sun, Jicang Lu, Qinlong Fan, Ningbo Huang, Shiyu Wang. cs.CL/cs.AI. Two challenges: (1) 'Numerous unrelated entity pairs introduce noise and interfere with the relation prediction for truly related entity pairs'; (2) relation labels beyond the predefined set are treated as errors. RelPrior uses a binary relation prior to filter irrelevant pairs + a predefined-relation prior to match entities. arXiv preprint (no published venue).

[6] [RelPrior PDF (grepped) — 'unrelated entity pairs' filtering, binary-classifier prior, DocRED/Re-DocRED](https://arxiv.org/pdf/2511.08143) — fetch_grep extraction. VERBATIM challenge (1): 'Numerous unrelated entity pairs introduce noise and interfere with the relation prediction for truly related entity pairs.' Method: 'fine-tuning a binary classification LLM that determines whether there is a relation between entity pairs' (Step1 unrelated-pair filter; Step2 relation-as-prior matching). Keywords: 'Document-level relation extraction; Unrelated entity pairs; Relation as a prior.' Datasets: 'document-level relation extraction public datasets DocRED and RE-DocRED.' Trained (fine-tuned classifier); single-hop NA filtering, not deductive multi-hop.

[7] [Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning (Qin et al.)](https://arxiv.org/abs/2504.06438) — arXiv abstract page (v2, last revised 16 Feb 2026; v1 8 Apr 2025). Authors Yuehan Qin, Shawn Li, Yi Nian, Xinyan Velocity Yu, Yue Zhao, Xuezhe Ma. cs.CL/cs.AI. Comments field: 'TMLR 2026'. Transforms a query into a logical representation, then uses retrieval-augmented generation (RAG) to validate each premise against factual sources, and feeds verification into the prompt. 'does not require access to model logits or large-scale fine-tuning' — but DOES require external retrieval/KB. THE closest structural-premise-verification neighbor.

[8] [Premise Verification PDF (grepped) — logicalize+RAG-over-external-KG, no-logits/no-fine-tuning, TMLR 02/2026, KG-FPQ/CREAK](https://arxiv.org/pdf/2504.06438) — fetch_grep extraction. Page header on every page: 'Published in Transactions on Machine Learning Research (02/2026)' (CONFIRMS TMLR 2026). VERBATIM method: 'Our method first transforms a user's query into a logical representation, then applies retrieval-augmented generation (RAG) to assess the validity of each premise using factual sources' and 'transform the user's query into a logical form ... employ retrieval-augmented generation (RAG) to check the accuracy of these statements against a knowledge graph.' VERBATIM cost claim: 'does not require access to model logits or large-scale fine-tuning'. Datasets: KG-FPQ (Zhu et al. 2024, from KoPL/Wikidata) + CREAK. EXTERNAL-KB/RAG, atomic-premise, world-fact check (NOT document-internal, NOT deductive-closure).

[9] [GraphEval: A Knowledge-Graph Based LLM Hallucination Evaluation Framework (Sansford et al.)](https://arxiv.org/abs/2407.10793) — arXiv abstract page (v1, 15 Jul 2024). Authors Hannah Sansford, Nicholas Richardson, Hermina Petric Maretic, Juba Nait Saada (Univ. of Bristol / Amazon Science). cs.CL/cs.AI/cs.LG. Comments: 'to be published at KiL'24: Workshop on Knowledge-infused Learning co-located with 30th ACM KDD Conference, August 26, 2024, Barcelona, Spain.' Builds a KG of (subject,predicate,object) triples from a response and feeds each triple to an NLI model to check consistency vs the provided context; GraphCorrect rectifies. FIRST AUTHOR = Sansford (NOT Wang — corrects the planner's tentative 'Wang2024GraphEval' key).

[10] [GraphEval PDF (grepped) — triple-level NLI vs PROVIDED CONTEXT, balanced-accuracy gain, GraphCorrect, world-knowledge out-of-scope](https://arxiv.org/pdf/2407.10793) — fetch_grep extraction. VERBATIM: 'identifies the specific triples in the KG that are prone to hallucinations'; 'using our approach in conjunction with state-of-the-art natural language inference (NLI) models leads to an improvement in balanced accuracy on various hallucination benchmarks, compared to using the raw NLI models'. Scope (VERBATIM): 'we focus on the problem of detecting hallucinations with respect to the provided context ... detecting hallucinations that have deviated from the LLM's original training data is out of the scope of this work'; binary classification, 0=consistent given provided context, 1=>=1 inconsistency. Faithfulness-vs-context NLI on single triples (NOT deductive, NOT a no-path certificate); needs a trained NLI model. GraphCorrect = KG-structure correction.

[11] [KDD 2024 Workshop KiL (OpenReview) + CEUR-WS Vol-3894 — GraphEval venue confirmation](https://openreview.net/group?id=KDD.org/2024/Workshop/KiL) — OpenReview/CEUR confirm GraphEval venue: KiL 2024 (4th International Workshop on Knowledge-infused Learning, co-located with ACM SIGKDD/KDD 2024, 26 Aug 2024, Barcelona), 'KiL 2024 Oral', CEUR-WS Vol-3894; Amazon Science PDF cites 'Proceedings of the Fourth ACM SIGKDD Workshop on Knowledge-infused Learning', pages 20-31. Authoritative venue for the Sansford2024GraphEval BibTeX.

[12] [KG-FPQ: Evaluating Factuality Hallucination in LLMs with Knowledge Graph-based False Premise Questions (COLING 2025)](https://aclanthology.org/2025.coling-main.698/) — Adjacency / triangulation. KG-FPQ = ~178k false-premise questions across three knowledge domains constructed by editing KG triples (KoPL/Wikidata). Confirms that the false-premise QA datasets the structural-verification cluster uses are SINGLE-TRIPLE-LEVEL (one edited subject-relation-object fact), not compositional/multi-hop derivation premises — reinforcing DELTA-1. This is the dataset Qin2026PremiseVerification [8] evaluates on.

[13] [Breadth probe — cross-document / multi-hop DocRE infers relations via reasoning paths (no deductive no-path abstention)](https://openreview.net/pdf?id=aolJqJ50ZA) — Representative of the time-boxed breadth search ('document-level relation extraction deductive closure abstain'; 'transitive relation hallucination KG abstain'). Multi-hop / cross-document DocRE work (e.g. CodRED reasoning-path bridging, multi-hop evidence retrieval arXiv:2212.10786) uses reasoning paths to INFER present relations, not to issue a no-derivation-path certificate that ABSTAINS on absent relations. Confirms the deductive-multi-hop-NA (abstain-on-no-path) niche is unclaimed — strengthens DELTA-1/DELTA-2 novelty.

[14] [Li2024 venue cross-check — listed as arxiv-cs.CL 2024-08 (no authoritative published venue)](https://www.paperdigest.org/2020/04/recent-papers-on-relation-extraction/) — Triangulation of the LLM+Relation-Classifier publication venue. PaperDigest and ResearchGate list arXiv:2408.13889 as 'arxiv-cs.CL, 2024-08' with no peer-reviewed venue; the Semantic Scholar 'IEEE Transactions on Big Data' association is uncorroborated. BibTeX therefore pins it as an arXiv preprint with a venue-unconfirmed note.

## Follow-up Questions

- DEPTH, LLM+Relation-Classifier, and RelPrior are all arXiv preprints (or near-press): should the camera-ready re-verify their venues at submission time, and does any of them land at ACL/EMNLP 2026 in a way that lets us cite a peer-reviewed venue instead of arXiv?
- Premise Verification (TMLR 2026) is the closest method neighbor and is itself training-free / logits-free -- should we add it as a THIRD external-KB baseline (RAG premise check against a small Wikidata slice) to harden the 'no-external-KB' method delta, or does that exceed the $0/commodity-hardware and reproducibility constraints?
- KG-FPQ (COLING 2025) and the RE-NA datasets (SciERC, DocRED/Re-DocRED) are all single-edge; is there ANY published dataset of compositional/multi-hop FALSE relational premises we could cite or adapt, or is our document-internal closure corpus the first such evaluation -- which would further strengthen DELTA-1?

---
*Generated by AI Inventor Pipeline*
