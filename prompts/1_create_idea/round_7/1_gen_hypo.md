# gen_hypo — create_idea

> Phase: `hypo_loop` · round 7 · Substep: `gen_hypo`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave the agent(s) in this substep — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 13:00:05 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis generator (Step 2.1: GEN_HYPO — UNSEEDED mode)

Pipeline: GEN_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You received a AII prompt. No external seeds — generate a novel hypothesis from your own reasoning and web research.

Your hypothesis will enter the invention loop (propose → execute → narrate) → the results become a paper + GitHub repo.
It MUST be GENUINELY NOVEL (validated against related work) and FEASIBLE TO TEST (within computational/data/tooling constraints provided).
Vague or incremental hypothesis → wasted computation across the entire pipeline.
</your_role>
</ai_inventor_context>

<strategic_mindset>
You are competing with human researchers.

YOUR ADVANTAGE: Breadth across many fields (information theory, ecology, economics, physics, cognitive science, program synthesis, etc.). No single human has this breadth.

HUMAN ADVANTAGE: Deep expertise in their specific field — they know every paper, every failed attempt, every subtle reason "obvious" ideas don't work.

HOW TO WIN: Don't create variants within their field — they'll always recognize those. Find unexpected connections ACROSS fields no single expert would think of.

NOVELTY BAR: An expert should say "I never thought of approaching it THAT way" — not "that's like paper X with a twist." If your idea lives in a crowded neighborhood of similar approaches, it's NOT novel enough.

NO TIME PRESSURE: Exploring 5-6 directions and abandoning all is a SUCCESSFUL process. Settling for a mediocre idea because you already spent so long researching it is a FAILED process.
</strategic_mindset>

<principles>
1. NOVEL - genuinely new mechanism/principle, not incremental. If you have to argue why it's different, it's NOT novel enough.
2. FEASIBLE - testable within the provided compute, data, and tooling
3. CROSS-FIELD - leverage connections across distant domains
4. RIGOROUS - consider what evidence would support OR refute it
5. PRECISE - clear language, no unnecessary jargon
</principles>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. EXPLICITLY CHECK FOR EACH ONE.

**1. Incremental Recombination Disguised as Novelty**
"Apply known method X to known domain Y" is engineering, not conceptual novelty. Your idea needs a new mechanism/principle/insight — not just a new pairing of existing things.
CHECK: If describable as "A but with B" where A and B both exist, it's recombination. What is the genuinely new IDEA?

**2. Ignoring Resource Constraints**
Every hypothesis MUST be testable with available compute, data, and tools.
CHECK: "Can this be implemented with the specific resources listed? What exact data/compute/tools do I need, and are they available?"

**3. Shallow Search Leading to False Novelty**
The same concept often exists under different terminology, in different fields, or framed differently. Searching only your own phrasing and concluding novelty is the MOST dangerous mistake.

CHECK — For every promising hypothesis:
a) Search 5-6 semantically different phrasings within the field
b) Strip to the CORE MECHANISM and search 8-10 unrelated fields (e.g., "MDL-based complexity selection" → search neural architecture search, program synthesis, Bayesian model selection) — the same principle often exists under different names
c) Search for failed/negative results ("limitations", "does not improve")
d) Search in plain English without jargon
If a paper does the same thing under a different name, it's NOT novel.

**4. Rationalizing Overlapping Prior Work**
When you find similar work, do NOT rationalize minor differences as novelty. Two common traps:

FRAMEWORK PORTING: "Nobody did this in MY framework" — if the core mechanism exists in any context (different algorithm, different ensemble type, different field), porting it is engineering, not novelty.

GAP-FILLING: Papers A, B, C each cover variants → you propose the missing combination. An expert would say "obviously someone will do that eventually."

CHECK: Strip your idea to its core mechanism. Search if that mechanism exists ANYWHERE — any framework, any field, any algorithm family. If yes, ABANDON. Don't salvage by narrowing scope or listing "critical differences."

**5. Anchoring Bias**
Once invested in a direction, you'll unconsciously downplay overlap and inflate minor differences into "key differentiators." This feels like thoroughness but is actually defensiveness.

WARNING SIGNS: listing "critical differences" instead of reconsidering; reluctance to "waste" prior search effort; refining the SAME idea instead of exploring different ones; differentiators about context/framework rather than core mechanism.

CHECK: If you found even 1 paper with a similar core mechanism, ABANDON. The best hypotheses rarely come from your first direction. Each abandonment is progress.

**6. Relying on Search Snippets Without Fetching**
Search snippets are NOT enough to assess overlap or understand an approach. The actual mechanism and limitations are only in the full text.
CHECK: FETCH and read any potentially relevant result. Don't assess novelty from titles and snippets alone.

**7. Same-Neighborhood Pivoting**
Replacing one idea with a variant in the same conceptual space is NOT a genuine pivot. If all your directions are "[different adjective] + [same core concept]", you haven't actually explored.

CHECK: Would a single expert in that subfield have thought of ALL your directions? If yes, bring in a mechanism or framing from a completely unrelated field. That's where genuine novelty lives.
</common_mistakes_to_avoid>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<task_preview>
You will generate 1 novel groundbreaking research hypothesis in the AII prompt provided in the accompanying user message.
</task_preview>

<YOUR_AII_PROMPT>
Your AII prompt — the research prompt to invent within — is provided as a SEPARATE user message in this turn, immediately following this one. Treat that message as the definition of what to generate a hypothesis for.
</YOUR_AII_PROMPT>

<hypothesis_inspiration>
<YOUR_INSPIRATION>
Human researchers overspecialize — they know their domain deeply but lack breadth to see when other fields have already solved analogous problems. Your advantage is breadth. Only propose a cross-domain transfer if it concretely outperforms existing approaches in this domain. Avoid handwavy analogies — if the imported method is vaguer or weaker than what domain experts already use, it's not worth proposing.

Explore cross-domain inspiration at three levels, from abstract to concrete. At each level, consider both established and recent developments — with slight priority for newer work, which tends to leverage more powerful tools and be less widely known.

1. CONCEPTUAL: Borrow high-level ideas, framings, or design philosophies from distant fields.
   What mental model or approach from another domain suggests a novel angle on this problem?

2. PROCEDURAL: Adapt specific problem-solving processes from other domains.
   What workflow, iterative strategy, or pipeline used elsewhere could restructure how this problem is attacked?

3. METHODOLOGICAL: Import concrete methods directly from other fields with minimal modification.
   What algorithm, formula, or technique from a different domain applies here as-is or with adaptation?

Cast wide — draw from ANY field, not just these examples: ecology, economics, physics, linguistics, game theory, control theory, materials science, cognitive science, epidemiology. The best hypotheses often come from Level 2-3 transfers that experts in the field would never encounter.
</YOUR_INSPIRATION>
</hypothesis_inspiration>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>
</available_resources>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<YOUR_TASK>
Generate 1 novel groundbreaking research hypothesis in the AII prompt that is feasible with the above constraints.

<web_research_process>
Read and STRICTLY follow these skills: aii-web-tools.

1. DIVERGE: Brainstorm 5-7 diverse directions WITHOUT searching.
   Think across fields — what techniques from unrelated domains (ecology, economics, physics,
   linguistics, game theory, etc.) could inspire a novel mechanism? What assumptions does the field
   take for granted? Diversity matters more than depth here.

2. SEARCH: Web search for a high-level overview of each direction.
   What similar approaches exist? Is this genuinely novel or incremental? Remember: snippets
   are NOT enough for detailed understanding — treat search as discovery only.

3. FETCH & READ: MUST fetch any potentially relevant URL — you cannot assess novelty from
   snippets alone. Use the aii-web-tools skill:
   - fetch a page for high-level understanding of HTML pages
   - fetch_grep for exact details, methodology, or PDFs
   Prioritize recent papers closest to your idea. If you find significant overlap, PIVOT.

4. ADVERSARIAL NOVELTY CHECK: Actively try to DISPROVE novelty. Most important step.
   Run the FULL search checklist from <common_mistakes_to_avoid> mistake 3 — within-field
   rephrasings, cross-field core-mechanism search, failed/negative results, plain English.
   Ask: "Is the core insight of your hypothesis new, or known things in a new wrapper?"
   "Would an expert find this genuinely surprising?"
   MANDATORY SELF-CHECK: State the core mechanism in one sentence. Does it exist in ANY
   algorithm, framework, or field? If yes — even in a different framework — ABANDON.

5. FEASIBILITY CHECK: Verify your hypothesis is testable with provided resources. What specific data/compute/tools
   needed? All available within constraints?

6. ABANDON or PROCEED:
   ABANDON if: 2+ similar papers exist; you need to argue "critical differences"; core mechanism
   exists in any context.
   Abandoning is progress — go back to step 1 in a genuinely DIFFERENT direction (not a variant).
   PROCEED only if novelty is SELF-EVIDENT — an expert would immediately see it's new without
   explanation.

7. ITERATE: Expect to repeat steps 1-6 multiple times. The first few directions will likely be
   non-novel. This is normal. Don't settle for your first idea just because you've invested time.

<CRITICAL>We want SCIENTIFIC novelty (new mechanism, principle, or insight — the contribution is
knowledge), NOT application novelty (known methods applied to a new domain — the contribution is a
product). If an expert would say "clever engineering but known science," keep searching.
Hypothesis must be feasible within available resources.</CRITICAL>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>
</web_research_process>

Prioritize simplicity. Use concise, approachable language. The explanation should be fully self-contained.
</YOUR_TASK>

<previous_hypothesis>
Your hypothesis from the previous iteration. The reviewer evaluated it below.

hypothesis_id: gen_hypo_1
model: claude-opus-4-8
is_seeded: false
seeds: []
kind: hypothesis
title: >-
  Closure-Certified Composition (Arm-Scoped): Cross-Path Sound Narrowing Beats Path-Isolated Reasoning on Real Text, Iterated
  Closure Error-Corrects on Synthetic Networks, and an Empirically-Audited Recall-Bounded Redundancy Optimum -- for the Deduction
  Module of a Text-to-Logic Pipeline
hypothesis: |-
  LEAD -- THREE ARM-SCOPED CLAIMS, ONE GENUINE DISCONFIRMER EACH (read first; everything below only elaborates). (REAL-TEXT CLAIM) On the DEDUCTION-REQUIRED, multi-path subset of REAL TEXT, cross-path SOUND NARROWING (Mode A) achieves strictly higher SELECTIVE ACCURACY AT MATCHED COVERAGE -- coverage = resolution to a single relation, the SAME object for every method -- than Path-of-Thoughts AND self-consistency voting, gap CI-separated from zero under paired bootstrap; DISCONFIRMED if no such gap exists on that subset. (SYNTHETIC CLAIM) On synthetic long-hop / cyclic qualitative constraint networks, FULL ITERATED closure beats a NAIVE single-pass intersection with a gap that GROWS in hop-count and cyclomatic number, CI-separated; DISCONFIRMED if full == naive even on multi-hop/cyclic queries (then the contribution is 'any intersection,' not ITERATION). (REDUNDANCY CLAIM) At fixed per-edge recall, net Mode-A gain is an INVERTED-U in path redundancy whose peak location increases with recall and shifts outward under a recall-floor gate; the ONE genuine disconfirmer is the ABSENCE of any redundancy region whose net gain beats BOTH best-single-path and naive-intersection baselines -- a flat or turned-over curve alone is NOT a disconfirmation, it is the predicted recall x redundancy interaction.

  THE CRITICAL FIX THIS ITERATION -- ARM SCOPING DISSOLVES THE PRIOR INTERNAL CONTRADICTION. The previous version asked Mode A to beat naive single-pass intersection ON REAL TEXT, while ALSO predicting full-closure == naive-intersection at length-2; since the real-text held-out-edge construction (hide one edge of a local event cluster, recover it from >=2 constraining paths) is structurally the length-2 / acyclic (theta) regime, those two clauses contradicted. We RESOLVE this by SPLITTING the headline by arm and stating the tie out loud: on the real-text arm Mode A is PREDICTED TO TIE naive intersection (one pass already equals the fixpoint for a query edge in an acyclic theta), so the real-text win is claimed ONLY over PATH-ISOLATED reasoning (Path-of-Thoughts reasons each path independently and, when paths disagree, emits multiple relations without intersecting or abstaining) and over answer-VOTING (which cannot see that individually-popular composition steps are jointly inconsistent). The strict 'beats naive single-pass intersection, attributable to ITERATED closure' claim is reserved for the SYNTHETIC long-hop/cyclic arm, where iteration to a fixpoint with algebra-seeded converse propagation provably adds value a single pass cannot. We additionally report the prevalence of >=3-edge / cyclic constraint structures in the real corpus and, where they exist, run full-vs-naive there too -- but the headline does not depend on it.

  T0 -- A-PRIORI ENVELOPE GATE (zero LLM spend, runs FIRST, gates whether a real-text headline exists at all). Before any model call, from the MATRES gold graph ALONE we compute the count N* of held-out edges that SIMULTANEOUSLY: (i) satisfy a structural deduction-required PROXY -- their two events share NO local/adjacent-sentence span, so the relation cannot be read off one place; (ii) are constrained by >=2 paths through distinct intermediate events; (iii) have convex point-algebra GOLD compositions that are non-universal (retain bite) AFTER the non-convex {<,>}->VAGUE widening; and (iv) whose cross-path intersection equals the gold singleton. We report N*, the candidate count DESTROYED by the {<,>}->VAGUE widening, and a paired-bootstrap POWER calculation (minimum n for CI-separation at the pilot-anticipated effect). This converts the previously pilot-deferred 'tiny envelope' risk into an up-front, computable go/no-go. PRE-REGISTERED ESCALATION LADDER keyed to N*: if MATRES N* powers the CI -> MATRES (direct human start-point gold, convex point algebra where PC is COMPLETE) is the real-text primary; if too thin -> escalate to a DENSE, DIRECT-human-gold corpus (NarrativeTime: timeline-based annotation with full TLink coverage, MORE links than TimeBank-Dense, human-placed rather than closure-built -- so recovering a held-out edge by closure is NOT circular, unlike TimeBank-Dense whose non-adjacent gold is SputLink output) whose deduction-required multi-path envelope is structurally far larger; if STILL insufficient -> the SYNTHETIC arm becomes the headline and real text is demoted to an honestly-scoped 'niche safety-net' boundary. The paper's headline is therefore never contingent on an unmeasured quantity.

  MODE A -- SOUND NARROWING (PRIMARY, zero-false-positive, over-commitment-ROBUST). The LLM emits, per text span, a high-recall 'sound-but-loose' DISJUNCTIVE set of base relations the span does NOT exclude (with an explicit underdetermined/universal option). When these sets are SOUND (gold inside each) but sub-universal, intersecting the compositions that arrive at a query pair from MULTIPLE constraining paths yields a set that STILL contains gold yet is strictly tighter than any single path. We report TWO yields and name the load-bearing one: (i) STRICT-TIGHTENING yield (any reduction, e.g. 5->3) and (ii) the HEADLINE-DRIVING SINGLETON-RESOLUTION-TO-CORRECT yield (intersection collapses the query to the single correct relation). Because the matched-coverage axis is single-relation resolution, only (ii) moves answered-point selective accuracy, so the headline number is the singleton-resolution yield. Mode A requires only sub-universal edge BREADTH + MULTI-PATH BITE (>=2 non-universal constraining paths) and SOUND inputs; it does NOT require over-commitment, is SAFEST at the high-recall end of the elicitation knob, and is inert ONLY in the degenerate all-universal limit.

  MODE B -- DETECTION/REPAIR (SECONDARY, Tier-2, zero-FP DETECTION conditional on measured recall). An empty closure collapse is a deductive certificate that some LLM edge is UNSOUND, with no gold labels; it requires at least one over-committed/recall-failed edge to fire and carries the pre-registered DUAL of SILENT WRONG NARROWING (an unsound set that OMITS gold drives closure to a confident WRONG singleton with NO collapse). Magnitude tracks the measured over-commitment rate; reported distinctly from Mode A.

  REDUNDANCY IS DOUBLE-EDGED -- NOW AUDITED ON EMPIRICAL JOINT SOUNDNESS, NOT AN INDEPENDENCE PRODUCT (the second key fix). Mode A's zero-FP narrowing holds only when EVERY contributing edge is sound. We NO LONGER assume independent per-edge soundness (a single LLM reading one document produces positively-correlated reading errors). Instead of the product prod_e r_e we MEASURE the EMPIRICAL joint soundness J(E) = realized fraction of E-edge constraining subnetworks in which ALL edges are sound, directly from data, and we report the within-document cross-edge reading-error correlation rho. The zero-FP audit's reliability curve is pre-registered against EMPIRICAL J(E), not r^E; the inverted-U cost term is 1 - J(E); and because positive rho makes J(E) decay SLOWER than r^E, the predicted peak sits FURTHER out than an independence model would say. We pre-register the attribution rule for a reliability slope != 1: an offset that DISAPPEARS when the predictor is switched from r^E to empirical J(E) is the independence approximation failing (NOT a disconfirmation of the mechanism); an offset that PERSISTS under empirical J(E) is a genuine soundness failure. Net Mode-A gain therefore RISES while marginal narrowing dominates, then FALLS once (1 - J(E)) silent-narrowing cost dominates -- an error-correcting code's OPTIMAL RATE, with the decoding radius set by recall and the channel correlation measured, not assumed.

  ITERATED-CLOSURE ISOLATION (so the synthetic win is not 'any intersection'). A NAIVE-INTERSECTION baseline intersects the compositions arriving at the query pair in a SINGLE pass, WITHOUT iterating to a fixpoint and WITHOUT algebra-seeded converse propagation. On length-2 multi-path queries naive-intersection and full closure COINCIDE (we predict and verify no gap, including on the real-text arm); on longer/cyclic networks iterated fixpoint propagation is the distinguishing ingredient, so the full-closure-minus-naive gap GROWS with hop-count and cyclomatic structure -- localizing the synthetic contribution to ITERATED path consistency.

  DEDUCTION-REQUIRED ENVELOPE + REAL-TEXT DECOMPOSITION ANCHOR (third fix to the rigor critique). A LOCAL-ONLY READER probe predicts each held-out edge from ONLY the minimal local span(s) where its two events co-occur (or a 'no-shared-span' flag), classifying each edge DIRECTLY-READABLE vs DEDUCTION-REQUIRED; we foreground the deduction-required fraction, stratify the headline by it, and draw the primary subset PREFERENTIALLY from non-locally-stated triangles. CRUCIALLY, we do NOT report the load-bearing redundancy decomposition on synthetic data alone: we ALSO estimate coarse Mode-A benefit and silent-narrowing-cost curves directly on REAL sub-networks binned by contributing-edge count / hop-count, and check the qualitative inverted-U against the synthetic curve. The realism-matching statistic is EXTENDED beyond marginal error-type TV-distance to ALSO match (a) the cross-edge error CORRELATION rho and (b) the redundancy / path-topology distribution (contributing-edge-count and cycle-structure histograms) -- because those, not the marginals, set the peak; all thresholds fixed before generating the curve.

  ESTIMATION-PRECISION PRE-REGISTRATION (so the inverted-U is falsifiable, not retro-fit). >=4 fixed per-edge-recall levels (e.g. .70/.80/.90/.95), >=500 synthetic networks per (recall x redundancy) cell, and a minimum-detectable peak SHIFT of >=1 redundancy bin between adjacent recall levels. A 'located peak' counts as CONFIRMED only if the peak bin's net gain is CI-ABOVE both neighbors AND the peak-vs-recall monotonicity clears the >=1-bin shift; otherwise the prediction is reported as merely 'directionally consistent,' not confirmed.

  HONESTY COMMITMENTS + READER-AGNOSTICITY. (1) zero-FP for Mode A = the intersected set still contains gold whenever ALL contributing inputs are sound -- audited against the EMPIRICAL joint-soundness J(E), not an independence product; (2) zero-FP for Mode B is scoped to DETECTION only -- minimal-hitting-set localization/repair can blame the wrong edge; (3) path consistency is SOUND-BUT-INCOMPLETE for full Allen IA and RCC-8 (consistency is NP-complete; COMPLETE only for the convex point algebra and ORD-Horn), so the closure-detectable hallucination rate is a LOWER BOUND while the real-text PRIMARY arm is the convex point algebra where it is exact; (4) silent wrong narrowing is pre-registered, bounded per-edge by (1-recall) and per-network by (1 - J(E)), and tested with a recall-floor gate. Finally the gain must be reader-AGNOSTIC: an ALTERNATIVE disjunctive edge-reader (a METRE-style multi-label 'Vague-as-disjunction' head, and a second LLM/prompt family) fed into the SAME closure pipeline preserves the cross-path-closure gain -- showing the win is in the ALGEBRA, not the elicitation.
motivation: >-
  Faithful multi-hop relational reasoning over short professional text -- temporal ordering of events in news, kinship in
  narratives, containment/region relations in descriptions -- is where LLM hallucination is most damaging and where a text-to-logic
  pipeline most needs to fuse explicit document facts with implicit composition knowledge while staying auditable. The umbrella
  pipeline reads text into FOL/Prolog predicates, types entities against an upper ontology, and answers queries with a reasoner;
  the WEAK LINK is the composition/deduction step. Existing systems handle composition unsatisfyingly: humans hand-craft composition
  rules (the kinship rules behind CLUTRR), which do not scale; the LLM composes freely, locally fluent but globally inconsistent,
  producing silent errors that solver-crash feedback (Logic-LM) and answer voting (LINC) cannot see; or paths are reasoned
  in ISOLATION (LAMBADA, Path-of-Thoughts), which deliberately avoids the global check and so cannot tighten a disjunctive
  query by intersecting evidence from multiple paths nor detect contradictions arriving at the same pair from two paths. A
  cluster of negative/commit-contract results sharpens the opportunity: Knez & Sun (2024, arXiv:2406.11486) show zero-shot
  LLMs assign MORE THAN ONE temporal relation to a pair for >=50% (up to 97%) of pairs and violate transitivity, then enforce
  consistency with ILP and find it DOES NOT improve F1; and -- decisively up to date -- a 2025 global zero-shot temporal-graph
  generator (arXiv:2502.11114, EMNLP 2025) STILL enforces uniqueness/symmetry/transitivity by ILP, committing to a single
  label per pair, preserving no disjunction, issuing no certificate, and offering no abstention. We read this lineage as evidence
  that consistency enforcement under the F1-maximizing COMMIT contract is the wrong objective; the LLM's native multi-relation
  output is not noise to be collapsed but a SOUND DISJUNCTION to be PRESERVED and NARROWED, and the right objective is faithfulness-by-abstention,
  not extraction F1. The qualitative-reasoning community has had exact, commodity-cheap path-consistency algorithms over relation
  algebras (Allen 1983; Renz & Nebel; GQR, SparQ) for forty years, but they assume a clean hand-given table and have never
  been coupled to an LLM reading relations off natural language. We are NOT the first to run closure over machine-extracted
  temporal relations (SputLink densifies TimeBank; CAEVO does global temporal inference via cascaded sieves; Ning et al.'s
  ILP enforces transitivity) -- but ALL COMMIT to a single consistent labeling to maximize F1, preserving no disjunction,
  certifying no reading error, offering no abstention. Our contribution is the OPPOSITE output contract: keep the LLM's job
  as high-recall disjunctive READING, use cross-path INTERSECTION as a zero-FP faithfulness operation (Mode A) and closure
  COLLAPSE as a gold-free reading-error certificate (Mode B), and optimize faithfulness via a risk-coverage objective. Three
  ideas make the transfer a genuine contribution rather than a port. FIRST, because Allen/point/RCC-8 tables are EXACT ground
  truth, cross-path intersection of SOUND sets can only move toward gold -- a calibration-free, zero-FP narrowing that needs
  no over-commitment and no labels, and multi-path redundancy becomes an ERROR-CORRECTING CODE over LLM extractions. SECOND
  -- the iteration's sharpening, now made rigorous -- the coding-theory lens predicts an OPTIMAL RATE: since narrowing stays
  zero-FP only while all contributing edges are sound and that JOINT probability (measured EMPIRICALLY as J(E), not assumed
  independent) decays with redundancy, net benefit is an INVERTED-U whose peak we predict from measured recall and the measured
  cross-edge error correlation and shift with a recall-floor gate. THIRD, the objective inverts F1 -- we preserve disjunctive
  uncertainty and ABSTAIN, trading coverage for faithfulness, and we measure the ACTIONABLE yield (intersection-to-correct-singleton
  at matched coverage), not whether a set merely shrank. Recent QSTR evaluations show frontier LLMs are good at SINGLE-STEP
  composition (QSTRBench ~98% on Allen-interval composition for the best model) yet do not PROPAGATE constraints across paths,
  and a temporal-constraint study (Marin 2025) finds even simple before/during relations applied brittlely, explicitly calling
  for hybrid symbolic modules. To keep the contribution honest about its REACH, we (a) compute the deduction-required, multi-path-with-bite
  envelope A PRIORI from the gold graph and gate the real-text headline on it, and (b) demonstrate end-to-end hallucination
  reduction on at least one subset where the deduced relation is genuinely ABSENT from local text (the deduction-required
  MATRES/NarrativeTime stratum; CLUTRR multi-hop as a Tier-2 echo). If it works, this is a general, training-free recipe for
  trustworthy relational deduction over text with quantified, certificate-backed hallucination reduction and replayable trace-graphs;
  if it fails (intersection rarely resolves correct singletons because real sets are near-universal; the redundancy peak sits
  at trivially low redundancy; recall failures dominate the joint-soundness bound; or the deduction-required multi-path-with-bite
  slice is too thin to power a CI), each is itself a publishable scope boundary on repairing LLM-read relational knowledge.
assumptions:
- >-
  ARM-SCOPED CLAIMS (resolving the prior internal contradiction). The contribution is split by arm and the predicted real-text
  TIE with naive intersection is stated out loud. REAL-TEXT arm: cross-path SOUND NARROWING (Mode A) beats PATH-ISOLATED reasoning
  (Path-of-Thoughts) and answer-VOTING at matched coverage on the deduction-required multi-path subset, and is PREDICTED ONLY
  TO TIE a naive single-pass intersection there (length-2 / acyclic theta regime where one pass equals the fixpoint). SYNTHETIC
  arm: FULL ITERATED closure beats NAIVE single-pass intersection with a gap growing in hop-count / cyclomatic number -- the
  strict 'beats naive, attributable to ITERATION' claim lives here, never on the real-text headline.
- >-
  REDUNDANCY IS DOUBLE-EDGED, AUDITED ON EMPIRICAL JOINT SOUNDNESS (no independence assumption). Mode A's zero-FP narrowing
  holds only when ALL contributing edges are sound. We do NOT assume independent per-edge soundness; we MEASURE the empirical
  joint soundness J(E) = realized fraction of E-edge subnetworks with all edges sound, and report the within-document cross-edge
  reading-error correlation rho. Net Mode-A gain is an INVERTED-U in redundancy at fixed recall, with the cost term 1 - J(E)
  and the peak located using empirical J(E); positive rho pushes the peak outward relative to an independence model. A flat/non-monotone
  curve is the predicted recall x redundancy interaction, not a disconfirmation. The zero-FP reliability audit is pre-registered
  against empirical J(E), with a stated rule separating an independence-approximation offset (vanishes under J(E)) from a
  genuine soundness failure (persists).
- >-
  A-PRIORI ENVELOPE GATE + ESCALATION LADDER (the real-text headline is contingent on a COMPUTABLE quantity, decided before
  LLM spend). From the gold graph alone we count N*, the held-out edges that are deduction-required (no shared local span),
  multi-path (>=2 distinct constraining paths), bite-retaining after non-convex->VAGUE widening, and singleton-resolving to
  gold; we report N*, widening-induced bite loss, and a paired-bootstrap power calculation. The real-text primary is MATRES
  if N* powers the CI; else escalate to a dense direct-human-gold corpus (NarrativeTime, non-circular unlike closure-built
  TimeBank-Dense non-adjacent gold); else the synthetic arm is the headline and real text is an honestly-scoped niche boundary.
- >-
  SCOPE/MODULE FRAMING + EXACT-TABLE primacy with point-algebra COMPLETENESS for the real-text PRIMARY. The target reasoning
  is RELATIONAL and COMPOSITIONAL (relation between a pair obtained by composing base relations along graph paths: temporal,
  spatial containment/region, kinship); this is the deduction MODULE of a text-to-logic pipeline, not a replacement for it
  (RuleTaker propositional chaining is out of scope, used as a contrastive negative). 'Mathematical ground truth' applies
  cleanly to synthetic Allen/point/RCC-8 AND to the real-text MATRES arm, whose BEFORE/AFTER/EQUAL/VAGUE start-point labels
  instantiate the CONVEX POINT ALGEBRA where path-consistency is provably COMPLETE and the table exact; TimeBank-Dense's 6-label
  scheme is a designed coarsening (SputLink/CAEVO convex table, cited verbatim, ~43% VAGUE caps narrowing -- reported). The
  LLM is NEVER asked to supply the composition table for any primary setting; LLM-elicited tables are studied only as a CLUTRR/kinship
  Tier-2 ablation against a gold table.
- >-
  ACTIONABLE-YIELD = SINGLETON-RESOLUTION-TO-CORRECT, AND READER-AGNOSTICITY. The matched-coverage win is driven by intersection-to-correct-SINGLETON,
  not by mere strict tightening; the coverage axis is single-relation resolution applied IDENTICALLY to closure and every
  baseline, so the comparison cannot be conflated with 'closure has a better-calibrated abstain.' We report strict-tightening
  and singleton-resolution yields separately and state singleton-resolution is load-bearing. The gain is attributable to the
  ALGEBRA: swapping the disjunctive edge-reader (LLM prompt -> METRE-style trained multi-label head -> a second LLM) into
  the SAME closure pipeline preserves the cross-path-closure gain at comparable per-edge recall.
investigation_approach: |-
  TIERING (pre-committed; T0 then Tier-1 must COMPLETE before Tier-2; a fully-executed T0+Tier-1 with a thin Tier-2 is the acceptable minimum publishable unit). T0 -- A-PRIORI ENVELOPE GATE (zero LLM spend): from the MATRES gold graph compute N* (deduction-required AND >=2-path AND bite-after-widening AND singleton-resolving), the widening-induced bite loss, the prevalence of >=3-edge/cyclic structures, and a paired-bootstrap power calc; decide the real-text primary via the escalation ladder (MATRES -> NarrativeTime dense direct-gold -> synthetic-primary). TIER-1 (headline-critical): (T1) the RECALL-BITE FRONTIER map + pre-registered go/no-go; (T2) the real-text Mode-A comparison vs Path-of-Thoughts and self-consistency (NOT vs naive-intersection, which is predicted to tie) at MATCHED COVERAGE with paired-bootstrap CIs, stratified by deduction-required vs directly-readable; (T3) the SYNTHETIC long-hop/cyclic redundancy-scaling DECOMPOSITION separating Mode-A BENEFIT from silent-narrowing COST, locating the inverted-U peak, conditioning the zero-FP audit on EMPIRICAL J(E), AND a coarse REAL-TEXT decomposition anchor binned by contributing-edge count; (T4) the isolating ablations -- closure ON/OFF table-held-fixed, Mode-A-only, and NAIVE-INTERSECTION vs FULL ITERATED closure with hop/cyclomatic stratification (the synthetic 'beats naive' claim). TIER-2 (runs only after Tier-1): RCC-8 second algebra, CLUTRR elicited-table ablation + absent-relation end-to-end demo, TimeBank-Dense (framed noisy-read-vs-clean-read), Mode-B repair quality, the METRE-style alternative-reader ablation, exploratory semiring variant.

  COMPACT LOGICAL STRUCTURE (claim -> precondition -> metric -> baseline -> CI test). [C1a REAL-TEXT HEADLINE] Mode-A singleton-resolution-to-correct > PoT & self-consistency (ties naive-intersection) -> precondition: real-text deduction-required multi-path-with-bite subset with N* powering the CI (from T0) -> metric: selective accuracy at matched coverage (coverage = single-relation resolution) -> baselines: PoT (path-agreement abstain), self-consistency (vote margin) -> paired-bootstrap CI on the gap, separated from 0. [C1b SYNTHETIC ITERATION HEADLINE] full closure > naive-intersection, gap grows with hop/cyclomatic -> precondition: synthetic paths longer than 2 / cycles present -> metric: selective-accuracy gap vs hop-count bin -> baseline: naive single-pass intersection -> bootstrap per-bin gap + monotone-trend test. [C2 PATH-CONSISTENCY] closure ON > OFF, table held FIXED -> precondition: multi-path -> metric: selective accuracy -> baseline: closure-OFF same table -> paired bootstrap. [C3 ZERO-FP AUDIT, EMPIRICAL] realized fraction-still-contains-gold tracks EMPIRICAL J(E) -> precondition: per-edge soundness + cross-edge correlation measured -> metric: reliability curve vs empirical-joint-soundness bin -> slope ~1; attribution rule for slope!=1 pre-registered. [C4 REDUNDANCY OPTIMUM] net gain inverted-U with located peak; peak increases with recall; gate shifts it -> precondition: fixed per-edge-recall arms + estimation-precision pre-reg -> metric: separate benefit and cost curves vs redundancy on SYNTHETIC and a coarse REAL anchor -> peak-detection + CIs meeting the >=1-bin shift bar. [C5 READER-AGNOSTIC] closure gain persists when edge-reader swapped -> precondition: alternative reader at comparable recall -> paired bootstrap, gains overlap. [C6 MODE-B] zero-FP DETECTION; repair toward gold -> precondition: non-trivial over-commitment rate -> metric: FP-flag rate, toward-vs-away movement -> bootstrap.

  PILOT AS A FRONTIER MAP (after T0, before main runs). On synthetic and real edges, SWEEP a prompt-elicited breadth knob across >=5 settings from 'name THE relation' to 'name the maximal SOUND set the text does not exclude.' At each setting MEASURE: (a) per-edge RECALL = P(gold in emitted set); (b) breadth distribution; (c) over-commitment vs under-specification rate; (d) raw closure-collapse rate; (e) strict-tightening AND singleton-resolution-to-correct yields; (f) local-only reader accuracy defining the deduction-required fraction; and (g) the within-document cross-edge reading-error correlation rho. PLOT the RECALL-BITE FRONTIER as a primary deliverable and pre-register go/no-go (a region clearing a recall gate AND non-trivial singleton-resolution-to-correct) BEFORE any main run. PRE-REGISTER the EXTENDED REALISM-MATCHING STATISTIC: total-variation distance between real and synthetic per-edge error-type distributions PLUS a cross-edge error-CORRELATION (rho) match term PLUS a redundancy/path-topology match (contributing-edge-count and cycle-structure histograms), with thresholds FIXED before generating the redundancy-scaling curve.

  PIPELINE (four stages). (1) NEURAL READING -- prompt the LLM to map each surface relation phrase onto a SOUND DISJUNCTION of canonical base relations at the pre-registered frontier operating point; for the MATRES point-algebra arm restrict emitted vocabulary to CONVEX point relations (widen non-convex {<,>} to VAGUE) so PC stays COMPLETE, and MEASURE the bite lost. (2) ALGEBRA -- use the EXACT published composition table (Allen 13-relation, point algebra, RCC-8; SputLink/CAEVO convex table for TB-Dense); seed converses/identity from the algebra, never from an LLM. (3) SYMBOLIC CLOSURE -- build a QCN (nodes=events/entities, edges=relation SETS; query/held-out edge starts universal), run path-consistency to a FIXPOINT. Three instrumented variants: FULL iterated PC; NAIVE single-pass intersection at the query node (no fixpoint, no converse seeding); closure-OFF (table fixed). MODE A narrows by cross-path intersection and emits an answer ONLY when the query resolves to a single relation (coverage axis), else ABSTAINS. MODE B (Tier-2): an empty collapse CERTIFIES a reading error; compute a minimal Reiter-style hitting-set/MaxSAT repair preferring lowest-confidence edges, recording the diagnosis and flagging possible mislocalization. (4) AUDIT -- emit the QCN, which compositions fired on which paths, and repairs as a TRACE-GRAPH, optionally discharged in SWI-Prolog/ASP from the closed table for a replayable proof (connective tissue to the umbrella pipeline's auditability + quantified-hallucination-reduction requirements).

  DATASETS. SYNTHETIC PRIMARY (clean ground truth, controlled redundancy): a Renz-Nebel-style random consistent Allen/point QCN generator that GUARANTEES redundant paths/cycles and sweeps redundancy/density/hop-count INDEPENDENTLY; the NL-realization protocol (a fixed library mapping each base relation to graded clean->ambiguous paraphrases) is VALIDATED to clear the EXTENDED realism-matching statistic (marginals + correlation + topology), and the redundancy DECOMPOSITION is reported at the realism-matched setting and at >=4 FIXED per-edge-recall levels with >=500 networks per cell (so the inverted-U peak vs recall is observed at the pre-registered precision). REAL-TEXT PRIMARY: MATRES (Ning, Wu & Roth 2018; ~275 news docs, ~13.6k pairs) as a HELD-OUT-EDGE NARROWING arm -- locally-redundant event clusters where >=2 human-annotated convex point edges constrain a HIDDEN human-annotated edge; gold is DIRECT human start-point annotation (IAA .84), same scheme, NOT closure-built. Edges classified directly-readable vs deduction-required via the local-only reader; primary subset drawn preferentially from deduction-required triangles. DENSE FALLBACK (selected by T0): NarrativeTime (dense timeline-based human annotation, full TLink coverage, more links than TimeBank-Dense, non-circular direct gold) when MATRES N* is too thin; TimeBank-Dense as a Tier-2 noisy-read-vs-clean-read arm. RCC-8 synthetic gives a second algebra; CLUTRR is the kinship venue for the ELICITED-table ablation plus a mined/synthesized multi-path subset doubling as the end-to-end hallucination-reduction-on-ABSENT-relation demonstration; RuleTaker is an out-of-scope contrast.

  KEY ABLATIONS: (i) closure/intersection ON vs OFF with the table HELD FIXED (isolates path consistency from 'a fixed table exists' -- the DSR-LM contribution); (ii) NAIVE single-pass intersection vs FULL iterated closure with hop/cyclomatic stratification (isolates ITERATION; the SYNTHETIC 'beats naive' claim); (iii) Mode A ONLY vs Mode A+B; (iv) disjunction OFF (force singletons -- tests the sound-but-loose claim); (v) exact-table vs LLM-elicited-table (kinship); (vi) recall-floor gate ON vs OFF (tests suppression of silent wrong narrowing AND its effect on the redundancy peak); (vii) ALTERNATIVE EDGE-READER (METRE-style multi-label head + a second LLM into the SAME closure pipeline -- reader-agnosticity). BASELINES, EACH WITH A MATCHED ABSTENTION SIGNAL thresholded to the SAME coverage object: raw LLM (verbalized confidence), CoT (verbalized confidence), self-consistency (vote margin), LINC-style multi-formalization vote, DSR-LM-style induced-rule Prolog (no closure), Path-of-Thoughts (PRIMARY real-text baseline; path-agreement abstain), NAIVE single-pass intersection (synthetic iteration contrast), a TempRel-style COMMIT baseline, and a soft-unification neural theorem prover.

  METRICS, per-regime and STRATIFIED (single- vs multi-path; single- vs disjunctive-query; directly-readable vs deduction-required): (1) SINGLETON-RESOLUTION-TO-CORRECT yield + risk-coverage / selective accuracy AT MATCHED COVERAGE (HEADLINE) with paired-bootstrap CIs vs each baseline, reported alongside strict-tightening yield with an explicit statement that (1) is load-bearing; (2) empirical zero-FP audit CONDITIONED on EMPIRICAL J(E) (reliability curve, slope ~1; cross-edge rho reported); (3) REDUNDANCY DECOMPOSITION -- separate Mode-A benefit and silent-narrowing cost curves vs redundancy/hop-count at fixed recall on SYNTHETIC plus a coarse REAL anchor, located peak, recall-floor-gate shift, meeting the estimation-precision bar; (4) full-closure-minus-naive-intersection gap vs hop-count/cyclomatic (SYNTHETIC); (5) Mode-B detection (closure-detectable hallucination rate, SECONDARY, lower bound on Allen IA/RCC-8, exact on point algebra) with gold-wrong non-abstained predictions decomposed into collapse-caught / silent-wrong-narrowing / invisible-single-chain; (6) repair quality (toward- vs away-from-gold, CI-separated); (7) reader-agnostic closure delta under each edge-reader; (8) APPLICABILITY ENVELOPE -- relation-composable, multi-path-with-bite, AND deduction-required fractions per corpus (N* from T0 reported up front); (9) atomic extraction P/R as a HELD-FIXED control; (10) end-to-end hallucination-rate reduction vs raw LLM on the deduction-required/absent-relation subset. All LLM calls go through OpenRouter; cost stays well under $10 via short documents, caching, and a cheap extraction model; closure and repair run in milliseconds per network on a laptop.
success_criteria: |-
  THREE ARM-SCOPED HEADLINE PREDICTIONS (each falsifiable; stated before all qualifiers). (REAL-TEXT) On the deduction-required, multi-path-with-bite subset at realism-matched difficulty and the pre-registered frontier operating point, Mode A achieves strictly higher SELECTIVE ACCURACY AT MATCHED COVERAGE (coverage = single-relation resolution, the SAME object for every method) than Path-of-Thoughts AND self-consistency voting, gap CI-separated from zero under paired bootstrap, driven by SINGLETON-RESOLUTION-TO-CORRECT (not strict tightening); Mode A is PREDICTED TO TIE naive single-pass intersection here and we report that tie as a confirmation of the length-2 prediction, NOT as a failure. (SYNTHETIC) On long-hop/cyclic QCNs, FULL ITERATED closure beats NAIVE single-pass intersection with the gap GROWING in hop-count/cyclomatic number (and ~0 on length-2), CI-separated -- the iteration win. (REDUNDANCY) Net Mode-A gain is an INVERTED-U whose peak location increases with measured recall and shifts outward under the recall-floor gate, established at the pre-registered estimation precision (>=4 recall levels, >=500 networks/cell, >=1-bin minimum-detectable peak shift, peak bin CI-above both neighbors). CONFIRMS if, in addition: (1) T0 reports N* (and post-widening N*) large enough to power the real-text CI (go/no-go met) OR the escalation ladder cleanly selects a corpus that does, AND the frontier map shows a region clearing the recall gate with non-trivial singleton-resolution-to-correct; (2) the empirical zero-FP audit holds when conditioned on EMPIRICAL J(E) (realized fraction-still-contains-gold tracks the measured joint quantity, slope ~1), with the cross-edge correlation rho reported and any slope!=1 correctly attributed (offset vanishing under J(E) = independence-approx, not disconfirmation; persisting = genuine soundness failure); (3) the coarse REAL-TEXT redundancy anchor is qualitatively consistent (same inverted-U sign) with the synthetic decomposition; (4) at least ONE real-text arm (MATRES deduction-required preferred, NarrativeTime dense fallback acceptable) clears the pre-registered deduction-required multi-path-with-bite threshold so the headline is genuine deduction, not re-reading; (5) the disjunction-ON variant beats commit-to-singleton; (6) the cross-path-closure gain is READER-AGNOSTIC. SECONDARY (Tier-2, Mode B, magnitude tracks over-commitment, reported distinctly): conditional on pilot-measured per-edge recall, closure produces ZERO false-positive DETECTION flags; repairs move the query edge toward gold significantly more often than away (CI-separated, weaker localization claim); end-to-end hallucination rate on the deduction-required/absent-relation subset drops vs raw LLM. APPLICABILITY ENVELOPE (pre-registered significance bar): we report relation-composable, multi-path-with-bite, AND deduction-required fractions and pre-register the threshold distinguishing a 'significant general mechanism' from a 'niche safety-net with low yield.'

  DISCONFIRMS / SCOPES if: (REAL-TEXT) no singleton-resolution-to-correct advantage over Path-of-Thoughts OR voting at matched coverage on the deduction-required multi-path-with-bite subset even when sound sets are sub-universal and bite exists; (SYNTHETIC) the full-closure-minus-naive gap is ~0 even on multi-hop/cyclic queries (the win is 'any intersection,' not iteration); (REDUNDANCY) the SINGLE genuine disconfirmer -- the ABSENCE of any net-positive redundancy region beating both best-single-path and naive-intersection baselines (a turned-over or flat curve ALONE is NOT a disconfirmation, it is the predicted recall x redundancy interaction); or T0/the frontier shows NO corpus with both adequate recall and a deduction-required multi-path envelope large enough to power the CI (then the contribution is honestly scoped to synthetic + niche-safety-net). PRE-REGISTERED HONEST FAILURE MODES (each a publishable scope boundary): (a) NEAR-UNIVERSAL UNDER-SPECIFICATION -- sets effectively universal, intersection cannot resolve singletons (Mode A inert); the ONLY under-specification outcome that disconfirms Mode A; (b) CONSISTENT-BUT-WRONG elicited table -- shown only in kinship, quantified vs gold, shown NOT to arise in exact-table settings; (c) INVISIBLE hallucinations -- confident self-consistent single-chain errors closure cannot see; (d) SILENT WRONG NARROWING -- an UNSOUND set that omits gold drives closure to a confident WRONG singleton with NO collapse; rate bounded per-edge by (1-recall) and per-network by (1 - J(E)), suppressed by the recall-floor gate which also shifts the redundancy peak; (e) TINY ENVELOPE -- N* below the bar even after escalation, scoping the contribution to synthetic + niche safety-net. Throughout, 'zero false-positive' is stated separately for Mode A (intersected set still contains gold under JOINT-sound inputs, audited against EMPIRICAL J(E)) and Mode B (DETECTION only); the closure-detectable hallucination rate is a LOWER BOUND because PC is incomplete for Allen IA/RCC-8 (complete only for the convex point-algebra real-text arm). Atomic extraction P/R must remain comparable to baselines, the per-corpus fractions (including the a-priori N*) must be reported up front, and trace-graphs must be judged human-auditable.
related_works:
- >-
  Global Zero-shot Temporal Graph Generation (2025, arXiv:2502.11114; EMNLP 2025 main): prompts an LLM to generate a whole
  temporal graph (free-form timeline then all-pair classification), aggregates M=5 generations, then enforces uniqueness/symmetry/transitivity
  with ILP using Allen's transitivity laws. MOST RECENT directly-relevant prior art. Difference: it COMMITS to a single deterministic
  label per pair, preserves NO disjunction, intersects NO compositions across paths, issues NO gold-free certificate, and
  does NOT abstain -- the same F1-maximizing COMMIT contract we invert. Its 2025 existence shows the field STILL collapses
  LLM multi-relation output rather than preserving it as a sound disjunction to be narrowed; we read it as fresh motivation
  for the opposite output contract.
- >-
  Knez & Sun 2024 (arXiv:2406.11486): zero-shot LLMs assign MORE THAN ONE relation to a pair for >=50% (up to 97%) of pairs
  and violate uniqueness/transitivity; the authors ENFORCE consistency with ILP and find it DOES NOT improve F1. Closest recent
  analysis. Difference: it enforces consistency under the F1-maximizing COMMIT contract (which it shows fails); no closure-as-CERTIFICATE,
  no preserved disjunction, no abstention/risk-coverage, no cross-path zero-FP narrowing. We read its negative result as motivation:
  PRESERVE the multi-relation output as a sound disjunction and NARROW it, optimizing faithfulness-by-abstention.
- >-
  Hu, Huang & Feng 2024 (arXiv:2408.07353, METRE): a TRAINED multi-LABEL classifier inferring the possibility of each temporal
  relation independently, treating VAGUE as >1 possible relation, on TB-Dense/MATRES/UDS-T. Directly relevant to our sound-but-loose
  disjunctive labeling. Difference: METRE is a trained per-pair classifier predicting a label-set to maximize F1; it does
  NOT carry the set through an EXACT composition table across MULTIPLE paths, performs no cross-path intersection, issues
  no certificate, and does not abstain. CRUCIALLY, because METRE produces disjunctive sets on the SAME corpora, we use it
  as an ALTERNATIVE EDGE-READER into the SAME closure pipeline (Tier-2) to show the cross-path-closure gain is reader-AGNOSTIC
  -- the win is the algebra, not the LLM elicitation.
- >-
  Temporal-relation extraction with ILP global inference (Ning, Feng & Roth 2017, EMNLP; CogCompTime): a TRAINED extractor
  produces per-pair scores and ILP enforces transitivity + symmetry to output a single globally-consistent labeling. Closest
  classic prior art for 'enforce qualitative consistency on machine-extracted temporal relations.' Differences: (1) it COMMITS
  to one relation per pair for F1; we PRESERVE disjunction, NARROW by cross-path intersection, and ABSTAIN (opposite contract);
  (2) it uses LEARNED scores + approximate optimization; we use the EXACT table so intersection is sound and collapse is a
  gold-free DETECTION certificate (conditional on recall); (3) it needs a trained per-corpus model; our reader is an untrained
  LLM that generalizes across algebras.
- >-
  SputLink (Verhagen 2004/2005) and CAEVO (Chambers et al. 2014, TACL): SputLink computes temporal closure over a convex Allen
  subset to DENSIFY TimeBank; CAEVO is a precision-ranked sieve cascade imposing transitivity over the coarse TB-Dense algebra.
  Difference: both COMMIT to a single dense consistent labeling for F1; neither preserves LLM disjunction, certifies a reading
  error, nor abstains. We reuse CAEVO's coarse composition table verbatim but invert the objective; and we avoid the circularity
  that TB-Dense's non-adjacent gold is SputLink OUTPUT by using MATRES's DIRECT per-pair human gold for the primary arm and
  NarrativeTime's direct timeline gold for the dense fallback.
- >-
  Path-of-Thoughts (2024, arXiv:2412.17963): graph extraction -> path identification -> per-path reasoning, beating SOTA by
  up to 21.3% on StepGame/CLUTRR. PRIMARY real-text baseline. Difference (verified): it calls an external reasoner 'for each
  reasoning path' INDEPENDENTLY and does NOT intersect relations arriving at the same pair from multiple paths nor detect
  cross-path contradictions; when paths disagree it outputs multiple possible relations but does NOT abstain. This is EXACTLY
  the gap Mode A fills, so the real-text claim is restricted to the multi-path-with-bite subset and PoT is given a matched
  abstention signal (path-agreement). The ITERATION-specific 'beats naive intersection' claim is reserved for the synthetic
  arm, since PoT-vs-Mode-A already isolates path-isolation-vs-intersection on real text.
- >-
  DSR-LM / 'LLMs can Learn Rules' (Yang et al. 2023, arXiv:2305.03742; Zhu et al. 2023, arXiv:2310.07064): INDUCE weighted/symbolic
  composition rules to fit task accuracy. Difference: rule induction optimizes data fit and gives a point answer; we enforce
  the EXACT ALGEBRAIC LAWS (converse, associativity, disjointness) necessary for soundness independent of training data, and
  use closure for zero-FP narrowing, detection, localization, repair, and abstention. Our table-held-fixed closure ON-vs-OFF
  ablation specifically isolates path-consistency from 'a fixed consistent table exists' (DSR-LM's contribution).
- >-
  Logic-LM (Pan et al. 2023, arXiv:2305.12295) and LINC (Olausson et al. 2023, arXiv:2310.15164): Logic-LM self-refines using
  solver crash/unsat messages; LINC majority-votes the answers of multiple formalizations. Difference: Logic-LM reacts only
  to crashes and has no positive global INVARIANT over relational knowledge; LINC's answer-level voting cannot see that individually-popular
  composition steps are JOINTLY inconsistent, nor tighten a disjunctive query by intersection. Algebraic closure is a global
  necessary condition both lack; we give LINC vote-agreement as a matched abstention signal.
- >-
  LAMBADA (Kazemi et al. 2023, arXiv:2212.13894) and path-isolation reasoning: backward chaining / per-path reasoning that
  manages inconsistency by COMPOSITIONAL ISOLATION rather than global enforcement. Difference: we INTERSECT across paths via
  closure, which both tightens disjunctions (Mode A) and detects contradictions (Mode B); isolation can return mutually inconsistent
  answers and cannot resolve disjunctive uncertainty.
- >-
  Logically Consistent Language Models / LOCO-LMs (Calanzone, Teso & Vergari 2024, arXiv:2409.13724; ICLR 2025): a TRAINING-TIME
  neuro-symbolic loss fine-tuning an LLM to be consistent with propositional facts/rules. Difference: it is training-time
  and PROPOSITIONAL; we are training-free at INFERENCE time and enforce multi-hop COMPOSITION closure over a RELATION ALGEBRA
  read off text, producing per-instance certificates, abstention, and trace-graphs -- pre-empting a 'consistency enforcement
  is not new' objection (prior LM-consistency work enforces propositional/factual consistency, not relation-algebra composition
  closure).
- >-
  Generic LLM selective prediction / abstention (e.g. SelectLLM 2025; 'Know Your Limits' abstention survey 2025; self-consistency
  + token-entropy abstention pipelines; Liu et al. 2026 abstention in temporal QA, arXiv:2602.04755): reduce error by abstaining
  on hard queries via learned uncertainty, vote margins, or RL with abstention-aware rewards. Relevant to our risk-coverage
  objective. Difference: abstention is driven by GENERIC confidence/uncertainty signals or learned at the QA-answer level;
  there is no algebraic consistency certificate, no per-edge reading-error localization, no preserved relation-algebra disjunction,
  and no closure-based narrowing. Ours abstains precisely because deductive closure leaves the query a disjunction -- a structural,
  training-free, per-edge certificate, not a calibrated scalar.
- >-
  Classical qualitative reasoners and tractability theory: GQR, SparQ, Allen (1983), Mackworth (1977, path-consistency PC-1/PC-2
  ITERATED to a fixpoint -- distinguishing full closure from a single intersection pass, exploited in our naive-intersection
  ablation), Renz & Nebel (path consistency / random network model A(n,d,l)), Vilain & Kautz 1986 (point algebra), van Beek
  (PC insufficient for the full point algebra with !=), Nebel & Burckert 1995 (ORD-Horn, JACM 42(1)) proving PC decides satisfiability
  in ORD-Horn but not in general for the full algebra (NP-hard). So PC is COMPLETE for the convex point algebra and ORD-Horn
  yet SOUND-BUT-INCOMPLETE for full Allen IA / RCC-8. Difference: these assume a clean human-given table on already-formal
  data; none read the algebra off NL via an LLM, certify reading errors, narrow by cross-path intersection of LLM disjunctions,
  model an EMPIRICALLY-audited recall-bounded redundancy OPTIMUM, or optimize risk-coverage.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer from Qualitative Spatial-Temporal Reasoning and Tarski's relation algebras
  -- Allen's interval algebra, RCC-8, the convex point algebra, composition tables, and the path-consistency / algebraic-closure
  constraint-propagation algorithms (GQR/SparQ; Mackworth's iterated PC), plus the tractability theory (point-algebra and
  ORD-Horn completeness vs full-Allen NP-completeness) -- imported into LLM-based relational reasoning and hallucination control,
  with Reiter's 1980s model-based diagnosis (minimal hitting sets of conflict sets) for localizing which extracted atom to
  retract. The Level-1 framing is CODING THEORY: an exact composition table turns multi-path redundancy in a document into
  an error-correcting code over LLM extractions -- redundant constraining paths let closure DETECT and CORRECT mis-reads with
  no external labels, as parity checks detect bit errors. This iteration keeps the coding-theory 'optimal rate' sharpening
  (net benefit is an INVERTED-U because narrowing stays zero-FP only while every contributing symbol is sound) but makes it
  RIGOROUS: the joint-soundness 'decoding margin' is now MEASURED empirically as J(E) rather than assumed as the independence
  product r^E, since a single LLM reader produces positively-correlated reading errors -- so the predicted peak location uses
  the measured channel correlation, not an idealized memoryless channel. The Level-2 framing comes from SELECTIVE PREDICTION
  / risk-coverage in ML: compare an abstaining method against non-abstaining baselines at MATCHED COVERAGE, each given its
  own confidence signal and the SAME single-relation-resolution coverage object, and report the ACTIONABLE (singleton-resolution-to-correct)
  yield. The decisive design move this iteration is ARM SCOPING borrowed from the discipline of stating where a mechanism's
  advantage must and must not appear: because iterated closure provably equals a single intersection pass on acyclic length-2
  structures, the real-text held-out-edge regime can only demonstrate the win over PATH-ISOLATED reasoning, while the ITERATION
  win belongs to synthetic long-hop/cyclic networks -- so we claim each only where its own theory predicts it, dissolving
  an internal contradiction rather than overclaiming. Three refined cross-field insights drive the design: (1) LLMs are competent
  LOCAL qualitative namers that do NOT propagate constraints across paths -- the missing piece is global ITERATED propagation,
  and cross-path INTERSECTION of sound sets is a zero-FP win needing no over-commitment; (2) because the table is mathematical
  ground truth, intersection-of-sound-sets can only move toward gold and collapse-of-unsound-sets is a calibration-free certificate
  -- flipping the objective from accuracy-by-committing (ILP global inference, whose own results show consistency-enforcement
  does not raise F1) to faithfulness-by-abstaining; (3) the coding-theory lens names BOTH the safe primary mode (erasure-style
  narrowing) and the Achilles heel (a recall-bounded decoding radius whose EMPIRICAL joint-soundness decay produces an inverted-U),
  which we elevate to a pre-registered, DECOMPOSED, estimation-precision-bounded prediction anchored on both synthetic and
  real text rather than hide.
terms:
- term: Arm-scoped headline (the key revision)
  definition: >-
    Splitting the contribution so each claim is made only where its own theory predicts it. REAL-TEXT arm: Mode A beats path-isolated
    Path-of-Thoughts and answer-voting at matched coverage, and is predicted only to TIE a naive single-pass intersection
    (length-2/acyclic regime where one pass equals the fixpoint). SYNTHETIC arm: full ITERATED closure beats naive intersection
    with the gap growing in hop-count/cyclomatic number. This dissolves the prior internal contradiction between the real-text
    'beats naive' clause and the 'full==naive at length-2' prediction.
- term: A-priori envelope gate (T0)
  definition: >-
    A zero-LLM-spend computation, run FIRST, of N* = the count of MATRES gold-graph held-out edges that are simultaneously
    deduction-required (no shared local span), multi-path (>=2 distinct constraining paths), bite-retaining after non-convex->VAGUE
    widening, and singleton-resolving to gold; reported with the widening-induced bite loss and a paired-bootstrap power calc.
    It is an explicit go/no-go that decides whether a real-text headline exists before any model call, converting the previously
    pilot-deferred 'tiny envelope' risk into an up-front measured quantity.
- term: Escalation ladder (pre-registered)
  definition: >-
    The corpus-selection rule keyed to N*: MATRES (direct human point-algebra gold, PC complete) if N* powers the CI; else
    NarrativeTime (dense timeline-based DIRECT human gold, full TLink coverage, non-circular unlike TimeBank-Dense's SputLink-built
    non-adjacent gold) whose deduction-required multi-path envelope is structurally far larger; else synthetic-primary with
    real text demoted to an honestly-scoped niche-safety-net boundary. The headline is never contingent on an unmeasured quantity.
- term: Empirical joint soundness J(E)
  definition: >-
    The realized fraction of E-edge constraining subnetworks in which ALL edges are sound, MEASURED directly from data, replacing
    the independence product prod_e r_e. The zero-FP audit's reliability curve is pre-registered against J(E); the inverted-U
    cost term is 1 - J(E); and because positive within-document cross-edge error correlation rho makes J(E) decay slower than
    r^E, the predicted peak sits further out than an independence model says. Removes the unstated independence assumption
    the prior version relied on.
- term: Cross-edge reading-error correlation (rho)
  definition: >-
    The measured within-document correlation of per-edge soundness failures from a single LLM reader. Reported explicitly;
    used both to interpret J(E) (positive rho => slower joint-soundness decay => outward peak shift) and as a match term in
    the extended realism statistic. The pre-registered attribution rule: a reliability-slope offset that DISAPPEARS when the
    predictor switches from r^E to empirical J(E) is the independence approximation failing (not a disconfirmation); one that
    PERSISTS under J(E) is a genuine soundness failure.
- term: Sound narrowing (Mode A, primary)
  definition: >-
    The zero-false-positive value mode: when every contributing LLM edge set is SOUND (contains its gold relation) but sub-universal,
    intersecting the compositions arriving at a query pair from MULTIPLE non-universal paths yields a set that still contains
    gold yet is strictly tighter than any single path. Requires breadth + multi-path bite, NOT over-commitment; its ACTIONABLE
    yield is intersection-to-correct-SINGLETON; inert only in the degenerate all-universal limit.
- term: Singleton-resolution-to-correct yield (headline metric)
  definition: >-
    The load-bearing Mode-A metric: the fraction of multi-path SOUND-input query pairs whose cross-path intersection collapses
    the query to the single CORRECT relation. Distinguished from STRICT-TIGHTENING yield (any reduction, e.g. 5->3), which
    does NOT move matched-coverage selective accuracy when the coverage axis is single-relation resolution. Both reported;
    singleton-resolution drives the headline.
- term: Inverted-U redundancy optimum
  definition: >-
    Net Mode-A selective-accuracy gain RISES then FALLS as path redundancy/hop-count increases at fixed per-edge recall: more
    paths add narrowing benefit, but each added contributing edge lowers empirical joint soundness J(E), so silent-narrowing
    cost (1 - J(E)) eventually dominates. Coding-theory optimal-rate analogue. Peak location increases with recall; the recall-floor
    gate truncates the cost tail and shifts the peak outward. Established only at a pre-registered estimation precision (>=4
    recall levels, >=500 networks/cell, >=1-bin minimum-detectable shift, peak bin CI-above neighbors); otherwise reported
    as 'directionally consistent.'
- term: Naive-intersection baseline
  definition: >-
    Intersect the compositions arriving at the query pair in a SINGLE pass, without iterating to a fixpoint and without algebra-seeded
    converse propagation -- i.e. 'PoT plus one obvious intersection step.' It COINCIDES with full closure on length-2 multi-path
    queries (so Mode A is predicted to TIE it on the real-text arm) but diverges on longer/cyclic networks, where the full-closure-minus-naive
    gap GROWS -- the SYNTHETIC iteration claim.
- term: Detection/repair (Mode B, secondary)
  definition: >-
    The collapse-based value mode: an empty closure certifies that some LLM edge is UNSOUND -- a gold-free zero-FP DETECTION
    flag (conditional on recall). Requires at least one over-committed/recall-failed edge to fire, supports Reiter-style minimal-hitting-set
    localization/repair (which can mislocalize), and carries the silent-wrong-narrowing dual. Reported distinctly from Mode
    A; magnitude tracks the measured over-commitment rate.
- term: Recall-bite frontier
  definition: >-
    The curve, traced by sweeping the prompt-elicited breadth knob from 'name the relation' to 'name the maximal sound set,'
    of per-edge recall against singleton-resolution-to-correct yield and collapse rate. Recall and bite are in direct tension
    on the SAME knob, so a single operating point cannot establish viability; we map the frontier and pre-register that the
    main run proceeds only if a region clears a recall gate AND yields non-trivial singleton-resolution-to-correct.
- term: Deduction-required vs directly-readable stratification
  definition: >-
    A LOCAL-ONLY READER probe predicts each held-out edge from ONLY the minimal local span(s) where its two events co-occur
    (or flags 'no shared span'). Edges it confidently and correctly names are DIRECTLY-READABLE; the rest are DEDUCTION-REQUIRED
    (obtainable only by composing >=2 edges). We foreground the deduction-required fraction, stratify the headline by it,
    and draw the primary subset preferentially from deduction-required triangles, so the win is genuine composition, not re-reading.
    The T0 gate uses a structural proxy (no shared local span) computable without the LLM.
- term: Extended realism-matching statistic
  definition: >-
    The pre-registered acceptance test for the synthetic NL-realization protocol, now matching THREE things, not one: (a)
    total-variation distance between real and synthetic per-edge error-type distributions (marginals), (b) the cross-edge
    error CORRELATION rho, and (c) the redundancy/path-topology distribution (contributing-edge-count and cycle-structure
    histograms). Because (b) and (c) -- not the marginals -- set the inverted-U peak, matching only marginals (the prior version)
    was insufficient. All thresholds fixed before generating the redundancy curve.
- term: Real-text decomposition anchor
  definition: >-
    A coarse estimate of Mode-A benefit and silent-narrowing-cost curves computed directly on REAL sub-networks binned by
    contributing-edge count / hop-count, checked for qualitative inverted-U consistency against the synthetic decomposition
    -- so the load-bearing redundancy result is anchored to real text rather than reported on synthetic data alone.
- term: Exact composition table
  definition: >-
    For each ordered pair of base relations (r,s), the set of base relations the composite r-then-s can take. For Allen IA,
    the point algebra, and RCC-8 these tables are PUBLISHED MATHEMATICAL GROUND TRUTH. The TimeBank-Dense 6-label table is
    a DESIGNED COARSENING (the SputLink/CAEVO convex table) cited verbatim. LLM-elicited tables (kinship) are studied only
    as a Tier-2 ablation against gold.
- term: Algebraic closure / path consistency
  definition: >-
    A constraint-propagation algorithm that repeatedly tightens each edge's relation set by intersecting it with the composition
    of relations along every two-step path, ITERATING to a fixpoint (Mackworth PC). It is SOUND and an empty collapse certifies
    inconsistency, but INCOMPLETE for full Allen IA / RCC-8 (consistency NP-complete) and COMPLETE only for the convex point
    algebra and ORD-Horn. Polynomial and millisecond-fast per document. Distinguished from a single-pass naive intersection
    by its iterated fixpoint and algebra-seeded converse propagation.
- term: Convex point algebra (MATRES arm)
  definition: >-
    The relation algebra over a single time point per event with convex base relations <=, =, >= (and disjunctions). MATRES's
    BEFORE/AFTER/EQUAL/VAGUE start-point labels instantiate this, for which path-consistency is provably COMPLETE and the
    table exact. We widen non-convex {<,>} (genuine !=) to VAGUE to preserve completeness and MEASURE the bite lost; if non-trivial
    we add a full-point-algebra arm scored as a lower-bound detector.
- term: Sound-but-loose disjunctive labeling
  definition: >-
    Reframing the LLM's task from 'name THE relation' (precision-oriented, over-commitment-prone) to 'name the set of base
    relations the text span does NOT exclude' (recall-oriented, NLI-like). Soundness means the gold relation is INSIDE the
    emitted set; precision is delegated to exact closure. Its failure is RECALL failure (gold omitted), the source of silent
    wrong narrowing.
- term: Silent wrong narrowing (pre-registered failure mode)
  definition: >-
    When a contributing set OMITS gold (unsound), closure can narrow the query to a confident WRONG singleton with NO empty
    collapse -- a certified-LOOKING hallucination the mechanism actively endorses. Its rate is governed per-edge by (1-recall)
    and per-network by (1 - J(E)) (empirical joint soundness), reported in the decomposition of gold-wrong non-abstained predictions;
    the recall-floor gate is tested as a mitigation and as the lever that shifts the inverted-U redundancy peak.
- term: Matched-coverage selective comparison
  definition: >-
    The protocol for comparing an abstaining method against baselines: each baseline is given its own abstention/confidence
    signal (vote margin, verbalized confidence, vote agreement, path-agreement), thresholds are swept so every method reports
    at the SAME coverage using the SAME coverage object (single-relation resolution), and selective accuracy is compared with
    paired bootstrap CIs -- preventing the headline from conflating 'closure' with 'closure has a better-calibrated abstain
    than baselines were given.'
- term: Trace-graph
  definition: >-
    A human-auditable record: the QCN, which composition entries fired on which paths during closure, any minimal repairs,
    and optionally an equivalent SWI-Prolog/ASP proof discharged from the closed table for replay -- the connective tissue
    to the umbrella text-to-logic pipeline's auditability and quantified-hallucination-reduction requirements.
summary: >-
  We import exact relation-algebra path consistency (Allen interval, convex point algebra, RCC-8) into the deduction module
  of a text-to-logic pipeline and ARM-SCOPE the contribution to dissolve a prior internal contradiction: on REAL text, cross-path
  SOUND NARROWING of the LLM's high-recall disjunctive sets beats path-isolated reasoning and voting at matched coverage (predicted
  only to TIE a single intersection pass, as the held-out-edge regime is length-2), while the ITERATED-closure-beats-naive-intersection
  win is claimed on SYNTHETIC long-hop/cyclic networks. We gate the real-text headline on an a-priori, zero-LLM-spend envelope
  count with a pre-registered escalation ladder (MATRES -> dense NarrativeTime -> synthetic-primary), and we audit the zero-FP
  guarantee and locate the recall-bounded inverted-U redundancy optimum using EMPIRICAL joint soundness J(E) and measured
  cross-edge error correlation, anchored on both synthetic and real text, rather than an independence product.
</previous_hypothesis>

<previous_review_feedback>
A reviewer evaluated your previous hypothesis and provided the feedback below.

IMPORTANT: Do NOT generate a completely new hypothesis. Take the previous hypothesis above and
REVISE it to address the feedback. Keep what works, fix what was criticized.

You MUST address ALL the critiques. Do NOT repeat the same mistakes.

kind: reviewer_feedback
id: review_hypo_adc099124893
overall_assessment: >-
  This is iteration 6 of a well-developed, training-free neuro-symbolic proposal that imports exact relation-algebra path
  consistency into the deduction module of a text-to-logic pipeline, splitting the value into a primary zero-false-positive
  cross-path SOUND-NARROWING mode (Mode A) and a secondary gold-free DETECTION mode (Mode B), with a coding-theory inverted-U
  redundancy optimum. The revision is excellent on process: it fixes ALL FIVE critiques from the previous round, and does
  so with the right tools. The prior MAJOR internal contradiction (real-text 'beats naive intersection' vs the 'full==naive
  at length-2' prediction) is dissolved cleanly by ARM-SCOPING -- the real-text arm now claims a win only over path-isolated
  reasoning (Path-of-Thoughts) and voting, and explicitly states it is PREDICTED TO TIE naive intersection on the length-2/acyclic
  held-out-edge regime, reserving the iterated-closure-beats-naive claim for synthetic long-hop/cyclic networks. The prior
  MAJOR envelope-feasibility risk is fixed by the T0 a-priori envelope gate (zero LLM spend) plus a pre-registered escalation
  ladder. The three minors (independence product -> empirical joint soundness J(E)+rho; synthetic-only / marginal-only decomposition
  -> real-text anchor + extended realism statistic; density / falsifier -> 3-claim lead + estimation-precision pre-registration)
  are all addressed precisely. The work is genuinely novel, honest to a fault, and feasible on the stated budget. What keeps
  it at a strong Weak-Accept rather than rising to Accept is that the arm-scoping fix, while correct, relocates the genuinely
  novel algorithmic contribution (iterated closure error-corrects) entirely onto SYNTHETIC data, while the real-text contribution
  is reduced to a single-pass cross-path intersection over a possibly-tiny, now-computable envelope -- and, decisively, the
  stated real-text PRIMARY (MATRES) is structurally near-certain to FAIL the deduction-required gate because MATRES only annotates
  same/adjacent-sentence pairs (all gold edges are locally co-occurring, hence directly-readable). The headline therefore
  lands on NarrativeTime, a corpus characterized in one sentence but not established with the algebraic rigor (completeness,
  exact-table, gold-directness) lavished on MATRES. Fixing the realized-corpus characterization up front (T0 already provides
  the mechanism) and strengthening the real-text significance are the two changes most likely to push this from 6 to 7.
strengths:
- >-
  ARM-SCOPING dissolves the prior internal contradiction in exactly the right way: each claim is now made only where its own
  theory predicts it. Conceding the real-text TIE with naive single-pass intersection out loud (length-2/acyclic theta regime
  where one pass equals the fixpoint -- a technically correct statement) and reframing it as a CONFIRMATION rather than a
  failure is a model of honest claim discipline. The win over Path-of-Thoughts and voting is precisely the gap those methods
  structurally cannot fill (path-isolation, answer-level voting that cannot see jointly-inconsistent steps).
- >-
  The T0 A-PRIORI ENVELOPE GATE is excellent experimental design: it converts the binding 'tiny envelope' risk into an up-front,
  zero-LLM-spend, computable go/no-go (count N* of held-out edges that are deduction-required AND >=2-path AND bite-retaining-after-widening
  AND singleton-resolving), reports the widening-induced bite loss and a paired-bootstrap power calc, and pre-registers an
  escalation ladder so the headline is never contingent on an unmeasured quantity. This fixes the prior MAJOR exactly.
- >-
  Replacing the independence product prod_e r_e with the EMPIRICAL joint soundness J(E) and a measured cross-edge reading-error
  correlation rho is a precise, well-motivated refinement. The pre-registered attribution rule -- a reliability-slope offset
  that VANISHES under J(E) is the independence approximation failing (not a disconfirmation), one that PERSISTS is a genuine
  soundness failure -- removes a real interpretive trap and is itself falsifiable.
- >-
  Genuine, well-differentiated novelty against a thorough (12-entry) related-work set: the 'opposite output contract' (preserve
  the LLM's multi-relation output as a SOUND DISJUNCTION and NARROW/ABSTAIN, vs commit-to-a-single-label-to-maximize-F1) is
  sharply positioned against the entire commit-via-ILP lineage including the most recent EMNLP 2025 system (arXiv:2502.11114)
  and Knez & Sun's negative result. The coding-theory error-correcting-code lens and the inverted-U 'optimal rate' prediction
  are a non-obvious, elegant cross-field synthesis.
- >-
  Top-tier honesty commitments: zero-FP is scoped SEPARATELY for Mode A (sound narrowing) and Mode B (DETECTION only, localization
  can mislocalize); silent-wrong-narrowing is pre-registered as the dual with explicit per-edge (1-recall) and per-network
  (1-J(E)) bounds and a recall-floor-gate mitigation; PC incompleteness for full Allen IA / RCC-8 is acknowledged (closure-detectable
  rate framed as a LOWER BOUND, exact only on the convex point algebra); and each failure mode is pre-committed as a publishable
  scope boundary.
- >-
  The real-text DECOMPOSITION ANCHOR plus the EXTENDED realism-matching statistic (marginal TV-distance PLUS cross-edge correlation
  rho PLUS redundancy/path-topology histograms) directly fix the prior 'synthetic-only / marginal-only' minor by matching
  the dimensions that actually set the inverted-U peak, not just per-edge error frequencies.
- >-
  Estimation-precision pre-registration (>=4 fixed recall levels, >=500 networks/cell, >=1-bin minimum-detectable peak shift,
  peak bin CI-above both neighbors else only 'directionally consistent') makes the inverted-U falsifiable in the intended
  way and pre-empts the 'confirmable under any curve shape' concern.
- >-
  Strong feasibility and venue fit on the mechanics: closure/repair run in milliseconds on commodity hardware, sub-$10 LLM
  budget via short docs/caching/cheap extraction, exact tables seeded from the algebra (never the LLM) for primary settings,
  and replayable trace-graphs that connect cleanly to the umbrella pipeline's auditability and quantified-hallucination-reduction
  requirements.
dimension_scores:
- dimension: soundness
  score: 3
  justification: >-
    The core mechanism is sound: cross-path intersection of SOUND disjunctive sets can only move toward gold regardless of
    PC completeness, the inverted-U follows rigorously from J(E) decay, and the arm-scoping (full==naive on length-2 theta
    structures) is technically correct. The empirical-J(E) and estimation-precision refinements materially raise rigor. It
    is not a 4 because the realized real-text arm's algebraic guarantees are unestablished: MATRES (adjacent-sentence-only
    annotation) almost certainly fails the deduction-required gate, so the headline lands on NarrativeTime, whose completeness/exact-table/gold-directness
    properties are asserted, not derived, and whose timeline-derived gold raises a residual circularity the proposal does
    not fully neutralize.
  improvements:
  - >-
    Extend T0 to compute the a-priori deduction-required multi-path-with-bite envelope for NarrativeTime (and any other candidate
    corpus), and establish its algebra and PC-completeness status BEFORE LLM spend -- because that corpus, not MATRES, is
    the near-certain landing spot.
  - >-
    State and bound the residual circularity of recovering a held-out edge by closure when gold is human-timeline-derived
    (a form of human global inference / implicit closure), distinct from but weaker than TimeBank-Dense's SputLink-output
    circularity; e.g. measure the fraction of held-out edges whose gold is independently locally justifiable vs purely timeline-implied.
- dimension: presentation
  score: 3
  justification: >-
    The LEAD is much improved: three arm-scoped claims, each with one explicit genuine disconfirmer, stated before the qualifiers,
    exactly as requested. The claim->precondition->metric->baseline->CI structure (C1a/C1b, C2-C6) and the T0/Tier-1/Tier-2
    ordering are clear. It is not a 4 because the body and especially success_criteria remain very long and qualifier-dense,
    and the MATRES-primary / NarrativeTime-fallback ordering misleads the reader about which corpus will actually host the
    headline.
  improvements:
  - >-
    Relabel NarrativeTime (or a dense direct-gold corpus) as a CO-PRIMARY candidate, and state plainly that MATRES is expected
    to fail the deduction-required gate by construction (adjacent-sentence-only annotation), so the reader is not surprised
    when the ladder escalates.
  - >-
    Tighten success_criteria: it currently restates the full mechanism with all qualifiers; move the honest-failure-mode catalogue
    to a single compact table and keep only the confirm/disconfirm lines inline.
- dimension: contribution
  score: 3
  justification: >-
    Genuine novelty and a meaningful problem, well-positioned. The contribution is capped below 4 by the same arm-scoping
    that fixes the soundness issue: the most novel algorithmic claim (iterated closure error-corrects, gap grows with hop/cyclomatic
    number) is now SYNTHETIC-ONLY and is close to a textbook property of path-consistency, while the real-text contribution
    is a single-pass cross-path intersection over an envelope that may be small. For the ACL Knowledge Extraction venue, a
    synthetic-primary fallback outcome would be a weak fit.
  improvements:
  - >-
    Quantify a-priori (from gold graphs, zero spend) the prevalence of >=3-edge / cyclic real-text constraint structures in
    the candidate corpora; NarrativeTime's density makes a real iteration demonstration plausible -- if even a small such
    stratum exists, run full-vs-naive there to bring at least a piece of the iteration win onto real text.
  - >-
    Promote the end-to-end real-text hallucination-reduction-on-ABSENT-relation demonstration from a Tier-2 echo to a headline-supporting
    result, since downstream hallucination reduction (the umbrella pipeline's actual requirement) is more venue-relevant than
    the held-out-edge selective-accuracy gap alone.
critiques:
- id: ''
  category: scope
  severity: major
  description: >-
    The stated real-text PRIMARY (MATRES) is structurally near-certain to FAIL the very deduction-required gate the proposal
    introduces, so the real-text headline will land on a corpus (NarrativeTime) that is under-characterized. MATRES annotates
    ONLY same-sentence and ADJACENT-sentence event pairs (confirmed: the scheme explicitly avoids non-adjacent pairs to escape
    an exponential annotation cost). Consequently every MATRES gold edge -- including the held-out edge of any triangle whose
    three pairs all have gold -- is by construction locally co-occurring, i.e. DIRECTLY-READABLE by the proposal's own local-only-reader
    probe. The deduction-required (no-shared-local-span) AND singleton-resolving stratum among MATRES gold edges is therefore
    not merely 'thin' (as the prior review and the hypothesis frame it) but structurally near-empty, so T0's N* on MATRES
    is very likely ~0 for the deduction-required criterion. The escalation ladder then selects NarrativeTime -- but NarrativeTime
    is timeline-based and converts to TimeML/Allen interval relations, so it does NOT obviously inherit the convex-point-algebra
    PC-COMPLETENESS, exact-table, and direct-per-pair-human-gold properties that the hypothesis carefully establishes for
    MATRES and uses as a distinctive selling point. The paper thus invests its strongest guarantees in a corpus that will
    likely not host the headline, while the corpus that will host it is described in a single sentence.
  suggested_action: >-
    Do for NarrativeTime (and any other dense direct-gold candidate) what was done for MATRES, BEFORE any LLM spend: (1) extend
    T0 to compute its a-priori deduction-required multi-path-with-bite singleton-resolving N* and power calc; (2) state precisely
    which relation algebra its gold lives in (can it be restricted to start-points to stay in the convex point algebra where
    PC is complete, as done for MATRES, or is it full Allen IA where PC is sound-but-incomplete?), and scope the exactness/Mode-B
    claims accordingly; (3) relabel NarrativeTime as a CO-PRIMARY rather than a fallback, and state explicitly that MATRES
    is expected to fail the deduction-required gate by construction. Note that Mode A's zero-FP sound-narrowing survives incompleteness
    (intersection of sound sets is always sound), so the mechanism is not lost -- but the 'exact/complete real-text arm' framing
    must be moved to wherever it actually holds.
- id: ''
  category: scope
  severity: major
  description: >-
    The arm-scoping fix, though correct and honest, lowers the ceiling on the real-text contribution and concentrates the
    genuinely novel algorithmic claim on synthetic data. After the split, the real-text arm demonstrates only that a SINGLE
    cross-path intersection plus abstention beats path-isolated reasoning and voting -- conceptually the contribution, but
    a one-step operation over an envelope that the proposal itself flags as possibly tiny. The distinctive, more sophisticated
    claim (ITERATED closure error-corrects, with the full-minus-naive gap growing in hop-count / cyclomatic number) is now
    reserved entirely for SYNTHETIC long-hop/cyclic networks with a researcher-controlled NL-realization, where it also approaches
    a textbook property of path-consistency (PC-1/PC-2 iterate to a fixpoint; single-pass != fixpoint on cyclic networks).
    For the target ACL Knowledge Extraction venue, the most likely outcome under the escalation ladder (a synthetic-primary
    headline with a niche real-text safety-net) would be a comparatively weak fit, and even the success case offloads the
    headline iteration result to synthetic data. This is the binding significance ceiling, not a soundness flaw.
  suggested_action: >-
    Bring at least part of the iteration win onto real text: compute a-priori (zero spend) the prevalence of >=3-edge / cyclic
    real constraint structures in the dense corpus and, if a usable stratum exists, run full-vs-naive there with hop/cyclomatic
    stratification. Independently, elevate the end-to-end hallucination-reduction-on-absent-relation demonstration (the umbrella
    pipeline's actual deliverable) from Tier-2 to a headline-supporting result with its own pre-registered effect size, so
    the real-text contribution is anchored to a downstream, venue-relevant metric rather than only the held-out-edge selective-accuracy
    gap. Pre-register the applicability-envelope threshold (the line between 'general mechanism' and 'niche safety-net') as
    a concrete number, not a qualitative bar.
- id: ''
  category: rigor
  severity: minor
  description: >-
    The reader-agnosticity test (C5) feeds a METRE-style trained multi-label head into the same closure pipeline. But METRE
    is trained to maximize extraction F1 (a precision/recall trade-off), not to emit RECALL-oriented SOUND sets (gold inside
    the set). Its label-sets may systematically omit gold more or differently than the LLM disjunctive reader, violating the
    soundness precondition Mode A requires and inflating silent-wrong-narrowing in a reader-specific way. Simply asserting
    'comparable per-edge recall' is insufficient, because matching marginal recall does not match the ERROR-CORRELATION structure
    (rho), which the proposal itself now argues sets the inverted-U peak; a reader with the same recall but different rho
    would give a different closure gain, confounding the 'win is in the algebra' conclusion.
  suggested_action: >-
    Specify the recall-matching protocol for the alternative readers: tune each reader's threshold to a matched per-edge recall
    AND report each reader's measured rho, then interpret the reader-agnosticity result conditional on both. If the readers
    differ materially in rho, condition the comparison on rho (or match it) so the closure-gain comparison is not confounded
    by reader-specific error correlation.
- id: ''
  category: rigor
  severity: minor
  description: >-
    The design now pre-registers a large family of CI tests -- C1a and C1b headlines, C2-C6, each stratified by deduction-required
    vs directly-readable and (for the redundancy arm) across >=4 recall levels and multiple redundancy bins, each with paired-bootstrap
    CIs separated from zero. Without a stated multiplicity policy, the headline 'CI-separated from zero' claim is vulnerable
    to a multiple-looks artifact, and a reviewer can discount any single separated CI as cherry-picked from many.
  suggested_action: >-
    State a multiplicity stance: designate which tests are CONFIRMATORY (the three arm-scoped headlines and the single redundancy
    disconfirmer) vs EXPLORATORY (the strata and per-bin curves), and apply a family-wise or hierarchical correction (or report
    adjusted CIs) for the confirmatory family. This costs nothing and inoculates the headline against a 'garden of forking
    paths' objection.
- id: ''
  category: clarity
  severity: minor
  description: >-
    The LEAD is genuinely improved and the C1-C6 table is helpful, but the hypothesis body and especially the success_criteria
    remain very long and qualifier-dense, with the honest-failure-mode catalogue, the empirical-J(E) attribution rule, the
    escalation ladder, and the estimation-precision bar all restated multiple times across sections. This makes the single
    most important prediction (the inverted-U with its one genuine disconfirmer) harder to locate than it should be, and risks
    a reviewer skimming and under-crediting the rigor that is actually present.
  suggested_action: >-
    Compress success_criteria to: the three confirm lines, the three disconfirm lines, and a single compact table of the five
    pre-registered failure modes (each one row: name / precondition / bound / scope-boundary interpretation). Move the J(E)
    attribution rule and escalation ladder to the investigation_approach only (they currently appear in both), so each appears
    once.
score: 6
confidence: 4
relation_type: evolution
relation_rationale: >-
  Same frame (Mode A/B closure, inverted-U, risk-coverage); refines via arm-scoping, T0 gate, empirical J(E).
</previous_review_feedback><user_data>
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
    "TermDefinition": {
      "description": "A technical term and its definition.",
      "properties": {
        "term": {
          "description": "The technical term",
          "title": "Term",
          "type": "string"
        },
        "definition": {
          "description": "Clear definition of the term",
          "title": "Definition",
          "type": "string"
        }
      },
      "required": [
        "term",
        "definition"
      ],
      "title": "TermDefinition",
      "type": "object"
    }
  },
  "description": "A research hypothesis with validation approach.",
  "properties": {
    "title": {
      "description": "Concise, self-explanatory title",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "The core hypothesis statement",
      "title": "Hypothesis",
      "type": "string"
    },
    "motivation": {
      "description": "Why this hypothesis matters - significance and impact",
      "title": "Motivation",
      "type": "string"
    },
    "assumptions": {
      "description": "Key assumptions that must hold for this hypothesis (2-5 items)",
      "items": {
        "type": "string"
      },
      "title": "Assumptions",
      "type": "array"
    },
    "investigation_approach": {
      "description": "High-level approach to investigating this hypothesis",
      "title": "Investigation Approach",
      "type": "string"
    },
    "success_criteria": {
      "description": "What outcomes would confirm or disconfirm this hypothesis?",
      "title": "Success Criteria",
      "type": "string"
    },
    "related_works": {
      "description": "The most similar existing works found during research. Each entry describes one related work: what it does and how the proposed hypothesis fundamentally differs from it.",
      "items": {
        "type": "string"
      },
      "title": "Related Works",
      "type": "array"
    },
    "inspiration": {
      "description": "What inspired this hypothesis - which patterns, techniques, or cross-field insights were adapted (from the explicit inspiration seeds if your prompt included any, otherwise from your own cross-domain exploration)",
      "title": "Inspiration",
      "type": "string"
    },
    "terms": {
      "description": "Definitions of key technical terms used in the hypothesis",
      "items": {
        "$ref": "#/$defs/TermDefinition"
      },
      "title": "Terms",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the hypothesis in 1-2 sentences",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "motivation",
    "assumptions",
    "investigation_approach",
    "success_criteria",
    "related_works",
    "inspiration",
    "terms",
    "summary"
  ],
  "title": "Hypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-17 13:00:05 UTC

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

### [3] SKILL-INPUT — aii-web-tools · 2026-06-17 13:02:12 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````
