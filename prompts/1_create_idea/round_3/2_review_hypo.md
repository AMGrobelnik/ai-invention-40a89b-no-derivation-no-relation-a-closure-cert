# review_hypo — create_idea

> Phase: `hypo_loop` · round 3 · Substep: `review_hypo`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave the agent(s) in this substep — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 12:01:18 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviewer (Step 2.2: REVIEW_HYPO)

Pipeline: GEN_HYPO → REVIEW_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You review a hypothesis BEFORE any experiments run. Catch problems early.

Rigorous pre-flight check → saves compute. Rubber-stamping → wasted pipeline run.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the hypothesis under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of
this research hypothesis BEFORE any experiments have been run.

GOAL: Your review feeds directly back to the hypothesis author. The objective is to
maximize the overall review score in subsequent rounds. Every piece of feedback you
give should be written with this goal in mind — prioritize the critiques and suggestions
that would produce the largest score improvement if addressed. Don't waste the author's
iteration budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the ideas new? Novel combination of known techniques? Clear
    differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the proposal technically sound? Are claims well supported? Is the
    methodology appropriate? Are the authors honest about limitations?
(c) Clarity: Is the hypothesis clearly written and well organized? Does it provide
    enough information for an expert to understand and evaluate it?
(d) Significance: Are the expected results important? Would others build on this?
    Does it address a meaningful problem better than prior work?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims and proposed methodology:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas, value to the broader research community:
  4: excellent  3: good  2: fair  1: poor

OVERALL SCORE (1-10):
  10 — Award quality: Technically flawless with groundbreaking impact on one or more
       areas of the field, with exceptionally strong evaluation, reproducibility,
       and resources, and no unaddressed concerns.
   9 — Very Strong Accept: Technically flawless with groundbreaking impact on at least
       one area and excellent impact on multiple areas, with flawless evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   8 — Strong Accept: Technically strong with novel ideas, excellent impact on at least
       one area or high-to-excellent impact on multiple areas, with excellent evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   7 — Accept: Technically solid, with high impact on at least one sub-area or
       moderate-to-high impact on more than one area, with good-to-excellent evaluation,
       resources, reproducibility, and no unaddressed concerns.
   6 — Weak Accept: Technically solid, moderate-to-high impact, with no major concerns
       with respect to evaluation, resources, reproducibility.
   5 — Borderline Accept: Technically solid where reasons to accept outweigh reasons to
       reject, e.g., limited evaluation. Use sparingly.
   4 — Borderline Reject: Technically solid where reasons to reject, e.g., limited
       evaluation, outweigh reasons to accept. Use sparingly.
   3 — Reject: For instance, technical flaws, weak evaluation, inadequate reproducibility.
   2 — Strong Reject: For instance, major technical flaws, poor evaluation, limited
       impact, poor reproducibility.
   1 — Very Strong Reject: For instance, trivial results or unaddressed concerns.

CONFIDENCE (1-5):
  5: Absolutely certain. Very familiar with related work, checked details carefully.
  4: Confident but not absolutely certain. Unlikely you misunderstood something.
  3: Fairly confident. Possible you missed some related work or details.
  2: Willing to defend your assessment, but quite likely missed central aspects.
  1: Educated guess. Not in your area or difficult to evaluate.

For each dimension, provide a list of specific improvements:
- WHAT needs to change
- HOW to change it (concrete enough for the author to act on immediately)
- EXPECTED SCORE IMPACT: how much would fixing this raise the overall score?

REVIEW PRINCIPLES:
- Be specific and actionable — vague critique is useless
- Ground your review in evidence — search for existing work, accepted papers, known results
- Rank critiques by score impact — address the biggest score blockers first
- Distinguish major issues (would waste compute if not fixed) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Flag fatal flaws that would make experiments pointless if not addressed first

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<hypothesis>
kind: hypothesis
title: >-
  Closure-Certified Composition: Exact Relation-Algebra Path Consistency as an Input-Recall-Bounded, Gold-Free Hallucination
  Filter for the Deduction Module of a Text-to-Logic Pipeline
hypothesis: >-
  We position the contribution precisely as the COMPOSITION / DEDUCTION MODULE of a neuro-symbolic text-to-logic pipeline
  (the LLM-to-Prolog reader and upper-ontology typing sit upstream and are held fixed): when an LLM converts text into a relational
  representation and the system must deduce a relation not stated in the text, confident-but-wrong (hallucinated) conclusions
  concentrate in the GLOBAL COMPOSITION of relations across MULTIPLE constraining paths, not in per-edge atomic extraction.
  We propose a specific division of labor: have the LLM emit, for each text span, the SET of base relations the span does
  NOT exclude (a high-recall, NLI-style 'sound-but-loose' disjunctive label rather than a single committed relation, with
  an explicit 'underdetermined'/universal option), and delegate all global PRECISION to an EXACT, decades-old symbolic algorithm
  — algebraic closure / path consistency over a relation algebra whose composition table is published mathematical ground
  truth (Allen's interval algebra, the point algebra, RCC-8). The central guarantee is ONE-DIRECTIONAL and CONDITIONAL ON
  PER-EDGE INPUT RECALL: IF every emitted edge set contains the gold relation, then the LLM network is a superset of a consistent
  gold network and cannot collapse, so a closure VIOLATION (an edge collapsing to the empty relation) is a deductive CERTIFICATE
  that some LLM-supplied edge is unsound — a zero-false-positive DETECTION flag requiring no gold labels. We make three honesty
  commitments the prior version lacked. (1) The certificate bounds DETECTION only; LOCALIZATION/repair via minimal hitting
  sets can blame the wrong edge even when the collapse is genuine, so 'zero-FP' is scoped to detection, not repair. (2) Path
  consistency is SOUND BUT INCOMPLETE for full Allen IA and RCC-8 (consistency is NP-complete; complete only for the point
  algebra and ORD-Horn-style tractable subclasses), so 'passes closure' does not mean consistent and the closure-detectable
  hallucination rate is a LOWER BOUND on catchable errors. (3) We pre-register the dangerous DUAL of recall failure: when
  a high-recall set OMITS gold (an UNSOUND label, rate 1−recall), closure can NARROW the query to a confident WRONG singleton
  with NO empty collapse — a certified-LOOKING hallucination the mechanism actively endorses, strictly worse than an invisible
  single-chain error. The method therefore trades the LLM's over-commitment for the LLM's recall failure, and 'high recall'
  is in direct tension with 'narrow enough to be useful'; we MEASURE per-edge recall in a pilot first and gate every soundness
  claim on it. We predict that on the regime where the mechanism can act — networks with REDUNDANT paths or cycles between
  the query pair (the relation is over-determined) — closure-certified composition (a) detects and localizes closure-detectable
  hallucinated atoms/compositions with zero false-positive DETECTION flags conditional on measured recall, (b) lets the system
  ABSTAIN when the query stays a disjunction rather than guess, and (c) yields a strictly better accuracy-vs-coverage (risk–coverage)
  trade-off AT MATCHED COVERAGE than free LLM composition, self-consistency voting, LINC, Path-of-Thoughts, and DSR-LM — each
  equipped with its own matched abstention signal. The advantage GROWS with the number of independent constraining paths (network
  redundancy / cyclomatic structure) — the qualitative analogue of an error-correcting code's redundancy — and therefore with
  hop count ONLY when extra hops add redundancy, not on single-chain inputs where closure provably reduces to plain table-lookup
  composition and we predict NO advantage. The net benefit is conditional on TWO co-occurring quantities, both measured before
  the main run: a non-trivial OVER-COMMITMENT rate (confident wrong singletons that create detectable contradictions, vs UNDER-SPECIFICATION
  which leaves nothing to narrow) AND non-trivial MULTI-PATH BITE in the data.
motivation: >-
  Faithful multi-hop relational reasoning over short professional text — temporal ordering of events in news, kinship in narratives,
  containment/region relations in descriptions — is where LLM hallucination is most damaging and where a text-to-logic pipeline
  most needs to fuse explicit document facts with implicit composition knowledge while staying auditable. The umbrella pipeline
  reads text into FOL/Prolog predicates, types entities against an upper ontology, and answers queries with a reasoner; the
  WEAK LINK is the composition/deduction step. Existing text-to-logic systems handle composition unsatisfyingly: humans hand-craft
  composition rules (the kinship rules behind CLUTRR), which do not scale; the LLM composes freely, which is locally fluent
  but globally inconsistent and produces silent errors that solver-crash feedback (Logic-LM) and answer voting (LINC) cannot
  see; or paths are reasoned in isolation (LAMBADA, Path-of-Thoughts), which deliberately avoids the global check and so cannot
  resolve disjunctive uncertainty or detect contradictions arriving at the same pair from two paths. The qualitative-reasoning
  community has had exact, commodity-cheap path-consistency algorithms over relation algebras (Allen 1983; Renz & Nebel; solvers
  GQR, SparQ) for forty years — but they assume a clean, hand-given table and have never been coupled to an LLM that reads
  relations off natural language. We are NOT the first to run closure over machine-extracted temporal relations: SputLink
  (Verhagen) computes temporal closure to densify TimeBank, and CAEVO (Chambers et al. 2014) does global temporal inference
  via cascaded sieves over the same coarse algebra. Our contribution is orthogonal to theirs: those systems COMMIT to a single
  consistent labeling to maximize extraction F1 (or are the very closure tool used to BUILD the gold), preserving no disjunction,
  certifying no reading error, and offering no abstention; we keep the LLM's job as high-recall disjunctive READING, use closure
  as a gold-free CERTIFICATE of reading error, and optimize faithfulness-by-abstention via a risk–coverage objective — the
  OPPOSITE output contract from F1-maximizing global inference (Ning et al.'s ILP). Two ideas make the transfer a genuine
  contribution rather than a port: first, because Allen/point/RCC-8 tables are EXACT ground truth, closure is a calibration-free
  hallucination certificate (conditional on input recall) and multi-path redundancy in a document becomes an error-correcting
  code over LLM extractions; second, the objective is the opposite of F1 — we preserve disjunctive uncertainty and ABSTAIN,
  trading coverage for faithfulness, which is what a hallucination-controlled, human-auditable pipeline actually needs. Recent
  QSTR evaluations show frontier LLMs are good at SINGLE-STEP composition (QSTRBench ~98% on Allen-interval composition for
  the best model) yet strong models tend to OVER-PREDICT and weak models UNDER-specify, and a temporal-constraint study (Marín
  2025) finds even simple before/during relations are applied brittlely and explicitly calls for hybrid symbolic modules.
  This reframes the opportunity: the LLM is a decent LOCAL namer that does not PROPAGATE constraints across paths, and its
  over-commitment is exactly the error a global closure check can certify and repair. If it works, this is a general, training-free
  recipe for trustworthy relational deduction over text with quantified, certificate-backed hallucination reduction and replayable
  trace-graphs; if it fails (closure detects but cannot reliably repair, LLMs under-specify so there is nothing to certify,
  or recall failures drive silent wrong narrowings), each is itself a publishable scope boundary on repairing LLM-read relational
  knowledge.
assumptions:
- >-
  SCOPE / MODULE FRAMING: the target reasoning is RELATIONAL and COMPOSITIONAL — the answer is a relation between a pair obtained
  by composing base relations along paths in an entity/event graph (temporal before/after/overlap/includes, spatial containment/region
  connection, kinship). This is the deduction MODULE of a general text-to-logic pipeline, not a replacement for it; arbitrary
  propositional rule chaining (RuleTaker) is out of scope and used only as a contrastive negative. We report, per corpus,
  the RELATION-COMPOSABLE FRACTION of queries (the module's applicability envelope) and hold atomic extraction precision/recall
  fixed across the comparison so any gain is attributable to composition, not extraction.
- >-
  EXACT-TABLE primacy, correctly scoped: 'mathematical ground truth' applies cleanly to the SYNTHETIC Allen/point/RCC-8 settings
  AND to the real-text MATRES arm, whose start-point labels (BEFORE/AFTER/EQUAL/VAGUE) instantiate the POINT ALGEBRA — where
  path-consistency is provably COMPLETE and the table is exact. It does NOT apply uniformly to TimeBank-Dense, whose 6-label
  scheme is a DESIGNED COARSENING of Allen's 13 relations realized by a specific transitivity table (the SputLink/CAEVO convex-relation
  table, which we cite and use verbatim rather than asserting it is canonical); for that arm disjunctive composites frequently
  collapse to VAGUE, structurally bounding narrowing yield. The LLM is NEVER asked to supply the composition table for any
  primary setting, dissolving elicitation circularity; LLM-elicited tables are studied ONLY as an explicit kinship/CLUTRR
  ablation against a gold table.
- >-
  INPUT-RECALL (measured, not assumed): every soundness/zero-FP statement is conditional on per-edge INPUT RECALL = P(gold
  relation ∈ LLM's emitted set). We do NOT assume recall=1; we MEASURE it in the pilot, report the decomposition of all gold-wrong
  non-abstained predictions into closure-collapse-caught vs silent-wrong-narrowing-from-an-unsound-edge vs invisible-single-chain,
  and (optionally) gate certified narrowings on a measured recall floor. The dual failure — an unsound tight set driving a
  confident wrong narrowing with no collapse — is a pre-registered failure mode whose rate is bounded by (1−recall).
- >-
  BITE (pre-measured per dataset): the data must contain instances where two or more NON-VAGUE/non-universal paths constrain
  the query pair (redundancy / cycles), so intersection and contradiction-detection are exercised. GUARANTEED by construction
  in the synthetic generator. For real text we PRE-MEASURE bite BEFORE the main run — non-VAGUE constraint density, fraction
  of query pairs with ≥2 non-VAGUE constraining paths, and achievable narrowing yield on held-out deduced pairs — and pre-register
  the bite threshold required for the real-text claim to be 'live' vs scoped as 'sound-but-inert'. All results are stratified
  into single-path vs multi-path subsets.
- >-
  ERROR-TYPE (measured, conditional): the benefit is conditional on the LLM's dominant per-edge error being OVER-COMMITMENT
  (confident wrong singleton → detectable contradiction) rather than UNDER-SPECIFICATION (safe broad disjunction → nothing
  to narrow). We MEASURE this in the pilot and predict realized gain tracks the measured over-commitment rate. GOLD is available
  without new annotation: synthetic networks ship exact gold; MATRES ships direct human start-point gold (not closure-densified);
  TimeBank-Dense ships gold whose transitive closure yields deduced gold (with the caveat that this gold is partly the OUTPUT
  of the closure tool we are testing, handled explicitly below).
investigation_approach: >-
  PILOT (cheap, first, de-risks the premise AND calibrates realism): generate small qualitative constraint networks, render
  each edge to NL, ask the LLM for the per-edge disjunctive relation, and MEASURE the error decomposition on BOTH synthetic
  and real (MATRES/TimeBank-Dense) edges — per-edge SOUNDNESS/recall (is gold inside the emitted set?), breadth (set size),
  over-commitment vs under-specification rate, and the raw closure-VIOLATION rate of un-checked LLM networks. This establishes
  (or refutes) the motivating premise and supplies the real-text error profile used to validate the synthetic generator's
  realism. PIPELINE (four stages): (1) NEURAL READING — prompt the LLM to map each surface relation phrase onto a SOUND DISJUNCTION
  of canonical base relations, optimizing recall with an explicit 'underdetermined'/universal option; for the MATRES point-algebra
  arm we restrict the emitted vocabulary to CONVEX point relations (treating the non-convex {<,>} as widened to VAGUE) so
  path-consistency stays COMPLETE. (2) ALGEBRA — use the EXACT published composition table (Allen 13-relation, point algebra,
  RCC-8; the SputLink/CAEVO convex table for the TimeBank-Dense arm, cited verbatim); seed converses/identity from the algebra,
  never from an LLM. (3) SYMBOLIC CLOSURE (the contribution) — build a QCN (nodes = events/entities, edges = relation SETS;
  explicit edges from stage 1, the query edge starts universal), run path-consistency to a fixpoint; closure NARROWS the query,
  an empty collapse CERTIFIES an extraction error (DETECTION, zero-FP conditional on recall). On inconsistency, compute a
  minimal repair (Reiter-style minimal hitting set / small MaxSAT) preferring to relax lowest-confidence edges, recording
  the diagnosis AND flagging that localization — unlike detection — may mislocalize; if the query stays a disjunction of >1
  relation, ABSTAIN. (4) AUDIT — emit the QCN, which compositions fired on which paths, and any repairs as a trace-graph,
  optionally discharged in SWI-Prolog/ASP from the closed table for a replayable proof (this is the connective tissue to the
  umbrella pipeline's auditability and quantified-hallucination-reduction requirements). DATASETS — SYNTHETIC PRIMARY (clean
  ground truth, controlled redundancy): a Renz–Nebel-style random consistent Allen/point QCN generator that GUARANTEES redundant
  paths/cycles and lets us sweep redundancy/density/hop-count independently. Critically, we PRE-REGISTER the NL-realization
  protocol (a fixed library mapping each base relation to a graded set of clean→ambiguous paraphrases) and VALIDATE that the
  per-edge error decomposition it induces (over-commitment/under-specification/breadth/recall) MATCHES the pilot's real-text
  decomposition; the redundancy-scaling curve is reported ONLY at the realism-matched difficulty setting, killing the 'tunable-difficulty
  artifact' confound. REAL-TEXT PRIMARY (to ensure the headline is not carried by a self-built generator): MATRES (Ning, Wu
  & Roth 2018; ~275 news docs, ~13.6k pairs) — its scheme 'explicitly compare[s] the time points' of event start-points so
  'the label set is simply before, after and equal' (verified in the paper) plus VAGUE, i.e. literally the POINT ALGEBRA,
  where path-consistency is provably COMPLETE and the table is exact; its gold is DIRECT crowdsourced human annotation (IAA
  .84 Cohen's Kappa), NOT transitive-closure-densified, making it the cleanest real arm. Caveat we account for: MATRES annotates
  only pairs within a 2-sentence sliding window on the same axis, so multi-path bite is PRE-MEASURED (not assumed); we draw
  long-distance (deduced) query pairs from TDDiscourse-style discourse-level pairs over the same documents. REAL-TEXT SECONDARY:
  TimeBank-Dense (36 docs, ~12.7k relations, 6-label coarse algebra) — used only if pre-measured bite clears threshold; we
  explicitly handle its two confounds — (i) its non-adjacent gold is partly the OUTPUT of SputLink closure, so we evaluate
  the LLM+closure pipeline as 'noisy-read-of-local-edges → closure vs clean-read closure' (the errors come from the LLM, gold
  deduced = closure over CLEAN human local edges, which is sound to compare against), and (ii) ~43% VAGUE caps narrowing,
  which we report rather than hide. RCC-8 synthetic gives a second algebra; CLUTRR is the kinship venue for the ELICITED-table
  ablation (with the caveat that single-chain CLUTRR has closure-ON == closure-OFF), plus a mined/synthesized multi-path subset.
  RuleTaker is an out-of-scope contrast. KEY ABLATIONS: (i) closure ON vs OFF with the table HELD FIXED (isolates path consistency
  from 'a fixed consistent table exists' — the DSR-LM contribution); (ii) repair OFF (detect-only/abstain); (iii) disjunction
  OFF (force singletons — tests the sound-but-loose claim); (iv) exact-table vs LLM-elicited-table (tests the gold-free-certificate
  claim, kinship only); (v) recall-floor gate ON vs OFF (tests whether gating on measured per-edge recall suppresses silent
  wrong narrowings). BASELINES, EACH WITH A MATCHED ABSTENTION SIGNAL: raw LLM (verbalized confidence), CoT (verbalized confidence),
  self-consistency (vote margin), LINC-style multi-formalization vote (vote agreement), DSR-LM-style induced-rule Prolog (no
  closure), Path-of-Thoughts (PRIMARY baseline; path-agreement as abstention, reported on the multi-path subset), a TempRel-style
  COMMIT baseline (forces a single consistent labeling), and a soft-unification neural theorem prover. METRICS, per-regime
  and STRATIFIED (single- vs multi-path, single- vs disjunctive-query): (1) risk–coverage / selective accuracy AT MATCHED
  COVERAGE (headline) with paired bootstrap CIs on the selective-accuracy gap vs each baseline; (2) closure-DETECTABLE hallucination
  rate, with the full decomposition of gold-wrong non-abstained predictions into (a) collapse-caught, (b) silent-wrong-narrowing-from-unsound-edge,
  (c) invisible-single-chain — explicitly reported as a LOWER BOUND given path-consistency incompleteness on Allen IA/RCC-8;
  (3) bite — fraction of instances triggering non-trivial intersection or empty collapse (proof the mechanism is exercised);
  (4) repair quality (fraction of repairs moving the query edge TOWARD vs AWAY from gold, CI-separated), reported separately
  from detection because localization can err; (5) elicited-table composition P/R vs gold + multi-sample self-agreement (kinship);
  (6) gain-vs-redundancy and gain-vs-hop-count curves at realism-matched difficulty; (7) atomic extraction P/R reported as
  a HELD-FIXED control. The optional probabilistic/semiring variant carries per-relation weights as EXPLORATORY soft propagation
  with a reliability diagram / ECE; the hard, exact, calibration-free closure path is the primary contribution. All LLM calls
  go through OpenRouter; cost stays well under $10 via short documents, caching, and a cheap extraction model; closure and
  repair run in milliseconds per network on a laptop.
success_criteria: >-
  HEADLINE PREDICTION (single, leads everything): on the MULTI-PATH subset at REALISM-MATCHED difficulty, closure-certified
  composition achieves strictly higher selective accuracy AT MATCHED COVERAGE than Path-of-Thoughts and self-consistency voting
  (each given its own matched abstention signal), with the gap CI-separated from zero under paired bootstrap. CONFIRMS if,
  in addition: (1) the table-held-fixed closure-ON ablation beats closure-OFF (isolating path consistency from the mere existence
  of a fixed table) and the gain scales with measured redundancy at realism-matched difficulty; (2) conditional on the pilot-measured
  per-edge recall, closure produces ZERO false-positive DETECTION flags (every certified collapse is a genuine reading error)
  — a DETECTION claim, stated separately from repair; (3) repairs move the query edge toward gold significantly more often
  than away (CI-separated), acknowledged as a weaker localization claim; (4) the disjunction-ON variant beats the commit-to-singleton
  variant (supports sound-but-loose labeling); (5) realized gain tracks the pilot-measured over-commitment rate; (6) at least
  ONE real-text arm (MATRES preferred) clears the pre-registered bite threshold so the headline is not synthetic-only. DISCONFIRMS
  / SCOPES if: no risk–coverage benefit over Path-of-Thoughts or voting at matched coverage on the multi-path subset; closure-ON
  == closure-OFF even when multi-path; gain does not scale with redundancy; or elicited-table repair frequently moves toward
  the wrong relation. PRE-REGISTERED HONEST FAILURE MODES (each a publishable scope boundary): (a) UNDER-SPECIFICATION — LLMs
  emit broad safe disjunctions, closure is sound but inert (low yield); (b) CONSISTENT-BUT-WRONG elicited table — shown only
  in kinship, quantified vs gold, shown NOT to arise in exact-table settings; (c) INVISIBLE hallucinations — confident self-consistent
  single-chain errors closure structurally cannot see; (d) NEW — SILENT WRONG NARROWING — an UNSOUND high-recall set that
  omits gold drives closure to a confident WRONG singleton with NO collapse; we report its rate, show it is bounded by (1−recall),
  and test whether the recall-floor gate suppresses it. Throughout, 'zero false-positive' is scoped to DETECTION (not repair),
  and the closure-detectable hallucination rate is reported as a LOWER BOUND because path-consistency is incomplete for Allen
  IA/RCC-8 (complete only for the MATRES point-algebra arm). Atomic extraction P/R must remain comparable to baselines (the
  contribution is at composition), the relation-composable fraction per corpus must be reported (applicability envelope),
  and trace-graphs must be judged human-auditable.
related_works:
- >-
  Temporal-relation extraction with ILP global inference (Ning, Feng & Roth 2017, EMNLP; arXiv:1906.04943; CogCompTime): a
  TRAINED extractor produces per-pair scores and Integer Linear Programming enforces transitivity + symmetry to output a single
  globally-consistent labeling. Closest prior art for 'enforce qualitative consistency on machine-extracted temporal relations.'
  Differences: (1) it COMMITS to one relation per pair to maximize extraction F1; we PRESERVE disjunctive uncertainty and
  ABSTAIN, optimizing risk–coverage — the opposite output contract; (2) it uses LEARNED scores and approximate optimization
  (a high-score consistent labeling can be wrong); we use the EXACT published table so closure is a sound, gold-free DETECTION
  certificate (conditional on input recall); (3) it needs a trained per-corpus model; our reader is an untrained LLM doing
  fuzzy semantic unification and generalizes across algebras. We additionally localize/repair and emit auditable trace-graphs.
- >-
  SputLink (Verhagen 2004/2005, 'Temporal Closure in an Annotation Environment'): computes temporal closure over TimeBank
  using a convex subset of Allen's interval algebra (a 29×29 composition table / hundreds of transitivity axioms), and was
  used to DENSIFY TimeBank and TimeBank-Dense so the resulting graphs are strongly connected and consistent. Difference: SputLink
  is the closure tool that BUILDS gold over already-formal human annotations and commits to a labeling; it does not read relations
  off NL, preserves no LLM disjunction, certifies no reading error, and has no abstention/risk–coverage objective. We explicitly
  treat its role to avoid circularity: on TimeBank-Dense, gold deduced relations are SputLink's output over CLEAN human local
  edges, and we test whether an LLM's NOISY read of those local edges, when closed, recovers them.
- >-
  CAEVO (Chambers, Cassidy, McDowell & Bethard 2014, TACL, 'Dense Event Ordering with a Multi-Pass Architecture'): a 'precision-ranked
  cascade of sieves' (12 sieves, verified) mixing rule-based and machine-learned classifiers; after each sieve the architecture
  'infers transitive links from the new labels and adds them to the graph' and 'imposes transitivity constraints' (verified)
  over the coarse TimeBank-Dense algebra. Difference: CAEVO is a trained/rule extractor that COMMITS to a single dense consistent
  labeling for F1; it does not preserve disjunction, does not use consistency as a gold-free hallucination certificate over
  LLM-read relations, and does not abstain. We reuse its coarse composition table (cited) but invert the objective to faithfulness-by-abstention
  over LLM disjunctive reads.
- >-
  QSTRBench (2026, arXiv:2605.18380): benchmarks whether LLMs can compute SINGLE-STEP composition-table entries, converses,
  and conceptual neighbourhoods across calculi, finding the best model ~98% on Allen-interval composition, with weak models
  UNDER-specifying and the strongest OVER-predicting. We use it to correctly characterize the premise (good local namer, model-dependent
  error type) — not to claim LLMs 'cannot compose.' Difference: it measures single-step ability only; we turn the closure
  ALGORITHM into a control wrapper that propagates the LLM's per-edge labels across multiple paths and uses violations to
  certify/repair — multi-hop propagation it does not test.
- >-
  Empirical Characterization of Temporal Constraint Processing in LLMs (Marín 2025, arXiv:2511.10654): characterizes LLM brittleness
  at applying even simple Allen relations and explicitly argues for hybrid architectures with symbolic reasoning modules.
  Difference: it is characterization and proposes NO coupling; it runs no external path-consistency solver over a disjunctive
  network nor uses consistency as a hallucination certificate. We build exactly the hybrid module it calls for and evaluate
  it as a faithfulness mechanism.
- >-
  TReMu (2025, arXiv:2502.01630): neuro-symbolic temporal reasoning that has the LLM identify timestamps and generate executable
  code. Difference: it quantizes to METRIC time and executes code, discarding qualitative disjunction; it cannot represent
  'the text leaves this relation underdetermined,' cannot abstain on a disjunction, and has no consistency certificate. We
  stay purely QUALITATIVE, carry disjunctive sets, narrow by exact path consistency, and abstain when underdetermined.
- >-
  Path-of-Thoughts (2024, arXiv:2412.17963): three stages — graph extraction, path identification, per-path reasoning — beating
  SOTA by up to 21.3% on relational benchmarks (StepGame, CLUTRR). PRIMARY baseline. Difference (verified in the paper): it
  calls an external reasoner 'for each reasoning path' INDEPENDENTLY and does NOT intersect relations arriving at the same
  pair from multiple paths nor detect cross-path contradictions; when paths disagree it 'output[s] multiple possible relations'
  but does NOT abstain or flag uncertainty. On single-chain inputs it captures most of what closure would, so our claim is
  restricted to the MULTI-PATH subset where intersection/contradiction-detection are required. We give it a matched abstention
  signal (path-agreement) for a fair matched-coverage comparison, which it otherwise lacks.
- >-
  DSR-LM / 'LLMs can Learn Rules' (Yang et al. 2023, arXiv:2305.03742; Zhu et al. 2023, arXiv:2310.07064): INDUCE weighted/symbolic
  composition rules to fit task accuracy. Difference: rule induction optimizes data fit and gives a point answer; we enforce
  the EXACT ALGEBRAIC LAWS (converse, associativity, disjointness) necessary for soundness independent of training data, and
  use closure to DETECT/CERTIFY/LOCALIZE/REPAIR/ABSTAIN. Our table-held-fixed closure-ON-vs-OFF ablation specifically isolates
  path-consistency from 'a fixed consistent table exists,' which is DSR-LM's contribution.
- >-
  Logic-LM (Pan et al. 2023, arXiv:2305.12295) and LINC (Olausson et al. 2023, EMNLP, arXiv:2310.15164): Logic-LM self-refines
  a formulation using solver crash/unsat messages; LINC majority-votes the answers of multiple formalizations. Difference:
  Logic-LM reacts only to crashes and has no positive global INVARIANT over relational knowledge; LINC's answer-level voting
  cannot see that individually-popular composition steps are JOINTLY inconsistent. Algebraic closure is a global necessary
  condition both lack, and it narrows disjunctive uncertainty rather than averaging samples. We give LINC vote-agreement as
  a matched abstention signal in the comparison.
- >-
  LAMBADA (Kazemi et al. 2023, arXiv:2212.13894) and path-isolation reasoning: backward chaining / per-path reasoning that
  manages inconsistency by COMPOSITIONAL ISOLATION rather than global enforcement. Difference: we do the opposite — intersect
  across paths via closure, which both tightens disjunctions and detects contradictions; isolation can return mutually inconsistent
  answers and cannot resolve disjunctive uncertainty.
- >-
  Logically Consistent Language Models / LOCO-LMs (Calanzone, Teso & Vergari 2024, arXiv:2409.13724; ICLR 2025): a TRAINING-TIME
  neuro-symbolic loss fine-tuning an LLM to be consistent with a set of propositional facts/rules. Difference: it is training-time
  and PROPOSITIONAL; we are training-free at INFERENCE time and enforce multi-hop COMPOSITION closure over a RELATION ALGEBRA
  read off text, producing per-instance certificates, abstention, and trace-graphs. This pre-empts a 'consistency enforcement
  is not new' objection: prior LM-consistency work enforces propositional/factual consistency, not relation-algebra composition
  closure on text-derived relations.
- >-
  Classical qualitative reasoners and tractability theory: GQR, SparQ, Allen (1983), Renz & Nebel (path consistency / random
  network model A(n,d,l)), and the tractability results (Vilain & Kautz 1986 point algebra; Nebel & Bürckert 1995 ORD-Horn,
  JACM 42(1)) which prove verbatim that 'the path-consistency method is sufficient for deciding satisfiability' in ORD-Horn
  (a 'maximal tractable subclass' strictly containing the pointisable subclass) but is 'in general not sufficient' for the
  full algebra, where consistency is 'NP-hard' — so path-consistency is COMPLETE for the point algebra and ORD-Horn yet SOUND-BUT-INCOMPLETE
  for full Allen IA / RCC-8. Difference: these assume a clean human-given table on already-formal data; none read the algebra
  off NL via an LLM, certify reading errors, or optimize risk–coverage. We import their exact machinery and tractability facts
  (which is why our MATRES point-algebra arm gives a COMPLETE check while Allen IA closure is reported as a lower-bound detector).
inspiration: >-
  A Level-3 (methodological) cross-domain transfer from Qualitative Spatial-Temporal Reasoning and Tarski's relation algebras
  — Allen's interval algebra, RCC-8, the point algebra, composition tables, and the path-consistency / algebraic-closure constraint-propagation
  algorithms (classical solvers GQR/SparQ), plus the tractability theory (point-algebra and ORD-Horn completeness vs full-Allen
  NP-completeness) — imported into LLM-based relational reasoning and hallucination control, together with Reiter's 1980s
  model-based diagnosis (minimal hitting sets of conflict sets) for localizing which extracted atom to retract. A Level-1
  framing is borrowed from CODING THEORY: an exact composition table turns multi-path redundancy in a document into an error-correcting
  code over the LLM's extractions — redundant constraining paths let closure DETECT and CORRECT mis-reads with no external
  labels, exactly as parity checks detect bit errors, and the benefit scales with redundancy the way decoding power scales
  with code rate. The revision sharpens this with a CHANNEL-CAPACITY caveat from the same field: a code only corrects errors
  if the inputs are within its decoding radius — here, the per-edge INPUT must actually contain the gold relation (recall),
  or closure 'decodes' confidently to the wrong codeword (the silent-wrong-narrowing failure). A Level-2 framing comes from
  SELECTIVE PREDICTION / risk–coverage in ML: the right way to compare an abstaining method against non-abstaining baselines
  is at MATCHED COVERAGE with each baseline given its own confidence signal. Three refined cross-field insights drive the
  design: (1) LLMs behave like competent LOCAL qualitative namers that do NOT propagate constraints across paths — the missing
  piece is global propagation, not local naming; (2) because the algebra's table is mathematical ground truth, consistency
  becomes a calibration-free, zero-false-positive DETECTION certificate — conditional on input recall — flipping the objective
  from accuracy-by-committing (ILP global inference) to faithfulness-by-abstaining; (3) the same coding-theory lens names
  the method's Achilles heel (recall-bounded decoding radius), which we elevate to a pre-registered failure mode rather than
  hide.
terms:
- term: Relation algebra
  definition: >-
    An algebraic structure (after Tarski) over a finite set of base relations with composition, converse, intersection, union,
    and identity, closed under these operations. Allen's 13 interval relations, the point algebra, and RCC-8 spatial regions
    are standard examples; it supplies the laws (converse, associativity) that correct compositional reasoning must obey.
- term: Exact composition table
  definition: >-
    For each ordered pair of base relations (r,s), the set of base relations the composite r-then-s can take. For Allen IA,
    the point algebra, and RCC-8 these tables are PUBLISHED MATHEMATICAL GROUND TRUTH. The TimeBank-Dense 6-label table is
    a DESIGNED COARSENING (the SputLink/CAEVO convex table) — cited verbatim, not asserted canonical. LLM-elicited tables
    (kinship) are studied only as an ablation against gold.
- term: Algebraic closure / path consistency
  definition: >-
    A constraint-propagation algorithm that repeatedly tightens each edge's relation set by intersecting it with the composition
    of relations along every two-step path, until a fixpoint. It is SOUND (never infers an inconsistent path) and an empty
    collapse certifies inconsistency, but it is INCOMPLETE for full Allen IA / RCC-8 (consistency is NP-complete) and COMPLETE
    only for the point algebra and ORD-Horn-style subclasses. Polynomial and millisecond-fast per document.
- term: Point algebra (MATRES arm)
  definition: >-
    The relation algebra over a single time point per event with base relations <, =, > and disjunctions thereof. MATRES's
    BEFORE/AFTER/EQUAL/VAGUE start-point labels instantiate the CONVEX point algebra, for which path-consistency is provably
    COMPLETE and the table is exact — making MATRES the cleanest real-text certificate arm. We restrict the LLM's emitted
    vocabulary to convex point relations (widening the non-convex {<,>} to VAGUE) to preserve completeness.
- term: Qualitative constraint network (QCN)
  definition: >-
    A graph whose nodes are entities/events and whose edges carry a SET of possible base relations (a singleton = known relation;
    a larger set = disjunctive uncertainty; the universal relation = unknown). The data structure on which closure operates;
    the query edge starts universal and is narrowed by closure.
- term: Sound-but-loose disjunctive labeling
  definition: >-
    Reframing the LLM's task from 'name THE relation' (precision-oriented, over-commitment-prone) to 'name the set of base
    relations the text span does NOT exclude' (recall-oriented, NLI-like). Soundness means the gold relation is INSIDE the
    emitted set; precision is delegated to exact closure. Its failure is RECALL failure (gold omitted), the source of silent
    wrong narrowing.
- term: Input-soundness / per-edge recall
  definition: >-
    The probability that an LLM's emitted edge set CONTAINS the gold relation. Every zero-false-positive / 'provably sound
    narrowing' claim is conditional on this quantity, which is MEASURED in the pilot (not assumed = 1). The rate of the dual
    failure (silent wrong narrowing) is bounded by 1 − recall; an optional recall-floor gate withholds certified narrowings
    when measured recall is below a threshold.
- term: Gold-free hallucination certificate (one-directional, detection-only)
  definition: >-
    Conditional on input recall, a closure collapse is a deductive PROOF that some LLM-supplied edge is unsound — a zero-false-positive
    DETECTION flag needing no gold labels. It is ONE-DIRECTIONAL (no collapse does NOT imply correctness) and scoped to DETECTION;
    LOCALIZATION/repair (minimal hitting set) may blame the wrong edge even when the collapse is genuine. Multi-path redundancy
    supplies the cross-checks, analogous to parity checks in an error-correcting code.
- term: Silent wrong narrowing (pre-registered failure mode)
  definition: >-
    When a high-recall set OMITS gold (an unsound label), closure can narrow the query to a confident WRONG singleton with
    NO empty collapse — a certified-LOOKING hallucination the mechanism actively endorses, strictly worse than an invisible
    single-chain error. Its rate is governed by per-edge unsoundness (1 − recall) and reported in the decomposition of gold-wrong
    non-abstained predictions.
- term: Over-commitment vs under-specification
  definition: >-
    The two per-edge LLM error types. Over-commitment = a confident WRONG singleton, producing detectable contradictions closure
    can certify/repair. Under-specification = a safe BROAD disjunction (sound but uninformative), giving closure little to
    narrow. Yield is conditional on a non-trivial over-commitment rate, measured by pilot.
- term: Multi-path bite
  definition: >-
    An instance where two or more NON-VAGUE/non-universal paths constrain the query pair, so closure performs a non-trivial
    intersection or detects an empty collapse. PRE-MEASURED per real dataset (non-VAGUE density, fraction of pairs with ≥2
    constraining paths, achievable narrowing) against a pre-registered threshold; it is the regime where closure provably
    differs from single-chain table-lookup composition.
- term: Matched-coverage selective comparison
  definition: >-
    The protocol for comparing an abstaining method against baselines: each baseline is given its own abstention/confidence
    signal (vote margin, verbalized confidence, vote agreement, path-agreement), thresholds are swept so every method reports
    at the SAME coverage, and selective accuracy is compared with paired bootstrap CIs — preventing the headline from conflating
    'closure' with 'closure has a better-calibrated abstain than baselines were given.'
- term: Realism-matched difficulty
  definition: >-
    A pre-registered NL-realization protocol for the synthetic generator (a fixed library of clean→ambiguous paraphrases per
    base relation) tuned so the induced per-edge error decomposition (over-commitment / under-specification / breadth / recall)
    MATCHES the pilot's real-text decomposition. The redundancy-scaling curve is reported only at this setting, so 'advantage
    grows with redundancy' cannot be a tunable-difficulty artifact.
- term: Minimal repair (model-based diagnosis)
  definition: >-
    On a certified inconsistency, the smallest set of LLM-supplied edges whose revision restores a non-empty closure, computed
    as a Reiter-style minimal hitting set of conflict sets (or small MaxSAT), preferring to relax lowest-confidence edges.
    It LOCALIZES and proposes a correction but — unlike DETECTION — can mislocalize; repair quality is scored as toward-vs-away-from-gold
    movement with CIs.
- term: Trace-graph
  definition: >-
    A human-auditable record: the QCN, which composition entries fired on which paths during closure, any minimal repairs,
    and optionally an equivalent SWI-Prolog/ASP proof discharged from the closed table for replay — the connective tissue
    to the umbrella text-to-logic pipeline's auditability and quantified-hallucination-reduction requirements.
summary: >-
  We position EXACT relation-algebra path consistency (Allen, point algebra, RCC-8), imported from qualitative spatial-temporal
  reasoning, as the gold-free deduction MODULE of a text-to-logic pipeline: the LLM emits high-recall 'sound-but-loose' disjunctive
  relation labels and closure supplies global precision, so — conditional on measured per-edge recall — a closure collapse
  is a one-directional, zero-false-positive DETECTION certificate that the LLM mis-read the text, enabling localization, repair,
  and principled abstention. We test it where it provably bites (synthetic multi-path QCNs at realism-matched difficulty plus
  a real-text point-algebra arm, MATRES, with pre-measured bite), with a table-held-fixed ablation isolating path consistency
  and a risk–coverage headline compared at MATCHED COVERAGE against baselines given matched abstention signals — predicting
  lower closure-detectable hallucination (a lower bound, since path consistency is incomplete for Allen IA/RCC-8) and better
  selective accuracy that scale with redundancy, while pre-registering silent-wrong-narrowing from recall failure as an explicit
  failure mode.
</hypothesis>

<review_context>
No experiments have been run yet — evaluate the hypothesis purely on its merits.
</review_context>

<previous_hypothesis>
The hypothesis from the PREVIOUS iteration (before the revision under review).
Use this to classify how the current hypothesis relates to it (see the H↔H
edge instructions in the task).

kind: hypothesis
title: >-
  Closure-Certified Reasoning: Exact Relation-Algebra Path Consistency as a Gold-Free Hallucination Filter over LLM-Read Disjunctive
  Relations
hypothesis: >-
  When an LLM converts text into a relational logical representation and a system must deduce a relation not stated in the
  text, the place where confident-but-wrong (hallucinated) multi-hop conclusions concentrate is the LLM's GLOBAL COMPOSITION
  of relations across MULTIPLE constraining paths, not its per-edge atomic extraction. We hypothesize a specific, testable
  division of labor: have the LLM emit, for each text span, the SET of base relations the span does NOT exclude (a high-recall,
  NLI-style 'sound-but-loose' disjunctive label rather than a single committed relation), and delegate all global PRECISION
  to an EXACT, decades-old symbolic algorithm — algebraic closure / path consistency over a relation algebra whose composition
  table is mathematical ground truth (Allen's interval algebra, the point algebra, RCC-8). Because the composition table is
  exact, a closure VIOLATION (an edge collapsing to the empty relation) is a CERTIFICATE — not a heuristic flag — that the
  LLM mis-read the text, and an intersection that NARROWS a query edge below what any single path licenses is provably sound.
  We predict that on the regime where this mechanism can act — networks with REDUNDANT paths or cycles between the query pair,
  exactly where the relation is over-determined — closure-certified reasoning (a) detects and localizes the hallucinated atom/composition
  with zero false-positive error flags, (b) lets the system ABSTAIN when the query relation stays a disjunction rather than
  guess, and (c) yields a strictly better accuracy-vs-coverage (risk–coverage) trade-off and a lower closure-DETECTABLE hallucination
  rate than free LLM composition, answer-level voting (LINC), path-isolation graph reasoning (Path-of-Thoughts), and LLM-induced-rule
  pipelines (DSR-LM). The advantage GROWS with the number of independent constraining paths (network redundancy / cyclomatic
  structure), the qualitative analogue of an error-correcting code's rate, and therefore with hop count ONLY when extra hops
  add redundancy — not on single-chain inputs, where closure provably reduces to plain table-lookup composition and we predict
  NO advantage. Crucially, the benefit is CONDITIONAL on the LLM's dominant per-edge error being OVER-COMMITMENT (a confident
  wrong singleton, which creates a detectable contradiction) rather than UNDER-SPECIFICATION (a safe-but-broad disjunction,
  which closure cannot narrow); we therefore measure the error-type first and predict the gain tracks the measured over-commitment
  rate.
motivation: >-
  Faithful multi-hop relational reasoning over short professional text — temporal ordering of events in news, kinship in narratives,
  containment/region relations in descriptions — is where LLM hallucination is most damaging and where a text-to-logic pipeline
  most needs to fuse explicit document facts with implicit composition knowledge while staying auditable. Existing text-to-logic
  systems handle the COMPOSITION step unsatisfyingly: humans hand-craft composition rules (the 92 kinship rules behind CLUTRR),
  which do not scale; the LLM composes freely, which is locally fluent but globally inconsistent and produces silent errors
  that solver-crash feedback (Logic-LM) and majority voting (LINC) cannot see; or paths are reasoned in isolation (LAMBADA,
  Path-of-Thoughts), which deliberately avoids the global check and so cannot resolve disjunctive uncertainty or detect contradictions
  arriving at the same pair from two paths. The qualitative-reasoning community has had exact, commodity-cheap path-consistency
  algorithms over relation algebras (Allen 1983; Renz & Nebel; solvers GQR, SparQ) for forty years — but they assume a clean,
  hand-given composition table and have never been coupled to an LLM that reads relations off natural language. The triggering
  cross-field insight is sharper than 'LLMs are inconsistent reasoners': recent QSTR evaluations show frontier LLMs are actually
  quite good at SINGLE-STEP composition (QSTRBench reports ~98% on Allen-interval composition for the best model) yet the
  strongest models tend to OVER-PREDICT relations, and a temporal-constraint study (Marín 2025) finds even simple before/during
  relations are applied brittlely and explicitly calls for 'hybrid architectures incorporating symbolic reasoning modules.'
  This reframes the opportunity: the LLM is a decent local namer but does not PROPAGATE constraints across paths, and its
  over-commitment is precisely the error a global closure check can certify and repair. Two ideas make the transfer a genuine
  contribution rather than a port of known temporal-consistency inference (Ning et al.'s ILP, which COMMITS to a single labeling
  to maximize extraction F1): first, because Allen/point/RCC composition tables are EXACT ground truth, closure is a GOLD-FREE
  hallucination CERTIFICATE — every violation is a real LLM error, no learned table can be 'consistent-but-wrong,' and multi-path
  redundancy in a document becomes an error-correcting code over LLM extractions; second, the objective is the OPPOSITE of
  F1-maximization — we preserve disjunctive uncertainty and ABSTAIN, trading coverage for faithfulness, which is what a hallucination-controlled,
  human-auditable pipeline actually needs. If it works, this is a general, training-free recipe for trustworthy relational
  reasoning over text with quantified hallucination reduction and replayable trace-graphs; if it fails (closure detects but
  cannot reliably repair, or LLMs under-specify so there is nothing to certify), that is itself a publishable scope boundary
  on repairing LLM-read relational knowledge.
assumptions:
- >-
  SCOPE: the target reasoning is RELATIONAL and COMPOSITIONAL — the answer is a relation between a pair obtained by composing
  base relations along paths in an entity/event graph (temporal before/after/overlap/includes, spatial containment/region
  connection, kinship). Arbitrary propositional rule chaining (RuleTaker) is deliberately out of scope and used only as a
  contrastive negative; we will quantify what fraction of a given corpus's queries are relation-composable so the mechanism
  is positioned as a MODULE inside a general text-to-logic pipeline, not a replacement for it.
- >-
  EXACT-TABLE primacy: for the PRIMARY temporal/spatial settings the composition table is mathematical ground truth (Allen's
  interval algebra, the point/coarse temporal algebra used by TimeBank-Dense, RCC-8). This is the load-bearing assumption
  that dissolves elicitation circularity — the LLM is NEVER asked to supply the composition table for the primary settings,
  so closure cannot be 'consistent-but-wrong'; it can only narrow toward truth or detect a real inconsistency. LLM-elicited
  tables are studied ONLY as an explicit ablation (kinship/CLUTRR, which has a gold table), measured by precision/recall against
  gold and by how often repair moves the query edge toward vs away from gold.
- >-
  BITE: the data contain instances where two or more paths constrain the query pair (redundancy / cycles), so intersection
  and contradiction-detection are actually exercised. This is GUARANTEED by construction in the synthetic generator and is
  empirically present in densely annotated temporal text (TimeBank-Dense). We will report, per dataset, the fraction of instances
  that trigger a non-trivial intersection or an empty-relation collapse, and stratify all results into single-path vs multi-path
  subsets.
- >-
  ERROR-TYPE: the mechanism's benefit is conditional on the LLM's dominant per-edge error being OVER-COMMITMENT (confident
  wrong singleton → detectable contradiction) rather than UNDER-SPECIFICATION (safe broad disjunction → nothing to narrow).
  We do NOT assume this; we MEASURE it in a cheap pilot before the main study and predict the realized gain tracks the measured
  over-commitment rate. (QSTR evidence is mixed: weak models under-specify, strong models over-predict — so the regime is
  model-dependent and must be established, not asserted.)
- >-
  GOLD availability without new annotation: synthetic networks ship exact gold (the generating scenario) and exact deduced
  relations; TimeBank-Dense ships gold pairwise relations whose transitive closure yields gold for deduced (non-adjacent)
  pairs; CLUTRR ships gold answers and a gold kinship table. No new large hand-annotation is on the critical path; any real-text
  legal/temporal extension is best-effort and scoped to a provably-algebraic fragment (effective-date temporal ordering),
  explicitly verified to satisfy associative composition + converse + identity before use.
investigation_approach: >-
  PILOT (cheap, first, de-risks the premise): generate small qualitative constraint networks, render each edge to NL, ask
  the LLM for the per-edge relation, and MEASURE the error decomposition — per-edge soundness (is the gold base relation inside
  the LLM's emitted set?), breadth (set size), and the over-commitment vs under-specification rate — plus the raw closure-VIOLATION
  rate of un-checked LLM networks. This establishes (or refutes) the motivating premise on our own data before any expensive
  run; the predicted target is a non-trivial over-commitment rate that produces measurable contradictions. PIPELINE (four
  stages): (1) NEURAL READING — prompt the LLM to map each surface relation phrase ('shortly after', 'is overridden by', 'mother-in-law',
  'is part of') onto a SOUND DISJUNCTION of canonical base relations, optimizing for recall (the gold relation should be in
  the set) with an explicit 'underdetermined' option; this is the calibration-free fuzzy-unification half. (2) ALGEBRA — use
  the EXACT published composition table for the algebra (Allen 13-relation, the 6-label TimeBank-Dense algebra, RCC-8); seed
  converses/type-signatures/identity from the algebra itself, NOT from an LLM. (3) SYMBOLIC CLOSURE (the contribution) — build
  a qualitative constraint network (nodes = events/entities, edges = relation SETS; explicit edges from stage 1, the query
  starts as the universal relation), run path-consistency to a fixpoint; closure NARROWS the query edge, and any empty collapse
  CERTIFIES an extraction error. On inconsistency, compute a minimal repair (Reiter-style minimal hitting set over conflict
  sets / small MaxSAT) preferring to relax the lowest-confidence stage-1 edges, recording the diagnosis; if the query stays
  a disjunction of >1 relation, ABSTAIN (or return the set). (4) AUDIT — emit the network, which compositions fired on which
  paths, and any repairs as a trace-graph, optionally discharged in SWI-Prolog/ASP from the closed table for a replayable
  proof. DATASETS — PRIMARY (multi-path, where closure bites): (a) a synthetic Allen/point-algebra QCN generator (Renz–Nebel-style
  random consistent networks) that GUARANTEES redundant paths/cycles, ships exact gold, and lets us sweep redundancy/density/hop-count
  independently; (b) TimeBank-Dense — 36 real news documents, 12,715 dense temporal relations, an EXISTING resource with multi-path
  structure and gold, so closure is exercised on real text with no new annotation, using its 6-label algebra (VAGUE = the
  abstain/underdetermined relation). SECONDARY: RCC-8 synthetic (second algebra, shows generality) and CLUTRR (kinship; used
  for the table-quality / hop-scaling story AND as the venue for the ELICITED-table ablation against gold, with the explicit
  caveat that single-chain CLUTRR has closure-ON == closure-OFF; we additionally mine/synthesize a multi-path CLUTRR subset
  via redundant relation mentions and marriage cycles). RuleTaker as an out-of-scope contrast. KEY ABLATIONS — designed to
  ISOLATE path consistency, not merely the presence of a table: (i) closure ON vs OFF with the composition table HELD FIXED
  (so the only difference is multi-path propagation); (ii) repair OFF (detect-only/abstain); (iii) disjunction OFF (force
  the LLM to commit to singletons — tests the sound-but-loose claim); (iv) exact-table vs LLM-elicited-table (tests the gold-free-certificate
  claim). BASELINES: raw LLM, chain-of-thought, RAG, self-consistency voting, LINC-style multi-formalization vote, LLM-emits-Prolog-with-induced-rules
  (DSR-LM-style, no closure), Path-of-Thoughts (PRIMARY baseline, reported specifically on the multi-path subset), a TempRel-style
  COMMIT baseline (global inference that forces a single consistent labeling, to contrast commit-everywhere vs abstain), and
  a soft-unification neural theorem prover. METRICS: per-regime, STRATIFIED into single-path vs multi-path and single-relation
  vs disjunctive-query subsets — (1) risk–coverage / accuracy-vs-coverage (headline), (2) closure-DETECTABLE hallucination
  rate with an explicit decomposition of all gold-wrong non-abstained predictions into closure-detectable (caught/repaired/abstained)
  vs invisible-to-closure, (3) the fraction of instances triggering non-trivial intersection or empty collapse (proof the
  mechanism is exercised), (4) repair quality as fraction of repairs moving the query edge TOWARD vs AWAY from gold (with
  bootstrap CIs), (5) for the elicited-table ablation, composition-table precision/recall vs the gold kinship table and multi-sample
  self-agreement, (6) gain-vs-redundancy and gain-vs-hop-count curves. The optional probabilistic/semiring variant carries
  per-relation weights and is presented as EXPLORATORY soft propagation with a measured reliability diagram / ECE against
  gold — the hard, exact, calibration-free closure path is the primary defensible contribution. All LLM calls go through OpenRouter;
  cost stays well under $10 via short documents, caching, and a cheap model for extraction; closure and repair run in milliseconds
  per network on a laptop.
success_criteria: >-
  PRE-REGISTERED, PER-REGIME (not 'beat everyone everywhere'). CONFIRMS if, on the MULTI-PATH / disjunctive-query subsets:
  (i) closure-certified reasoning gives a strictly better risk–coverage curve (higher selective accuracy at equal coverage)
  and a lower closure-detectable hallucination rate than free LLM composition, LINC voting, and Path-of-Thoughts; (ii) the
  table-held-fixed closure-ON ablation beats closure-OFF (isolating path consistency from the mere presence of a table) and
  the gain scales with measured network redundancy; (iii) with the EXACT table, closure produces ZERO false-positive error
  flags (every certified violation is a genuine extraction error) and repairs move the query edge toward gold significantly
  more often than away (CI-separated, not merely 'above chance'); (iv) the disjunction-ON variant beats the commit-to-singleton
  variant, supporting the sound-but-loose-labeling claim; (v) the predicted error-type holds — the realized gain tracks the
  pilot-measured over-commitment rate. DISCONFIRMS / SCOPES if: closure adds no risk–coverage benefit over Path-of-Thoughts
  or answer voting on the multi-path subset; closure-ON == closure-OFF even when multi-path (i.e., the LLM under-specifies
  so there is nothing to narrow and no contradictions arise); the gain does not scale with redundancy; or in the elicited-table
  ablation repair frequently 'fixes' toward the wrong relation. EXPLICITLY PRE-REGISTERED FAILURE MODES that count as honest,
  publishable scope boundaries: (a) UNDER-SPECIFICATION regime — LLMs emit broad safe disjunctions, so closure is sound but
  inert (the mechanism is a safety net with low yield); (b) CONSISTENT-BUT-WRONG elicited table — demonstrated only in the
  kinship ablation where the table is LLM-supplied, quantified against gold, and shown to NOT arise in the exact-table primary
  settings; (c) INVISIBLE hallucinations — confident self-consistent single-chain errors that closure structurally cannot
  see, reported as the explicit ceiling of the method. Atomic extraction precision/recall must remain comparable to baselines
  (the contribution is at composition, not extraction), and trace-graphs must be judged human-auditable (a reader can follow
  the certified path and any repair).
related_works:
- >-
  Temporal-relation extraction with ILP global inference (Ning, Feng & Roth 2017, EMNLP; arXiv:1906.04943; CogCompTime): a
  TRAINED extractor produces per-pair scores and Integer Linear Programming enforces transitivity + symmetry to output a single
  globally-consistent labeling. This is the closest prior art for 'enforce qualitative consistency on machine-extracted temporal
  relations.' Fundamental differences: (1) it COMMITS to one relation per pair to maximize extraction F1; we PRESERVE disjunctive
  uncertainty and ABSTAIN, optimizing a risk–coverage / hallucination-control objective — the opposite output contract; (2)
  it uses LEARNED scores and approximate optimization (a high-score consistent labeling can be wrong); we use the EXACT published
  composition table so closure is a deductively sound, gold-free CERTIFICATE that never adds an unsupported relation; (3)
  it needs a trained model per corpus; our reader is an untrained LLM doing fuzzy semantic unification of arbitrary surface
  phrases and generalizes across algebras (temporal, spatial, kinship). We additionally LOCALIZE/REPAIR via minimal diagnosis
  and emit auditable trace-graphs, which ILP global inference does not.
- >-
  QSTRBench (2026, arXiv:2605.18380): benchmarks whether LLMs can compute SINGLE-STEP composition-table entries, converses,
  and conceptual neighbourhoods across many calculi (point algebra, Allen IA, RCC-5/8/22, etc.), finding the best model ~98%
  on Allen-interval composition and ~92% overall, with weak models UNDER-specifying (false negatives) but the strongest models
  OVER-predicting. We use it to CORRECTLY characterize the premise (LLMs are good local namers, error-type is model-dependent)
  — not, as a naive reading would, to claim LLMs 'cannot compute composition tables.' Difference: QSTRBench only measures
  single-step ability; we turn the closure ALGORITHM into a control wrapper that propagates the LLM's (imperfect, possibly
  over-committed) per-edge labels across multiple paths and uses violations to certify/repair hallucinations — multi-hop propagation
  it does not test.
- >-
  Empirical Characterization of Temporal Constraint Processing in LLMs (Marín 2025, arXiv:2511.10654): characterizes LLM brittleness
  at applying even simple Allen relations (before/during) via a 'deadline detection' task, finds bimodal/scale-uncorrelated
  performance driven by training-data distribution, and explicitly argues hybrid architectures with symbolic reasoning modules
  are needed. Difference: it is benchmarking/characterization and proposes NO coupling; it does not run an external path-consistency
  solver over a disjunctive constraint network nor use consistency as a hallucination certificate. We build exactly the hybrid
  module it calls for and evaluate it as a faithfulness mechanism.
- >-
  TReMu (2025, arXiv:2502.01630): neuro-symbolic temporal reasoning for LLM agents that has the LLM identify event timestamps
  and generate Python/timestamp code which is executed to answer temporal questions. Difference: it quantizes to METRIC time
  and executes code, discarding qualitative disjunction; it cannot represent 'the text leaves this relation underdetermined,'
  cannot abstain on a disjunction, and has no consistency certificate. We stay purely QUALITATIVE, carry disjunctive relation
  sets, narrow them by exact path consistency, and abstain when underdetermined — the regime where metric timestamps are unavailable
  from text.
- >-
  Path-of-Thoughts (2024, arXiv:2412.17963): extracts a reasoning graph, identifies query-relevant paths, and reasons over
  them, beating SOTA by up to 21.3% on relational benchmarks incl. CLUTRR. It is our PRIMARY baseline. Difference: it reasons
  over individual paths and does not INTERSECT relations arriving at the same pair from multiple paths nor detect cross-path
  contradictions; on single-chain inputs it captures most of what closure would, so our claim is explicitly restricted to
  the MULTI-PATH subset where intersection/contradiction-detection are required and where we predict closure's advantage concentrates.
- >-
  DSR-LM / 'LLMs can Learn Rules' (Yang et al. 2023, arXiv:2305.03742; Zhu et al. 2023, arXiv:2310.07064): INDUCE weighted/symbolic
  composition rules to fit task accuracy (DSR-LM also uses 92 hand-crafted CLUTRR kinship rules in an ablation). Difference:
  rule induction optimizes data fit and gives a point answer; we enforce the EXACT ALGEBRAIC LAWS (converse, associativity,
  disjointness) that are necessary for soundness independent of any training data, and we use closure to DETECT, CERTIFY,
  LOCALIZE, REPAIR, and ABSTAIN — capabilities rule induction does not provide. We use the gold CLUTRR table to measure how
  good an LLM-ELICITED table is (a diagnostic), not to win accuracy.
- >-
  Logic-LM (Pan et al. 2023, arXiv:2305.12295) and LINC (Olausson et al. 2023, EMNLP, arXiv:2310.15164): Logic-LM self-refines
  a symbolic formulation using the solver's syntactic/unsat ERROR messages; LINC majority-votes the answers of multiple formalizations
  passed to a prover. Difference: Logic-LM reacts only to solver crashes and has no positive global INVARIANT over relational
  knowledge; LINC's answer-level voting cannot see that individually-popular composition steps are JOINTLY inconsistent. Algebraic
  closure is a global necessary condition that both lack, and it narrows disjunctive uncertainty rather than averaging independent
  samples.
- >-
  LAMBADA (Kazemi et al. 2023, arXiv:2212.13894) and path-isolation reasoning: backward chaining / per-path reasoning that
  manages inconsistency by COMPOSITIONAL ISOLATION rather than global enforcement. Difference: we do the opposite — intersect
  across paths via closure, which both tightens disjunctions and detects contradictions; isolation can return mutually inconsistent
  answers and cannot resolve disjunctive uncertainty.
- >-
  Logically Consistent Language Models via Neuro-Symbolic Integration / LOCO-LMs (Calanzone, Teso & Vergari 2024, arXiv:2409.13724;
  ICLR 2025): a TRAINING-TIME neuro-symbolic loss that fine-tunes an LLM to be consistent with a set of propositional facts
  and rules via a probabilistic logic reasoner. Difference: it is training-time and PROPOSITIONAL (consistency among atomic
  facts/implications); we are training-free at INFERENCE time and enforce multi-hop COMPOSITION closure over a RELATION ALGEBRA
  read off text, producing per-instance certificates, abstention, and trace-graphs rather than a globally fine-tuned model.
  This pre-empts a 'consistency enforcement is not new' objection: prior LM-consistency work enforces propositional/factual
  consistency, not relation-algebra composition closure on text-derived relations.
- >-
  Abductive gap-filling — ARGOS / 'A Balanced Neuro-Symbolic Approach for Commonsense Abductive Logic' (2026, arXiv:2601.18595):
  iteratively asks the LLM for missing commonsense clauses, guided by the SAT-solver backbone, to complete a proof. Difference:
  abduction has no NULL — it can invent a bridge for any goal, including false ones. Closure provides a consistency-based
  REJECTION: a composition that violates the exact algebra is refused even when the LLM proposes it confidently, so composition
  knowledge is admitted only if globally consistent.
- >-
  Classical qualitative reasoners and KG repair: GQR, SparQ, Allen (1983), Renz & Nebel (path consistency / random network
  model A(n,d,l)) provide mature exact machinery over GIVEN relation algebras; LLM-based SHACL/KG repair (e.g., arXiv:2507.22419)
  validates individual triples against shapes. Difference: classical solvers assume a clean human-given table and operate
  on already-formal data — none read the algebra off NL text via an LLM; SHACL repair validates single triples, not multi-hop
  COMPOSITION closure for deduction and hallucination control.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer from Qualitative Spatial-Temporal Reasoning and Tarski's relation algebras
  — Allen's interval algebra, RCC-8, the point algebra, composition tables, and the path-consistency / algebraic-closure constraint-propagation
  algorithms (classical solvers GQR/SparQ) — imported into LLM-based relational reasoning and hallucination control, plus
  Reiter's 1980s model-based diagnosis (minimal hitting sets of conflict sets) for localizing which extracted atom to retract.
  The revision adds a sharper Level-1/2 framing borrowed from CODING THEORY: an exact composition table turns multi-path redundancy
  in a document into an error-correcting code over the LLM's extractions — redundant constraining paths let closure DETECT
  and CORRECT mis-reads with no external labels, exactly as parity checks detect bit errors, and the benefit scales with redundancy
  the way decoding power scales with code rate. Two refined cross-field insights drive the design: (1) LLMs behave like competent
  LOCAL qualitative namers that do NOT propagate constraints across paths — and, for strong models, OVER-COMMIT — so the missing
  piece is global propagation, not local naming; (2) because the algebra's table is mathematical ground truth, consistency
  becomes a calibration-free, zero-false-positive CERTIFICATE, which flips the objective from accuracy-maximization-by-committing
  (as in ILP temporal global inference) to faithfulness-by-abstaining. The neuro-symbolic division of labor — LLM = soft,
  high-recall, disjunction-emitting semantic naming; exact algebra = hard global precision — is what makes the transfer a
  concrete mechanism rather than a loose analogy.
terms:
- term: Relation algebra
  definition: >-
    An algebraic structure (after Tarski) over a finite set of base relations with composition, converse, intersection, union,
    and identity, closed under these operations. Allen's 13 interval relations, the point algebra, and RCC-8 spatial regions
    are standard examples; it supplies the laws (converse, associativity) that correct compositional reasoning must obey.
- term: Exact composition table
  definition: >-
    For each ordered pair of base relations (r,s), the set of base relations the composite r-then-s can take. For Allen IA,
    the point algebra, and RCC-8 these tables are PUBLISHED MATHEMATICAL GROUND TRUTH (not learned, not elicited), which is
    why closure over them is a gold-free certificate. Only for ad-hoc domains (e.g., LLM-elicited kinship) is the table approximate;
    that case is studied as an ablation against a gold table.
- term: Algebraic closure / path consistency
  definition: >-
    A constraint-propagation algorithm that repeatedly tightens each edge's relation set by intersecting it with the composition
    of relations along every two-step path, until a fixpoint. It is a sound (necessary) global consistency check: any edge
    collapsing to the empty relation certifies inconsistency. Polynomial and millisecond-fast on per-document networks.
- term: Qualitative constraint network (QCN)
  definition: >-
    A graph whose nodes are entities/events and whose edges carry a SET of possible base relations (a singleton = known relation;
    a larger set = disjunctive uncertainty; the universal relation = unknown). The data structure on which closure operates;
    the query edge starts universal and is narrowed by closure.
- term: Sound-but-loose disjunctive labeling
  definition: >-
    The reframing of the LLM's extraction task from 'name THE relation' (precision-oriented, over-commitment-prone) to 'name
    the set of base relations the text span does NOT exclude' (recall-oriented, NLI-like). Soundness means the gold relation
    is inside the emitted set; precision is then delegated to exact algebraic closure rather than asked of the LLM.
- term: Gold-free hallucination certificate
  definition: >-
    Because the composition table is exact, a closure violation (empty-relation collapse) is a deductive PROOF that some LLM-supplied
    edge is wrong — a zero-false-positive error flag requiring no gold labels. Multi-path redundancy supplies the cross-checks,
    analogous to parity checks in an error-correcting code.
- term: Over-commitment vs under-specification
  definition: >-
    The two per-edge LLM error types. Over-commitment = a confident WRONG singleton, which produces detectable contradictions
    closure can certify/repair. Under-specification = a safe BROAD disjunction (often the gold relation plus extras), which
    is sound but gives closure little to narrow. The method's yield is conditional on a non-trivial over-commitment rate,
    measured by pilot.
- term: Minimal repair (model-based diagnosis)
  definition: >-
    On a certified inconsistency, the smallest set of LLM-supplied edges whose revision restores a non-empty closure, computed
    as a Reiter-style minimal hitting set of conflict sets (or small MaxSAT), preferring to relax the lowest-confidence edges.
    It localizes the hallucination and proposes a correction; repair quality is scored as toward-vs-away-from-gold movement.
- term: Risk–coverage (selective prediction)
  definition: >-
    The accuracy-vs-coverage trade-off when the system is allowed to ABSTAIN (return 'underdetermined'/the residual set) on
    queries that closure leaves as a multi-relation disjunction. The headline metric, replacing 'raw accuracy beating every
    baseline,' because the contribution is faithfulness-by-abstention, not commit-everywhere accuracy.
- term: Multi-path bite
  definition: >-
    An instance where two or more paths constrain the query pair, so closure performs a non-trivial intersection or detects
    an empty collapse. Reported per dataset as the fraction of instances triggering it; it is the regime where closure provably
    differs from single-chain table-lookup composition (where closure-ON == closure-OFF).
- term: TimeBank-Dense
  definition: >-
    An existing, densely-annotated temporal-relation corpus (36 news documents, 12,715 relations, labels BEFORE/AFTER/INCLUDES/IS_INCLUDED/SIMULTANEOUS/VAGUE)
    over a coarse temporal algebra. Its dense annotation creates multi-path structure with reliable gold, providing real-text
    ecological validity with no new annotation; VAGUE serves as the abstain/underdetermined relation.
- term: Trace-graph
  definition: >-
    A human-auditable record: the qualitative constraint network, which composition entries fired on which paths during closure,
    any minimal repairs, and optionally an equivalent SWI-Prolog/ASP proof discharged from the closed table for replay.
summary: >-
  We reframe LLM relation extraction as a high-recall 'sound-but-loose' disjunctive labeling task and delegate global precision
  to EXACT relation-algebra path consistency (Allen, point algebra, RCC-8) imported from qualitative spatial-temporal reasoning;
  because the composition table is mathematical ground truth, a closure violation is a gold-free CERTIFICATE that the LLM
  mis-read the text, enabling localization, minimal repair, and principled abstention. We test this where it provably bites
  — multi-path/disjunctive instances (a synthetic QCN generator and the densely-annotated TimeBank-Dense), with a table-held-fixed
  ablation isolating path consistency and a risk–coverage headline — predicting lower closure-detectable hallucination and
  better selective accuracy that scale with network redundancy, conditional on a measured LLM over-commitment rate.
</previous_hypothesis>

<previous_review>
Critiques from the previous review. Check which ones have been addressed
in the revised hypothesis. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (rigor) The headline guarantees ('zero false-positive certificate', 'an intersection that narrows a query edge ... is provably sound') are silently conditioned on per-edge INPUT SOUNDNESS — i.e., the LLM's high-recall disjunctive set actually CONTAINS the gold relation on every edge. The clean part is correct: with all inputs sound, supersets of a consistent gold network cannot collapse, so any collapse certifies a genuine reading error. But the dangerous dual is not pre-registered: when a high-recall set OMITS gold (a recall failure / unsound label), closure can NARROW the query to a confident WRONG singleton with NO empty collapse — a certified-looking hallucination that the mechanism actively endorses. This is strictly worse than, and distinct from, the pre-registered 'invisible self-consistent single-chain error': here closure produces the wrong answer via multi-path propagation. The method effectively trades the LLM's over-commitment (asked for a singleton) for the LLM's recall failure (asked for a high-recall set), and 'high recall' is in direct tension with 'narrow enough to be useful'. The realized rate of this failure is governed by per-edge unsoundness (1 - recall), the very quantity the pilot measures — so the fix is cheap but currently absent from the framing and the failure-mode list.
  Action: Add 'unsound high-recall input set -> confident wrong narrowing with no violation' as an explicit fourth pre-registered failure mode. Report, on the multi-path subset, the decomposition of all gold-wrong non-abstained predictions into: (a) closure-collapse caught, (b) silent wrong narrowing driven by an unsound input edge, (c) invisible single-chain. Condition all 'provably sound' / 'zero false-positive' language on the pilot-measured per-edge recall, and consider a recall-floor gate (only assert certificates/narrowings when per-edge soundness clears a measured threshold). Scope the zero-FP claim to DETECTION, separate from localization/repair, which can mislocalize even when the collapse is genuine.
- [MAJOR] (methodology) The one real-text arm (TimeBank-Dense) is at structural risk of low multi-path 'bite', which would leave the headline carried almost entirely by the self-constructed synthetic generator. Three compounding facts: (i) ~43% of TimeBank-Dense relations are VAGUE (the universal relation), and VAGUE composed with anything yields no constraint, so a large fraction of edges and paths carry zero narrowing power; (ii) the corpus was itself densified by a transitive-closure tool, so its non-adjacent 'deduced' gold is largely the output of the same closure you are testing, and the genuinely informative, multiply-constrained query pairs may be sparse; (iii) the 6-label coarse algebra is a DESIGNED coarsening of Allen's 13 relations in which most disjunctive composites collapse to VAGUE, so closure on real text will frequently widen to VAGUE rather than narrow — structurally limiting yield and undercutting 'exact = mathematical ground truth' for this arm (which is cleanest only for the synthetic Allen / point / RCC-8 settings). Separately, the zero-FP certificate assumes the GOLD network is itself consistent; TimeBank-Dense's closure tool largely enforces this, but residual human-annotation inconsistency could make a collapse reflect a gold error rather than an LLM error.
  Action: Before the main run, pre-measure on TimeBank-Dense: the non-VAGUE constraint density, the fraction of query pairs with >=2 non-VAGUE constraining paths, and the achievable narrowing yield on held-out deduced pairs. Cite the EXACT coarse composition table used (e.g., the CAEVO / SputLink transitivity rules) rather than asserting it is mathematical ground truth, and acknowledge that disjunctive composites mapping to VAGUE bound the narrowing yield. If real-text bite is too low, add a second real resource with denser non-VAGUE structure (e.g., MATRES or TDDiscourse-derived) or restrict to documents/sub-graphs with sufficient non-VAGUE redundancy, and pre-register what bite level is required for the real-text claim to be live vs. scoped as sound-but-inert.
- [MAJOR] (methodology) Two confounds in the headline comparison. (a) SYNTHETIC REALISM: the synthetic QCN generator controls BOTH the redundancy/density (the independent variable) AND the NL realization that determines the LLM's error profile. The 'advantage grows with redundancy' curve can therefore be an artifact of tunable difficulty: clean renderings -> the LLM reads edges near-perfectly -> few contradictions -> closure has nothing to fix; ambiguous renderings -> the LLM under-specifies -> closure inert. The redundancy-scaling result is only meaningful if the per-edge error distribution it induces matches the real error distribution measured in the pilot. (b) MATCHED ABSTENTION: a risk–coverage headline requires every baseline (raw LLM, CoT, self-consistency, LINC, Path-of-Thoughts, DSR-LM) to have a comparable abstention/confidence signal. Closure gets a principled abstain for free (residual disjunction); if baselines are given only a crude or no abstention, the headline advantage conflates 'closure' with 'closure has a better-calibrated abstain than the baselines were given.'
  Action: Pre-register the NL-realization protocol for the synthetic generator and validate that the induced per-edge error decomposition (over-commitment / under-specification / breadth / soundness) matches the pilot's real-text decomposition; report the redundancy-scaling curve only for realism-matched difficulty settings. For the risk–coverage comparison, equip every baseline with a matched abstention mechanism (self-consistency vote margin, verbalized confidence, or LINC vote agreement) and compare the closure method against baselines at MATCHED coverage, with bootstrap CIs on the selective-accuracy gap.
- [MINOR] (novelty) Running transitive/path closure over machine-extracted temporal relations from text is partly prior art beyond the cited Ning et al. ILP: SputLink (Verhagen) performs temporal closure over TimeBank relations, CAEVO (Chambers et al. 2014) does global temporal inference / cascaded sieves over the same coarse algebra, and TimeBank-Dense itself was built with a transitive reasoner. The novelty (LLM as disjunction-emitting reader + closure-as-gold-free-certificate + abstention/risk-coverage objective) survives, but omitting these invites a 'reinventing temporal closure' objection.
  Action: Add SputLink and CAEVO (and a note that TimeBank-Dense was densified by closure) to related work, each with one differentiating sentence: prior temporal-closure systems either COMMIT to a single labeling or are trained extractors and do not preserve disjunction, certify reading errors, abstain, or optimize a risk–coverage objective; closure here is a gold-free certificate over LLM-read disjunctive labels, not a labeling step.
- [MINOR] (clarity) The bridge from the binary-relation-algebra module to the umbrella application goal (FOL/Prolog text-to-logic with probabilistic reasoning, upper-ontology grounding, atomic-extraction P/R, hallucination reduction) is implicit. The hypothesis legitimately scopes itself to a MODULE inside a general pipeline and de-emphasizes atomic extraction ('comparable to baselines'), but a reviewer at ACL-KE will want the connective tissue made explicit so the contribution reads as advancing the stated text-to-logic goal rather than a self-contained QSTR exercise.
  Action: State up front that the contribution is the COMPOSITION/deduction module of a text-to-logic pipeline; report the relation-composable fraction per corpus (already promised) as the module's applicability envelope; and present atomic precision/recall explicitly as a held-fixed control to substantiate that the gains are at composition, not extraction. One paragraph tying the trace-graph/SWI-Prolog discharge to the umbrella auditability requirement would also strengthen venue fit.
</previous_review>

<task>
Provide a thorough peer review of this research hypothesis.

STEP 1 — GROUND YOUR REVIEW IN EVIDENCE:
Before writing critiques, search for relevant context to make your review authoritative:
- Search for accepted papers at top venues in this area — what level of
  contribution gets accepted? How does this hypothesis compare?
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes in the literature

STEP 2 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would waste compute if not fixed) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Flag fatal flaws that would waste compute if not fixed first.

STABILITY IS OK: If the hypothesis is on track and just needs more iterations to prove itself,
keep your feedback similar to the previous round. Don't manufacture new critiques — only escalate
when the revision introduced new issues or failed to address prior ones.

STEP 3 — H↔H EDGE (only if a <previous_hypothesis> block is present):
Classify how the current hypothesis relates to the previous iteration's hypothesis
using Moulines's structuralist typology. Set ``relation_type`` to one of:
    - "evolution": refining specialised claims while keeping the same conceptual frame
    - "embedding": the previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian, incommensurable shift)
Set ``relation_rationale`` to a brief justification (≤120 chars).

If no <previous_hypothesis> is present (this is iteration 1), leave both fields
null/empty.

Provide your review via structured output.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "ReviewerFeedback + Moulines H\u2194H typology for hypo_loop iterations.\n\nAdds ``relation_type`` + ``relation_rationale`` so the trace projection\ncan build a typed edge from the previous iteration's hypothesis to\nthis iteration's. On iteration 1 (no previous), both fields are\nempty/None.",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    },
    "relation_type": {
      "anyOf": [
        {
          "enum": [
            "evolution",
            "embedding",
            "replacement"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Moulines's structuralist typology classifying how this iteration's hypothesis relates to the previous iteration's: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (Kuhnian shift). Leave null on the first iteration (no previous hypothesis).",
      "title": "Relation Type"
    },
    "relation_rationale": {
      "default": "",
      "description": "Brief rationale (one short line, \u2264120 chars) for the relation_type. Empty on the first iteration.",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "HypoReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-17 12:01:18 UTC

```
### Goal

Develop an operational translation pipeline that converts unstructured textual content (e.g., short legal documents, news articles, kids' stories) into a formal first-order logic representation. The output must be capable of (probabilistic) reasoning using a logic reasoner (like Prolog), leveraging LLMs to dynamically resolve terminology, concepts, and relations that are not well defined in the explicit text.

### Reviewer Scope

Limit the technical core to areas the reviewer can deeply evaluate. Other fields are welcome for inspiration but should not host the substantive contribution.

Reviewer-evaluable areas: semantic technologies, logic programming, inductive logic programming, information retrieval, machine learning, LLMs, deep learning, knowledge extraction, knowledge graphs, reasoning, and text data analytics.

The pipeline should ingest a short document (approx. 3000 characters) and parse it into a structured, computable format. Methods may combine an LLM acting as a semantic translation engine (mapping natural text to first-order logic or Prolog predicates), a running logic interpreter (like SWI-Prolog) for symbolic execution, and the integration of upper ontologies like OpenCyc to supply necessary background structure and taxonomic grounding. Furthermore, an LLM should be deployed as a probabilistic reasoning engine to handle fuzzy unifications, semantic similarities, and logical gaps where strict symbolic matching fails due to language ambiguity.

Evaluation must be rigorous and compare the neuro-symbolic pipeline against purely neural baselines (e.g., standard RAG, chain-of-thought prompting) on standard logical reasoning benchmarks (e.g., RuleTaker, CLUTRR) or custom annotated datasets. It must specifically measure:
(i) the precision and recall of atomic fact extraction directly from the original document, and
(ii) the accuracy of multi-hop fact extraction and logical deductions that require synthesizing explicit document facts with implicit common-sense knowledge.

Outputs must provide human-auditable trace-graphs of the reasoning steps to clearly demonstrate the logical path taken.

Constraints: The pipeline must be highly reproducible on any short, professionally written documents. Inference must be executable on commodity hardware, and the system must report a quantified reduction in hallucination rates compared to raw LLM generation.

### Publication

Target ACL Knowledge Extraction track as the primary venue, with EMNLP or specialized neuro-symbolic AI conference tracks (e.g., NeSy) as fallback targets.

### Things to Avoid

Avoid simplistic propositional logic translations of the text. Avoid purely neural black-box systems that lack interpretable reasoning traces. The substantive contribution must be an operational, hybrid method for reasoning with textual content that explicitly minimizes hallucinations.
```

### [3] SYSTEM-USER prompt · 2026-06-17 12:08:54 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same closure-as-gold-free-certificate frame; sharpened with input-recall scoping, MATRES point-algebra primary, 4th failure mode.' is too long (at most 120 characters, got 129)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
