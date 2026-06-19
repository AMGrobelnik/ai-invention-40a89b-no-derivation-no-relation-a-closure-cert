#!/usr/bin/env python3
"""Paper-facing prose blocks for the eval_iter8_dir4 framing scaffold.

These are verbatim-ready text for GEN_PAPER_TEXT. Numbers embedded here are the
recomputed/verified literals (the eval.py reproduction gate asserts they match the
source artifacts before this prose is emitted). Keeping prose separate from the
deterministic statistics keeps eval.py auditable.

iter-8 PIVOT: the spine moves from per-signal family-level blindness to the
SIGNAL-AGNOSTIC MIXED-POOL CAPABILITY GAP. The per-signal x reader x corpus
16-cell SURVIVAL/CAUGHT table (built in eval.py) is the centerpiece evidence;
this file supplies the surrounding verbatim-ready narration.
"""

# --------------------------------------------------------------------------- #
# TASK 1 -- the NEW spine: signal-agnostic mixed-pool capability gap
# --------------------------------------------------------------------------- #
CAPABILITY_GAP_SPINE = (
    "The load-bearing finding is a SIGNAL-AGNOSTIC MIXED-POOL CAPABILITY GAP, not a claim about any "
    "one confidence signal. On a mixed pool of answerable (present) and unanswerable (absent) "
    "relational queries, NO single confidence threshold can SIMULTANEOUSLY cover the present pairs "
    "and abstain on the absent pairs at matched coverage, because one scalar knob cannot separate "
    "'confident-and-right (present)' from 'confident-and-wrong (absent)': the LLM emits both with "
    "the same high confidence (FACT A). A sound closure certificate separates them structurally -- "
    "it abstains exactly when no derivation path exists -- so it dominates every confidence "
    "threshold at matched coverage. This is a property of the DECISION GEOMETRY, so it survives the "
    "collapse of any per-signal blindness claim: it does not matter WHICH signal you pick. "
    "POWERED on clean templated CLUTRR: at matched coverage 0.266 the certificate's selective "
    "accuracy is 0.827 versus 0.413 / 0.373 / 0.440 / 0.373 for verbalized / sc-margin / P(True) / "
    "negentropy thresholds (~2x); the doc-clustered paired-bootstrap confident-wrong reductions are "
    "0.110 / 0.121 / 0.103 / 0.121, every 95% CI excludes 0, and all four survive Holm correction "
    "(p_adj 0.0004 / 0.0027 / 0.0027 / 0.0027). We state plainly that the capability gap is currently "
    "POWERED ONLY on clean CLUTRR. On the natural Re-DocRED corpus it does NOT yet win: the "
    "confident-wrong reductions are slightly negative (-0.055 / -0.034 / -0.047 / -0.034), every CI "
    "includes 0, and Holm rejects none -- because natural-prose extraction recall is 0.376 and that "
    "is the binding constraint, not the certificate's logic. The gold-read ceiling (present coverage "
    "1.0, correct-absent-abstention 1.0, present selective accuracy 1.0) isolates extraction, not "
    "closure, as the cause. PENDING: the parallel located-in same-component-sibling experiment lands "
    "the capability gap on a natural, NON-by-construction regime (iter-9), where abstention is a "
    "genuine deductive result rather than a disconnected-component artifact."
)

# --------------------------------------------------------------------------- #
# TASK 1 -- honest FACT-A (robust) vs FACT-B (reader/signal-dependent) reading
# --------------------------------------------------------------------------- #
FACT_A_VS_FACT_B_READING = (
    "Read the 16-cell table as two separate facts. FACT A is ROBUST: the high-confidence "
    "absent-relation FABRICATION RATE sits in a tight 0.32-0.48 band across BOTH corpora and BOTH "
    "readers (CLUTRR 0.472 gemini / 0.483 deepseek; Re-DocRED 0.326 gemini / 0.318 deepseek). This "
    "corpus-and-reader-transferable rate is the genuine non-circular content. FACT B is "
    "READER- AND SIGNAL-DEPENDENT and must NOT be overstated. Verbalized confidence is the most "
    "robustly blind signal -- its caught fraction never reaches a strong majority (0.565 / 0.328 / "
    "0.492 / 0.588 across the four reader x corpus cells). But the DISPERSION signals (self-"
    "consistency vote-margin, P(True), semantic-entropy negentropy) swing widely: they are blind "
    "for the weaker gemini reader (CLUTRR/gemini negentropy catches only 0.282; Re-DocRED/gemini "
    "sc-margin and negentropy catch only 0.15) yet catch the MAJORITY for the stronger deepseek "
    "reader (CLUTRR/deepseek sc-margin / P(True) / negentropy catch 0.776 / 0.897 / 0.776 = 78-90%; "
    "Re-DocRED/deepseek catch 0.706 / 0.676 / 0.706 = 68-71%). We therefore DROP the prior headline "
    "claims that 'the entire confidence/uncertainty family is structurally blind' and that the "
    "blindness is 'reader-diverse', and replace them with the signal-agnostic capability gap above, "
    "which does not depend on any signal being blind."
)

# --------------------------------------------------------------------------- #
# TASK 2 -- definitional vs empirical split (lead with empirical)
# --------------------------------------------------------------------------- #
DEFINITIONAL_VS_EMPIRICAL = {
    "definitional": (
        "Definitional half (state ONCE, briefly, as the explanatory mechanism -- NOT a contribution): "
        "a high-confidence, self-consistent fabrication survives ANY dispersion threshold BY "
        "CONSTRUCTION. If the model commits an absent relation with maximal confidence and zero "
        "answer-dispersion, then no threshold tuned on that same dispersion can single it out -- this "
        "is true by definition of a dispersion signal and needs no experiment."
    ),
    "empirical": (
        "Empirical half (LEAD with this -- it is the measured, non-obvious part): how OFTEN does the "
        "LLM actually emit absent-relation fabrications at high confidence and low dispersion, and how "
        "strongly does that fraction vary by reader? Answer: FACT A puts the high-confidence "
        "fabrication rate in a tight 0.32-0.48 band across two corpora and two readers, while the "
        "fraction a dispersion threshold can catch swings from ~15% (Re-DocRED/gemini) to ~90% "
        "(CLUTRR/deepseek). Neither the rate nor its reader-variance is derivable a priori; both are "
        "the 16-cell table's contribution."
    ),
}

# --------------------------------------------------------------------------- #
# TASK 2 -- softened-overclaim language (retire the evidence-MINOR)
# --------------------------------------------------------------------------- #
SOFTENED_OVERCLAIMS = {
    "removes_none_caveat": (
        "The statement 'no confidence signal removes a single hallucination' holds ONLY at the LLM's "
        "NATURAL (no-abstention) operating point: at that coverage every named-on-absent answer is by "
        "definition wrong, so all four thresholded baselines coincide with the raw answerer and remove "
        "none. It is NOT a claim that confidence is useless at every coverage."
    ),
    "at_certificate_coverage": (
        "At the CERTIFICATE's (lower) coverage the picture changes and we say so: a dispersion "
        "threshold tuned to the certificate's coverage already CATCHES a substantial share of the "
        "hallucinations. P(True) catches 75.3% on CLUTRR (1 - 0.247) and 51.7% on natural Re-DocRED "
        "prose (1 - 0.483) for the gemini reader. The certificate's advantage is that it catches them "
        "ALL via structural abstention, but the confidence signals are far from worthless once a "
        "non-natural coverage is permitted."
    ),
    "delete_marginal_framing": (
        "DELETE the marginal '>=3 of 4 signals keep >=50%' / '>=2 of 4 commit >=50%' framing. It "
        "obscures the strong reader-dependence. Replace it with the per-cell caught fractions from the "
        "16-cell table so the reader sees directly that the same signal swings from 15% to 90% caught "
        "depending on the reader."
    ),
}

# --------------------------------------------------------------------------- #
# TASK 3 -- abstract front-matter (scope) -- FIRST SENTENCE sets the scope
# --------------------------------------------------------------------------- #
ABSTRACT_FRONT_MATTER = (
    "This paper studies a closure-certified DEDUCTION SUB-MODULE -- a sound symbolic forward-closure "
    "over LLM-extracted relations that abstains rather than guess -- and explicitly NOT a full "
    "operational text-to-FOL umbrella pipeline; we name the umbrella components OUT OF SCOPE / FUTURE "
    "WORK THIS PAPER DOES NOT CLAIM in the first sentence so no reader mistakes the contribution. Out "
    "of scope and not claimed: (a) atomic / multi-hop fact EXTRACTION and re-extraction, which we "
    "MEASURE but do not improve (CLUTRR atomic precision/recall/F1 ~0.536 / 0.532 / 0.534; natural "
    "Re-DocRED recall 0.376, vs 0.465 against the locally-justifiable subset); (b) upper-ontology / "
    "OpenCyc grounding and taxonomic background knowledge; (c) reasoning over genuine ~3000-character "
    "professional documents -- no benchmark document we use reaches that length (CLUTRR <=871 chars; "
    "Re-DocRED Wikipedia intros average ~1020 chars, none family-bearing reach 3000), and the "
    "operational case study is bracket-selected, not naturally long; and (d) general open-vocabulary "
    "fuzzy unification -- our fuzzy contribution is scoped to disjunctions over a KNOWN base vocabulary "
    "(RCC-8 base relations; CLUTRR kinship primitives), not open-vocabulary predicate invention. We "
    "state plainly that, until the located-in second-domain fork lands, the certificate's NET utility "
    "is demonstrated only on clean / templated graphs (CLUTRR): on natural prose the result is an "
    "EXTRACTION-GATED BOUNDARY -- atomic recall 0.376 natural vs ~0.53 templated, and the gold-read "
    "ceiling (1.0 / 1.0 / 1.0) shows the boundary is extraction recall, not the closure logic. We "
    "therefore target a neuro-symbolic / NeSy (EMNLP Findings) venue and frame the contribution as a "
    "COMPOSITIONAL FALSE-PREMISE diagnostic plus a gold-free structural detector, not a new end-to-end "
    "system."
)

# --------------------------------------------------------------------------- #
# TASK 3 -- operational case study: strengthen compression to a CUT
# --------------------------------------------------------------------------- #
OPERATIONAL_COMPRESSION_RECOMMENDATION = (
    "CUT the concatenated-kinship arm of the operational ~3000-char case study ENTIRELY. Its 56/56 "
    "cross-story absent abstentions are trivial BY CONSTRUCTION -- concatenated stories share no "
    "entities, so the entities are in different connected components and a sound closure abstains by "
    "definition; the arm carries no evidential weight and reads as inflated coverage. KEEP ONLY the "
    "bracket-selected temporal arm, and demote it to a single one-paragraph feasibility note whose "
    "only claim is that the pipeline RUNS end-to-end at ~3000-character length. The reclaimed space "
    "(roughly a column) goes to the diagnostic (the 16-cell table + capability gap) and the "
    "second-domain located-in replication, which is the decisive evidence."
)

# --------------------------------------------------------------------------- #
# TASK 4 -- false-premise / unanswerable-question related-work positioning
# --------------------------------------------------------------------------- #
FALSE_PREMISE_POSITIONING = (
    "Position the contribution against the false-premise / unanswerable-question literature, NOT "
    "merely the neuro-symbolic literature. The raw LLM confidently answering an absent relational "
    "query is a COMPOSITIONAL FALSE-PREMISE / unanswerable-question instance: the question presupposes "
    "a relation that does not hold. Engage: FalseQA (Hu et al., ACL 2023) on questions with false "
    "presuppositions; AbstentionBench (NeurIPS 2025) on when models should abstain; and the query-side "
    "self-verification line (Wen et al., 'Know Your Limits', TACL 2025). The carved delta vs that "
    "literature is two-fold: (1) we operate in a MULTI-HOP RELATIONAL COMPOSITIONAL setting (the false "
    "premise is that a derivable kinship/located-in path exists), not single-fact factuality; and (2) "
    "our detector is GOLD-FREE and TRAINING-FREE -- a structural property of the extracted graph's "
    "closure -- rather than a learned or prompt-elicited confidence judgment. The credibility test for "
    "the certificate is whether it MATCHES OR BEATS a query-side false-premise verifier ('are these "
    "two entities related at all?') at matched coverage; that verifier is the established baseline for "
    "this failure mode and is a NAMED PENDING comparison (iter-9)."
)

# --------------------------------------------------------------------------- #
# Retained from iter-7 (still useful): structural-by-construction guard +
# count fix sentence. These police the 2.8% number and the 476/577 confusion.
# --------------------------------------------------------------------------- #
STRUCTURAL_BY_CONSTRUCTION_PARAGRAPH = (
    "A note on what the certificate's 2.8% confident-wrong rate on CLUTRR absent pairs does and does "
    "not establish. In the CLUTRR construction an absent pair is DEFINED as two entities in DIFFERENT "
    "connected components of the extracted kinship graph; a SOUND forward-closure least-fixpoint over "
    "that graph therefore derives the EMPTY relation set and ABSTAINS almost by definition. Imperfect "
    "extraction (atomic recall ~0.53) can only REMOVE edges, which can only INCREASE apparent "
    "disconnection, so it makes the certificate abstain MORE, never less, on absent pairs. The 2.8% is "
    "thus NEAR-TAUTOLOGICAL given the setup and must NOT carry the section. The genuinely non-circular "
    "content -- the headline -- is a property of the RAW LLM and the confidence signals, measured "
    "INDEPENDENTLY of the certificate: FACT A (the raw LLM confidently fabricates a kinship on 47.2% of "
    "absent pairs; deepseek 48.3%) and the signal-agnostic capability gap. This is also why the "
    "natural-corpus run is load-bearing: on natural prose extraction can DELETE a true edge and make "
    "the certificate OVER-abstain on a PRESENT pair, a cost the disconnected-by-construction CLUTRR "
    "regime hides."
)

COUNT_FIX_SENTENCE = (
    "The Re-DocRED natural-text corpus reports two figure pairs that are sometimes confused: the "
    "PRIMARY trustworthy-absent slice (re-docred) supplies 360 present multi-hop queries and 368 "
    "absent pairs, while the engine round-trip verification (476 present / 577 absent) is the COMBINED "
    "re-docred (360 / 368) plus secondary docred (116 / 209) total -- 360+116 = 476 and 368+209 = 577 "
    "-- so the two pairs are not in conflict; the larger pair is the union over both sources, the "
    "smaller is the load-bearing Re-DocRED slice on which absent gold is trustworthy."
)

# --------------------------------------------------------------------------- #
# Headline-structure guidance for GEN_PAPER_TEXT (updated for the iter-8 pivot)
# --------------------------------------------------------------------------- #
HEADLINE_STRUCTURE_GUIDANCE = [
    "LEAD with the SIGNAL-AGNOSTIC MIXED-POOL CAPABILITY GAP (one scalar knob cannot separate "
    "confident-right-present from confident-wrong-absent), powered on CLUTRR. This is the spine and it "
    "survives the collapse of any per-signal blindness claim.",
    "Present the 16-cell per-signal x reader x corpus SURVIVAL/CAUGHT table as the centerpiece "
    "evidence. Split FACT A (robust 0.32-0.48 fabrication band across both corpora and readers) from "
    "FACT B (reader/signal-dependent caught fraction, 15% to 90%).",
    "DROP the prior headlines 'the entire confidence/uncertainty family is structurally blind' and "
    "'reader-diverse blindness' -- the paper's own cross-reader data contradict them. The capability "
    "gap replaces them and does not depend on any signal being blind.",
    "CONCEDE the closure MECHANISM up front as INHERITED (+0.673 inherited / +0.0025 novel). The novel "
    "contribution is the compositional-false-premise DIAGNOSTIC + the gold-free structural detector, "
    "not the certificate mechanism.",
    "State the natural-corpus result as an EXTRACTION-GATED BOUNDARY, not a win: on Re-DocRED the "
    "capability gap does NOT yet hold (CIs include 0, Holm rejects none) because extraction recall "
    "0.376 binds; the gold-read ceiling 1.0/1.0/1.0 isolates extraction, not closure.",
    "Carry clearly-LABELED PENDING rows for (P1) the located-in same-component-sibling net-win and "
    "(P2) the query-side false-premise verifier baseline; do NOT assert them as wins.",
    "Do NOT present the 2.8% CLUTRR certificate confident-wrong as load-bearing; it is "
    "structural-by-construction. Use the non-circular-facts ledger to police this.",
    "Position against the false-premise / unanswerable-question literature (FalseQA; AbstentionBench; "
    "Know-Your-Limits), with the carved delta = multi-hop relational compositional setting + gold-free "
    "training-free structural detector.",
    "CUT the concatenated-kinship operational arm (56/56 trivial-by-construction); keep only the "
    "bracket-selected temporal arm as a one-paragraph feasibility note.",
    "Present evidence-class tags (REAL-LLM-READ / REAL-LLM-READ-ON-SYNTHETIC / SYNTHETIC-CHANNEL / "
    "GOLD-ONLY-GATE / THEOREM / NATURAL-CORPUS-PENDING) as table COLUMNS, not inline hedges.",
]
