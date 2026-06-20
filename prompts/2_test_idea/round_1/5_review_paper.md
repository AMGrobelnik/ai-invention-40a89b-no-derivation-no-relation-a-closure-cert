# review_paper — test_idea

> Phase: `invention_loop` · round 1 · Substep: `review_paper`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave the agent(s) in this substep — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 15:02:06 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An adversarial paper reviewer (Step 3.5: REVIEW_PAPER in the invention loop)

You received a paper draft written by a DIFFERENT model. Review it with fresh eyes.
Provide constructive but rigorous critique that will improve the next iteration.

Specific critiques → better paper. Vague praise → no improvement.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the paper under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of the paper.

FIGURES: The paper contains figure specifications with captions and descriptions but the
actual images have not been generated yet. Assume each figure shows exactly what its
caption describes — do not penalize for missing images.

ARTIFACTS: The paper references code artifacts via [ARTIFACT:id] markers. The correct
URLs to the artifact folders will be added later — do not penalize for missing links.

GOAL: Your review feeds directly back to the paper author. The objective is to maximize
the overall review score in subsequent rounds. Every piece of feedback you give should
be written with this goal in mind — prioritize the critiques and suggestions that would
produce the largest score improvement if addressed. Don't waste the author's iteration
budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the tasks or methods new? Novel combination of known techniques?
    Clear differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the submission technically sound? Are claims well supported by theoretical
    analysis or experimental results? Is the methodology appropriate? Is this a complete
    piece of work? Are the authors honest about limitations?
(c) Clarity: Is the submission clearly written and well organized? Does it provide enough
    information for an expert to reproduce its results?
(d) Significance: Are the results important? Would others build on them? Does it address
    a meaningful problem better than prior work? Does it advance the state of the art?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims, experimental and research methodology,
and whether central claims are adequately supported with evidence:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas and execution, value to the broader research community:
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
- Distinguish major issues (would cause rejection) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Check if figures are well-specified and would effectively communicate the results
- Verify that claims are supported by the artifacts described

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

<paper>

# Introduction

A growing class of systems aims to read a short, professionally written document -- a news report, a contract clause, a children's story -- into a formal representation (first-order logic predicates, Prolog facts) that a symbolic reasoner can execute, optionally grounded against an upper ontology, with a large language model (LLM) resolving the terminology, concepts, and relations that the surface text leaves implicit. Such a pipeline promises auditable, replayable reasoning over text, but it has a structurally identifiable weak link. Atomic extraction -- naming the entities and the relations that hold between locally co-occurring mentions -- is by now something LLMs do competently. The \emph{deduction} step is where faithfulness breaks: synthesizing the explicitly stated facts with implicit composition knowledge to answer a query about a pair of entities that never co-occur in any single span. This is the multi-hop relational reasoning the user ultimately cares about, and it is exactly where hallucination is most damaging and hardest to detect.

Faithful multi-hop relational reasoning over text matters wherever the cost of a confidently wrong answer is high: ordering the events in a news story, tracking kinship in a narrative, resolving containment and region relations in a description, chaining clauses in a legal document. The relations involved -- temporal order, kinship, spatial containment -- are precisely the ones for which mathematics has supplied exact \emph{composition laws} for forty years: Allen's interval algebra \citep{Allen1983}, the convex point algebra \citep{Vilain1986}, the region connection calculus RCC-8 \citep{Randell1992}, and the path-consistency constraint-propagation algorithms that operate over them \citep{Mackworth1977}. If a document says event $A$ is before $B$ and $B$ is before $C$, the relation between $A$ and $C$ is not a matter of opinion to be guessed; it is determined by an exact table. The opportunity is to make an LLM-driven pipeline reason with these laws rather than around them.

The deduction step is hard because the obvious ways of using an LLM all fail in characteristic ways. Composing freely, the LLM is locally fluent but globally inconsistent: it can assign more than one temporal relation to the same pair and violate transitivity, producing silent errors that an answer-level vote \citep{Wang2022} or a solver-crash signal \citep{Pan2023} cannot see. Reasoning each path in isolation -- the strategy of backward chaining \citep{Kazemi2022} and Path-of-Thoughts \citep{Zhang2024} -- deliberately avoids the global check, so it can neither tighten a disjunctive query by intersecting evidence from multiple paths nor detect a contradiction arriving at the same pair from two routes. Hand-crafting composition rules (the kinship rules behind CLUTRR \citep{Sinha2019}) does not scale, and inducing rules to fit task accuracy \citep{Zhang2023, Zhu2023} optimizes data fit rather than the algebraic laws needed for soundness.

Why has this not been solved? Because the entire recent lineage attacks it under the wrong output contract. A 2024 study of zero-shot temporal extraction finds LLMs assign multiple relations to over half (up to $97\%$) of pairs and violate transitivity, then enforces consistency with integer linear programming (ILP) and reports that consistency-enforcement \emph{does not improve} F1 \citep{Kougia2024}; the most recent global temporal-graph generator (EMNLP 2025) still aggregates generations and commits to a single label per pair via ILP, preserving no disjunction, issuing no certificate, and offering no abstention \citep{Eirew2025}. Classical temporal closure (SputLink densifies TimeBank \citep{Verhagen2005}; CAEVO does global inference by cascaded sieves \citep{Chambers2014}; structured learning enforces transitivity \citep{Ning2017}) likewise commits to one consistent labeling to maximize F1. We read this as evidence that consistency-enforcement under the F1-maximizing \emph{commit} contract is the wrong objective. The LLM's native multi-relation output is not noise to be collapsed; it is a \emph{sound disjunction} to be preserved and narrowed, and the right objective is faithfulness-by-abstention, not extraction F1.

Our approach inverts the contract. The LLM emits, per text span, a high-recall disjunctive set of base relations the span does not exclude. Because the composition tables are exact ground truth, intersecting the disjunctive sets arriving at a query pair from multiple constraining paths -- via iterated path consistency -- can only move toward the gold relation (Mode~A, a zero-false-positive narrowing that needs no over-commitment and no labels), while an empty intersection certifies that some read was unsound (Mode~B, a gold-free reading-error flag). Multi-path redundancy in a document thereby becomes an \emph{error-correcting code} over LLM extractions. The coding-theory lens predicts an optimal rate: narrowing stays zero-FP only while every contributing read is sound, and that joint probability decays as redundancy grows, so net benefit is an inverted-U whose peak we predict from the measured per-edge recall and the measured cross-edge error correlation. We validate the full mechanism on clean synthetic ground truth, contribute a zero-LLM-spend \emph{envelope gate} that decides a-priori where the mechanism can apply to real text, and -- our most decision-relevant result -- map a \emph{recall-bite frontier} that localizes the true bottleneck. The module runs in milliseconds on commodity hardware and emits human-auditable trace-graphs, directly serving the auditability and quantified-hallucination-reduction requirements of the surrounding text-to-logic pipeline.

[FIGURE:fig1]

## Summary of Contributions

- \textbf{An inverted output contract for the deduction module} (Section~3): preserve the LLM's disjunctive reading, narrow by exact-table cross-path intersection (Mode~A, zero-FP), certify reading errors by closure collapse (Mode~B), and abstain when deduction leaves a disjunction -- training-free, label-free, and auditable, in contrast to the F1-commit contract of all prior closure-over-extraction work \citep{Kougia2024, Eirew2025, Verhagen2005}.
- \textbf{A validated mechanism on clean ground truth} (Section~5.2): on 35{,}100 consistent-by-construction networks, \emph{iterated} closure error-corrects (full-minus-naive gap grows from $0.0$ at hop~2 to $0.99$ at hop~6, Page $p\approx10^{-13}$), net gain is a recall-dependent inverted-U ($K^\ast=2,4,5,5,8$ for recall $0.5\to0.95$), and the certificate is exactly zero-FP (all-sound $\Rightarrow$ gold-in-output probability $1.0$; silent-wrong rate $5.8\%$).
- \textbf{A zero-LLM-spend envelope gate} (Section~5.1): from gold graphs alone we compute, per corpus, the deduction-required, multi-path, bite-retaining, singleton-resolving count $N^\ast$ and a power calculation. The gate is discriminative -- MATRES yields $N^\ast{=}0$ (adjacent-sentence gold), NarrativeTime yields $N^\ast{=}25{,}450$ (applicability $0.88$) -- and costs nothing to run.
- \textbf{A recall-bite frontier that localizes the bottleneck} (Section~5.3): the binding constraint on real news text is LLM read-soundness, not the closure step. A cheap reader reaches per-edge recall $0.57$--$0.86$ across real arms (below the $0.85$/$0.90$ gates), while on clean text (recall $0.96$) closure resolves $42\%$ of deduction-required queries correctly. We report this as the pre-registered scope boundary it is, and show closure $\approx$ direct read when both use full document context, redirecting effort toward read-soundness and local-reader settings.

# Related Work

\textbf{Qualitative reasoning and tractability.} Allen's interval algebra \citep{Allen1983}, the convex point algebra \citep{Vilain1986}, and RCC-8 \citep{Randell1992} supply exact composition tables; Mackworth's path consistency \citep{Mackworth1977} iterates length-2 intersections to a fixpoint. Tractability is well charted: path consistency is \emph{complete} for the convex point algebra and the ORD-Horn fragment \citep{Nebel1994} but only \emph{sound-but-incomplete} for full Allen IA and RCC-8 \citep{Renz1999}. These frameworks assume a clean, human-given table on already-formal data; none read the algebra off natural language via an LLM, certify reading errors, narrow by intersecting LLM disjunctions, or model a recall-bounded redundancy optimum. We import the algorithms and inherit the tractability facts (our point-algebra arm is exact; Allen/RCC-8 collapse rates are lower bounds).

\textbf{Closure over machine-extracted temporal relations.} SputLink computes temporal closure to densify TimeBank annotations \citep{Verhagen2005}; CAEVO performs global temporal inference by cascaded sieves \citep{Chambers2014}; structured learning enforces transitivity for extraction \citep{Ning2017}. All commit to a single globally consistent labeling to maximize F1, preserve no disjunction, certify no reading error, and do not abstain. Critically, SputLink-style closure \emph{produces} the non-adjacent gold whose circularity we must avoid; we therefore evaluate against direct human-timeline gold \citep{Rogers2019} and manual long-distance gold \citep{Naik2019}.

\textbf{Consistency enforcement under the commit contract.} A zero-shot temporal study reports LLMs assign multiple relations to $50$--$97\%$ of pairs and that ILP consistency-enforcement does not raise F1 \citep{Kougia2024}; the most recent global temporal-graph generator still ILP-commits to one label per pair \citep{Eirew2025}. METRE trains a multi-label head to model temporal-relation ambiguity \citep{Hu2024} but is F1-trained, carries no set through a composition table across multiple paths, and does not abstain -- we use it conceptually as the alternative-reader contrast that future work plugs into the same closure pipeline at matched recall. LOCO-LMs fine-tune for propositional consistency at training time \citep{Calanzone2024}; we are training-free, at inference time, over a relation algebra.

\textbf{LLM reasoning, formalization, and abstention.} Chain-of-thought \citep{Wei2022} and self-consistency \citep{Wang2022} operate at the answer level and cannot see that individually popular composition steps are jointly inconsistent. Logic-LM self-refines on solver crashes \citep{Pan2023} and LINC majority-votes formalizations \citep{Olausson2023}, but neither maintains a positive global invariant over relational knowledge. Path-of-Thoughts reasons each extracted path independently \citep{Zhang2024}, beating prior methods on multi-hop spatial and kinship benchmarks \citep{Shi2022, Sinha2019} -- precisely the cross-path intersection gap Mode~A fills -- and rule-induction methods \citep{Zhang2023, Zhu2023} fit rules to data rather than enforcing algebraic law. Selective prediction \citep{Geifman2017} abstains on generic uncertainty; our abstention is structural, triggered when deductive closure leaves a disjunction. RuleTaker \citep{Clark2020} targets propositional entailment, an out-of-scope contrast to our relational composition. Reiter's model-based diagnosis \citep{Reiter1986} supplies the minimal-hitting-set machinery for the Mode-B repair we scope as future work. Hallucination in generation is a broad concern \citep{Ji2022}; our contribution is a per-edge, certificate-backed reduction rather than a generic confidence filter.

# Method

## Overview and the inverted output contract

The deduction module sits downstream of atomic extraction: it receives, for each pair of mentions that co-occur in a span, the relation the text licenses, and it must answer queries about pairs that do \emph{not} co-occur. We model the relations as a Qualitative Constraint Network (QCN): nodes are events/entities, and each edge carries a \emph{set} of base relations from a relation algebra $\mathcal{A}$ (the disjunction of relations not excluded by the evidence). The query (held-out) edge starts at the universal set. Three design commitments define the contract.

First, the LLM is a \emph{disjunctive, high-recall reader}: for each span it emits the maximal sound set of base relations the text does not exclude, with an explicit universal/underdetermined option, rather than committing to one relation. Soundness of an edge means its set contains the gold relation; recall is $P(\text{gold} \in \text{emitted set})$. Second, composition and converse come from the \emph{exact published table} of $\mathcal{A}$, never from the LLM. Third, the system narrows by closure and \emph{abstains} when the query edge remains a non-singleton.

## Two modes of value

\textbf{Mode~A (sound narrowing, primary).} When every contributing edge set is sound but sub-universal, intersecting the compositions arriving at the query pair from multiple paths yields a set that still contains gold yet is strictly tighter than any single path. The load-bearing metric is the \emph{singleton-resolution-to-correct} yield: the fraction of multi-path queries whose intersection collapses to the single correct relation (only this moves selective accuracy and the hallucination rate; strict-tightening is reported separately and is non-load-bearing). Mode~A requires only sub-universal breadth and multi-path bite; it does not require over-commitment, and its zero-FP guarantee survives path-consistency incompleteness because \emph{the intersection of sound sets is always sound}.

\textbf{Mode~B (detection/repair, secondary).} An empty closure is a deductive certificate that some edge is unsound, with no gold labels. It fires only when at least one over-committed or recall-failed edge is present, and it carries a pre-registered dual -- \emph{silent wrong narrowing}: an unsound set that \emph{omits} gold can drive closure to a confident wrong singleton with no collapse. We bound this per-edge by $(1-\text{recall})$ and per-network by $(1-J(E))$, where $J(E)$ is the empirical joint soundness defined below.

## Iterated closure versus naive intersection

We instrument three closure variants in one pipeline [ARTIFACT:art_K7riobQ_Rmwz]. \textsc{Full} is iterated Mackworth PC-2 run to a fixpoint with algebra-seeded converse propagation (our method). \textsc{Naive} intersects the compositions arriving at the query pair in a single pass, without iterating and without converse seeding -- i.e. Path-of-Thoughts plus one obvious intersection step. \textsc{Off} performs no propagation. A theorem we exploit and verify: on length-2 multi-path queries \textsc{Naive} equals \textsc{Full}; they diverge only on networks with $\geq 3$-edge paths or cyclomatic structure, where iterated propagation reaches tight-edge anchors a single pass cannot. The full-minus-naive gap is therefore the signature of \emph{iteration}, isolating our claim from "any intersection helps."

## Redundancy as a coding rate: the empirical inverted-U

Because Mode~A's zero-FP property holds only when all contributing edges are sound, and a single LLM reading one document produces positively correlated errors, we do not assume independent per-edge soundness. Instead of the product $\prod_e r_e$ we \emph{measure} the empirical joint soundness $J(E)$ = the realized fraction of $E$-edge constraining subnetworks in which all edges are sound, and we report the within-document cross-edge error correlation $\rho$. The inverted-U cost term is $1-J(E)$; positive $\rho$ makes $J(E)$ decay slower than $r^E$, so the predicted peak sits further out than an independence model says. Net gain rises while marginal narrowing dominates, then falls once silent-narrowing cost dominates -- an error-correcting code's optimal rate with the decoding radius set by recall and the channel correlation measured, not assumed.

## The a-priori envelope gate (T0)

Before spending any LLM budget, we compute from each gold graph \emph{alone} a four-stage funnel over held-out edges [ARTIFACT:art_K7riobQ_Rmwz]: (i) a structural deduction-required proxy (the two events share no local/adjacent span, i.e. sentence distance $> 1$); (ii) constrained by $\geq 2$ paths through distinct intermediates; (iii) a non-universal composition that retains bite after non-convex widening; (iv) cross-path intersection equal to the gold singleton ($N^\ast$). We also report the $\geq 3$-edge/cyclic prevalence (the real-text iteration envelope), the widening-induced bite loss, and a paired-bootstrap power calculation. The applicability threshold is pre-registered as a number: deduction-required-multi-path-with-bite fraction $\geq 10\%$ = general mechanism, $5$--$10\%$ = useful module, $<5\%$ = niche safety-net. The expected outcome -- MATRES $N^\ast\!\approx\!0$ (adjacent-sentence gold) versus a dense timeline $N^\ast \gg 0$ -- is itself a reported result validating the gate as discriminative rather than vacuous.

## Datasets, baselines, and metrics

\textbf{Real corpora} [ARTIFACT:art_PNrS9T8JeATf]. The dense co-primary is \emph{NarrativeTime}, a timeline-based, full-TLink-coverage human re-annotation of TimeBank-Dense \citep{Cassidy2014} (36 docs, 1{,}715 events, dense gold) \citep{Rogers2019}; its start-points instantiate the convex point algebra (path consistency complete, table exact), and its non-local gold is human-timeline-placed rather than algorithmic-closure output. Our build reproduces the shipped TLINKs exactly (a blocking gate over 207{,}496 relation-multisets), so the gold is non-circular. \emph{TDDMan} (TDDiscourse) supplies manually annotated long-distance ($>1$-sentence-apart) pairs that "cannot be inferred automatically from existing annotations" \citep{Naik2019} -- a structurally non-circular anchor. \emph{MATRES} \citep{Ning2018} annotates only same/adjacent-sentence pairs and serves as the gate-validation control.

\textbf{Synthetic backbone} [ARTIFACT:art_ghVQmxVlmOJJ]. 35{,}100 globally-consistent QCNs over the convex point and Allen algebras (primary) and RCC-8 (secondary), generated by model-based realization so the gold atomic relation on every edge is exact and the network is consistent by construction. Redundancy $P$, hop length $L$, and cyclomatic number $\mu$ are swept independently; a correctness gate (composition along every enumerated path contains the gold query relation) passes on all 35{,}100 networks.

\textbf{Baselines}, each given a matched abstention signal thresholded to the same coverage object (single-relation resolution): a raw LLM (verbalized confidence), chain-of-thought \citep{Wei2022}, self-consistency \citep{Wang2022}, LINC-style multi-formalization voting \citep{Olausson2023}, Path-of-Thoughts with path-agreement abstention \citep{Zhang2024}, the ILP-commit contract \citep{Eirew2025}, and \textsc{Naive} single-pass intersection (the iteration contrast); verified composition/converse tables, baseline configurations, and the corrected provenance of the consistency-no-F1-gain result \citep{Kougia2024} are drawn from an implementation dossier [ARTIFACT:art_aQ2Rf8rwqteI]. \textbf{Metrics}: singleton-resolution-to-correct and selective accuracy at matched coverage (headline), end-to-end confident-wrong (hallucination) rate, the zero-FP audit conditioned on $J(E)$, the full-minus-naive gap versus hop/cyclomatic structure, applicability $N^\ast$, and per-edge recall.

# Experimental Setup

We pre-registered a tiered plan that the artifacts execute in order. \textbf{T0} (zero LLM spend) is the envelope gate [ARTIFACT:art_K7riobQ_Rmwz]. \textbf{Tier-1 synthetic} de-risks the three mechanism claims on clean ground truth at full scale (600 networks/cell, 378 cells, 2{,}000 bootstrap resamples) [ARTIFACT:art_TV5eEjdDP-Xp]. The \textbf{recall-bite frontier pilot} sweeps a five-setting breadth knob on real corpora plus a synthetic battery and applies a pre-registered go/no-go [ARTIFACT:art_glhgFsBUrcYo]. The reading model is \texttt{google/gemini-3.1-flash-lite} at temperature 0 with a SHA-256 disk cache and a hard cost guard; total LLM spend was \$0.58 over the pilot's life and \$0 on the cached re-run. The QCN engine is bitmask-encoded and validated by a gating test suite: the Allen 169-cell table matches the published cells and the composition-converse law (0 failures), convex point completeness is confirmed against brute force (0 mismatches over 200 networks), and the iteration-isolation unit test confirms \textsc{Full}$=$\textsc{Naive} on a length-2 query and \textsc{Full}$\neq$\textsc{Naive} on a 3-hop chain [ARTIFACT:art_K7riobQ_Rmwz]. All synthetic results are fully deterministic; closure runs in $\sim$60s on 4 cores per experiment.

# Results

## The a-priori gate is discriminative and locates the structure

The T0 gate, run over three real corpora at zero LLM cost (59.6s total), behaves exactly as the design predicted [ARTIFACT:art_K7riobQ_Rmwz]. MATRES, whose gold is entirely same/adjacent-sentence, yields $N^\ast = 0$ (applicability $0.0$, niche band): the deduction-required gate correctly reports that there is nothing to deduce, confirming the gate is discriminative rather than vacuous. The dense NarrativeTime timeline yields $N^\ast = 25{,}450$ on its point-algebra arm out of 28{,}840 evaluable held-out edges -- applicability $0.882$, the \emph{general-mechanism} band -- recovered \emph{exactly} (the point algebra is complete), with $88.6\%$ of edges purely-timeline-implied (non-circular) and paired-bootstrap power $0.96$ at the pre-registered minimum effect $0.10$ (true-$N$ MDE $0.05$). TDDMan, the non-circular manual long-distance anchor, lands in the \emph{module} band (applicability $0.085$; $N^\ast = 408$ on the Allen arm, a sound lower bound), power $0.95$.

[FIGURE:fig5]

A subtler arm-scoping result emerges from the same gate. On NarrativeTime the iterated-PC advantage over single-pass is \emph{zero} (\texttt{full\_only}$=0$): the dense timeline is near-transitively closed, so a single intersection pass already has direct evidence for almost every query. The genuine iteration advantage appears only on \emph{sparse} long-hop gold: TDDMan exhibits 12 held-out edges that \textsc{Full} resolves but \textsc{Naive} cannot (\texttt{full\_only}$=12$; $408$ vs.\ $396$ resolved). This matches the theory -- iteration pays only on $\geq 3$-edge/cyclic structure -- and tells us the iteration claim must be demonstrated on sparse or synthetic long-hop networks, not dense timelines. The gate thus delivered its purpose: a GO on NarrativeTime for narrowing, with iteration scoped to TDDMan and synthetic data, all decided before any LLM spend.

## The mechanism works on clean ground truth: iteration, the inverted-U, and a zero-FP certificate

On the synthetic backbone, all three mechanism claims pass at full scale [ARTIFACT:art_TV5eEjdDP-Xp].

\textbf{Iteration error-corrects (H3).} The full-minus-naive selective-accuracy gap is a structural $0.0$ at hop length $L=2$ (95\% CI $[-0.047, 0.048]$, includes zero -- the predicted tie), then grows monotonically with chain length to $0.888$ at $L=3$, $0.955$ at $L=4$, $0.970$ at $L=5$, and $0.988$ at $L=6$ (Page trend $p\approx1.2\times10^{-4}$; Jonckheere $z=17.2$, $p\approx0$). The gap also rises with cyclomatic number, from $0.727$ at zero chords to $0.865$ at three. \textsc{Naive} resolves essentially nothing beyond $L=2$ ($\text{acc}=0.0$ for $L\geq3$), confirming that the contribution is specifically \emph{iterated} fixpoint propagation, not a single intersection.

[FIGURE:fig3]

\textbf{Redundancy is a recall-dependent inverted-U (H4).} The Mode-A resolution rate is an inverted-U in path redundancy $K$, and the optimum moves outward with per-edge recall: peak $K^\ast = 2, 4, 5, 5, 8$ as recall ranges over $0.5, 0.6, 0.75, 0.9, 0.95$. Under positive cross-edge correlation $\rho$, the measured joint soundness $J(E)$ exceeds the independence model $r^E$, pushing the optimum further out still (low-recall benefit-centroid shift $+0.95$), and the recall-floor gate shifts it outward again. Crucially, the redundancy downside manifests as \emph{detected collapse}, not silent error: as $K$ grows, the collapse rate rises (e.g. $0.14 \to 0.71$ at recall $0.5$) while the abstain rate falls, so over-redundancy converts to certificates rather than confident mistakes.

[FIGURE:fig4]

\textbf{The certificate is exactly zero-FP (C3).} Among the $97{,}803$ networks whose contributing edges are all sound, the Mode-A output contains the gold relation with probability $1.0$ -- the soundness invariant of path consistency -- and a detected collapse never co-occurs with an all-sound network. The overall silent-wrong rate is $5.8\%$; unsound networks decompose into $40.0\%$ absorbed-correct, $38.2\%$ detected-collapse, $11.2\%$ abstain, and only $10.6\%$ silent-wrong. The pre-registered "contains-gold slope $\approx 1$ on $J(E)$" target was not met -- the measured slope is $0.66$ -- but in the conservative direction: the convex algebra absorbs most single unsound reads, so gold is retained \emph{more} robustly than $J(E)$ predicts. We report this honestly as a certificate that over-delivers, with the slope offset correctly attributed to the independence approximation failing (the offset shrinks under $J(E)$) rather than to a soundness failure. The Allen generality arm replicates the inverted-U and the zero-FP certificate, with collapse rates reported as a lower bound (path consistency is incomplete for full Allen).

## The decisive finding: read-soundness, not closure, is the bottleneck

The recall-bite frontier pilot connects the validated mechanism to the messy reality of reading relations off news text, and its verdict is the paper's most decision-relevant result: \textbf{NO-GO/NICHE on real text, because the binding constraint is LLM read-soundness, not the closure step} [ARTIFACT:art_glhgFsBUrcYo].

[FIGURE:fig2]

Sweeping the breadth knob from "name the single relation" (S1) to "name the maximal sound set" (S5) traces recall and bite in direct tension on the same knob. Per-edge recall tops out below the pre-registered soundness gates on every real arm: TimeBank-Dense (the NarrativeTime stand-in) reaches $0.796$, MATRES $0.860$, and TDDMan only $0.579$, against gates of $0.85$ (Allen) and $0.90$ (point). Pushing the knob toward higher recall inflates breadth -- at S5 the universal-set rate reaches $0.37$ -- so the sets become too loose to resolve singletons even when sound. No recall-gated operating point reaches the $5\%$ deduction-yield floor; hence the pre-registered NO-GO. By contrast, the synthetic clean-text battery reaches recall $0.958$ at \emph{every} knob and resolves $42\%$ of deduction-required queries to the correct singleton (S1 $0.417$, S5 $0.375$), comfortably above the $10\%$ general-mechanism floor. \emph{The closure mechanism works whenever reads are sound; the failure on real text is upstream, in reading.}

Two corollaries sharpen the boundary. First, gate validation passes inside the pilot too: MATRES's deduction-required fraction is $0.000$ and its deduction-yield $0.0$, as constructed. Second, and importantly for how the contribution should be measured: on real long-distance edges read \emph{with full document context}, iterated closure provides essentially no net gain over the direct read ($\Delta \leq 0$; best closure singleton-to-correct $0.172$ vs.\ direct read $0.184$). The reason is that a full-context reader already exploits the global evidence closure would reconstruct. A local-only probe confirms the diagnosis: local reads pin the gold singleton only $26.7\%$ of the time, so closure's value must be measured against a \emph{local-only} reader (a pipeline reading one span at a time) rather than a full-context oracle. The within-document error correlation is $\rho = 0.10$, with measured joint soundness $J(2)=0.55 > r^2 = 0.48$ and $J(3)=0.34 > r^3 = 0.33$ -- positive correlation that, as the synthetic model predicts, pushes the redundancy optimum outward.

# Discussion

\textbf{What the evidence supports, and what it does not.} The three mechanism claims -- iteration error-corrects, the redundancy optimum is a recall-dependent inverted-U, and the certificate is exactly zero-FP -- are established on clean ground truth with adequate power and pre-registered trend tests. The a-priori gate is validated as discriminative ($N^\ast{=}0$ on MATRES, $25{,}450$ on NarrativeTime). What is \emph{not} supported this iteration is the real-text headline (Mode-A beating Path-of-Thoughts and voting at matched coverage, and an end-to-end hallucination-rate reduction on real news): the pre-registered recall gate fired NO-GO because a cheap reader cannot read real temporal relations soundly enough. Per our pre-registered escalation ladder, this demotes real text to an honestly scoped niche/safety-net boundary and makes the synthetic mechanism plus the bottleneck localization the headline. We resist the temptation to spin the real-text result as future work: it is a measured frontier, and the measurement is the contribution.

\textbf{Why the bottleneck localization matters.} A recurring puzzle in neuro-symbolic temporal reasoning is that consistency enforcement does not improve F1 \citep{Kougia2024, Eirew2025}. Our frontier explains the mechanism behind that puzzle from the opposite direction: when reads are sound (synthetic, recall $0.96$), exact closure resolves $42\%$ of deduction-required queries and the certificate is provably zero-FP; when reads are not sound (real news, recall $0.57$--$0.86$), no global operation can manufacture the missing soundness, and a full-context reader already captures whatever the global structure would contribute. The actionable implication is that effort in this space should move from consistency-enforcement and from full-context readers toward (a) raising per-edge read recall to the $0.85$--$0.90$ regime and (b) the local-reader setting, where a span-at-a-time pipeline has genuine information for closure to recover -- exactly the setting the local-only probe ($26.7\%$ gold-pinning) shows is non-trivial.

\textbf{Connection to the text-to-logic pipeline.} The module satisfies the surrounding pipeline's stated requirements: it is training-free and runs in milliseconds on commodity hardware; it preserves disjunction and abstains, so its outputs are certificate-backed rather than confidently guessed; and it emits a trace-graph (the QCN, which compositions fired on which paths, and any repair) that can be discharged in SWI-Prolog or ASP for a replayable proof. It targets multi-hop deduction specifically while holding atomic extraction precision/recall fixed, and it works over a relation algebra rather than a propositional encoding, avoiding the simplistic-propositional pitfall that motivated the project.

\textbf{Limitations.} (1) The real-text Mode-A and end-to-end hallucination claims are gated on reader improvement and were not confirmed; our positive narrowing evidence is synthetic plus the a-priori structural gate. (2) Path consistency is complete only for the convex point algebra; Allen/RCC-8 collapse and recovery numbers are sound lower bounds. (3) The synthetic reader is a controlled noisy channel; although we match per-edge error-type, correlation, and topology distributions to the real frontier, the total-variation distance to real error types is $0.25$, so the synthetic regime is an idealization of, not a substitute for, real reading. (4) Mode-B repair quality, the RCC-8 second-algebra arm, the CLUTRR elicited-table and absent-relation end-to-end demos, and the METRE-style alternative-reader agnosticity test were scoped as Tier-2 and are not executed here. (5) The deduction-required proxy for NarrativeTime uses a whitespace/punctuation sentence segmentation; MATRES and TDDMan locality is exact.

# Conclusion

We treated the deduction step of a text-to-logic pipeline as a coding problem: keep the LLM as a high-recall disjunctive reader, and let exact relation-algebra path consistency error-correct over the redundant constraining paths a document supplies. On clean ground truth the mechanism delivers exactly as the coding-theory lens predicts -- iterated closure (not a single intersection) error-corrects with a gap that grows from $0.0$ at hop~2 to $0.99$ at hop~6, the net narrowing gain is an inverted-U whose peak ($K^\ast=2,4,5,5,8$) tracks per-edge recall, and the certificate is exactly zero-false-positive with the only downside being detected collapse rather than silent error. A zero-LLM-spend envelope gate decides a-priori where the mechanism can apply ($N^\ast{=}0$ on adjacent-sentence MATRES, $25{,}450$ on the dense NarrativeTime timeline). And a recall-bite frontier localizes the true obstacle on real news text: read-soundness, not closure. We see three concrete next steps: (1) raise per-edge read recall into the $0.85$--$0.90$ regime, where the validated mechanism predicts a real-text payoff; (2) measure closure's value against a local-only reader, the setting the data show is non-trivial; and (3) execute the Tier-2 arms -- Mode-B repair, RCC-8, and the alternative-reader agnosticity test -- now that the mechanism and its operating envelope are characterized.

\bibliographystyle{plainnat}
\bibliography{references}

</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

--- Item 1 ---
id: art_aQ2Rf8rwqteI
type: research
title: >-
  Implementation/Resource Dossier for the Closure-Certified Text-to-Logic Deduction Module
summary: >-
  Verified, executor-ready specifications for the closure-certified temporal-deduction pipeline: (1) corpus access+parse formats
  for NarrativeTime (repo github.com/text-machine-lab/nt, MIT, nt_format JSONL with per-event numeric `time` coordinate +
  bracket-type interval model + same-branch get_event_relation), TDDMan (4-col TSV, codes a/b/i/ii/s, join text from TimeBank-Dense;
  long-distance non-auto-inferable gold), and MATRES (start-point convex point algebra, 2-sentence window = N*~=0 gate control);
  (2) machine-readable GQR composition/converse tables for Allen (13 tokens with < / > for before/after), convex point algebra
  (with the only-non-convex != -> universal widening rule), and RCC-8, each with verified unit-test cells; (3) Mackworth PC-2
  iterated a-closure pseudocode + the precise naive single-pass-intersection contrast (naive==full on length-2, diverges at
  hop>=3 / cyclomatic>=1) + soundness/completeness tractability facts (point-algebra arm EXACT, full Allen/RCC-8 a LOWER BOUND);
  (4) the Renz-Nebel A(n,d,l) model plus the scenario-then-abstract recipe for guaranteed-consistent synthetic QCNs with independent
  density/hop/cyclomatic/recall knobs; (5) baseline configs each with a matched abstention signal (Path-of-Thoughts, self-consistency,
  LINC, DSR-LM/HtT, ILP-commit Eirew et al. M=5, METRE) and a corrected citation (the >=50-97% multiple-relation + ILP-no-F1-gain
  facts are Kougia et al. arXiv:2406.11486, not 'Knez & Sun'); (6) OpenRouter model choice (primary google/gemini-2.5-flash-lite
  $0.10/$0.40, second-family DeepSeek-V3.2/Qwen2.5-72B/Llama-3.3-70B) with arithmetic showing <$10 and a disk-cache + hard
  cost-guard strategy; and (7) the operationalized three-part realism-matching statistic (per-edge error-type TV<=0.10, cross-edge
  soundness-correlation |dro|<=0.10 via ICC, topology histogram TV<=0.15) with J(E) vs r^E. Includes a full decision table,
  a 12-item gotchas list, and 3 unresolved follow-ups.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_PNrS9T8JeATf
type: dataset
title: 'Fold-split gold temporal relation graphs: NarrativeTime, TDDMan, MATRES'
summary: |-
  Frozen, reusable real-text gold temporal relation graphs that all downstream real-text closure experiments (the T0 envelope go/no-go pilot now; later arms) consume. Schema exp_sel_data_out, grouped by dataset, ONE example per (corpus, document) row (345 examples): input = the stripped document text (string), output = json.dumps(gold_graph) (string; parse with json.loads). The gold_graph has nodes [{node_id, node_type in {event,timex,dct}, surface, char_start, char_end, global_token_index, sentence_index, eiid/tid/eid, event_class, plus nt_event_type/nt_time/nt_branch/nt_start/nt_end for NarrativeTime}] and edges [{source, target, native_relation, canonical_algebra, canonical_relation_set, coarse_superset_set?, startpoint_relation_set, vague_widened, src/tgt_sentence_index, sentence_distance, locality_class in {intra,adjacent,long_distance}, structural_deduction_required_proxy (dist>=2), locally_justifiable_proxy (dist<=1), edge_fold, phenomena?}], plus per_doc_descriptive_counts. Each example also carries metadata_corpus/doc_id/fold/n_nodes/n_edges/n_events/long_distance_edges/descriptive_counts.

  Three corpora by role: (1) NarrativeTime (36 docs, 1,715 events, 103,748 edges, dense full TLink coverage, 1.58M event-event triangles) is the DENSE headline host; relations are produced by the corpus authors' OWN code (narrative_time.event_relations + conversion_utils), reproducing the shipped nt_converted_to_tml TLINKs EXACTLY (blocking gate: 207,496 relation-multisets + node counts match across all 36 docs) — non-circular gold; canonical_algebra=interval_allen with start-point point relations, non-convex {<,>} widened to {<,=,>} (vague_widened, 124 edges). (2) TDDMan (34 docs, 6,137 manually-annotated event-event pairs, 99.9% long-distance >=2 sentences apart) is the non-circularity anchor; codes {b,a,s,i,ii} mapped to tightest Allen + coarse superset + convex point sets; 107 test pairs carry TDDiscourse phenomena tags. (3) MATRES (275 docs, 6,099 events, 13,577 edges, 0% long-distance: 30% intra / 70% adjacent) is the gate-validation control with a near-empty deduction envelope; point algebra (BEFORE/AFTER/EQUAL/VAGUE -> {<}/{>}/{=}/{<,=,>}, no non-convex relations).

  Folds: document-level TimeBank-Dense 22/5/9 train/dev/test for NarrativeTime/TDDMan; MATRES train(TimeBank+AQUAINT)/test(Platinum); TDDMan edges also carry native edge_fold. One frozen NLTK Punkt sentence segmentation is reused across NarrativeTime/TDDMan; MATRES uses the canonical qiangning per-token sentence ids with SENTDIFF as authoritative distance. A doc-id overlap table (overlap_table.json) shows 33 documents shared by all three corpora. Aggregate + per-document DESCRIPTIVE structural counts (sizes, native/canonical label distributions, locality distribution, triangles, >=2-intermediate query edges, cyclomatic number, >=3-hop pairs) are in descriptive_counts.json. The gated statistics (deduction-required N*, bite-after-widening, singleton-resolution) are intentionally NOT computed here — they need composition closure / held-out-edge resolution and are the T0 experiment's job. Caveats: 1 TDDMan eid absent from the muk343 .tml version (APW19980213.1310/e257, 13 pairs dropped, reported in metadata.coverage_gaps); 238/6,099 MATRES events (3.9%) lack a char offset (boundary edge cases) but retain sentence_index + global_token_index; every non-null MATRES offset is surface-exact by construction; NarrativeTime gold uses annotator a1. Sources cited in README.md and metadata.sources (CogComp MATRES, qiangning EMNLP19 XML, TDDiscourse, text-machine-lab narrative_time, muk343 TimeBank-Dense, TempEval-3 TBAQ-cleaned). Reproduce via data.py / build_dataset.py with pinned pyproject.toml. An optional 4th TimeBank-Dense corpus builder is available (builders.build_timebank_dense) but not emitted.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 3 ---
id: art_ghVQmxVlmOJJ
type: dataset
title: >-
  Synthetic QCN Backbone: consistent Allen/Point/RCC-8 networks with NL realizations
summary: |-
  Clean-ground-truth SYNTHETIC backbone for the redundancy (H4) and iteration (H3) claims: 35,100 globally-consistent Qualitative Constraint Networks over three relation algebras -- convex Point ('<','=','>') and Allen Interval (13 relations) as PRIMARY (500 networks/cell), RCC-8 (8 relations) as SECONDARY (300/cell). Every network is built by model-based realization (integer points / integer-grid intervals / collinear integer discs), so the gold ATOMIC relation on each edge is read exactly off the model and the whole scenario is globally consistent BY CONSTRUCTION (no solver needed). Composition + converse come from the authoritative alreich/qualreas tables, independently cross-checked by 436 tests (Allen composition matches exhaustive endpoint-CSP enumeration; RCC-8 reader sound vs disc enumeration; relation-algebra identity/converse axioms).

  Each network has a held-out query pair (s,t) that shares no edge and never co-occurs in one sentence -- DEDUCTION-REQUIRED: the query relation is obtainable only by composing >=1 multi-edge path. Topology is independently swept across 27 cells per algebra: redundancy P in {1,2,3,4,6,8}; hop L in {2,3,4,5}; cyclomatic mu in {0,1,2,3} via chord augmentation; small/medium/large node-count regimes; and random Renz-Nebel A(n,d) for the natural joint distribution. The intended structural signal is clean (results/dataset_metadata.json -> cell_summary): singleton-resolution rises monotonically with redundancy P (allen 0.40->0.89), bite decays with hop length, cyclomatic augmentation adds paths.

  Output is the aii exp_sel_data_out schema with 3 datasets (synthetic_qcn_point / synthetic_qcn_allen / synthetic_qcn_rcc8); ONE ROW = ONE network. input = template NL realization (one professional-prose sentence per non-query edge, 2-3 paraphrases per relation, + a final 'Query:' line); output = JSON string of the gold graph {edges:[{source,target,relation}], query_edge:{...,is_query:true}}. Rich metadata_* per row: fold (pilot/dev/test by md5(seed)%100 within each cell), algebra, cell labels, MEASURED structure (cyclomatic_number, cycle_basis_size, num_simple_paths_s_t, paths_truncated, contributing_edge_count, avg_degree), enumerated s-t paths with per-path gold composition + naive_intersection + has_bite + singleton_resolved, abstract_graph, entity_map, reference_disjunctive_labels (SOUND superset per edge; convex-only for point), model_embedding, seed. The CORRECTNESS GATE -- composition of gold atomic relations along every enumerated path CONTAINS the gold query relation -- passed on all 35,100 networks. Pre-registered realism thresholds (validated=false; TV<=0.15 / rho<=0.10 / EMD<=0.10) are recorded for next-iteration matching against the real-text frontier pilot.

  Files: full corpus split into full_data_out/full_data_out_1.json + full_data_out_2.json (each <100 MB; concatenate datasets with the same name across parts to reconstruct), plus mini_data_out.json (3 examples/algebra) and preview_data_out.json (10 examples/algebra, strings truncated). Generated deterministically by `uv run data.py` (~18 s on 4 cores; per (algebra, cell, index) md5 seeds, resumable). QA/provenance/dataset-card in results/dataset_metadata.json; algebra package + 436-check verification suite in qcn/ and tests/. The real-text corpora (NarrativeTime / TDDMan / MATRES) are delivered by SIBLING artifacts and are NOT duplicated here.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 4 ---
id: art_K7riobQ_Rmwz
type: experiment
title: Zero-LLM T0 Envelope Gate + QCN Path-Consistency Engine over Temporal Corpora
summary: |-
  Implements and unit-validates a reusable Qualitative Constraint Network (QCN) path-consistency engine and runs the decisive zero-LLM-spend T0 envelope gate over three real temporal corpora, deciding whether (and where) a real-text headline is viable before iter-2 spends any LLM budget.

  ENGINE (engine.py): bitmask-encoded Algebra (Allen-13, convex Linear Point, RCC-8) loaded from authoritative qualreas tables (bundled in algebras/ for self-containment), a QCN, and THREE instrumented closure variants used as METHOD vs BASELINES in one pipeline: pc2_full = FULL iterated Mackworth PC-2 to fixpoint (OUR METHOD); naive_single_pass = single pass of length-2 intersections at the query edge (BASELINE, Path-of-Thoughts-style); closure_off = no propagation (lower baseline). Predictions appear per example as predict_our_method_full_pc / predict_baseline_naive_singlepass / predict_baseline_closure_off, with gold as output.

  ENGINE VALIDATION (tests.py, gates everything, ALL PASS): Allen 169-cell table validated against published Allen-1983 canonical cells + the composition-converse algebra law on all 169 cells + converse involution + identity; convex point COMPLETENESS confirmed vs brute-force enumeration (0 label/consistency mismatches over 200 random nets) => point arm is EXACT; A<B<C<A detected inconsistent; iteration isolation (FULL==NAIVE on a length-2 query, FULL!=NAIVE on a 3-hop chain).

  CORPORA (parsers.py, gold only, cached to cache/ for iter-2 reuse): MATRES (CogComp txt + qiangning EMNLP-19 sentence alignment) -> convex point on start-points; 100% of pairs are same/adjacent sentence (SENTDIFF in {0,1}). TDDMan (TDDiscourse tsv, strict Allen map + broad sensitivity) -> all pairs deduction-required by construction (non-circularity anchor). NarrativeTime (text-machine-lab annotator a1 timeline coords) -> dense full-coverage point gold + Allen interval arm.

  T0 FUNNEL + RESULTS (method.py -> method_out.json, exp_gen_sol_out schema-VALID): per held-out edge funnel evaluable -> (i) deduction-required -> (ii) multi-path -> (iii) bite-after-widening -> (iv) N* exact recovery, plus the >=3-edge/cyclic iteration envelope (full_only), widening bite-loss, paired-bootstrap power + faithful normal-approx MDE at true N, and the NarrativeTime locally-justifiable vs purely-timeline-implied split. Findings: MATRES N*=0 (control; gate discriminative). TDDMan applicability 0.085 (module band; 0.104 broad), N*=408, full_only=12 -> genuine iterated-PC advantage on sparse manual long-distance gold; Allen recovery is a sound LOWER BOUND. NarrativeTime applicability 0.882 (general band), N*=25450 recovered EXACTLY, but full_only=0 because the dense timeline is near-transitively-closed so single-pass already has direct evidence (iteration ties single-pass on dense gold; 88.6% of edges purely-timeline-implied). Power: both real arms clear the pre-registered min effect 0.10 with power>=0.80 (NarrativeTime true-N MDE 0.05). A complete-graph fast path (full-PC == single-pass on complete graphs) was VERIFIED against genuine PC on 1095 cross-checks (0 mismatches), keeping runtime ~60s.

  VERDICT (hosting_decision.verdict_text): GO -> host the real-text headline on NarrativeTime; TDDMan is the non-circular corroboration arm; MATRES is the N*~0 control. This matches the pre-registered arm-scope: the certificate beats closure-off broadly, but iterated>single-pass only on SPARSE long-hop gold (TDDMan), not on dense timelines. Deliverables: engine.py, tests.py, parsers.py, method.py, bundled algebras/, reusable cache/, README.md, and full/mini/preview method_out JSON.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_TV5eEjdDP-Xp
type: experiment
title: Synthetic QCN de-risking of iterated closure (H3) and redundancy inverted-U (H4)
summary: |-
  This experiment de-risks two mechanism claims for neuro-symbolic text->logic pipelines on clean synthetic ground truth, with ZERO LLM spend. It generates consistent-by-construction Qualitative Constraint Networks (QCNs) by realization off a sampled point assignment, and simulates the LLM reader as an exactly-controlled noisy channel with three knobs: per-edge recall r (P(gold in emitted set)), a sub-universal breadth distribution, and a within-network cross-edge soundness correlation rho (latent equicorrelated Gaussian). PRIMARY algebra = the convex point algebra ({<,=,>}; path-consistency provably COMPLETE), matching the NarrativeTime start-point arm; an optional Allen interval generality arm derives the 13x13 composition table from endpoint point-relations and self-verifies it.

  METHOD vs BASELINES run side-by-side in one pipeline: FULL iterated path-consistency closure (our method) vs NAIVE single-pass query-node intersection and OFF direct-read (baselines). Mode-A answers are singleton resolutions; each is classified CORRECT / WRONG (silent narrowing) / ABSTAIN / COLLAPSE (detected contradiction = the Mode-B certificate firing).

  RESULTS at the pre-registered full scale (N=600/cell, B_BOOT=2000, 378 cells, fully deterministic, ~60s on 4 cores) -- all three hypotheses PASS:
  - H3 (iteration > naive): FULL-minus-NAIVE selective-accuracy gap is 0.0 at hop-length L=2 (structural tie, CI includes 0) and grows monotonically to 0.99 at L=6 (3/3 ordered-trend tests: Page p~1e-13, Spearman bootstrap CI [0.9,1.0], hand-rolled Jonckheere p~0); the gap also rises with cyclomatic number (0.73->0.87 over 0..3 chords). Mechanism: longer/denser chains give iteration more tight-edge anchors that single-pass intersection cannot reach.
  - H4 (recall-dependent redundancy inverted-U): the Mode-A resolution rate P(CORRECT) is an inverted-U in redundancy K; the optimum K* moves OUTWARD with recall (peak K = 2,4,5,5,8 across r=0.5..0.95) and under the recall-floor gate; under positive rho the empirically MEASURED joint soundness J(E) exceeds the r^E independence model, pushing the optimum further out (low-recall benefit-centroid shift +0.95). Crucially the redundancy downside manifests as DETECTED collapse, not silent error.
  - C3 (zero false-positive certificate): among networks whose contributing edges are all sound, P(gold in Mode-A output) = 1.0 EXACTLY (soundness invariant of path-consistency); collapse never co-occurs with all-sound; overall silent-WRONG rate is only 5.8%; unsound networks decompose into 40% absorbed-correct / 38% detected-collapse / 11% abstain / 11% silent-wrong. The pre-registered contains-gold-vs-J(E) slope~1 is NOT met (slope 0.66) -- reported honestly -- because the convex algebra absorbs most single unsound reads, so retention OVER-delivers versus joint soundness (a stronger-than-predicted certificate).
  - Allen generality arm (exploratory): 13x13 table self-verified against canonical entries (o.o={p,m,o}, d.d={d}, p.P=universal, equals=identity); the resolution inverted-U and the zero-FP certificate both replicate; collapse rates are reported as a LOWER BOUND since PC is sound-but-incomplete for full Allen (the point arm stays exact).

  DELIVERABLES: method.py (full pipeline including Stage-0 algebra self-verify and Stage-1 hand-checked toy networks), allen_arm.py, method_out.json (exp_gen_sol_out-validated; metadata holds config/seeds/breadth, per-section H3/H4/C3/modeB/Allen results, a compact summary_for_paper block, and overall_verdict; the datasets array holds 240 worked QCN query examples each carrying predict_full/predict_naive/predict_off baseline columns and metadata_* fields), four PNG figures (H3 gap-vs-L tie+growth; H4 resolution inverted-U with outward-moving peaks + channel decomposition; J(E) vs r^E; zero-FP audit), and pyproject.toml pinning numpy==2.4.6/scipy==1.17.1/matplotlib==3.11.0. Downstream paper-writing can consume metadata.summary_for_paper and the figures directly; every PASS/FAIL boolean, located peak, trend p-value, and bootstrap CI is in metadata. Verdict: H3=PASS, H4=PASS, C3=PASS.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 6 ---
id: art_glhgFsBUrcYo
type: experiment
title: Recall-Bite Frontier & Go/No-Go Pilot for Closure-Certified Temporal Composition
summary: >-
  T0/pilot viability gate for the closure-certified temporal-composition study (does NOT run the main comparison). Self-contained
  pipeline: engine.py (POINT + Allen-13 qualitative algebras built programmatically by the endpoint method, cross-checked
  against the dossier's verified GQR composition cells; Mackworth PC-2 closure, length-2 triangle narrowing, naive-single-pass
  baseline, convex '!=' -> universal widening with counting), corpora.py (three real arms: TimeBank-Dense .tml TLINKs as the
  dense NarrativeTime stand-in [ALLEN]; TDDMan TSV joined to .tml text as the non-circular all-deduction-required arm [ALLEN];
  MATRES qiangning XML as the local gate control [POINT]), synth.py (scenario-then-abstract consistent QCNs as a clean-text
  reference), llm.py (async OpenRouter client with sha256 disk cache, hard cost-guard, robust JSON/relation parsing), method.py
  (orchestrator). Sweeps a 5-setting breadth knob (S1_single -> S5_maximal) via google/gemini-3.1-flash-lite (the dossier's
  gemini-2.5-flash-lite is delisted) at temperature 0, measuring per-edge recall (with doc-clustered bootstrap CIs), breadth,
  error-type mix, triangle collapse rate, strict-tightening, singleton-to-correct (overall + deduction-required subset, with
  CI), an explicit method(closure)-vs-baseline(direct read) delta, within-document error correlation rho (ICC), J(2)/J(3)
  vs a matched independence baseline, a local-only-reader probe, and point-vs-Allen bite-lost. RESULT: VERDICT=NO-GO/NICHE
  -- no real arm clears the pre-registered recall gate at any knob (TBDense 0.80, MATRES 0.86, TDDMan 0.58; gates 0.85 Allen
  / 0.90 point), so real-text READ SOUNDNESS, not the closure step, is the binding constraint; the synthetic clean-text arm
  reaches recall 0.96 with closure deduction-resolution ~0.37-0.42 (>=0.10), and closure ~= direct read on full-context deduction
  edges (delta~=0). Gate validation PASSED (MATRES deduction-fraction 0.0); rho=0.10 with J(E)>r^E; bite-lost=0; local-probe
  pins gold only 27% on deduction edges. Spend $0.58 over 4191 billed calls, 0 parse failures, 0 API errors. Output method_out.json
  validates against exp_gen_sol_out (840 per-edge examples with predict_<knob> fields + a 30-field metadata block: frontier_table,
  selected/fallback operating point, rho, J_E, deduction_required_fraction, gate_validation, method_vs_baseline_deduction,
  applicability_verdict, synthetic block, provenance, figures). For iter-2: headline the synthetic arm, scope real text as
  a niche safety-net, and measure closure's value against a LOCAL-only reader (not a full-context reader). Three figures:
  frontier scatter, breadth-vs-recall, collapse-vs-knob.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</supplementary_materials>



<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
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
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
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
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-17 15:02:07 UTC

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
