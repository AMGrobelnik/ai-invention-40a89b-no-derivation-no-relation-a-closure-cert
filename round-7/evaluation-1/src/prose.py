#!/usr/bin/env python3
"""Paper-facing prose blocks for the eval_iter7_dir3 framing scaffold.

These are verbatim-ready text for GEN_PAPER_TEXT. Numbers embedded here are the
recomputed/verified literals (the eval.py reproduction gate asserts they match the
source artifacts before this prose is emitted). Keeping prose separate from the
deterministic statistics keeps eval.py auditable.
"""

# --------------------------------------------------------------------------- #
# STEP 1A -- structural-by-construction paragraph (verbatim-ready)
# --------------------------------------------------------------------------- #
STRUCTURAL_BY_CONSTRUCTION_PARAGRAPH = (
    "A note on what the certificate's 2.8% confident-wrong rate on CLUTRR absent pairs "
    "does and does not establish. In the CLUTRR construction an absent pair is DEFINED as "
    "two entities that fall in DIFFERENT connected components of the extracted kinship graph; "
    "a SOUND forward-closure least-fixpoint over that graph therefore derives the EMPTY relation "
    "set for such a pair and ABSTAINS almost by definition. Imperfect extraction (atomic recall "
    "~0.53) can only REMOVE edges, which can only INCREASE apparent disconnection, so it makes "
    "the certificate abstain MORE, never less, on absent pairs. The certificate's 2.8% "
    "confident-wrong on this stratum is thus NEAR-TAUTOLOGICAL given the setup: one side of the "
    "comparison is handed the answer by the way the regime is built, and this number must NOT be "
    "allowed to carry the section. The genuinely non-circular content -- the content that becomes "
    "the headline -- is a property of the RAW LLM and of the confidence signals, measured "
    "INDEPENDENTLY of the certificate. FACT A: the raw LLM confidently fabricates a kinship "
    "relation on 47.2% of these absent pairs (cross-family deepseek-v3.2: 48.3%). FACT B: not one "
    "member of a strong four-signal confidence battery -- verbalized confidence, self-consistency "
    "vote-margin, Kadavath P(True), and semantic-entropy negentropy -- removes those "
    "hallucinations at a coverage matched to the certificate; the fractions surviving a "
    "certificate-matched rule are 0.4353 / 0.7176 / 0.2471 / 0.7176, and even the single best "
    "signal, P(True), still lets 24.7% through. These two facts hold no matter how the certificate "
    "behaves. Finally, this is exactly why extraction recall and the natural-corpus run are "
    "load-bearing: on a NATURAL corpus the extracted graph -- and hence absent-detection -- is no "
    "longer trivially correct, because extraction errors can also DELETE a true edge and make the "
    "certificate OVER-abstain on a PRESENT pair (a cost the disconnected-by-construction CLUTRR "
    "regime hides). That asymmetry is what converts the iter-7 natural-corpus experiment from a "
    "confirmatory check into a DECISIVE test of whether the certificate's abstention discipline "
    "survives when the graph is no longer handed to it."
)

# --------------------------------------------------------------------------- #
# STEP 2 -- count breakdown + one-clause fix sentence
# --------------------------------------------------------------------------- #
COUNT_FIX_SENTENCE = (
    "The Re-DocRED natural-text corpus reports two figure pairs that are sometimes confused: the "
    "PRIMARY trustworthy-absent slice (re-docred) supplies 360 present multi-hop queries and 368 "
    "absent pairs, while the engine round-trip verification (476 present / 577 absent) is the "
    "COMBINED re-docred (360 / 368) plus secondary docred (116 / 209) total -- 360+116 = 476 and "
    "368+209 = 577 -- so the two pairs are not in conflict; the larger pair is the union over both "
    "sources, the smaller is the load-bearing Re-DocRED slice on which absent gold is trustworthy."
)

# --------------------------------------------------------------------------- #
# STEP 3 -- abstract front-matter (scope) + operational-study compression
# --------------------------------------------------------------------------- #
ABSTRACT_FRONT_MATTER = (
    "Scope. This paper studies a closure-certified DEDUCTION SUB-MODULE -- a sound symbolic "
    "forward-closure over LLM-extracted relations that abstains rather than guess -- and NOT a "
    "full operational text-to-FOL umbrella pipeline. We therefore state up front what is "
    "explicitly OUT OF SCOPE and named here as FUTURE WORK THIS PAPER DOES NOT CLAIM TO DELIVER: "
    "(a) upper-ontology / OpenCyc grounding and taxonomic background knowledge; (b) general fuzzy "
    "unification over arbitrary predicates -- our fuzzy contribution is scoped to disjunctions over "
    "a KNOWN base vocabulary (RCC-8 base relations; CLUTRR kinship primitives), not open-vocabulary "
    "predicate invention; (c) atomic re-extraction -- extraction quality is MEASURED, not improved "
    "(CLUTRR atomic precision/recall/F1 ~0.536 / 0.532 / 0.534); and (d) reasoning over genuine "
    "~3000-character professional documents -- no benchmark document we use reaches that length "
    "(CLUTRR <=871 chars; Re-DocRED Wikipedia intros average ~1020 chars, none family-bearing reach "
    "3000), and the operational case study is bracket-selected and concatenation-constructed rather "
    "than naturally long. Because extraction is the ceiling (~0.53 atomic recall implies only ~19% "
    "Mode-A deductive coverage on dense prose), we report real-text utility as structurally "
    "EXTRACTION-LIMITED. Accordingly we target a neuro-symbolic / temporal-and-qualitative-reasoning "
    "venue (NeSy; EMNLP Findings) rather than a full knowledge-extraction-pipeline track, and frame "
    "the contribution as an EMPIRICAL ISOLATION of confidence-blindness, not as a new end-to-end system."
)

OPERATIONAL_COMPRESSION_RECOMMENDATION = (
    "Compression recommendation for the operational ~3000-char case study (art_WQoePKrpsTPo): "
    "collapse its two arms -- the bracket-selected temporal arm and the concatenation-constructed "
    "kinship arm (in which all 56/56 cross-story absent pairs are abstained trivially BY "
    "CONSTRUCTION, because concatenated stories share no entities) -- into ONE short paragraph whose "
    "only claims are that the pipeline RUNS at ~3000-character length and that EXTRACTION recall is "
    "the binding ceiling. This frees roughly a column of space for the natural-corpus (Re-DocRED) "
    "result, which is the decisive evidence; the operational study should support feasibility, not "
    "headline accuracy."
)

# --------------------------------------------------------------------------- #
# STEP 4 -- fuzzy downweight + 5/5 Mode-B lead + demoted unit caveat
# --------------------------------------------------------------------------- #
FUZZY_REFRAME = {
    "lead": (
        "The distinctive fuzzy-unification contribution is the abstain-on-collapse CATCH of "
        "SOUND-VIOLATING reads, not a calibration number. Worked case: the vague preposition "
        "'around' is read as the RCC-8 disjunction {NTPPi, TPPi}, which DROPS the gold relation EC; "
        "the closure then collapses to the empty set, so the certificate ABSTAINS instead of "
        "committing the wrong relation DC. On the spatial setting every sound-violating read was "
        "caught: 5 of 5 unsound reads triggered collapse-or-abstain, with 0 silent-wrong answers "
        "missed (read-soundness-conditional zero-FP, asserted with 0 violations). The kinship "
        "setting had 0 unsound reads, so its catch holds only TRIVIALLY there and is reported as "
        "UNTESTED rather than as evidence."
    ),
    "calibration_contrast": (
        "Supporting honesty contrast: on genuinely-vague reads the LLM emits calibrated sub-1.0 "
        "disjunctions -- the fraction of reads at confidence exactly 1.0 is 0.00 in BOTH settings, "
        "versus the memorized iter-4 Mode-P's 1.00 (which was table recall, not fuzzy unification). "
        "Per-candidate ECE is 0.142 (spatial) and 0.111 (kinship)."
    ),
    "supporting_number": (
        "The clean within-artifact risk-coverage comparison: the certificate has confident-wrong "
        "0.000 at coverage 0.535 on spatial (n=228, 38 multipath) and 0.000 at coverage 0.314 on "
        "kinship (n=1013), versus commit-argmax confident-wrong 0.364 and 0.216 respectively "
        "(doc-clustered paired-bootstrap reduction CIs [0.303, 0.430] and [0.192, 0.242], both "
        "exclude 0). LEAD with the 5/5 catch; cite this as the supporting magnitude."
    ),
    "demoted_unit_caveat": (
        "DEMOTED caveat (keep, but no headline table): an earlier 0.000-vs-0.415 framing is "
        "APPLES-TO-ORANGES, because the certificate's confident-wrong is measured at the "
        "closure-QUERY level while the confidence baseline's 0.415 / 0.346 thresholded-abstainer "
        "figures (from a different artifact, art_0MDLD-w-RXOu) are at the edge-READ level, matched "
        "only on coverage fraction. The unit mismatch means that contrast must not anchor a table; "
        "the query-level certificate-vs-commit-argmax comparison above is the matched one."
    ),
}

# --------------------------------------------------------------------------- #
# STEP 5 -- headline-structure guidance for GEN_PAPER_TEXT
# --------------------------------------------------------------------------- #
HEADLINE_STRUCTURE_GUIDANCE = [
    "LEAD with the empirical-isolation / confidence-blindness result (FACT A + FACT B + the "
    "mixed-pool showdown), NOT with the closure mechanism.",
    "CONCEDE the mechanism up front as INHERITED: the multi-hop deduction win is a standard "
    "neuro-symbolic premise (+0.673 of the gap is inherited closure; the novel empirical-isolation "
    "increment is +0.0025). Make this concession a framing sentence, not a buried footnote.",
    "Do NOT present the 2.8% certificate confident-wrong on CLUTRR absent pairs as the load-bearing "
    "number; it is structural-by-construction (disconnected components => sound closure abstains by "
    "definition). Use the non-circular-facts ledger to police this.",
    "Carry a clearly-LABELED PENDING slot for the iter-7 natural-corpus run: on Re-DocRED, report "
    "FACT-A (raw absent-hallucination rate), FACT-B (signal survival), and the mixed-pool showdown; "
    "this is what makes the natural-corpus result DECISIVE (the extracted graph is no longer "
    "trivially correct).",
    "Present evidence-class tags (THEOREM / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / REAL-LLM-READ / "
    "REAL-LLM-READ-ON-SYNTHETIC) as table COLUMNS, not inline hedges.",
    "Keep the spatial single-path boundary (P_O honesty): on ordinary single-path RCC-8 the "
    "certificate ties/loses (selective-accuracy gap -0.088, CI brackets 0). State it plainly as the "
    "scope boundary so the paper cannot overclaim generality.",
]
