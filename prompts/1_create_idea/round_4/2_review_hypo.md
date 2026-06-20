# review_hypo — create_idea

> Phase: `hypo_loop` · round 4 · Substep: `review_hypo`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave the agent(s) in this substep — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 12:15:31 UTC

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
  Closure-Certified Composition: Cross-Path Sound Narrowing as a Zero-False-Positive Faithfulness Mechanism (Primary), and
  Recall-Bounded Gold-Free Detection (Secondary), for the Deduction Module of a Text-to-Logic Pipeline
hypothesis: >-
  We separate, for the first time, TWO distinct value modes of exact relation-algebra path consistency over LLM-read relations,
  with different requirements, risk profiles, and metrics, and we lead with the mode the reviewer identified as the robust
  one. MODE A — SOUND NARROWING (PRIMARY, zero false-positive, the headline): the LLM emits, per text span, a high-recall
  'sound-but-loose' DISJUNCTIVE set of base relations the span does NOT exclude (with an explicit underdetermined/universal
  option); when these sets are SOUND (the gold relation is inside each) but sub-universal, intersecting the compositions that
  arrive at a query pair from MULTIPLE constraining paths yields a set that STILL contains gold yet is strictly tighter than
  any single path — a provably zero-false-positive narrowing TOWARD gold that improves selective accuracy at matched coverage.
  This requires only edge BREADTH that is sub-universal plus MULTI-PATH BITE (≥2 non-universal constraining paths); it does
  NOT require LLM over-commitment, and it is exactly what per-path-isolated reasoners (Path-of-Thoughts) structurally cannot
  do because they never intersect relations arriving at the same pair from different paths. Crucially, because narrowing is
  zero-FP precisely WHEN edges are sound, the HIGH-RECALL end of the elicitation knob — where sets are broad and gold is most
  likely inside — is exactly where Mode A is SAFEST and most reliable; it is inert ONLY in the degenerate all-universal limit,
  not merely when sets are 'broad.' MODE B — DETECTION/REPAIR (SECONDARY, zero-FP DETECTION conditional on measured recall):
  an empty closure collapse is a deductive certificate that some LLM edge is UNSOUND, requiring no gold labels; but it requires
  at least one over-committed/recall-failed edge to fire, and it carries the dangerous DUAL we pre-register — SILENT WRONG
  NARROWING, where an unsound high-recall set that OMITS gold drives closure to a confident WRONG singleton with NO collapse
  (rate bounded by 1−recall). The two modes sit on opposite ends of the SAME prompt-elicited breadth knob (narrow→more bite/collapse
  but lower recall; broad→higher recall but less collapse), so we do not assert a single operating point: we MAP THE RECALL–BITE
  FRONTIER as a curve and pre-register go/no-go on a viable region existing. Our central, over-commitment-ROBUST prediction
  is: on the MULTI-PATH-WITH-BITE subset at realism-matched difficulty, closure-certified SOUND NARROWING (Mode A) achieves
  strictly higher selective accuracy AT MATCHED COVERAGE than Path-of-Thoughts and self-consistency voting (each given its
  own matched abstention signal), with the gap CI-separated from zero under paired bootstrap — and we attribute this win to
  CROSS-PATH INTERSECTION of sound disjunctive sets, NOT to contradiction-catching, so the headline does not depend on the
  over-commitment rate. The advantage GROWS with the number of independent constraining paths (network redundancy / cyclomatic
  structure), the qualitative analogue of an error-correcting code's redundancy, and therefore with hop count ONLY when extra
  hops add redundancy; on single-chain inputs closure provably reduces to plain table-lookup composition and we predict NO
  advantage. Mode B (detection/repair/abstention from collapse) is reported as a distinct, SECONDARY result whose magnitude
  tracks the measured over-commitment rate and whose silent-narrowing dual we quantify and gate. We make four honesty commitments:
  (1) zero-FP for Mode A means the intersected set still contains gold whenever inputs are sound — a property we verify empirically
  against measured recall, not assume; (2) zero-FP for Mode B is scoped to DETECTION only — LOCALIZATION/repair via minimal
  hitting sets can blame the wrong edge; (3) path consistency is SOUND-BUT-INCOMPLETE for full Allen IA and RCC-8 (consistency
  is NP-complete; COMPLETE only for the point algebra and ORD-Horn-style subclasses), so the closure-DETECTABLE hallucination
  rate is a LOWER BOUND, while our real-text PRIMARY arm is the CONVEX POINT ALGEBRA where path consistency is COMPLETE; (4)
  silent wrong narrowing is a pre-registered failure mode bounded by (1−recall) and tested with a recall-floor gate. The net
  benefit is conditioned, separately per mode, on quantities all MEASURED before the main run: Mode A on sub-universal breadth
  + multi-path bite; Mode B on a non-trivial over-commitment rate.
motivation: >-
  Faithful multi-hop relational reasoning over short professional text — temporal ordering of events in news, kinship in narratives,
  containment/region relations in descriptions — is where LLM hallucination is most damaging and where a text-to-logic pipeline
  most needs to fuse explicit document facts with implicit composition knowledge while staying auditable. The umbrella pipeline
  reads text into FOL/Prolog predicates, types entities against an upper ontology, and answers queries with a reasoner; the
  WEAK LINK is the composition/deduction step. Existing text-to-logic systems handle composition unsatisfyingly: humans hand-craft
  composition rules (the kinship rules behind CLUTRR), which do not scale; the LLM composes freely, which is locally fluent
  but globally inconsistent and produces silent errors that solver-crash feedback (Logic-LM) and answer voting (LINC) cannot
  see; or paths are reasoned in ISOLATION (LAMBADA, Path-of-Thoughts), which deliberately avoids the global check and so cannot
  tighten a disjunctive query by intersecting evidence from multiple paths nor detect contradictions arriving at the same
  pair from two paths. A very recent and directly relevant negative result sharpens the opportunity: Knez & Sun (2024, arXiv:2406.11486)
  show zero-shot LLMs assign MORE THAN ONE temporal relation to a pair for ≥50% (up to 97%) of pairs and violate transitivity,
  then enforce consistency with ILP — and find consistency enforcement DOES NOT improve F1. We read this as decisive evidence
  that consistency enforcement under the F1-maximizing COMMIT contract is the wrong objective; the LLM's native multi-relation
  output is not noise to be collapsed but a SOUND DISJUNCTION to be PRESERVED and NARROWED, and the right objective is faithfulness-by-abstention,
  not extraction F1. The qualitative-reasoning community has had exact, commodity-cheap path-consistency algorithms over relation
  algebras (Allen 1983; Renz & Nebel; solvers GQR, SparQ) for forty years — but they assume a clean hand-given table and have
  never been coupled to an LLM reading relations off natural language. We are NOT the first to run closure over machine-extracted
  temporal relations: SputLink (Verhagen) computes temporal closure to densify TimeBank, CAEVO (Chambers et al. 2014) does
  global temporal inference via cascaded sieves, and Ning et al.'s ILP enforces transitivity — but ALL of these COMMIT to
  a single consistent labeling to maximize F1, preserving no disjunction, certifying no reading error, and offering no abstention.
  Our contribution is the OPPOSITE output contract: keep the LLM's job as high-recall disjunctive READING, use cross-path
  INTERSECTION as a zero-FP faithfulness operation (Mode A) and closure COLLAPSE as a gold-free reading-error certificate
  (Mode B), and optimize faithfulness via a risk–coverage objective. Two ideas make the transfer a genuine contribution rather
  than a port: first, because Allen/point/RCC-8 tables are EXACT ground truth, cross-path intersection of SOUND sets can only
  ever move the query toward gold — a calibration-free, zero-false-positive narrowing that needs no over-commitment and no
  labels, and multi-path redundancy becomes an error-correcting code over LLM extractions; second, the objective inverts F1
  — we preserve disjunctive uncertainty and ABSTAIN, trading coverage for faithfulness, which is what a hallucination-controlled,
  human-auditable pipeline actually needs. Recent QSTR evaluations show frontier LLMs are good at SINGLE-STEP composition
  (QSTRBench ~98% on Allen-interval composition for the best model) yet do not PROPAGATE constraints across paths, and a temporal-constraint
  study (Marín 2025) finds even simple before/during relations are applied brittlely and explicitly calls for hybrid symbolic
  modules. If it works, this is a general, training-free recipe for trustworthy relational deduction over text with quantified,
  certificate-backed hallucination reduction and replayable trace-graphs; if it fails (intersection rarely tightens because
  real sets are near-universal, recall failures drive silent wrong narrowings, or the multi-path-with-bite slice of real queries
  is tiny), each is itself a publishable scope boundary on repairing LLM-read relational knowledge.
assumptions:
- >-
  TWO-MODE DECOUPLING (the central revision): the mechanism delivers value through two SEPARATE modes with different preconditions,
  and the HEADLINE rides the over-commitment-ROBUST one. MODE A — SOUND NARROWING: requires only sub-universal edge breadth
  + multi-path bite (≥2 non-universal paths to the query pair) and SOUND inputs (gold inside each set); cross-path intersection
  then provably tightens toward gold with zero false-positive risk and does NOT require over-commitment. MODE B — DETECTION/REPAIR:
  requires at least one UNSOUND (over-committed or recall-failed) edge so closure can collapse; it is secondary and carries
  the silent-wrong-narrowing dual. We report and gate each mode on its OWN measured precondition; under-specification (broad
  sets) is NOT a global failure — it suppresses Mode B but PRESERVES Mode A, which is inert only in the degenerate all-universal
  limit.
- >-
  SCOPE / MODULE FRAMING: the target reasoning is RELATIONAL and COMPOSITIONAL — the answer is a relation between a pair obtained
  by composing base relations along paths in an entity/event graph (temporal before/after/overlap/includes, spatial containment/region
  connection, kinship). This is the deduction MODULE of a general text-to-logic pipeline, not a replacement for it; arbitrary
  propositional rule chaining (RuleTaker) is out of scope and used only as a contrastive negative. We report, per corpus,
  the RELATION-COMPOSABLE FRACTION and the MULTI-PATH-WITH-BITE FRACTION of queries (the module's applicability envelope,
  foregrounded as headline-adjacent numbers) and hold atomic extraction precision/recall fixed across the comparison so any
  gain is attributable to composition, not extraction.
- >-
  EXACT-TABLE primacy, correctly scoped: 'mathematical ground truth' applies cleanly to the SYNTHETIC Allen/point/RCC-8 settings
  AND to the real-text MATRES arm, whose start-point labels (BEFORE/AFTER/EQUAL/VAGUE) instantiate the CONVEX POINT ALGEBRA
  — where path-consistency is provably COMPLETE and the table is exact. It does NOT apply uniformly to TimeBank-Dense, whose
  6-label scheme is a DESIGNED COARSENING of Allen's 13 relations realized by the SputLink/CAEVO convex table (which we cite
  and use verbatim rather than asserting canonical); for that arm disjunctive composites frequently collapse to VAGUE, structurally
  bounding narrowing yield. The LLM is NEVER asked to supply the composition table for any primary setting, dissolving elicitation
  circularity; LLM-elicited tables are studied ONLY as an explicit kinship/CLUTRR ablation against a gold table.
- >-
  RECALL–BITE FRONTIER (mapped, not point-estimated): per-edge INPUT RECALL = P(gold ∈ LLM's emitted set) and BITE (tight-wrong
  singletons that create collapses) are in DIRECT mutual tension and are controlled by the SAME prompt-elicited breadth knob.
  We therefore do NOT assume a single good operating point; we SWEEP prompting from 'name the relation' to 'name the maximal
  sound set' and map recall, narrowing-yield, and collapse-rate as a FRONTIER curve (a primary deliverable). The viability
  claim is pre-registered: the main run proceeds only if some frontier region simultaneously clears a recall gate AND yields
  non-trivial narrowing. Because Mode A is zero-FP exactly when inputs are sound, we expect Mode A to SURVIVE at the high-recall
  end even where Mode B (collapse-detection) does not — dissolving the tension for the primary mode.
- >-
  MATRES QUERY-GOLD PROVENANCE (scheme-matched, closure-tool-free): the real-text PRIMARY is reframed as a HELD-OUT-EDGE NARROWING
  arm. MATRES gives DENSE, DIRECT human start-point annotation within a 2-sentence window; we take locally-redundant event
  clusters/triangles where multiple annotated point-algebra edges constrain a held-out edge, HIDE one human-annotated edge,
  and predict it by closure over the others. Gold is then DIRECT human start-point annotation in the SAME convex point-algebra
  scheme as the inputs — NOT the output of any closure tool, NOT scheme-mismatched. Long-distance / cross-window deduction
  is SECONDARY/best-effort and used only with gold mapped via a verified point↔interval correspondence (documented information
  loss), confirmed not to be closure-tool output, with document overlap between edge and gold sources verified.
investigation_approach: >-
  PILOT AS A FRONTIER MAP (cheap, first, de-risks the premise AND fixes realism): on BOTH synthetic and real (MATRES, TimeBank-Dense)
  edges, SWEEP a prompt-elicited breadth knob across ≥5 settings from 'name THE relation' (precision/over-commit end) to 'name
  the maximal SOUND set the text does not exclude' (recall end). At each setting MEASURE: (a) per-edge RECALL = P(gold ∈ emitted
  set); (b) set BREADTH distribution (fraction universal vs sub-universal vs singleton); (c) over-commitment vs under-specification
  rate; (d) raw closure-VIOLATION/collapse rate of un-checked LLM networks; and (e) NARROWING-YIELD = fraction of multi-path
  SOUND-input query pairs whose cross-path intersection STRICTLY tightens the query set (and the realized fraction where the
  tightened set still contains gold — the empirical zero-FP audit of Mode A). PLOT the RECALL–BITE FRONTIER (recall vs narrowing-yield
  vs collapse-rate over breadth) as a PRIMARY DELIVERABLE; pre-register go/no-go (a frontier region clearing a recall gate
  AND non-trivial narrowing-yield) BEFORE any main run. Also MEASURE (per Critique 6i) how often the LLM wants to emit non-convex
  {<,>}/≠ relations on MATRES text and the bite lost by widening them to VAGUE; if non-trivial, add a parallel FULL-point-algebra
  arm scored as a lower-bound detector. PRE-REGISTER (per Critique 6ii) the REALISM-MATCHING STATISTIC: total-variation distance
  between the real-text and synthetic per-edge error-type distributions (over-commit/under-spec/breadth bins) plus a recall
  and mean-breadth tolerance band, with the acceptance threshold fixed BEFORE generating the redundancy-scaling curve. PIPELINE
  (four stages): (1) NEURAL READING — prompt the LLM to map each surface relation phrase onto a SOUND DISJUNCTION of canonical
  base relations at the pre-registered frontier operating point; for the MATRES point-algebra arm restrict the emitted vocabulary
  to CONVEX point relations (widening non-convex {<,>} to VAGUE) so path-consistency stays COMPLETE. (2) ALGEBRA — use the
  EXACT published composition table (Allen 13-relation, point algebra, RCC-8; the SputLink/CAEVO convex table for the TB-Dense
  arm, cited verbatim); seed converses/identity from the algebra, never from an LLM. (3) SYMBOLIC CLOSURE — build a QCN (nodes
  = events/entities, edges = relation SETS; the query/held-out edge starts universal), run path-consistency to a fixpoint.
  MODE A: closure NARROWS the query by cross-path intersection (zero-FP under sound inputs); if the query stays a disjunction
  of >1 relation, ABSTAIN. MODE B: an empty collapse CERTIFIES a reading error (DETECTION, zero-FP conditional on recall);
  on inconsistency compute a minimal Reiter-style hitting-set / small-MaxSAT repair preferring lowest-confidence edges, recording
  the diagnosis AND flagging that localization may mislocalize. (4) AUDIT — emit the QCN, which compositions fired on which
  paths, and any repairs as a trace-graph, optionally discharged in SWI-Prolog/ASP from the closed table for a replayable
  proof (connective tissue to the umbrella pipeline's auditability + quantified-hallucination-reduction requirements). DATASETS
  — SYNTHETIC PRIMARY (clean ground truth, controlled redundancy): a Renz–Nebel-style random consistent Allen/point QCN generator
  that GUARANTEES redundant paths/cycles and sweeps redundancy/density/hop-count independently; the NL-realization protocol
  (a fixed library mapping each base relation to graded clean→ambiguous paraphrases) is VALIDATED to clear the pre-registered
  realism-matching statistic, and the redundancy-scaling curve is reported ONLY at the realism-matched setting (kills the
  tunable-difficulty confound). REAL-TEXT PRIMARY: MATRES (Ning, Wu & Roth 2018; ~275 news docs, ~13.6k pairs) as a HELD-OUT-EDGE
  NARROWING arm — locally-redundant event clusters in which ≥2 human-annotated convex point-algebra edges constrain a HIDDEN
  human-annotated edge; gold is DIRECT human start-point annotation (IAA .84), same scheme, not closure-built. We FOREGROUND
  the multi-path-with-bite fraction (pairs with ≥2 non-VAGUE constraining paths) as the applicability envelope. REAL-TEXT
  SECONDARY: (i) MATRES long-distance/cross-window deduction with point↔interval-mapped gold (documented loss, closure-tool-free,
  document-overlap verified), used only if it clears the bite threshold; (ii) TimeBank-Dense (36 docs, ~12.7k relations, 6-label
  coarse algebra) handling its two confounds explicitly — non-adjacent gold is SputLink's output over CLEAN human local edges
  (we frame the test as noisy-LLM-read-of-local-edges→closure vs clean-read closure) and ~43% VAGUE caps narrowing (reported,
  not hidden). RCC-8 synthetic gives a second algebra; CLUTRR is the kinship venue for the ELICITED-table ablation (single-chain
  CLUTRR has closure-ON==closure-OFF) plus a mined/synthesized multi-path subset; RuleTaker is an out-of-scope contrast. KEY
  ABLATIONS: (i) closure/intersection ON vs OFF with the table HELD FIXED (isolates path consistency from 'a fixed table exists'
  — the DSR-LM contribution); (ii) Mode A ONLY (narrow/abstain, NO collapse-repair) vs Mode A+B — cleanly separates the zero-FP
  narrowing driver from detection; (iii) disjunction OFF (force singletons — tests the sound-but-loose claim); (iv) exact-table
  vs LLM-elicited-table (kinship only); (v) recall-floor gate ON vs OFF (tests suppression of silent wrong narrowings). BASELINES,
  EACH WITH A MATCHED ABSTENTION SIGNAL: raw LLM (verbalized confidence), CoT (verbalized confidence), self-consistency (vote
  margin), LINC-style multi-formalization vote (vote agreement), DSR-LM-style induced-rule Prolog (no closure), Path-of-Thoughts
  (PRIMARY baseline; path-agreement as abstention, reported on the multi-path subset), a TempRel-style COMMIT baseline (single
  consistent labeling), and a soft-unification neural theorem prover. METRICS, per-regime and STRATIFIED (single- vs multi-path,
  single- vs disjunctive-query): (1) NARROWING-YIELD + risk–coverage / selective accuracy AT MATCHED COVERAGE (HEADLINE, attributed
  to cross-path intersection / Mode A) with paired-bootstrap CIs on the selective-accuracy gap vs each baseline; (2) empirical
  zero-FP audit of Mode A (fraction of tightened sets that still contain gold, vs measured recall); (3) Mode B detection:
  closure-DETECTABLE hallucination rate (SECONDARY) with the full decomposition of gold-wrong non-abstained predictions into
  collapse-caught / silent-wrong-narrowing-from-unsound-edge / invisible-single-chain — reported as a LOWER BOUND on Allen
  IA/RCC-8, exact on the point-algebra arm; (4) repair quality (toward- vs away-from-gold movement, CI-separated), reported
  separately because localization can err; (5) elicited-table composition P/R vs gold (kinship); (6) gain-vs-redundancy and
  gain-vs-hop-count curves at realism-matched difficulty; (7) APPLICABILITY ENVELOPE numbers — relation-composable fraction
  AND multi-path-with-bite fraction per corpus — reported up front; (8) atomic extraction P/R as a HELD-FIXED control. The
  optional probabilistic/semiring variant carries per-relation weights as EXPLORATORY soft propagation with a reliability
  diagram / ECE; the hard, exact, calibration-free closure path is the primary contribution. All LLM calls go through OpenRouter;
  cost stays well under $10 via short documents, caching, and a cheap extraction model; closure and repair run in milliseconds
  per network on a laptop.
success_criteria: >-
  HEADLINE PREDICTION (single, leads everything, over-commitment-ROBUST): on the MULTI-PATH-WITH-BITE subset at REALISM-MATCHED
  difficulty and the pre-registered frontier operating point, closure-certified SOUND NARROWING (Mode A) achieves strictly
  higher selective accuracy AT MATCHED COVERAGE than Path-of-Thoughts and self-consistency voting (each given its own matched
  abstention signal), with the gap CI-separated from zero under paired bootstrap — AND this win is attributable to CROSS-PATH
  INTERSECTION (the closure/intersection-ON-vs-OFF table-held-fixed ablation reproduces it; the Mode-A-only ablation reproduces
  it WITHOUT collapse-repair), so it does NOT depend on the over-commitment rate. CONFIRMS if, in addition: (1) the frontier
  map shows a region clearing the pre-registered recall gate AND non-trivial narrowing-yield (the go/no-go is met), and Mode
  A's empirical zero-FP audit holds (tightened sets still contain gold at the rate predicted by measured recall); (2) gain
  scales with measured redundancy at realism-matched difficulty; (3) at least ONE real-text arm — the MATRES HELD-OUT-EDGE
  narrowing arm preferred — clears the pre-registered multi-path-with-bite threshold so the headline is not synthetic-only;
  (4) the disjunction-ON variant beats the commit-to-singleton variant (supports sound-but-loose labeling). SECONDARY (Mode
  B, magnitude tracks over-commitment, reported distinctly): conditional on pilot-measured per-edge recall, closure produces
  ZERO false-positive DETECTION flags; repairs move the query edge toward gold significantly more often than away (CI-separated,
  weaker localization claim). APPLICABILITY ENVELOPE (pre-registered significance bar): we report the multi-path-with-bite
  fraction of real composable queries and pre-register the threshold distinguishing a 'significant general mechanism' (fraction
  at/above the bar) from a 'niche safety-net with low yield' (below), and frame the contribution's reach honestly against
  it. DISCONFIRMS / SCOPES if: no narrowing-yield advantage over Path-of-Thoughts or voting at matched coverage on the multi-path-with-bite
  subset EVEN WHEN sound sets are sub-universal and multi-path bite exists; closure/intersection-ON == OFF when multi-path;
  gain does not scale with redundancy; or the frontier has NO region with both adequate recall and non-trivial yield. PRE-REGISTERED
  HONEST FAILURE MODES (each a publishable scope boundary): (a) NEAR-UNIVERSAL UNDER-SPECIFICATION — LLM sets are so broad
  they are effectively universal, so intersection cannot tighten (Mode A inert); this is distinct from merely 'broad' sets
  and is the ONLY under-specification outcome that disconfirms Mode A; (b) CONSISTENT-BUT-WRONG elicited table — shown only
  in kinship, quantified vs gold, shown NOT to arise in exact-table settings; (c) INVISIBLE hallucinations — confident self-consistent
  single-chain errors closure structurally cannot see; (d) SILENT WRONG NARROWING — an UNSOUND high-recall set that omits
  gold drives closure to a confident WRONG singleton with NO collapse; we report its rate, show it is bounded by (1−recall),
  and test whether the recall-floor gate suppresses it; (e) TINY ENVELOPE — the multi-path-with-bite fraction of real queries
  falls below the pre-registered bar, scoping the contribution to a niche safety-net. Throughout, 'zero false-positive' is
  stated separately for Mode A (intersected set still contains gold under sound inputs, audited against measured recall) and
  Mode B (DETECTION only, not repair); the closure-detectable hallucination rate is a LOWER BOUND because path-consistency
  is incomplete for Allen IA/RCC-8 (complete only for the MATRES point-algebra arm). Atomic extraction P/R must remain comparable
  to baselines (the contribution is at composition), the relation-composable AND multi-path-with-bite fractions per corpus
  must be reported (applicability envelope), and trace-graphs must be judged human-auditable.
related_works:
- >-
  Knez & Sun 2024 (arXiv:2406.11486, 'Analysing zero-shot temporal relation extraction on clinical notes using temporal consistency'):
  zero-shot LLMs assign MORE THAN ONE relation to a pair for ≥50% (up to 97%, Gemma BatchQA) of pairs and violate uniqueness/transitivity;
  the authors ENFORCE consistency with ILP and find it DOES NOT improve F1 ('even when temporal consistency is achieved, the
  predictions can remain inaccurate'). Closest recent analysis. Difference: it MEASURES consistency as a diagnostic and enforces
  it under the F1-maximizing COMMIT contract (which it shows fails); it has no closure-as-CERTIFICATE, no preserved disjunction,
  no abstention/risk–coverage, and no cross-path zero-FP narrowing. We read its negative result as motivation: we PRESERVE
  the multi-relation output as a sound disjunction and NARROW it, optimizing faithfulness-by-abstention rather than F1.
- >-
  Hu, Huang & Feng 2024 (arXiv:2408.07353, 'Only One Relation Possible? Modeling the Ambiguity in Event Temporal Relation
  Extraction', METRE): a multi-LABEL classifier that infers the possibility of each temporal relation independently and treats
  VAGUE as >1 possible relation, with a speculation mechanism. Directly relevant to our 'sound-but-loose disjunctive labeling.'
  Difference: METRE is a TRAINED per-pair classifier predicting a label-set to maximize extraction F1; it does NOT carry the
  disjunctive set through an EXACT composition table across MULTIPLE paths, performs no cross-path intersection, issues no
  gold-free certificate, and does not abstain via risk–coverage. We obtain the disjunction training-free from an LLM and delegate
  ALL precision to exact closure.
- >-
  Liu et al. 2026 (arXiv:2602.04755, 'When Silence Is Golden: Can LLMs Learn to Abstain in Temporal QA and Beyond?', ICLR
  2026): TRAINS LLMs to abstain in temporal QA via Chain-of-Thought supervision + RL with abstention-aware rewards. Relevant
  to our risk–coverage objective. Difference: abstention is a LEARNED skill at the QA-answer level from data; there is no
  algebraic consistency certificate, no per-edge reading-error localization, no preserved relation-algebra disjunction, and
  no closure-based narrowing. Ours is training-free, operates at the per-edge/QCN level, and abstains because the deductive
  closure leaves the query a disjunction.
- >-
  Temporal-relation extraction with ILP global inference (Ning, Feng & Roth 2017, EMNLP; CogCompTime): a TRAINED extractor
  produces per-pair scores and ILP enforces transitivity + symmetry to output a single globally-consistent labeling. Closest
  prior art for 'enforce qualitative consistency on machine-extracted temporal relations.' Differences: (1) it COMMITS to
  one relation per pair to maximize F1; we PRESERVE disjunctive uncertainty, NARROW by cross-path intersection, and ABSTAIN
  (opposite output contract); (2) it uses LEARNED scores + approximate optimization (a high-score consistent labeling can
  be wrong); we use the EXACT table so intersection is sound and collapse is a gold-free DETECTION certificate (conditional
  on recall); (3) it needs a trained per-corpus model; our reader is an untrained LLM that generalizes across algebras.
- >-
  SputLink (Verhagen 2004/2005, 'Temporal Closure in an Annotation Environment'): computes temporal closure over TimeBank
  using a convex subset of Allen's interval algebra to DENSIFY TimeBank/TimeBank-Dense. Difference: SputLink is the closure
  tool that BUILDS gold over already-formal human annotations and commits to a labeling; it does not read NL, preserves no
  LLM disjunction, certifies no reading error, and has no abstention. We avoid circularity by using only MATRES's DIRECT human
  gold for the primary arm and framing TB-Dense as noisy-LLM-read-of-CLEAN-human-local-edges→closure vs clean-read closure.
- >-
  CAEVO (Chambers, Cassidy, McDowell & Bethard 2014, TACL, 'Dense Event Ordering with a Multi-Pass Architecture'): a precision-ranked
  cascade of 12 sieves that infers transitive links and imposes transitivity over the coarse TB-Dense algebra. Difference:
  CAEVO COMMITS to a single dense consistent labeling for F1; it does not preserve disjunction, does not use consistency as
  a gold-free certificate over LLM-read relations, and does not abstain. We reuse its coarse composition table (cited verbatim)
  but invert the objective to faithfulness-by-abstention over LLM disjunctive reads.
- >-
  Path-of-Thoughts (2024, arXiv:2412.17963): three stages — graph extraction, path identification, per-path reasoning — beating
  SOTA by up to 21.3% on StepGame/CLUTRR. PRIMARY baseline. Difference (verified): it calls an external reasoner 'for each
  reasoning path' INDEPENDENTLY and does NOT intersect relations arriving at the same pair from multiple paths nor detect
  cross-path contradictions; when paths disagree it outputs multiple possible relations but does NOT abstain. This is EXACTLY
  the gap our Mode A (cross-path intersection of sound sets) fills, so our claim is restricted to the MULTI-PATH-WITH-BITE
  subset; we give PoT a matched abstention signal (path-agreement) for a fair matched-coverage comparison.
- >-
  DSR-LM / 'LLMs can Learn Rules' (Yang et al. 2023, arXiv:2305.03742; Zhu et al. 2023, arXiv:2310.07064): INDUCE weighted/symbolic
  composition rules to fit task accuracy. Difference: rule induction optimizes data fit and gives a point answer; we enforce
  the EXACT ALGEBRAIC LAWS (converse, associativity, disjointness) necessary for soundness independent of training data, and
  use closure for zero-FP narrowing, detection, localization, repair, and abstention. Our table-held-fixed closure/intersection-ON-vs-OFF
  ablation specifically isolates path-consistency from 'a fixed consistent table exists,' which is DSR-LM's contribution.
- >-
  Logic-LM (Pan et al. 2023, arXiv:2305.12295) and LINC (Olausson et al. 2023, arXiv:2310.15164): Logic-LM self-refines a
  formulation using solver crash/unsat messages; LINC majority-votes the answers of multiple formalizations. Difference: Logic-LM
  reacts only to crashes and has no positive global INVARIANT over relational knowledge; LINC's answer-level voting cannot
  see that individually-popular composition steps are JOINTLY inconsistent, nor can it TIGHTEN a disjunctive query by intersection.
  Algebraic closure is a global necessary condition both lack; we give LINC vote-agreement as a matched abstention signal.
- >-
  LAMBADA (Kazemi et al. 2023, arXiv:2212.13894) and path-isolation reasoning: backward chaining / per-path reasoning that
  manages inconsistency by COMPOSITIONAL ISOLATION rather than global enforcement. Difference: we do the opposite — INTERSECT
  across paths via closure, which both tightens disjunctions (Mode A) and detects contradictions (Mode B); isolation can return
  mutually inconsistent answers and cannot resolve disjunctive uncertainty.
- >-
  Logically Consistent Language Models / LOCO-LMs (Calanzone, Teso & Vergari 2024, arXiv:2409.13724; ICLR 2025): a TRAINING-TIME
  neuro-symbolic loss fine-tuning an LLM to be consistent with propositional facts/rules. Difference: it is training-time
  and PROPOSITIONAL; we are training-free at INFERENCE time and enforce multi-hop COMPOSITION closure over a RELATION ALGEBRA
  read off text, producing per-instance certificates, abstention, and trace-graphs — pre-empting a 'consistency enforcement
  is not new' objection (prior LM-consistency work enforces propositional/factual consistency, not relation-algebra composition
  closure).
- >-
  Classical qualitative reasoners and tractability theory: GQR, SparQ, Allen (1983), Renz & Nebel (path consistency / random
  network model A(n,d,l)), Vilain & Kautz 1986 (point algebra), van Beek (PC insufficient for the full point algebra with
  ≠), and Nebel & Bürckert 1995 (ORD-Horn, JACM 42(1)) proving path-consistency decides satisfiability in ORD-Horn but is
  'in general not sufficient' for the full algebra (NP-hard). So PC is COMPLETE for the convex point algebra and ORD-Horn
  yet SOUND-BUT-INCOMPLETE for full Allen IA / RCC-8. Difference: these assume a clean human-given table on already-formal
  data; none read the algebra off NL via an LLM, certify reading errors, narrow by cross-path intersection of LLM disjunctions,
  or optimize risk–coverage. We import their exact machinery and tractability facts (hence our MATRES convex-point-algebra
  arm gives a COMPLETE check while Allen IA closure is a lower-bound detector).
inspiration: >-
  A Level-3 (methodological) cross-domain transfer from Qualitative Spatial-Temporal Reasoning and Tarski's relation algebras
  — Allen's interval algebra, RCC-8, the convex point algebra, composition tables, and the path-consistency / algebraic-closure
  constraint-propagation algorithms (classical solvers GQR/SparQ), plus the tractability theory (point-algebra and ORD-Horn
  completeness vs full-Allen NP-completeness) — imported into LLM-based relational reasoning and hallucination control, together
  with Reiter's 1980s model-based diagnosis (minimal hitting sets of conflict sets) for localizing which extracted atom to
  retract. The Level-1 framing is CODING THEORY: an exact composition table turns multi-path redundancy in a document into
  an error-correcting code over LLM extractions — redundant constraining paths let closure DETECT and CORRECT mis-reads with
  no external labels, exactly as parity checks detect bit errors, and the benefit scales with redundancy the way decoding
  power scales with code rate. This revision sharpens the coding-theory lens to NAME TWO DISTINCT OPERATIONS the field already
  separates: (1) ERASURE-style narrowing — when every received symbol is a SOUND superset of the truth, intersecting redundant
  constraints shrinks the candidate set toward the codeword with zero risk of excluding it (our Mode A, the zero-FP headline,
  the analogue of list-decoding within a guaranteed-correct list); and (2) ERROR-correction — when a symbol is corrupted (unsound),
  the code DETECTS it via a parity violation but can mis-correct (our Mode B and its silent-wrong-narrowing dual, the channel-capacity
  caveat that a code only corrects within its decoding radius — here the per-edge INPUT must contain the gold relation, i.e.
  recall). Recognizing that the SAME breadth knob trades recall (decoding radius) against bite (parity-violation rate) gives
  the RECALL–BITE FRONTIER as the right object to map, not a point. The Level-2 framing comes from SELECTIVE PREDICTION /
  risk–coverage in ML: compare an abstaining method against non-abstaining baselines at MATCHED COVERAGE, each baseline given
  its own confidence signal. Three refined cross-field insights drive the design: (1) LLMs are competent LOCAL qualitative
  namers that do NOT propagate constraints across paths — the missing piece is global propagation, and cross-path INTERSECTION
  of sound sets is a zero-FP win that needs no over-commitment; (2) because the table is mathematical ground truth, intersection-of-sound-sets
  can only move toward gold and collapse-of-unsound-sets is a calibration-free certificate — flipping the objective from accuracy-by-committing
  (ILP global inference, whose own authors show consistency-enforcement does not raise F1) to faithfulness-by-abstaining;
  (3) the coding-theory lens names BOTH the safe primary mode (erasure-style narrowing) and the Achilles heel (recall-bounded
  decoding radius), which we elevate to a pre-registered failure mode rather than hide.
terms:
- term: Sound narrowing (Mode A, primary)
  definition: >-
    The zero-false-positive value mode: when every LLM edge set is SOUND (contains the gold relation) but sub-universal, intersecting
    the compositions that arrive at a query pair from MULTIPLE non-universal paths yields a set that still contains gold yet
    is strictly tighter than any single path. It requires breadth + multi-path bite, NOT over-commitment, and is exactly what
    per-path-isolated reasoners cannot do. It is inert only in the degenerate all-universal limit and is the over-commitment-robust
    driver of the risk–coverage headline.
- term: Detection/repair (Mode B, secondary)
  definition: >-
    The collapse-based value mode: an empty closure (an edge collapsing to the empty relation) is a deductive certificate
    that some LLM edge is UNSOUND — a gold-free zero-false-positive DETECTION flag (conditional on recall). It requires at
    least one over-committed/recall-failed edge to fire, supports Reiter-style minimal-hitting-set localization/repair (which
    can mislocalize), and carries the silent-wrong-narrowing dual. Its magnitude tracks the measured over-commitment rate
    and is reported distinctly from Mode A.
- term: Recall–bite frontier
  definition: >-
    The curve, traced by sweeping the prompt-elicited breadth knob from 'name the relation' to 'name the maximal sound set,'
    of per-edge recall against narrowing-yield and collapse-rate. Recall (Mode A/B soundness) and bite (Mode B collapses)
    are in direct tension on the SAME knob, so a single operating point cannot establish viability; we map the frontier as
    a primary deliverable and pre-register that the main run proceeds only if some region clears a recall gate AND non-trivial
    narrowing-yield.
- term: Narrowing-yield
  definition: >-
    The headline Mode-A metric: the fraction of multi-path SOUND-input query pairs whose cross-path intersection STRICTLY
    tightens the query set, together with the realized fraction of tightened sets that still contain gold (the empirical zero-FP
    audit against measured recall) and the resulting matched-coverage selective-accuracy gain. Distinct from the Mode-B detection
    rate.
- term: Multi-path-with-bite fraction (applicability envelope)
  definition: >-
    The fraction of real composable queries with ≥2 non-VAGUE/non-universal constraining paths to the query pair (so intersection
    or collapse is exercised). Reported up front as a headline-adjacent number alongside the relation-composable fraction;
    a pre-registered threshold distinguishes a 'significant general mechanism' from a 'niche safety-net with low yield.'
- term: Held-out-edge MATRES narrowing arm
  definition: >-
    The reframed real-text PRIMARY: within MATRES's dense same-axis annotation, take locally-redundant event clusters/triangles
    where ≥2 human-annotated convex point-algebra edges constrain a held-out edge; hide one human-annotated edge and predict
    it by closure over the others. Gold is DIRECT human start-point annotation in the SAME point-algebra scheme — not closure-tool
    output, not scheme-mismatched — dissolving the query-gold provenance confound. Long-distance deduction is secondary/best-effort
    with point↔interval-mapped gold.
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
    only for the convex point algebra and ORD-Horn-style subclasses. Polynomial and millisecond-fast per document.
- term: Convex point algebra (MATRES arm)
  definition: >-
    The relation algebra over a single time point per event with convex base relations ≤, =, ≥ (and disjunctions). MATRES's
    BEFORE/AFTER/EQUAL/VAGUE start-point labels instantiate this, for which path-consistency is provably COMPLETE and the
    table exact. We widen the non-convex {<,>} (genuine ≠) to VAGUE to preserve completeness and MEASURE the bite lost by
    that widening; if non-trivial we add a full-point-algebra arm scored as a lower-bound detector.
- term: Qualitative constraint network (QCN)
  definition: >-
    A graph whose nodes are entities/events and whose edges carry a SET of possible base relations (a singleton = known relation;
    a larger set = disjunctive uncertainty; the universal relation = unknown). The data structure on which closure operates;
    the query/held-out edge starts universal and is narrowed by closure.
- term: Sound-but-loose disjunctive labeling
  definition: >-
    Reframing the LLM's task from 'name THE relation' (precision-oriented, over-commitment-prone) to 'name the set of base
    relations the text span does NOT exclude' (recall-oriented, NLI-like). Soundness means the gold relation is INSIDE the
    emitted set; precision is delegated to exact closure. Its failure is RECALL failure (gold omitted), the source of silent
    wrong narrowing.
- term: Input-soundness / per-edge recall
  definition: >-
    The probability that an LLM's emitted edge set CONTAINS the gold relation. Mode A's zero-FP narrowing holds exactly when
    inputs are sound, and Mode B's zero-FP detection is conditional on this quantity, which is MEASURED across the breadth
    sweep (not assumed = 1). The rate of silent wrong narrowing is bounded by 1−recall; an optional recall-floor gate withholds
    certified narrowings/repairs when measured recall is below threshold.
- term: Silent wrong narrowing (pre-registered failure mode)
  definition: >-
    When a high-recall set OMITS gold (an unsound label), closure can narrow the query to a confident WRONG singleton with
    NO empty collapse — a certified-LOOKING hallucination the mechanism actively endorses, strictly worse than an invisible
    single-chain error. Its rate is governed by per-edge unsoundness (1−recall) and reported in the decomposition of gold-wrong
    non-abstained predictions; the recall-floor gate is tested as a mitigation.
- term: Matched-coverage selective comparison
  definition: >-
    The protocol for comparing an abstaining method against baselines: each baseline is given its own abstention/confidence
    signal (vote margin, verbalized confidence, vote agreement, path-agreement), thresholds are swept so every method reports
    at the SAME coverage, and selective accuracy is compared with paired bootstrap CIs — preventing the headline from conflating
    'closure' with 'closure has a better-calibrated abstain than baselines were given.'
- term: Realism-matched difficulty (with pre-registered matching statistic)
  definition: >-
    A pre-registered NL-realization protocol for the synthetic generator (a fixed library of clean→ambiguous paraphrases per
    base relation) tuned so the induced per-edge error decomposition MATCHES the pilot's real-text decomposition. To remove
    researcher degrees of freedom, the matching statistic (total-variation distance between real and synthetic per-edge error-type
    distributions, plus a recall and mean-breadth tolerance band) and its acceptance threshold are FIXED BEFORE generating
    the redundancy-scaling curve, which is reported only at this setting.
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
  We split exact relation-algebra path consistency (Allen, convex point algebra, RCC-8), imported from qualitative spatial-temporal
  reasoning, into two value modes for the deduction module of a text-to-logic pipeline: PRIMARY — cross-path SOUND NARROWING,
  where intersecting the LLM's high-recall sound disjunctive sets across multiple paths tightens a query toward gold with
  zero false-positive risk and no need for over-commitment (exactly what path-isolated reasoners cannot do), driving the risk–coverage
  headline; and SECONDARY — collapse-based DETECTION/repair, a gold-free reading-error certificate conditional on measured
  recall, with silent-wrong-narrowing as a pre-registered (1−recall)-bounded dual. We map the recall–bite frontier (not a
  point), test on synthetic multi-path QCNs at pre-registered realism-matched difficulty and on a scheme-clean MATRES held-out-edge
  point-algebra arm (where path consistency is complete), foreground the multi-path-with-bite applicability envelope, and
  compare at matched coverage against Path-of-Thoughts and voting with paired-bootstrap CIs.
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
</previous_hypothesis>

<previous_review>
Critiques from the previous review. Check which ones have been addressed
in the revised hypothesis. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (methodology) The success criteria over-condition the ENTIRE benefit on a non-trivial over-commitment rate ('the net benefit is conditional on ... a non-trivial OVER-COMMITMENT rate ... vs UNDER-SPECIFICATION which leaves nothing to narrow'), and list under-specification as failure mode (a) ('sound but inert, low yield'). This is too strong and risks a mis-scoped DISCONFIRM. There are two distinct mechanisms with different requirements and risk profiles. (1) NARROWING: when all edges are SOUND (gold inside the set) but broad, intersecting the compositions arriving at the query pair from multiple paths yields a set that still contains gold yet can be strictly tighter than any single path — a ZERO-false-positive narrowing toward gold that improves risk-coverage. This requires breadth + multi-path bite, NOT over-commitment, and it is precisely what Path-of-Thoughts structurally cannot do (the hypothesis itself notes PoT 'does NOT intersect relations arriving at the same pair from multiple paths'). It is inert ONLY when sets are essentially universal, not merely 'broad'. (2) DETECTION/repair: an empty collapse requires at least one UNSOUND edge (over-commitment / recall failure), and carries the silent-wrong-narrowing dual. The risk-coverage HEADLINE is largely driven by mode (1), which operates in the under-specification regime. Conflating these makes the central bet fragile: if the pilot measures low over-commitment, the pre-registered criteria could declare 'no benefit' even though the safe narrowing mode delivered exactly the contribution's value.
  Action: Separate the two modes in the framing, success criteria, and metrics. Report NARROWING-YIELD (mode 1: fraction of multi-path sound-input queries the intersection strictly tightens, and the resulting matched-coverage gain) as the zero-FP primary driver, distinctly from DETECTION/repair (mode 2). Recast 'under-specification' as a regime with safe value as long as edge sets are sub-universal and multi-path bite exists — inert only in the all-universal limit. Make the headline prediction robust to the over-commitment rate by attributing the matched-coverage win to cross-path intersection, not to contradiction-catching.
- [MAJOR] (rigor) The recall-vs-bite tension is FUNDAMENTAL and the viable operating regime may be narrow or empty, yet the pilot is framed around point estimates. The method asks the LLM for high-recall sets (so gold is inside, preserving soundness); but high recall means broad sets, which reduces the tight-wrong singletons that create detectable contradictions (bite) — and any tightening that DOES create bite is exactly the over-commitment that drops gold (recall failure -> silent wrong narrowing). So the two conditions for value are in direct mutual tension and are controlled by the SAME prompt-elicited breadth knob. A single (over-commitment, recall, bite) point measurement cannot establish that a useful operating point exists; the method needs the LLM to be well-calibrated about its own uncertainty (emit sets exactly as broad as warranted), which is a strong assumption. The author states the tension in prose but does not turn it into a measurement plan.
  Action: Reframe the pilot to map the RECALL-BITE FRONTIER as a curve over prompt-elicited breadth (e.g., sweep prompting from 'name the relation' to 'name the maximal sound set', plotting per-edge recall against narrowing-yield and collapse-rate). Pre-register that the main run proceeds only if a region of the frontier achieves both recall above the gate threshold AND non-trivial yield; report the frontier itself as a primary deliverable. Combined with the narrowing/detection decoupling above, this also tells you whether the safe narrowing mode survives at high-recall settings even when detection does not.
- [MAJOR] (methodology) The real-text PRIMARY arm has an under-specified query-gold provenance that risks reintroducing the exact confounds the author worked to escape on TimeBank-Dense. The local edges are MATRES start-point relations (convex POINT algebra), but the long-distance / deduced QUERY pairs are drawn from 'TDDiscourse-style discourse-level pairs.' TDDiscourse annotates document-level temporal relations with an INTERVAL-style scheme (before/after/includes/included/simultaneous/vague), which is NOT the point algebra: a deduced start-point relation (start(A) < start(C)) is not the same object as an interval relation (A BEFORE C => end(A) < start(C)), so scoring point-algebra-deduced queries against interval gold is a scheme mismatch. Worse, TDDiscourse-style long-distance gold may itself be partially derived by transitive closure — the same circularity the author explicitly handles for TB-Dense but does NOT address for the MATRES query set. If unaddressed, the 'cleanest real arm' claim and the 'not synthetic-only' headline are at risk.
  Action: Specify that long-distance query gold is in the SAME convex point-algebra scheme as the edges — either re-derived from human start-point annotation or mapped via a verified point<->interval correspondence with documented information loss — and confirm it is NOT the output of the closure tool under test. Verify document overlap between the MATRES edge source and the long-distance gold source. If clean point-algebra long-distance gold is unavailable, pre-register MATRES as a NARROWING/abstention arm on locally-redundant event triangles (where MATRES already gives dense same-axis annotation within the 2-sentence window), with long-distance deduction scoped as secondary/best-effort.
- [MINOR] (scope) The reach of the headline is unquantified, which bounds the perceived significance to the umbrella text-to-logic goal. The headline lives on 'the multi-path subset at realism-matched difficulty.' If, after pre-measurement, only a small fraction of REAL queries are multi-path-with-bite, then even a CI-separated win is a thin slice of the deduction problem and reads as a niche safety-net rather than a general recipe. The pre-measurement already computes the relevant quantity (fraction of pairs with >=2 non-VAGUE constraining paths); it just needs to be elevated and contextualized.
  Action: Report the multi-path-with-bite fraction of real (MATRES/TB-Dense) queries as a headline-adjacent number alongside the relation-composable fraction, and pre-register the threshold that distinguishes a 'significant general mechanism' from a 'niche safety-net with low yield.' Frame the contribution's reach honestly against that threshold in the success criteria.
- [MINOR] (novelty) A recent cluster of LLM + temporal-consistency / temporal-ambiguity / temporal-abstention work (2024-2026) is uncited and is in some respects closer than the cited trained-extractor systems (Ning ILP, SputLink, CAEVO). Examples surfaced: zero-shot LLM temporal-relation extraction analysed via transitivity/temporal consistency (arXiv:2406.11486), explicit modeling of ambiguity / multiple-relation labels in event temporal relation extraction (arXiv:2408.07353, directly relevant to the 'sound-but-loose disjunctive labeling' claim), and LLM abstention in temporal QA (arXiv:2602.04755, relevant to the risk-coverage objective). The core novelty survives — none combines a gold-free closure CERTIFICATE over a disjunctive QCN with faithfulness-by-abstention — but omitting this cluster invites an 'incremental over existing LLM temporal-consistency work' objection at ACL-KE.
  Action: Add these (and verify each) to related work with one-line differentiators: analysis-only (measures consistency, no closure-as-certificate / no abstention); ambiguity-modeling (predicts a distribution over single relations rather than carrying a sound disjunctive set narrowed by exact closure); temporal-abstention (abstains on QA but has no algebraic consistency certificate or per-edge reading-error localization).
- [MINOR] (rigor) Two smaller technical items. (i) The convex-point-algebra restriction (widening non-convex {<,>} to VAGUE to preserve completeness) silently discards any genuine ≠ constraint; its cost in lost bite is unquantified. In practice it is likely small (≠ is rarely READ directly from text, and the convex relations are closed under composition so composition does not manufacture ≠), but this should be measured rather than assumed. (ii) 'Realism-matched difficulty' matching is a multi-dimensional target (over-commitment / under-specification / breadth / recall) with researcher degrees of freedom: declaring the synthetic decomposition a 'match' to the pilot's real decomposition is post-hoc unless a distance metric and tolerance are fixed in advance.
  Action: (i) In the pilot, report how often the LLM wants to emit ≠/non-convex relations on MATRES text and the bite lost by widening to VAGUE; if non-trivial, consider a parallel full-point-algebra arm scored as a lower-bound detector (since PC is incomplete there). (ii) Pre-register the matching statistic (e.g., total-variation distance between the real and synthetic per-edge error-type distributions plus a recall/breadth tolerance band) and the acceptance threshold BEFORE generating the redundancy-scaling curve.
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

### [2] HUMAN-USER prompt · 2026-06-17 12:15:31 UTC

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

### [3] SYSTEM-USER prompt · 2026-06-17 12:21:15 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same closure-certificate frame; refines by promoting Mode-A cross-path narrowing to the headline, mapping the recall-bite frontier, and reframing MATRES as a clean held-out-edge arm.' is too long (at most 120 characters, got 182)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
