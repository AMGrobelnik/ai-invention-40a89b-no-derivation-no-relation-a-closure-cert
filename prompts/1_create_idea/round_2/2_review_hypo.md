# review_hypo — create_idea

> Phase: `hypo_loop` · round 2 · `review_hypo`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 11:42:48 UTC

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
  Closure-Guarded Reasoning: Enforcing Relation-Algebra Consistency on LLM-Elicited Knowledge to Faithfully Reason over Text
hypothesis: >-
  When converting a short document into a logical representation and performing multi-hop reasoning, the dominant source of
  confident-but-wrong (hallucinated) conclusions is not faulty atomic extraction but globally-inconsistent COMPOSITION of
  relations: the LLM supplies relation-composition steps (e.g., 'mother's father = grandfather', 'event A is before B', 'clause
  X supersedes Y') that are each locally plausible yet jointly violate basic algebraic laws (converse, associativity, disjointness,
  intersection across multiple paths). We hypothesize that treating the relations the LLM extracts and composes as a CONSTRAINT
  NETWORK over a RELATION ALGEBRA, and enforcing classical ALGEBRAIC CLOSURE (path consistency) borrowed from Qualitative
  Spatial-Temporal Reasoning, will (a) detect and localize these inconsistent compositions without gold labels, (b) repair
  them via minimal correction or abstain when the relation stays underdetermined, and (c) thereby yield strictly more faithful
  multi-hop deduction and a measurably lower hallucination rate than free LLM composition, answer-level voting (LINC-style),
  path isolation (Path-of-Thoughts), or LLM-induced rules (DSR-LM) — with the advantage GROWING with the number of reasoning
  hops, because local inconsistencies compound over long composition chains. The LLM handles the soft/semantic work (entity
  and relation extraction, fuzzy unification of surface relation phrases onto canonical algebra elements, proposing composition-table
  entries it is confident about); a cheap, exact, decades-old symbolic closure algorithm enforces the hard GLOBAL consistency
  that no local or answer-level method can guarantee.
motivation: >-
  Multi-hop relational reasoning over professionally written text — kinship in narratives, temporal ordering of events in
  news, supersession/obligation/cross-reference chains in legal and regulatory documents — is exactly where LLM hallucination
  is most damaging and where neuro-symbolic pipelines most need to fuse explicit document facts with implicit composition
  knowledge. Today's text-to-logic systems handle the COMPOSITION knowledge in one of three unsatisfying ways: (1) a human
  hand-crafts the composition rules (e.g., the 92 kinship rules used for CLUTRR), which does not scale to new relation families
  such as legal supersession or organizational hierarchy; (2) the LLM composes relations freely, which is locally fluent but
  globally inconsistent, producing silent errors that solver-error feedback (Logic-LM) and majority voting (LINC) cannot see
  because the individual steps each look fine; or (3) paths are reasoned in isolation (LAMBADA, Path-of-Thoughts), which deliberately
  AVOIDS the global consistency check and therefore cannot resolve disjunctive uncertainty or detect contradictions arriving
  at the same entity pair from two different paths. Independent evaluations confirm the core failure: on qualitative relational
  benchmarks (RCC-8, Allen's interval algebra) LLMs 'fail at multi-path disjunctive/intersection tasks rather than performing
  algebraic closure, instead treating paths independently.' Meanwhile, the qualitative-reasoning community has had exact,
  commodity-cheap algorithms for enforcing exactly this global consistency (path consistency / algebraic closure over relation
  algebras; GQR, SparQ) for forty years — but those classical solvers assume a clean, given composition table and have never
  been coupled to an LLM that READS the table off natural language. Bridging these two worlds gives a principled hallucination
  filter that is symbolic, auditable, free of probability-calibration guesswork, and runs on a laptop. If it works, it offers
  a new and general recipe for trustworthy relational reasoning over text, directly producing the human-auditable trace-graphs
  and quantified hallucination reduction the application demands.
assumptions:
- >-
  The target reasoning is RELATIONAL and COMPOSITIONAL: the answer is obtained by composing base relations along paths in
  an entity/event graph (kinship, temporal before/after/overlap, spatial containment, organizational reports-to, legal supersedes/obligates/cross-references).
  This is a deliberate scope condition; arbitrary propositional rule chaining (e.g., generic RuleTaker rules) is out of scope
  and used only as a contrastive negative.
- >-
  A relation algebra for the domain can be assembled cheaply: a small set of canonical base relations plus a converse operation
  and a composition table, where the well-defined backbone (converses, type signatures, disjointness/cardinality axioms) is
  seeded by an upper ontology (SUMO/OpenCyc/OWL-Time) and the remaining composition-table entries are elicited from the LLM.
  The base-relation set is small enough (tens, not thousands) that algebraic closure is trivially fast on commodity hardware.
- >-
  LLMs make locally-plausible but globally-inconsistent compositional judgments (empirically established by qualitative-reasoning
  LLM evaluations), so closure VIOLATIONS actually occur and carry diagnostic signal about which compositions or extractions
  are hallucinated.
- >-
  Atomic relation extraction from short (~3000-character) professionally written documents is reliable enough that most residual
  error enters at the composition / disjunction-resolution step; extraction errors that DO occur and that create a contradiction
  are themselves caught and localized by closure (an extracted edge that makes a path collapse to the empty relation becomes
  a repair candidate).
- >-
  Gold annotations for atomic relations and for multi-hop answers are available or constructible (CLUTRR ships them; a temporal-ordering
  testbed over short news/legal documents can be annotated against Allen relations) so that atomic precision/recall and the
  hallucination rate can be measured.
investigation_approach: >-
  Build a four-stage pipeline and evaluate it against neural and neuro-symbolic baselines. STAGE 1 (Neural extraction, LLM):
  prompt the LLM to extract entities/events and surface relation mentions from the document into typed atoms; an LLM 'fuzzy
  unification' step normalizes each surface phrase ('dad', 'in-law', 'shortly after', 'is overridden by') onto canonical base
  relations of the target algebra, emitting a weighted DISJUNCTION of base relations when the mapping is uncertain (this is
  precisely the probabilistic / fuzzy-unification engine the task calls for). STAGE 2 (Algebra assembly): seed the relation
  algebra from an upper ontology (converses, type signatures, disjointness/cardinality axioms from SUMO/OpenCyc/OWL-Time);
  query the LLM for the missing composition-table entries (r composed with s) with a confidence each; cache the table once
  per domain so per-document cost is just extraction. STAGE 3 (Symbolic closure, the contribution): assemble a qualitative
  constraint network (nodes = entities/events, edges = disjunctive relation sets; explicit edges are singletons, the queried
  pair starts as the universal relation), then run algebraic closure / path consistency — iteratively intersect each edge
  with the composition of relations along every two-step path until a fixpoint. Closure NARROWS the query edge to the deduced
  relation, and any edge collapsing to the EMPTY set flags a global inconsistency. On inconsistency, compute a minimal repair
  (Reiter-style minimal-diagnosis / small MaxSAT over the lowest-confidence composition entries and extracted edges) to restore
  a non-empty closure, recording the diagnosis. If the query relation remains a disjunction of more than one base relation
  after closure, ABSTAIN (or return the set) rather than guess. STAGE 4 (Audit): emit the constraint network, the closure
  derivation (which compositions fired on which paths), and any repairs as a trace-graph; the final relation can additionally
  be discharged in SWI-Prolog/ASP using the repaired, closed table as rules for an executable, replayable proof. Probabilistic
  variant: carry per-base-relation weights and run a semiring (soft) path consistency so the output is a calibrated distribution
  over base relations and the hallucination risk is its mass on wrong relations. DATASETS: primary = CLUTRR (kinship is a
  textbook relation algebra; crucially test on hop-depths greater than those seen in prompts to probe compositional generalization);
  secondary = a temporal event-ordering testbed built from short news/legal/regulatory documents annotated with Allen interval
  relations, plus a legal supersession/cross-reference relation set; RuleTaker as an out-of-scope contrast to delimit where
  the mechanism applies. BASELINES: raw LLM, chain-of-thought, standard RAG, self-consistency voting, LINC-style multi-formalization
  majority vote, LLM-emits-Prolog-with-its-own-induced-rules (no closure), Path-of-Thoughts (path isolation), and a soft-unification
  neural-theorem-prover. ABLATIONS isolate each load-bearing piece: closure OFF (free composition), repair OFF (detect-only/abstain),
  ontology-seed OFF (LLM supplies the whole algebra), disjunctive-uncertainty OFF (force singleton relations). All LLM calls
  go through OpenRouter; total spend tracked and kept well under $10 by caching the composition table and using short documents;
  closure runs in milliseconds per network on a laptop.
success_criteria: >-
  CONFIRMS the hypothesis if the closure-guarded pipeline (i) raises multi-hop deduction accuracy and (ii) lowers the hallucination
  rate (fraction of confident, non-abstained, wrong relation predictions) versus EVERY baseline on CLUTRR and the temporal
  testbed, AND the accuracy/hallucination gap GROWS monotonically with hop count (the signature prediction that global inconsistency
  compounds over long chains); ablations must show closure and minimal-repair are individually load-bearing (removing closure
  erases most of the gain; detect-only abstention already beats free composition on a selective-prediction / accuracy-vs-coverage
  curve). Atomic relation extraction precision/recall should be comparable to baselines (the contribution is at the composition
  step, not extraction), while closure should measurably REDUCE the closure-violation rate from raw LLM elicitation to repaired
  networks, and the localized repairs should agree with gold about which atom/composition was wrong above chance. Trace-graphs
  must be judged human-auditable (a person can follow the path that produced the answer and the repair). DISCONFIRMS / SCOPES
  if: closure adds no accuracy or hallucination benefit over answer-level voting or path isolation (e.g., because LLM-elicited
  tables are already globally consistent, or because errors are dominated by extraction rather than composition); the advantage
  does NOT increase with hop count; or repair frequently 'fixes' the network toward the wrong relation. A clean negative (closure
  detects the inconsistency but cannot reliably repair it, so abstention is the only safe action) is itself a publishable,
  honest scope-boundary result about the limits of repairing LLM-elicited relational knowledge.
related_works:
- >-
  Logic-LM (Pan et al., 2023, arXiv:2305.12295): LLM translates a problem into a symbolic formulation, a solver runs, and
  a self-refinement loop edits the formulation using the solver's ERROR messages. Difference: Logic-LM only reacts to syntactic/unsatisfiability
  errors; it has no notion of a positive global consistency INVARIANT over the relational knowledge. We enforce algebraic
  closure (a necessary soundness condition that catches SILENT semantic inconsistency in compositions) and repair via minimal
  diagnosis rather than re-prompting on solver crashes.
- >-
  LINC (Olausson et al., 2023): converts premises to first-order logic and majority-votes the answers of multiple formalizations
  passed to a theorem prover. Difference: answer-level voting cannot detect that a set of individually-popular composition
  steps are JOINTLY inconsistent; closure is a global necessary condition that voting structurally lacks, and it narrows disjunctive
  uncertainty rather than averaging over independent samples.
- >-
  LAMBADA (Kazemi et al., 2023) and Path-of-Thoughts (2024, arXiv:2412.17963): backward chaining / extracting individual reasoning
  paths and reasoning over each path IN ISOLATION, explicitly 'managing inconsistency through compositional isolation rather
  than global consistency enforcement.' Difference: we do the opposite — INTERSECT the relations arriving at the same entity
  pair across multiple paths via algebraic closure, which both tightens disjunctive uncertainty and detects contradictions;
  path isolation cannot do either and can return multiple mutually inconsistent answers.
- >-
  Differentiable symbolic programming for CLUTRR / DSR-LM (Yang et al., 2023, arXiv:2305.03742) and 'Large Language Models
  can Learn Rules' (Zhu et al., 2023, arXiv:2310.07064): INDUCE weighted/symbolic composition rules to maximize task accuracy.
  Difference: rule induction optimizes data fit; we instead enforce ALGEBRAIC LAWS (converse, associativity, disjointness,
  closure) that are necessary for logical soundness independent of training data, and we use closure to DETECT, LOCALIZE,
  REPAIR, and ABSTAIN — capabilities rule induction does not provide.
- >-
  Soft-unification Neural Theorem Provers (Rocktaschel & Riedel, 2017; and follow-ups): replace exact unification with embedding-similarity
  scores so 'dad' and 'father' can match. Difference: NTP's unification is local, uncalibrated, and has no global consistency
  mechanism — it can compose softly-matched relations into a globally impossible configuration. We keep unification symbolic
  and ontology-grounded, let the LLM handle the fuzzy NAMING, and let the relation algebra enforce hard global consistency.
- >-
  Abductive neuro-symbolic gap-filling: ARGOS and 'A Balanced Neuro-Symbolic Approach for Commonsense Abductive Logic' (2026,
  arXiv:2601.18595) iteratively ask the LLM for missing commonsense clauses whenever the solver is stuck. Difference: abductive
  injection has no NULL — it can invent a bridge for any goal, including false ones. Algebraic closure provides a consistency-based
  rejection: a composition that violates closure is refused even when the LLM proposes it confidently, so commonsense composition
  knowledge is admitted only if it is globally consistent.
- >-
  QSTRBench (2026, arXiv:2605.18380) and other qualitative-spatial-temporal LLM evaluations: BENCHMARK whether LLMs can compute
  converses, composition-table entries, and closures, finding that they cannot. Difference: those papers only measure the
  failure; we turn the classical closure ALGORITHM into a control wrapper that elicits the (imperfect) table from the LLM
  and FIXES that failure inside a working text-to-logic pipeline.
- >-
  Classical qualitative constraint reasoners (GQR, SparQ, SQTR for TimeML; Allen 1983; Renz & Nebel) and knowledge-graph repair
  with SHACL/constraint solvers (e.g., arXiv:2507.22419): mature symbolic machinery for path consistency over given relation
  algebras, and for validating triples against shapes. Difference: these assume a clean, human-provided table/schema and operate
  on already-formal data; none read the relation algebra OFF natural-language documents via an LLM, and SHACL validates individual
  triples rather than enforcing multi-hop COMPOSITION closure for deduction and hallucination control.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer from Qualitative Spatial-Temporal Reasoning and Tarski's relation algebras
  — Allen's interval algebra, the Region Connection Calculus, composition tables, and the path-consistency / algebraic-closure
  constraint-propagation algorithms (with classical solvers like GQR/SparQ) — a mature 1980s-2000s knowledge-representation
  subfield, imported into LLM-based relational reasoning and hallucination control, a setting where it has never been applied
  because that community has always assumed a hand-given composition table. The triggering cross-field insight is that LLMs
  behave like locally-consistent but globally-inconsistent qualitative reasoners (they answer each composition query plausibly
  yet violate converse/associativity/intersection laws across a path), and the exact, cheap, decades-old tool for enforcing
  global consistency of qualitative relations is precisely the missing hallucination filter. The localization-and-repair step
  further borrows Reiter's model-based diagnosis (minimal hitting sets of conflict sets) from 1980s KR to pinpoint which extracted
  atom or composition entry to retract — again a technique foreign to the NLP/KE community. The neuro-symbolic division of
  labor (LLM = soft semantic naming and fuzzy unification; algebra = hard global consistency) is what makes the transfer concrete
  rather than a loose analogy.
terms:
- term: Relation algebra
  definition: >-
    An algebraic structure (after Tarski) over a finite set of base relations equipped with composition, converse, intersection,
    and union operations plus an identity, closed under these operations. Kinship, Allen's temporal intervals, and RCC spatial
    regions are standard examples; it provides the laws (converse, associativity) that correct compositional reasoning must
    obey.
- term: Composition table
  definition: >-
    For every ordered pair of base relations (r, s), the set of base relations that the composite r-then-s can take (e.g.,
    parent composed with parent yields grandparent; 'before' composed with 'before' yields 'before'). Here the well-defined
    backbone is seeded from an upper ontology and the remaining entries are elicited from the LLM.
- term: Algebraic closure / path consistency
  definition: >-
    A constraint-propagation algorithm that repeatedly tightens each edge's relation set by intersecting it with the composition
    of relations along every two-step path, until a fixpoint. It is a sound (necessary) global consistency check: if any edge
    collapses to the empty relation, the network is inconsistent. Cheap (polynomial on tiny per-document networks).
- term: Qualitative constraint network
  definition: >-
    A graph whose nodes are entities or events and whose edges are labeled with a SET of possible base relations (a singleton
    means a known relation; a larger set encodes disjunctive uncertainty; the universal relation means 'unknown'). The data
    structure on which algebraic closure operates.
- term: Qualitative Spatial-Temporal Reasoning (QSTR)
  definition: >-
    The knowledge-representation subfield that reasons about space and time using relation algebras and composition tables
    rather than numbers, with mature solvers (GQR, SparQ) for checking consistency via path consistency. The source domain
    of this hypothesis's imported method.
- term: Fuzzy unification (here)
  definition: >-
    The LLM-driven mapping of varied surface relation phrases ('dad', 'in-law', 'shortly after', 'is overridden by') onto
    canonical base relations of the algebra, emitting a weighted disjunction when uncertain. This is the soft/semantic half
    of the neuro-symbolic split; the algebra then enforces hard consistency over these mappings.
- term: Minimal repair (model-based diagnosis)
  definition: >-
    When closure detects an inconsistency, the smallest set of network elements or composition-table entries whose revision
    restores a non-empty closure, computed as a Reiter-style minimal diagnosis (minimal hitting set of conflict sets) or a
    small MaxSAT, preferring to relax the lowest-confidence LLM-supplied items. It both localizes the hallucination and proposes
    a correction.
- term: Selective abstention
  definition: >-
    Returning 'underdetermined' (or the residual relation set) instead of a single answer when closure leaves the query relation
    as a disjunction of more than one base relation, trading coverage for faithfulness and yielding an accuracy-vs-coverage
    curve.
- term: Hallucination rate (operational)
  definition: >-
    The fraction of relational conclusions the system asserts confidently (without abstaining) that are wrong against gold;
    the primary quantity the closure layer is hypothesized to reduce relative to free LLM composition and to answer-level
    voting.
- term: Trace-graph
  definition: >-
    A human-auditable record of the reasoning: the qualitative constraint network, which composition entries fired on which
    paths during closure, any minimal repairs applied, and (optionally) the equivalent SWI-Prolog/ASP proof discharged from
    the repaired, closed table.
summary: >-
  We treat the relational knowledge an LLM extracts and composes from a document as a constraint network over a relation algebra
  and enforce classical algebraic closure (path consistency) — imported from qualitative spatial-temporal reasoning — to detect,
  localize, and repair the globally-inconsistent compositions where multi-hop hallucinations hide, abstaining when relations
  stay underdetermined. The result is more faithful multi-hop reasoning, a lower and quantified hallucination rate (with the
  gain growing with hop count), and auditable trace-graphs, all on commodity hardware.
</previous_hypothesis>

<previous_review>
Critiques from the previous review. Check which ones have been addressed
in the revised hypothesis. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (methodology) Mechanism–dataset mismatch on the PRIMARY dataset. Closure's distinguishing capability is intersecting relations that arrive at the same entity pair from MULTIPLE paths and narrowing DISJUNCTIONS. CLUTRR (confirmed: random kinship graph → target sampling → backward chaining → NL realization) gives a single backward-chained path between the query pair, with gender-determined (functional) kinship composition, so disjunction and multi-path intersection are essentially absent. On a single chain, algebraic closure reduces to forward composition along that chain using the table—i.e., closure-ON is operationally identical to closure-OFF given the same table. Therefore any CLUTRR gain (including a gap that grows with hop count) is attributable to USING A FIXED CONSISTENT COMPOSITION TABLE (the DSR-LM / hand-crafted-rules contribution), not to the path-consistency algorithm that is the stated contribution. The headline experiment as designed cannot separate these.
  Action: Make a multi-path/disjunctive qualitative setting (Allen interval or RCC with cycles/redundant paths) the PRIMARY evaluation. On CLUTRR, either (a) construct/select instances with two or more paths between the query pair (marriage cycles, redundant relation mentions) so intersection is required and report the fraction of instances that trigger a non-trivial intersection or an empty-relation collapse, or (b) explicitly demote CLUTRR to the table-quality/hop-scaling story and acknowledge that closure-ON==closure-OFF there. Design the closure ablation to hold the composition table FIXED so it isolates path consistency rather than the presence of a table.
- [MAJOR] (evidence) The central motivating empirical claim is not supported by the cited source. The hypothesis repeatedly asserts that LLMs 'fail at multi-path disjunctive/intersection tasks rather than performing algebraic closure, instead treating paths independently,' attributing this to QSTR LLM evaluations (QSTRBench, arXiv:2605.18380). QSTRBench is real, but it tests SINGLE-STEP composition-table entries, converses, and conceptual neighbourhoods—not multi-hop constraint propagation—so it does not establish the multi-path-failure premise. It further reports frontier models around 92% on composition (weak models ~6%) and a systematic tendency toward FALSE NEGATIVES (under-specification), which is the opposite of the 'confident, locally-plausible, globally-inconsistent composition' the method is designed to catch: under-specification yields broad disjunctions (safe but un-narrowable), not contradictions. The premise that closure violations 'actually occur and carry diagnostic signal' is thus only partially supported and may be over-stated.
  Action: Cite the precise source that demonstrates multi-path/closure failure (or run a small, cheap pilot on your own networks to establish it before the main study). Replace 'LLMs cannot compute composition tables' with the measured ~72–92% single-step accuracy and characterize the dominant ERROR TYPE (false-negative under-specification vs false-positive over-commitment), since only over-commitment produces the detectable contradictions closure exploits. State the expected closure-violation rate you are targeting and why it is non-trivial.
- [MAJOR] (rigor) Elicitation circularity / necessary-not-sufficient gap. The method's reliability hinges on the LLM supplying the missing composition-table entries (r∘s=?)—exactly the operation it is documented to be imperfect at. Path consistency is a NECESSARY but not sufficient global-consistency condition: a self-consistent but systematically wrong table passes closure with no empty collapse, and minimal repair will then 'restore consistency' toward a wrong relation. Ontology seeding mitigates only the backbone (converses, type signatures, disjointness), not the substantive composition entries that are the hard part. The success criterion 'localized repairs agree with gold above chance' is far too weak to rule this failure mode out.
  Action: Add an explicit, separate metric: composition-table precision/recall against a gold table (CLUTRR provides one for kinship). Report repair quality as the fraction of repairs that move the query edge TOWARD vs AWAY from the gold relation (with CIs), not merely 'above chance.' Detect consistent-but-wrong tables by (i) validating elicited entries against the few ontology-derivable ones, (ii) measuring agreement across multiple independent LLM elicitations, and (iii) reporting how often closure narrows toward gold vs toward a wrong singleton. Make 'consistent-but-wrong table' an explicit, pre-registered failure mode in the analysis.
- [MAJOR] (scope) The testbed where the mechanism actually bites is vapor and is the largest unbudgeted cost. 'A temporal-ordering testbed over short news/legal documents can be annotated against Allen relations' hand-waves the single most load-bearing dataset; annotating Allen interval relations over real text is an entire subfield (TimeML/TimeBank/TempEval) and is hard and expensive to do reliably with multi-path structure. Separately, the claim that legal 'supersedes/obligates/cross-references' forms a relation algebra is asserted, not established—obligation is a deontic modality (not a composable binary interval relation), and cross-reference is not obviously closed under composition/converse. Risk: the experiment defaults to CLUTRR (where closure does not bite, see critique 1) while the temporal/legal arm is too thin or too late to carry the contribution.
  Action: Adopt an EXISTING qualitative-temporal resource with gold structure (a TimeML/TimeBank-derived qualitative set, or a CLUTRR-style SYNTHETIC Allen-network generator that guarantees multi-path instances and ships gold) so closure is exercised with reliable labels and no new annotation effort. De-scope the legal claim to one provably-algebraic fragment (e.g., effective-date temporal ordering, or a transitive supersession-only relation), and explicitly verify it satisfies relation-algebra axioms (associative composition, converse, identity) before building on it. Move any large hand-annotation off the critical path.
- [MAJOR] (rigor) Over-strong success criterion plus a strong, recent baseline that already covers much of the win. Requiring the pipeline to beat EVERY baseline on BOTH CLUTRR AND the temporal testbed AND show a monotonically growing gap with hop count invites a partial outcome that reads as disconfirmation when the true result is 'helps in the multi-path regime.' Path-of-Thoughts (arXiv:2412.17963, confirmed: graph extraction + path identification + reasoning, +21.3% over SOTA, explicitly noise- and composition-robust) already does graph+path reasoning on these datasets and, on single-chain CLUTRR, captures most of what closure would.
  Action: Reframe the headline claim around the regime where closure is provably necessary (multi-path/disjunctive instances) and pre-register a STRATIFIED comparison (single-path vs multi-path subsets, single-relation vs disjunctive queries). Treat Path-of-Thoughts as the primary baseline and report specifically on the multi-path subset. Replace 'beats every baseline everywhere' with a precise per-regime prediction; keep the hop-scaling claim but tie it to the multi-path subset where compounding is genuine, not to single-chain composition where it confounds table-quality.
- [MINOR] (rigor) Calibration tension in the probabilistic/semiring variant. The hypothesis advertises being 'free of probability-calibration guesswork' yet the soft path-consistency variant carries per-base-relation LLM weights and calls the output a 'calibrated distribution' whose mass on wrong relations is the hallucination risk. LLM-supplied confidences are not calibrated, so this is an internal tension and the 'calibrated' label is unjustified as stated.
  Action: Either drop the 'calibrated' language and present the semiring variant as exploratory soft propagation, or add an explicit calibration measurement (reliability diagram / ECE on the soft outputs against gold) and, if needed, a post-hoc calibration step. Keep the calibration-free hard-closure path as the primary, defensible contribution.
- [MINOR] (rigor) The operational hallucination-rate definition catches only the inconsistency-DETECTABLE error subclass. Closure reduces errors that surface as detectable contradictions or that can be narrowed by intersection; confident, self-consistent hallucinations (e.g., a wrong-but-consistent extracted edge on a single chain, or a uniformly biased composition) pass through untouched. Claiming general 'hallucination reduction' over-states the reach of the mechanism.
  Action: Scope the hallucination claim to the detectable subclass and report the decomposition: of all gold-wrong, non-abstained predictions, what fraction are closure-detectable (caught/abstained/repaired) vs invisible to closure. This makes the method's ceiling explicit and strengthens the honest-negative narrative.
- [MINOR] (novelty) A few citations should be pinned/verified and one nearby line is uncited. QSTRBench (2605.18380) and Path-of-Thoughts (2412.17963) verified real; QSTRBench is currently MIScharacterized (see critique 2). The 'A Balanced Neuro-Symbolic Approach for Commonsense Abductive Logic' (2601.18595), SHACL-repair (2507.22419), and the Bhalla-style references should each be re-checked for exact ID/claim. Recent LLM-consistency lines that enforce logical consistency on LM outputs (e.g., 'Logically Consistent Language Models via Neuro-Symbolic Integration') are close in spirit and currently uncited.
  Action: Re-verify every arXiv ID and the exact claim each supports before submission; correct the QSTRBench characterization. Add a short paragraph differentiating from neuro-symbolic logical-consistency-enforcement work for LMs (training-time/propositional) to pre-empt a 'consistency enforcement is not new' objection, emphasizing that your novelty is reading a RELATION ALGEBRA off text and enforcing multi-hop COMPOSITION closure (not propositional fact/rule consistency).
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

### [2] HUMAN-USER prompt · 2026-06-17 11:42:48 UTC

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
