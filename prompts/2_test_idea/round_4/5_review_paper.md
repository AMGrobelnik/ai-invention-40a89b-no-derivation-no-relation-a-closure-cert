# review_paper — test_idea

> Phase: `invention_loop` · round 4 · `review_paper`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 22:10:54 UTC

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

A growing class of systems reads a short, professionally written document---a news report, a contract clause, a children's story---into a formal representation (first-order-logic predicates, Prolog facts) that a symbolic reasoner can execute, with a large language model (LLM) resolving the terminology, concepts, and relations the surface text leaves implicit. Such a pipeline promises auditable, replayable reasoning over text, but it has a structurally identifiable weak link. Atomic extraction---naming the entities and the relations that hold between locally co-occurring mentions---is by now something LLMs do competently, if imperfectly. The \emph{deduction} step is where faithfulness breaks: synthesizing the explicitly stated facts with implicit composition knowledge to answer a query about a pair of entities that never co-occur in any single span. This multi-hop relational reasoning is what the user ultimately cares about, and it is exactly where hallucination is most damaging and hardest to detect. We therefore scope this paper, deliberately and up front, to the \emph{deduction sub-module} of such a pipeline: we measure atomic-extraction quality but do not try to improve it, we leave upper-ontology grounding \citep{Lenat1995} out of scope, and we are explicit that in every venue we run the composition table is \emph{hand-supplied}, so the LLM extracts atoms and never resolves implicit common-sense composition (one minimal exception, a single LLM-filled composition cell, is studied in Section~\ref{sec:fuzzy}).

Faithful multi-hop relational reasoning over text matters wherever the cost of a confidently wrong answer is high: ordering the events in a news story, tracking kinship in a narrative, resolving containment in a description, chaining clauses in a legal document. The relations involved---temporal order, kinship, spatial containment---are precisely those for which mathematics has supplied exact \emph{composition laws} for forty years: Allen's interval algebra \citep{Allen1983}, the convex point algebra \citep{Vilain1986}, the region connection calculus RCC-8 \citep{Randell1992}, and the path-consistency constraint-propagation algorithms over them \citep{Mackworth1977}. If a document says event $A$ is before $B$ and $B$ is before $C$, the relation between $A$ and $C$ is not a matter of opinion to be guessed; it is fixed by an exact table. The opportunity is to make an LLM-driven pipeline reason \emph{with} these laws rather than around them.

The deduction step is hard because the obvious ways of using an LLM fail in characteristic ways. Composing freely, the LLM is locally fluent but globally inconsistent: it can assign more than one temporal relation to the same pair and violate transitivity, producing silent errors that an answer-level vote \citep{Wang2022} or a solver-crash signal \citep{Pan2023} cannot see. Reasoning each path in isolation---the strategy of backward chaining \citep{Kazemi2022} and Path-of-Thoughts \citep{Zhang2024}---deliberately avoids the global check, so it can neither tighten a disjunctive query by intersecting evidence from multiple paths nor detect a contradiction arriving at the same pair from two routes. Hand-crafting composition rules (the kinship rules behind CLUTRR \citep{Sinha2019}) does not scale, and inducing rules to fit task accuracy \citep{Zhang2023, Zhu2023} optimizes data fit rather than the algebraic laws needed for soundness.

Why has this not been solved? Because the recent lineage attacks it under the wrong \emph{output contract}. A study of zero-shot temporal extraction finds LLMs assign multiple relations to over half (up to $97\%$) of pairs and violate transitivity, then enforces consistency with integer linear programming (ILP) and reports that consistency enforcement \emph{does not improve} F1 \citep{Kougia2024}; the most recent global temporal-graph generator still aggregates generations and ILP-commits to a single label per pair, preserving no disjunction, issuing no certificate, and offering no abstention \citep{Eirew2025}. Classical temporal closure (SputLink densifies TimeBank \citep{Verhagen2005}; CAEVO does global inference by cascaded sieves \citep{Chambers2014}; structured learning enforces transitivity \citep{Ning2017}) likewise commits to one consistent labeling to maximize F1. Even the newest neuro-symbolic temporal work shares this contract: NeSTR generates then abductively \emph{repairs} to a single revised conclusion \citep{Liang2025}, TReMu generates and commits Python over dialogue memory \citep{Ge2025}, discourse-level work pairs Allen-algebra prompts with reflection to \emph{commit} to one consistent label per pair \citep{Fan2025}, and GDLLM fine-tunes an LLM whose soft probabilities feed a graph network to \emph{classify} one relation per pair \citep{Zhao2025}. We read this as evidence that consistency enforcement under the F1-maximizing \emph{commit} contract is the wrong objective for faithfulness. The LLM's native multi-relation output is not noise to be collapsed; it is a \emph{sound disjunction} to be preserved and narrowed, and the right objective is faithfulness-by-abstention.

Our approach inverts the contract. The LLM emits, per text span, a high-recall disjunctive set of base relations the span does not exclude. Composition and converse come only from the exact published table. Iterated path consistency then narrows the query edge; the system \emph{emits} a singleton, \emph{abstains} on a residual disjunction, and \emph{flags an unsound read} when the closure collapses to the empty set. Two value modes follow. Mode~A (sound narrowing) intersects the disjunctive sets arriving at a query pair from multiple constraining paths; because the table is exact ground truth, the intersection of sound sets is always sound, so this is a zero-false-positive narrowing \emph{conditional on every contributing read being sound}---multi-path redundancy in a document thereby becomes an \emph{error-correcting code} over LLM extractions, with a coding-theory inverted-U optimal rate. Mode~B (detection) reads an empty closure as a gold-free certificate that some read was unsound. \textbf{The central finding of this iteration is an honest split of these two modes by their evidence class}, summarized in Table~\ref{tab:split}. The \emph{certificate} and the inherited exact-table composition \emph{transfer}: confirmed at power on a real (but templated) benchmark. The \emph{cross-path intersection coding mechanism} does \emph{not} yet transfer: a decisive real-text test came back as a sharp, interpretable scope boundary, and the mechanism remains synthetic-channel-only. We tag every number by evidence class (\textsc{theorem} / \textsc{synthetic-channel} / \textsc{gold-only-gate} / \textsc{real-llm-read} / \textsc{real-llm-read-on-synthetic}) so the reader can weight it immediately.

[FIGURE:fig1]

\begin{table}[t]
\centering
\small
\begin{tabular}{p{3.05cm}p{1.45cm}p{2.55cm}}
\hline
Contribution & Where it holds & Status \\
\hline
Inherited exact-table multi-hop composition + gold-free, training-free, per-edge \textbf{abstain-on-collapse certificate} & templated CLUTRR; certificate also on natural temporal text & \textbf{Transferable; confirmed at power} \\
Neuro-symbolic \textbf{cell-gap-filling} (LLM fills one atomic rule, engine chains) & templated CLUTRR & \textbf{Transferable; confirmed} \\
Natural-text temporal comparative advantage & NarrativeTime / TDDMan & Marginal; not robustly significant \\
\textbf{Cross-path intersection} error-correcting code + inverted-U rate & synthetic channel only & Synthetic-channel-only (real-text test = scope boundary) \\
\hline
\end{tabular}
\caption{The organizing principle of this paper: an honest split of the contribution by evidence class and by \emph{where each claim holds}. The portable contribution is the certificate plus exact-table composition; the signature cross-path coding mechanism is characterized as synthetic-only and its real-text transfer is an explicit open problem (Section~\ref{sec:decisive}).}
\label{tab:split}
\end{table}

## Summary of Contributions

\begin{itemize}
\item \textbf{A transferable closure certificate, confirmed at power on a real (templated) benchmark} (Section~\ref{sec:transferable}). On CLUTRR, a training-free, gold-free, per-edge abstain-on-collapse pipeline reaches matched-coverage selective accuracy $0.886$ versus Path-of-Thoughts $0.457$ (gap $+0.429$, Holm $p_{\text{adj}}{=}0.0015$), delivers all four pipeline goal items---atomic P/R/F1 $0.536/0.532/0.534$, multi-hop accuracy that holds $0.75$--$1.00$ through 10-hop chains, SWI-Prolog-executed traces ($40/40$ match the engine, $39/40$ match gold), and a $0.444$ absent-relation hallucination reduction reported as a risk-coverage tradeoff [ARTIFACT:art_0a7i481ZRwS1].
\item \textbf{A minimal neuro-symbolic cell-gap-filling result that substantiates the ``fuzzy-unification'' framing} (Section~\ref{sec:fuzzy}). When the LLM supplies only a missing \emph{atomic} composition rule and the symbolic engine does the multi-hop chaining, CLUTRR gap coverage is recovered at precision $1.00$ (net $+391$) and the confident-wrong rate is cut from $0.522$ to $0.000$ at full coverage; a naive story-level fill is \emph{not} net-faithful ($0.33$ precision), quantifying the right division of labour [ARTIFACT:art_OvidVcsfr5HM].
\item \textbf{A decisive negative that localizes why cross-path error-correction does not transfer} (Section~\ref{sec:decisive}). The a-priori gate is GO ($n{=}125$ gold multi-path-with-bite queries), a synthetic Allen channel confirms the mechanism at reader-recall $0.95$, yet on real text both a weak and a strong cross-family reader read constituent Allen edges as near-universe (underdetermined-rate $0.79$--$0.99$), so the intersection has zero bite---a \emph{precision/recall impossibility}: high-recall reads are sound-but-bite-free, tight reads are only $3.2\%$ correct [ARTIFACT:art_0AIWMhwc1pJM].
\item \textbf{An honest reporting correction on the natural-text temporal claim} (Section~\ref{sec:temporal}). A fixed-operating-point bootstrap shows the temporal Mode-A-vs-PoT gap ($+0.027$) has a corrected CI $[-0.088,0.140]$ that includes zero ($p{=}0.33$); the previously published significance was a bootstrap artifact. On dense temporal prose the certificate is weakly protective: among the $19\%$ of queries Mode~A answers, $42.5\%$ are confident-wrong [ARTIFACT:art_Vc1UBGIVSi0T].
\item \textbf{A decomposition and an algebra-richness scaling law} (Section~\ref{sec:decomp}). The $+0.676$ Allen system gap over per-path reasoning splits into an \emph{inherited} exact-table-vs-LLM-composition term ($+0.673$) and a \emph{novel}-on-selective-accuracy term of $\sim 0$; with real LLM reads the advantage over Path-of-Thoughts grows monotonically with base-relation count (point $3$: $+0.043 \rightarrow$ RCC-8 $8$: $+0.448 \rightarrow$ Allen $13$: $+0.676$) [ARTIFACT:art_D0cHQUJ8kY75] [ARTIFACT:art_QToTkRe6Umb8], and the redundancy inverted-U is established only on a realism-matched synthetic channel [ARTIFACT:art_FtN4LBzazO_l].
\end{itemize}

# Related Work
\label{sec:related}

\textbf{What is new, in one sentence.} Path consistency over relation algebras and consistency enforcement over machine-extracted relations are both well established; the contribution uniquely demonstrated end-to-end on a real benchmark is a \emph{training-free, per-edge, gold-free abstain-on-collapse certificate} over LLM-extracted relational facts that inverts the F1-maximizing commit contract---kept cleanly separate from the cross-path-intersection / coding-rate thesis, which we exercise only synthetically.

\textbf{Qualitative reasoning and tractability.} Allen's interval algebra \citep{Allen1983}, the convex point algebra \citep{Vilain1986}, RCC-8 \citep{Randell1992}, and the projection cardinal-direction calculus \citep{Frank1996, Ligozat1998} supply exact composition tables; Mackworth's path consistency \citep{Mackworth1977} iterates length-2 intersections to a fixpoint. Tractability is well charted: path consistency is \emph{complete} for the convex point algebra and the ORD-Horn fragment \citep{Nebel1994} but only \emph{sound-but-incomplete} for full Allen IA and RCC-8 \citep{Renz1999}. These frameworks assume a clean, human-given table on already-formal data; none reads the algebra off natural language via an LLM, certifies reading errors, narrows by intersecting LLM disjunctions, or models a recall-bounded redundancy optimum. We import the algorithms and inherit the tractability facts: our point-algebra arm is exact; our Allen and RCC-8 arms are sound lower bounds.

\textbf{Closure over machine-extracted temporal relations.} SputLink computes temporal closure to densify TimeBank annotations \citep{Verhagen2005}; CAEVO performs global temporal inference by cascaded sieves \citep{Chambers2014}; structured learning enforces transitivity \citep{Ning2017}. All commit to a single globally consistent labeling to maximize F1, preserve no disjunction, certify no reading error, and do not abstain. Critically, SputLink-style closure \emph{produces} the non-adjacent gold whose circularity we must avoid; we therefore evaluate against direct human-timeline gold \citep{Rogers2019} and manual long-distance gold \citep{Naik2019}.

\textbf{Consistency enforcement and abstention under the commit contract.} A zero-shot study reports LLMs assign multiple relations to $50$--$97\%$ of pairs and that ILP consistency enforcement does not raise F1 \citep{Kougia2024}; the most recent global temporal-graph generator still ILP-commits \citep{Eirew2025}. Our closest recent neighbors all retain a commit objective. NeSTR repairs detected inconsistencies toward a single \emph{committed} conclusion rather than preserving the disjunction \citep{Liang2025}. TReMu generates Python over timeline-summarized dialogue memory to compute and commit to one answer \citep{Ge2025}. Fan and Strube's discourse-level extractor is the contract we most directly invert: it pairs Allen-algebra-inspired prompts with reflection to commit to a single F1-maximizing label per pair \citep{Fan2025}. GDLLM fine-tunes an LLM whose soft distribution feeds a distance-aware graph attention network to \emph{classify} the one relation per pair \citep{Zhao2025}---a single-label COMMIT. METRE trains a multi-label head to model relation ambiguity \citep{Hu2024} but is F1-trained, carries no set through a composition table across paths, and does not abstain. ``When Silence Is Golden'' targets temporal abstention but \emph{trains} the skill via chain-of-thought supervision and abstention-aware rewards at the QA-answer level \citep{Zhou2026}; ours is structural, training-free, and per-edge. BeDiscovER is a recent 52-dataset discourse \emph{evaluation} suite \citep{Li2025} that contributes no reasoning mechanism. Differentiated by output contract, the cluster splits into single-label COMMIT-for-F1 (GDLLM, Fan and Strube, the ILP-commit line), abductive REPAIR / code-gen (NeSTR, TReMu), TRAINED abstention (When Silence Is Golden), and EVALUATION-only (BeDiscovER): none preserves a relation-algebra disjunction \emph{and} abstains on closure-collapse with a gold-free, training-free, per-edge certificate.

\textbf{LLM reasoning, formalization, and abstention.} Chain-of-thought \citep{Wei2022} and self-consistency \citep{Wang2022} operate at the answer level and cannot see that individually popular composition steps are jointly inconsistent. Logic-LM self-refines on solver crashes \citep{Pan2023} and LINC majority-votes formalizations \citep{Olausson2023}, but neither maintains a positive global invariant over relational knowledge. Path-of-Thoughts reasons each extracted path independently \citep{Zhang2024}---precisely the cross-path intersection gap Mode~A targets. The discourse-level reading prompts of \citet{Wei2024} ground our span-local protocol. Selective prediction \citep{Geifman2017} abstains on generic uncertainty; our abstention is structural. RuleTaker \citep{Clark2020} targets propositional entailment, out of scope for our relational composition. Reiter's model-based diagnosis \citep{Reiter1987} supplies the minimal-hitting-set machinery for the Mode-B repair we scope as future work. Hallucination in generation is a broad concern \citep{Ji2022}; ours is a per-edge, certificate-backed reduction.

# Method
\label{sec:method}

## Overview and the inverted output contract

The deduction module sits downstream of atomic extraction: it receives, for each pair of mentions co-occurring in a span, the relation the text licenses, and must answer queries about pairs that do \emph{not} co-occur. We model the relations as a Qualitative Constraint Network (QCN): nodes are events/entities, and each edge carries a \emph{set} of base relations from a relation algebra $\mathcal{A}$ (the disjunction not excluded by the evidence). The query (held-out) edge starts at the universal set. Three commitments define the contract. First, the LLM is a \emph{disjunctive, high-recall reader}: for each span it emits the maximal sound set the text does not exclude, with an explicit universal/underdetermined option, rather than committing to one relation. \emph{Soundness} of an edge means its set contains the gold relation; \emph{recall} is $r=P(\text{gold}\in\text{emitted set})$. Second, composition and converse come from the \emph{exact published table} of $\mathcal{A}$, never from the LLM. Third, the system narrows by closure and \emph{abstains} when the query edge remains a non-singleton, and \emph{flags an unsound read} when it collapses to the empty set. Table~\ref{tab:notation} fixes the notation.

\begin{table}[t]
\centering
\small
\begin{tabular}{ll}
\hline
Symbol / term & Meaning \\
\hline
$\mathcal{A}$ & relation algebra (point: 3; RCC-8: 8; Allen: 13) \\
$r$ & per-edge recall, $P(\text{gold}\in\text{emitted set})$ \\
sound edge & emitted set contains the gold relation \\
\textsc{full} & iterated closure to a fixpoint (our method) \\
\textsc{naive} & single-pass query-node intersection (PoT $+$ 1 step) \\
Mode~A & cross-path intersection narrows the query (primary) \\
Mode~B & empty closure certifies an unsound read \\
matched cov. & every method scored at the same resolution rate \\
$J(E)$ & empirical joint soundness of $E$-edge subnetworks \\
$N^\ast$ & a-priori count of deduction-required, multi-path, \\
 & bite-retaining, singleton-resolving held-out edges \\
\hline
\end{tabular}
\caption{Notation and metrics used throughout.}
\label{tab:notation}
\end{table}

## Two modes of value, and an honest distinction

\textbf{Mode~A (sound narrowing).} When every contributing edge set is sound but sub-universal, intersecting the compositions arriving at the query pair yields a set that still contains gold yet is strictly tighter than any single path. The load-bearing metric is the \emph{singleton-resolution-to-correct} yield. Mode~A's zero-FP guarantee survives path-consistency incompleteness because the intersection of sound sets is always sound---\emph{conditional on every contributing read being sound}. \textbf{Mode~B (detection).} An empty closure is a deductive certificate that some edge is unsound, with no gold labels. It fires only when an over-committed or recall-failed edge is present. Both modes carry the \emph{silent-wrong-narrowing} dual: if the gold relation is \emph{omitted} from a contributing set (recall failure), closure can narrow to a confident wrong singleton with no collapse---the failure mode we bound per-edge by $(1-r)$ and per-network by $(1-J(E))$, and which we show empirically dominates the natural-text errors (Section~\ref{sec:temporal}).

\textbf{A crucial distinction the prior draft blurred.} The \emph{cross-path intersection} variant of Mode~A---intersecting disjunctive reads that arrive at the same pair from $\geq 2$ \emph{distinct} constraining paths---is the paper's signature novel mechanism and the carrier of the coding-theory lens. It is \emph{not} the same as ``any multi-hop closure.'' In particular, our end-to-end CLUTRR engine does \emph{not} exercise it: CLUTRR's kinship relations form a finite composition table but not a relation algebra (no involutive converse), so the Mackworth converse-intersection step is unsound there and collapses $\sim 13\%$ of gold-clean chains to the empty set [ARTIFACT:art_0a7i481ZRwS1]. The sound closure for kinship is a forward least-fixpoint \emph{union} derivation over single chains---exactly the backward-chaining proof CLUTRR uses for its own gold. We therefore state plainly throughout: \emph{the CLUTRR result exercises inherited exact-table composition plus iterated multi-hop chaining plus the abstain-on-collapse certificate; it does not exercise cross-path intersection.}

## A worked example (single-chain union, not cross-path intersection)

Consider three entities read span-locally from a CLUTRR story \citep{Sinha2019} (the exact case discharged in SWI-Prolog in Section~\ref{sec:transferable}): \emph{``Irvin's grandfather, James, went out to get groceries. \dots Irvin's mother, Lena, cooked up some vegetables. James took his daughter Lynn out for dinner.''} The local reads give Irvin $\to$ James (\textsf{inv-grand}), Irvin $\to$ Lena (\textsf{inv-child}), and James $\to$ Lynn (\textsf{child}). The query Lena $\to$ Lynn never co-occurs. \textbf{Mode~A (single-chain union).} Composing along the chain, $\textsf{child}\circ\textsf{inv-grand}=\textsf{inv-child}$ ($\textsf{Lena}\!\rightarrow\!\textsf{James}$), then $\textsf{inv-child}\circ\textsf{child}=\textsf{sibling}$, a singleton; gold is \textsf{sister}. This is sequential transitive composition under a union fixpoint, with near-singleton kinship reads and \emph{no} redundant constraining paths---not the cross-path intersection of Section~\ref{sec:decisive}. \textbf{Mode~B (collapse).} If two contributing reads supported incompatible derivations of the same pair, their intersection is empty, certifying---with no gold label---that some read is unsound, and the system abstains rather than guess.

## Iterated closure, the redundancy coding rate, and the a-priori gate

We instrument three closure variants in one engine [ARTIFACT:art_K7riobQ_Rmwz]: \textsc{full} (iterated Mackworth PC-2 with algebra-seeded converse propagation, our method), \textsc{naive} (single-pass intersection at the query pair---Path-of-Thoughts plus one obvious step), and \textsc{off} (no propagation). A theorem we verify by unit test: on length-2 multi-path queries \textsc{naive} equals \textsc{full}; they diverge only on $\geq 3$-edge or cyclomatic structure. The full-minus-naive gap is therefore the signature of \emph{iteration}. Because Mode~A's zero-FP property holds only when all contributing edges are sound, and a single LLM reading one document produces positively correlated errors, we do not assume independent per-edge soundness; instead of the product $\prod_e r_e$ we measure the empirical joint soundness $J(E)$ and report the within-document error correlation $\rho$. The coding lens predicts that net narrowing is an inverted-U in redundancy: narrowing benefit rises with more paths, while the joint-soundness cost $1-J(E)$ eventually dominates.

Before spending any LLM budget, we compute from each gold graph \emph{alone} a four-stage funnel over held-out edges (deduction-required; $\geq 2$ paths; non-universal after widening; intersection equal to the gold singleton, $N^\ast$) plus the $\geq 3$-edge/cyclic prevalence and a power calculation [ARTIFACT:art_K7riobQ_Rmwz]. The applicability threshold is pre-registered as a number: deduction-required-multi-path-with-bite fraction $\geq 10\%$ = general mechanism, $5$--$10\%$ = useful module, $<5\%$ = niche. For auditability the closed QCN is emitted as an executable SWI-Prolog program: the algebra composition table as \texttt{comp/3} facts, each local read as a \texttt{rel/3} fact, and the query as the intersection (point/Allen/RCC-8) or union-fixpoint (kinship) of all path compositions; $|R|{=}1$ emits, $|R|{>}1$ abstains, $|R|{=}0$ flags an unsound read.

## A minimal LLM-resolved composition step
\label{sec:method-fuzzy}

To touch---without overclaiming---the project's ``fuzzy-unification'' framing, we add one neuro-symbolic variant scoped to composition-\emph{cell} gap-filling: when the symbolic engine abstains because a composition cell is missing or ambiguous, a probabilistic LLM read fills that single cell, and the engine then chains as usual. We contrast \emph{Mode~P} (the LLM supplies only the missing \emph{atomic} rule; the engine does the multi-hop reasoning) against \emph{Mode~S} (the LLM is asked to do the multi-hop read directly given the symbolic candidate set). This is explicitly \emph{not} OpenCyc/upper-ontology grounding and \emph{not} general fuzzy unification, both of which remain out of scope.

## Datasets, baselines, and metrics

\textbf{End-to-end venue (templated).} CLUTRR kinship \citep{Sinha2019}, standardized to gold graphs with typed atomic edges, held-out multi-hop queries (hops $2$--$10$), and $71{,}684$ within-document absent-relation pairs [ARTIFACT:art_HS7-lxhZnU9m]. We are explicit that CLUTRR is \emph{not} natural text: it is a template-generated kinship benchmark (semi-synthetic), its stories are short (max $871$ characters, none reaching the $\sim 3000$-character target), entity grounding uses gold surface forms, and---decisively---its composition table is hand-supplied, so the LLM never resolves implicit composition. \textbf{Natural-text temporal corpora.} The dense host is \emph{NarrativeTime}, a timeline-based full-TLink-coverage human re-annotation of TimeBank-Dense ($36$ docs, $1{,}715$ events) \citep{Rogers2019, Cassidy2014}, whose start-points instantiate the convex point algebra (PC complete) and whose gold our build reproduces exactly (non-circular); \emph{TDDMan} supplies manual long-distance pairs that ``cannot be inferred automatically'' \citep{Naik2019}; \emph{MATRES} \citep{Ning2018} annotates only same/adjacent-sentence pairs and is the gate-validation control [ARTIFACT:art_PNrS9T8JeATf]. \textbf{Synthetic backbone.} $35{,}100$ globally-consistent QCNs over the convex point, Allen, and RCC-8 algebras, generated by model-based realization with redundancy, hop length, and cyclomatic number swept independently [ARTIFACT:art_ghVQmxVlmOJJ]. \textbf{Baselines}, each given a matched abstention signal thresholded to the same coverage object: raw LLM, chain-of-thought \citep{Wei2022}, self-consistency \citep{Wang2022}, LINC-style voting \citep{Olausson2023}, Path-of-Thoughts \citep{Zhang2024}, the ILP-commit contract \citep{Eirew2025}, \textsc{naive} single-pass, and---for the decisive cross-path test---a \emph{best-single-path} composition baseline. \textbf{Metrics}: singleton-resolution-to-correct and selective accuracy at matched coverage; end-to-end confident-wrong (hallucination) rate paired with abstention; the full-minus-naive gap vs hop/cyclomatic; applicability $N^\ast$; atomic P/R (held-fixed control); per-edge recall.

# Experimental Setup
\label{sec:setup}

We execute a tiered plan. \textbf{T0} (zero LLM spend) is the envelope gate over the real corpora [ARTIFACT:art_K7riobQ_Rmwz]. \textbf{The CLUTRR end-to-end run} reads $282$ scored queries ($102$ present, $180$ absent) span-by-span and discharges Prolog [ARTIFACT:art_0a7i481ZRwS1]. \textbf{The fuzzy-unification study} reads composition cells across point/RCC-8/Allen/kinship and fills gaps on a mixed CLUTRR pool of $663$ queries [ARTIFACT:art_OvidVcsfr5HM]. \textbf{The decisive cross-path test} reads $125$ gold multi-path-with-bite TDDMan queries in the full Allen algebra with two readers and a synthetic positive control [ARTIFACT:art_0AIWMhwc1pJM]. \textbf{The powered temporal study} reads $600$ deduction-required queries across NarrativeTime and TDDMan [ARTIFACT:art_OETjJkketEVS], re-analyzed with corrected bootstrap CIs [ARTIFACT:art_Vc1UBGIVSi0T]. \textbf{The matched-coverage showdown} and \textbf{RCC-8 arm} read synthetic networks with a real LLM [ARTIFACT:art_N0e4pH_C_Cxw] [ARTIFACT:art_QToTkRe6Umb8]; \textbf{the realism-matched channel} re-establishes the mechanism claims under a calibrated reader channel [ARTIFACT:art_FtN4LBzazO_l]. Readers are \texttt{google/gemini-3.1-flash-lite} (primary, temperature $0$) and stronger cross-family readers (\texttt{deepseek/deepseek-v3.2}, \texttt{deepseek/deepseek-v4-pro}); all LLM calls use a SHA-256 disk cache and a hard global cost guard. Realized spend is small: the CLUTRR run and decisive test together cost $\sim\$1$; the fuzzy-unification cache cost $\$0.28$; the powered temporal study $\sim\$2.4$; cached re-runs are $\$0$. The QCN engine is gated by a unit-test suite: the Allen 169-cell table matches the published cells and the composition-converse law ($0$ failures), convex-point completeness is confirmed against brute force, the RCC-8 $64$-cell table reproduces with $0$ mismatches, and the iteration-isolation test confirms \textsc{full}$=$\textsc{naive} at length 2 and \textsc{full}$\neq$\textsc{naive} on a 3-hop chain.

# Results

We tag every subsection with its evidence class.

## The transferable contribution: certificate + composition on a real (templated) benchmark (\textsc{real-llm-read})
\label{sec:transferable}

The portable result is delivered end-to-end on CLUTRR. A real LLM reads atomic kinship triples span-by-span from each de-bracketed story; the forward-union closure engine recovers the held-out query and emits a certificate [ARTIFACT:art_0a7i481ZRwS1]. As a $0$-LLM go/no-go, the gold-atomic engine on all $16{,}131$ clean stories is $100\%$ accurate on every emitted answer at a $98.5\%$ singleton rate; the $1.5\%$ abstentions are a genuine table ambiguity (the same surface chain yields \textsf{mother} for one story and \textsf{mother-in-law} for another), so the engine correctly declines to guess.

[FIGURE:fig2]

\textbf{Matched-coverage win.} On $102$ present deduction queries spanning hops $2$--$10$, Mode~A attains selective accuracy $0.886$ at matched coverage $0.686$, versus Path-of-Thoughts $0.457$ (gap $+0.429$, $95\%$ CI $[0.299,0.563]$, Holm $p_{\text{adj}}{=}0.0015$), self-consistency $0.557$ (gap $+0.329$, CI $[0.203,0.453]$), and raw LLM $0.543$ (gap $+0.343$, CI $[0.222,0.465]$); \textsc{off} resolves nothing (Table~\ref{tab:clutrr}). The advantage is reader-agnostic: with \texttt{deepseek-v3.2} at matched per-edge recall ($0.51$), Mode~A reaches $0.867$ versus raw $0.511$ (gap $+0.356$, CI $[0.191,0.514]$). A gold-read oracle isolates the bottleneck: given gold atomic reads, Mode~A is $1.00$ accurate at coverage $0.951$ versus $0.433$ for raw and Path-of-Thoughts (gap $+0.567$), so the symbolic closure is not the limiting factor---the neural read is (atomic recall $\sim 0.53$).

\textbf{The iteration claim, routed through the coverage axis (R2 fix).} Following the reviewer, we no longer anchor the iteration result on the forced selective-accuracy contrast. The \textsc{naive} baseline's \emph{natural} coverage is only $0.216$ (selective accuracy $0.727$, predominantly hop-2); its matched-coverage value of $0.229$ is \emph{force-extended} to $0.686$ with representative-surface answers and is flagged as such (Table~\ref{tab:clutrr}). The genuine, like-for-like iteration signature lives on the coverage axis: the full-minus-naive resolve-to-correct coverage gap is $0.0$ at hop-2 (the predicted tie), $0.586$ at hop-3, and up to $0.875$ at hop-9 (\textsc{naive} resolves only hop-2 chains).

\begin{table}[t]
\centering
\small
\begin{tabular}{lccc}
\hline
Method (matched cov.\ $0.686$) & Sel.\ acc. & Nat.\ cov. & Gap \\
\hline
\textbf{Mode~A (ours)} & \textbf{0.886} & 0.686 & --- \\
Self-consistency \citep{Wang2022} & 0.557 & 0.794 & $+0.329$ \\
Raw LLM (forced single) & 0.543 & 0.794 & $+0.343$ \\
Path-of-Thoughts \citep{Zhang2024} & 0.457 & 0.882 & $+0.429$ \\
\textsc{naive} (natural cov.) & 0.727 & 0.216 & --- \\
\textsc{naive} (force-extended)$^\dagger$ & 0.229 & 0.686 & --- \\
\textsc{off} (no propagation) & 0.000 & 0.000 & --- \\
\hline
Gold-read oracle (Mode~A) & 1.000 & 0.951 & --- \\
\hline
\end{tabular}
\caption{CLUTRR end-to-end selective accuracy (\textsc{real-llm-read}, $n{=}102$ present queries, hops $2$--$10$). Gaps vs.\ Mode~A are Holm-adjusted-CI-separated from zero. $^\dagger$\textsc{naive}'s matched value is \emph{force-extended} beyond its natural coverage $0.216$ with representative-surface answers; the iteration claim is routed through the coverage axis, not this row. The gold-read oracle shows closure is not the bottleneck; the neural read is.}
\label{tab:clutrr}
\end{table}

\textbf{All four pipeline goal items.} (i) \emph{Atomic extraction}: the span-local reader extracts typed kinship triples at P/R/F1 $=0.536/0.532/0.534$ (doc-clustered CIs precision $[0.486,0.589]$, recall $[0.483,0.583]$), stable across hop length; reported as a held-fixed control. (ii) \emph{Multi-hop accuracy}: Mode~A's selective accuracy stays between $0.75$ and $1.00$ from hop-2 through hop-10, while raw collapses (hop-3 $0.444 \rightarrow$ hop-10 $0.0$) and Path-of-Thoughts degrades (hop-3 $0.357 \rightarrow$ hop-10 $0.20$). (iii) \emph{Auditable, executed trace}: the closed network is emitted as a runnable SWI-Prolog program; we install SWI-Prolog 9.0.4 and \emph{execute} $40$ sampled query programs---$40/40$ run to exit code $0$, $40/40$ match the Python engine, and $39/40$ match gold (the one miss is a read recall failure, not a closure error). (iv) \emph{Hallucination reduction}: on $180$ absent-relation queries (disconnected components, where the truthful answer is ``no relation''), the raw LLM is confidently wrong $47.2\%$ of the time; Mode~A, which emits ``no relation'' only when no derivation exists, is confidently wrong $2.8\%$---a $0.444$ reduction (CI $[0.317,0.583]$, $p_{\text{one-sided}}{=}0.0005$, clearing the pre-registered $0.20$ bar). On a \emph{mixed} present/absent pool ($n{=}282$) so that abstaining on everything cannot win, Mode~A answers $26.6\%$ at confident-wrong $4.6\%$ while the raw LLM answers $58.9\%$ at confident-wrong $44.0\%$: a genuine risk-coverage improvement.

## A minimal LLM-resolved composition step cuts hallucination to zero at full coverage (\textsc{real-llm-read})
\label{sec:fuzzy}

The project goal invokes an LLM as a probabilistic reasoner for fuzzy unification. We substantiate a \emph{scoped} version of that framing and find a clean positive [ARTIFACT:art_OvidVcsfr5HM]. First, an LLM's exact-match accuracy at composing a relation algebra \emph{degrades monotonically with richness}: point ($3$ relations) $0.67$, RCC-8 ($8$) $0.52$, Allen ($13$) $0.38$, with Allen soundness only $0.44$ (the LLM drops feasible relations $56\%$ of the time---the silent-wrong-narrowing hazard). By contrast the LLM knows the CLUTRR kinship calculus \emph{perfectly} ($16/16$ cells $=1.00$): common-sense calculi are where its implicit knowledge shines.

[FIGURE:fig3]

This dichotomy predicts where neuro-symbolic gap-filling helps. On a mixed CLUTRR pool ($n{=}663$) under a converse-closed ablated kinship table (the symbolic engine is then provably hallucination-safe: $0$ confident-wrong), \emph{Mode~P}---the LLM supplies only the missing \emph{atomic} composition rule and the engine does the multi-hop chaining---recovers $100\%$ of the $391$ manufactured gaps at precision $1.00$ (net $+391$), extending the engine's perfect accuracy to \emph{full coverage} and cutting the confident-wrong (hallucination) rate from raw-LLM $0.522$ to $0.000$ (Table~\ref{tab:fuzzy}). The honest negative sharpens the lesson: \emph{Mode~S}---asking the same LLM to do the multi-hop read directly---recovers gaps at only $0.33$ precision (net $-133$), because the weak reader inherits its own chain errors. The right neuro-symbolic division of labour is therefore to let the LLM fill only the atomic rule, not do the reasoning; and the method's success is conditional on the LLM knowing the calculus (decisive on kinship, unsafe on abstract Allen, where synthetic gap-fill precision falls to $0.30$ at $30\%$ ablation).

\begin{table}[t]
\centering
\small
\begin{tabular}{lccc}
\hline
Method (mixed pool $n{=}663$) & Cov. & Acc. & Conf.-wrong \\
\hline
Symbolic-only (abstain) & 0.41 & 1.00 & \textbf{0.000} \\
\textbf{Mode~P (cell-fill, neuro-sym.)} & \textbf{1.00} & \textbf{1.00} & \textbf{0.000} \\
Mode~S (story-fill) & 0.99 & 0.61 & 0.394 \\
Raw LLM CoT (pure neural) & 1.00 & 0.48 & 0.522 \\
\hline
\end{tabular}
\caption{Neuro-symbolic cell gap-filling on CLUTRR (\textsc{real-llm-read}). Mode~P (LLM fills one atomic rule, engine chains) attains full coverage at precision $1.00$ and cuts the confident-wrong rate $100\%$ ($0.522 \rightarrow 0.000$) versus the raw LLM. Mode~S (LLM does the multi-hop read) is \emph{not} net-faithful.}
\label{tab:fuzzy}
\end{table}

## The decisive negative: cross-path error-correction does not transfer to real Allen text (\textsc{real-llm-read})
\label{sec:decisive}

The prior reviewer's central concern---that the signature cross-path-intersection coding mechanism was demonstrated at power only synthetically---was \emph{not} retired by the templated CLUTRR win (which uses a single-chain union fixpoint, Section~\ref{sec:method}). We therefore ran the decisive experiment the reviewer asked for: on frozen real temporal gold graphs, do cross-path full-PC intersections of disjunctive LLM \emph{Allen} reads narrow deduction-required queries strictly beyond the best single path's composition, at statistical power? We use the full $13$-relation Allen algebra (not the coarse point projection that made \textsc{full}$=$\textsc{naive} in prior temporal arms) [ARTIFACT:art_0AIWMhwc1pJM].

[FIGURE:fig4]

The verdict is a sharp, interpretable \textbf{scope boundary}, established by three converging pre-registered results (Table~\ref{tab:decisive}). (1) The \emph{a-priori gate is GO}: the coding structure exists in the gold---combined gold-singleton multi-path-with-bite $N{=}125$ on TDDMan (bite histogram $\{2{:}62,\,4{:}63\}$), while NarrativeTime contributes $0$ (its dense start-point gold is structurally disjunctive, which also explains why iteration ties single-pass on dense timelines) and MATRES contributes $0$ (intra/adjacent only, confirming the gate is discriminative). (2) The \emph{synthetic Allen positive control passes}: on consistent-by-construction Allen QCNs with a noisy reader channel, intersection beats best-single-path at reader-recall $0.95$ (selective accuracy $0.976$ vs $0.717$), so the comparison code detects a true effect when reads are sound. (3) \emph{Real text fails for a localized reason}: LLM Allen reads of constituent edges are near-universe/underdetermined across both read regimes (event-local underdetermined-rate $0.87$; wider inter-event window $0.79$, breadth $11.5$ of $13$) and both readers---the stronger cross-family \texttt{deepseek-v3.2} is \emph{more} conservative (underdetermined-rate $0.99$, breadth $12.9$), so this is not a weak-model artifact. Composition of near-universe sets stays at the universe, so intersection, best-single, and naive all resolve $0/125$ (gap $0.0$, Holm not significant).

This is a \emph{precision/recall impossibility}. High-recall disjunctive Allen reads are sound but bite-free (recall $0.90$, clearing the $0.85$ gate only because near-universe sets trivially contain gold); forcing a single tight Allen relation (the raw baseline) restores tightness but is only $3.2\%$ correct---unsound. Text underdetermines interval endpoints, so no reader operating point yields tight-\emph{and}-sound Allen reads: the richer algebra that \emph{enables} intersection bite is exactly the one LLMs cannot read informatively. The few times the intersection did commit to a singleton it was wrong (confident-wrong $1.0$)---the error-correcting-code failure mode, surfaced in auditable Prolog traces. This extends the read-soundness finding (Section~\ref{sec:temporal}) from the point algebra to Allen, and it cleanly explains why the coding mechanism remains synthetic-channel-only on these corpora.

\begin{table}[t]
\centering
\small
\begin{tabular}{lc}
\hline
Quantity & Value \\
\hline
A-priori gate (gold multi-path-with-bite $N$) & \textbf{GO}, $125$ \\
\quad NarrativeTime / MATRES contribution & $0$ / $0$ \\
Synthetic control (recall $0.95$): inter.\ $>$ best-single & \textbf{True} ($0.976$ vs $0.717$) \\
Real: intersection $-$ best-single gap (Holm) & $0.0$ (n.s.) \\
Real: intersection resolution rate & $0.0 / 125$ \\
Window read underdetermined-rate / breadth & $0.79$ / $11.5$ of $13$ \\
Cross-family (\texttt{deepseek-v3.2}) underdet.\ / breadth & $0.99$ / $12.9$ \\
High-recall read recall (sound, near-universe) & $0.90$ \\
Forced single tight read correct-rate (unsound) & $0.032$ \\
\hline
\end{tabular}
\caption{The decisive cross-path test on real Allen text (\textsc{real-llm-read} / \textsc{gold-only-gate} / \textsc{synthetic-allen-control}, $n{=}125$ TDDMan gold-singleton queries). The mechanism is structurally present and works synthetically, but cannot realize on real text: a precision/recall impossibility for LLM Allen reads.}
\label{tab:decisive}
\end{table}

## Natural-text temporal: marginal advantage, weakly protective certificate, corrected statistics (\textsc{real-llm-read})
\label{sec:temporal}

We scale the temporal head-to-head to $600$ deduction-required queries ($300$ NarrativeTime, $300$ TDDMan) read span-locally in the PC-complete convex point algebra [ARTIFACT:art_OETjJkketEVS], and we re-analyze it with a corrected bootstrap [ARTIFACT:art_Vc1UBGIVSi0T]. \textbf{We must report two corrections honestly.} First (the reviewer's rigor MINOR), the previously published temporal H1 confidence intervals were a bootstrap \emph{artifact}: the matched-coverage gap was re-derived inside each resample, recentering the distribution on the volatile low-coverage baseline curve, so the published CI $[0.045,0.315]$ did not even contain its own point estimate $+0.0265$. Holding the operating point fixed across resamples yields a CI that brackets the point but is \emph{wide and includes zero}: Mode~A vs Path-of-Thoughts $+0.027$, CI $[-0.088,0.140]$, $p{=}0.33$; vs self-consistency $+0.035$, CI $[-0.061,0.135]$, $p{=}0.26$. Neither H1 gateway clears Holm after correction. \textbf{On natural temporal text, the Mode-A selective-accuracy advantage over per-path reasoning and voting is therefore marginal and not robustly significant}---and the raw LLM is in fact more accurate than Mode~A at this coverage point ($0.699$ vs $0.575$, gap $-0.124$).

Second (the reviewer's evidence MINOR), the certificate is \emph{weakly protective} on dense temporal prose. Among the $18.8\%$ of queries Mode~A commits to, it is confident-wrong $42.5\%$ of the time ($48/113$), and \emph{all $48$} are silent-wrong-narrowing: gold was omitted from a contributing local read, so closure narrowed to a confident wrong singleton with no empty collapse, which Mode~B cannot flag. At $\sim 0.85$ read recall this failure mode is undetectable by closure. We therefore temper ``faithfulness-by-abstention'': on natural temporal text Mode~A's value is the gold-free certificate and abstention-as-an-\emph{option}, not selective-accuracy dominance, and even that protection is bounded by read recall. The end-to-end confident-wrong reduction vs the raw LLM ($0.61 \rightarrow 0.425$, a $0.185$ reduction, CI $[0.087,0.280]$) is real but must be read alongside Mode~A's $0.188$ coverage versus the raw LLM's $1.0$.

\textbf{Read-soundness is the binding real-text constraint, and it is corpus-specific.} At $n\approx 160$ stronger-reader edges per corpus (Table~\ref{tab:readsound}), the stronger reader reaches recall $0.932$ on NarrativeTime (CI $[0.888,0.967]$, straddling the $0.90$ gate) but stays below it on discourse-level TDDMan gold ($0.819$); the within-document soundness correlation is positive ($\rho=0.003$--$0.167$). An earlier single-reader TDDMan ``crossing'' did not replicate at power. A $\$0$ synthetic backstop closes the loop: when reads are sound (recall $0.96$), Mode~A beats the raw LLM by $+0.225$ at matched coverage [ARTIFACT:art_FtN4LBzazO_l]---confirming the mechanism works and isolating read-soundness, not closure, as the real-text gate.

\begin{table}[t]
\centering
\small
\begin{tabular}{llc}
\hline
Corpus & Reader & Recall (CI) vs.\ $0.90$ gate \\
\hline
NarrativeTime & primary & 0.856 $[.832,.880]$ below \\
NarrativeTime & stronger & 0.932 $[.888,.967]$ straddles \\
TDDMan & primary & 0.828 $[.778,.869]$ below \\
TDDMan & stronger & 0.819 $[.727,.897]$ below \\
\hline
\end{tabular}
\caption{Per-corpus span-local read recall vs.\ the $0.90$ point gate (\textsc{real-llm-read}, doc-clustered bootstrap, $n{\approx}160$ stronger-reader edges/corpus). Gate-crossing is corpus-specific: a stronger reader reaches the gate on dense news prose but not on discourse-level manual gold.}
\label{tab:readsound}
\end{table}

## Decomposition and an algebra-richness scaling law (\textsc{real-llm-read-on-synthetic}, re-analysis)
\label{sec:decomp}

A reviewer rightly warned against presenting the $+0.676$ Allen advantage over per-path reasoning as a single ``iteration win.'' We decompose it [ARTIFACT:art_D0cHQUJ8kY75]. On the matched-coverage selective-accuracy axis the Allen gap splits additively into an \emph{inherited} exact-table-vs-LLM-composition term ($+0.673$)---that an LLM composes $13$-relation Allen poorly (Path-of-Thoughts $0.308$) is the standard neuro-symbolic premise, not our discovery---plus a \emph{novel} iteration term of only $+0.0025$. The genuine iteration novelty lives on the \emph{coverage} axis (full-minus-naive resolve-to-correct gap $+0.344$ point / $+0.144$ Allen at hop-3, an exact tie at length-2). Adding RCC-8 as a third real-LLM data point completes a scaling curve [ARTIFACT:art_QToTkRe6Umb8]: the advantage over Path-of-Thoughts grows monotonically with base-relation count, point ($3$) $+0.043 \rightarrow$ RCC-8 ($8$) $+0.448 \rightarrow$ Allen ($13$) $+0.676$ (Table~\ref{tab:scaling}). On a coarse algebra the LLM rarely has more than one plausible composition, so the symbolic step is redundant; as branching grows, free neural composition accumulates locally-fluent but globally-inconsistent steps that exact intersection eliminates. We state plainly that this scaling is the \emph{inherited} table-vs-LLM-composition effect measured across algebras at recall $\sim 1.0$ on templated NL, not new evidence of the coding mechanism. Because PC is incomplete for RCC-8 and Allen, those numbers are sound lower bounds; only the point arm is exact.

[FIGURE:fig5]

\begin{table}[t]
\centering
\small
\begin{tabular}{lcccc}
\hline
Algebra & Base rel. & Mode~A & PoT & Gap \\
\hline
Point (exact) & 3 & 1.000 & 0.957 & $+0.043$ \\
RCC-8 (l.\ bound) & 8 & 1.000 & 0.552 & $+0.448$ \\
Allen (l.\ bound) & 13 & 0.984 & 0.308 & $+0.676$ \\
\hline
\end{tabular}
\caption{Algebra-richness scaling, matched-coverage selective accuracy (\textsc{real-llm-read-on-synthetic}). The advantage over neural per-path reasoning grows monotonically with the number of base relations; all gaps are Holm-significant. This is the inherited table-vs-LLM-composition effect, not the cross-path coding mechanism.}
\label{tab:scaling}
\end{table}

## The coding mechanism on a realism-matched channel (\textsc{synthetic-channel}, \textsc{theorem})
\label{sec:mechanism}

The cross-path coding mechanism is established at power only on a synthetic channel calibrated to the real-text frontier [ARTIFACT:art_FtN4LBzazO_l]: a single ordinal knob samples the per-edge error-type category from the calibrated real distribution (recall becomes an output; reproduced to a maximum error of $0.003$; per-edge error-type total-variation distance $\le 0.0065$). On this channel iterated closure error-corrects as the theory predicts, per recall slice: the full-minus-naive gap is a structural $0.0$ at hop length $L{=}2$ and grows with $L$ and cyclomatic number (Page trend $p\approx 5\times 10^{-4}$, correcting the prior draft's mis-stated $10^{-13}$); the maximum-$L$ gap rises monotonically from $0.22$ to $0.885$ as recall climbs from $0.572$ to $1.0$. Net Mode-A resolution is an inverted-U in path redundancy $K$, with the optimum moving outward with recall (peak $K^\ast = 2,4,7,10,16$ for recall $0.5,0.625,0.78,0.90,0.95$). The zero-FP property---on all-sound contributing edges the Mode-A output contains gold with probability exactly $1.0$, and a collapse never co-occurs with all-sound reads---is the soundness invariant of path consistency, which we tag a \textsc{theorem} (verified on $100{,}296$ all-sound networks), not an empirical discovery. The empirical content is the conditionality: as per-edge recall falls, the silent-wrong rate rises ($0.006, 0.015, 0.044, 0.095, 0.146$ at recall $0.95$ down to $0.50$), always below the bounds $(1-J(E))$ and $(1-r)$. We follow the reviewer in stating that this inverted-U is a property of a \emph{controlled} channel: recall and $\rho$ are inputs, so it characterizes the mechanism rather than predicting a real-text operating point---and the decisive test of Section~\ref{sec:decisive} shows that, for Allen on real text, that operating point does not exist.

## The a-priori gate, stated as what it is (\textsc{gold-only-gate})

Run over the three temporal corpora at zero LLM cost, the T0 gate is discriminative by construction [ARTIFACT:art_K7riobQ_Rmwz]: MATRES yields $N^\ast=0$ (adjacent-sentence gold), NarrativeTime yields $N^\ast=25{,}450$ at applicability $0.882$, and TDDMan lands in the module band ($0.085$). We state plainly what these are: the NarrativeTime ``exact recovery'' is \emph{guaranteed}, not earned---a dense human timeline is a globally consistent point network, so closure trivially recovers every pairwise relation and iteration adds nothing there (\texttt{full\_only}$=0$). The genuine iteration signal lives on sparse long-hop gold, where TDDMan exhibits $12$ held-out edges \textsc{full} resolves but \textsc{naive} cannot. The gate thus scopes the iteration claim to sparse/long-hop structure and away from the dense timeline.

# Discussion

\textbf{What the evidence now supports.} The portable contribution---a training-free, gold-free, per-edge abstain-on-collapse certificate plus inherited exact-table composition---is confirmed at power on a real (templated) benchmark: on CLUTRR it beats per-path reasoning, voting, and the raw LLM at matched coverage by a wide Holm-adjusted margin, delivers all four pipeline goal items, executes its traces in SWI-Prolog, and cuts the absent-relation hallucination rate by $0.444$ in a risk-coverage comparison abstention alone cannot win. A new neuro-symbolic cell-gap-filling result substantiates the project's ``fuzzy-unification'' framing in a scoped, falsifiable way: when the LLM fills only the missing atomic rule and the engine chains, hallucination on CLUTRR drops to zero at full coverage.

\textbf{What it does not support, stated without spin.} The signature cross-path-intersection coding mechanism remains synthetic-channel-only. The decisive real-text test is a clean negative: the structure is present in the gold and the mechanism works synthetically, but LLM Allen reads of real text are either sound-but-near-universe or tight-but-$3\%$-correct, so the intersection has no bite. The natural-text temporal comparative advantage is marginal and not robustly significant under a corrected bootstrap, and the certificate is weakly protective there because recall-driven silent narrowing is undetectable ($42.5\%$ confident-wrong among answered). CLUTRR is a templated kinship benchmark, not natural text; its composition table is hand-supplied; and real-text utility is extraction-limited ($\sim 0.53$ atomic recall $\rightarrow \sim 19\%$ coverage).

\textbf{Why the algebra-richness scaling matters---and its sharp limit.} A recurring puzzle is that consistency enforcement does not improve F1 \citep{Kougia2024, Eirew2025}. Our scaling result reframes it: on a coarse algebra there is little for a symbolic step to fix, so enforcement looks inert; the symbolic advantage materializes on rich algebras and deep chains, where free neural composition is most error-prone. But the decisive test exposes the catch: on real text the same richness that creates symbolic headroom also defeats the LLM \emph{reader}, because rich algebras are exactly the ones text underdetermines. The actionable implication is to deploy closure where the relation algebra is rich \emph{and the constituent relations are locally readable} (kinship, where atoms are explicit; possibly spatial RCC-8, where containment is often stated)---and to invest in per-edge read-soundness rather than more consistency post-processing. Our descriptive spatial prevalence gate suggests SpaRTUN-style RCC-8 corpora \citep{Mirzaee2022} host the requisite multi-path redundancy ($27.4\%$ tight-bite fraction) and may read more locally than Allen intervals [ARTIFACT:art_f-ofxduZjwSM] [ARTIFACT:art_2Xp7DiYUxoNo]---the recommended next real venue.

\textbf{Limitations.} (1) The cross-path coding mechanism is synthetic-channel-only; its real-text transfer is an open problem we localize to Allen-read informativeness, not to the closure step. (2) Natural-text temporal gaps are marginal and the certificate is weakly protective there. (3) Path consistency is complete only for the convex point algebra; Allen and RCC-8 numbers are sound lower bounds. (4) CLUTRR is templated, short ($\leq 871$ characters), and uses gold entity grounding; the composition table is hand-supplied. (5) OpenCyc grounding, atomic re-extraction, and general fuzzy unification are out of scope; the contribution is the deduction sub-module, and real-text utility is extraction-limited. (6) Mode-B repair quality and a METRE-style trained-reader test are scoped as future work.

# Conclusion

We treated the deduction sub-module of a text-to-logic pipeline as a faithfulness problem: keep the LLM as a high-recall disjunctive reader, compose only through exact relation-algebra tables, and abstain when iterated closure leaves a disjunction or collapses to the empty set. The portable contribution is a training-free, gold-free, per-edge abstain-on-collapse certificate, confirmed at power on the templated CLUTRR benchmark (Mode~A $0.886$ vs Path-of-Thoughts $0.457$, Holm-adjusted; all four pipeline goal items with SWI-Prolog-executed traces; a $0.444$ hallucination reduction), and augmented by a minimal cell-gap-filling step that cuts the confident-wrong rate from $0.522$ to $0.000$ at full coverage. We are equally explicit about what does not yet transfer: the signature cross-path-intersection error-correcting-code mechanism is synthetic-channel-only, because a decisive real-text test found a precision/recall impossibility for LLM Allen reads, and the natural-text temporal advantage is marginal after a corrected bootstrap. Three concrete next steps follow: (1) test the cross-path mechanism on a spatial RCC-8 corpus whose constituent relations may be locally readable, where our prevalence gate finds the requisite multi-path redundancy; (2) raise per-edge read recall on discourse-level gold into the $0.90$ regime; and (3) integrate the validated certificate and cell-gap-filling step into the full pipeline with upper-ontology grounding.

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

--- Item 7 ---
id: art_Dm5vYXmD1R8h
type: research
title: Iter-2 Local-Reader / Prolog-Discharge / CLUTRR Implementation-Decision Dossier
summary: >-
  Executor-ready, web-verified resolution of the six NEW implementation decisions the iter-2 closure-certified text-to-logic
  experiments need (beyond the iter-1 dossier art_aQ2Rf8rwqteI). (1) LOCAL-READER PROTOCOL: minimal-span unit = the single
  sentence containing each event mention (default; +/-1 sentence as a sensitivity arm), grounded in TimeBank-Dense's own annotation
  window (same-sentence + immediately-following-sentence + DCT; 5 relations BEFORE/AFTER/INCLUDES/IS_INCLUDED/SIMULTANEOUS
  + VAGUE=underdetermined); 'no shared span' = mentions never co-occur within the window => DEDUCTION-REQUIRED, computable
  WITHOUT the LLM (T0-safe); disjunctive Pairwise read prompt adapted from Wei et al. arXiv:2407.19568 (Bulk/Iterative/Event-Ranking/Pairwise)
  + METRE arXiv:2408.07353 multi-label, enumerate base relations + explicit UNIVERSAL option, 'name every relation the text
  does NOT rule out'. (2) DISCHARGE: SWI-Prolog via pyswip v0.3.3 (class-method Prolog.assertz/query, Python>=3.9, needs apt
  swi-prolog>=8.4.2, ctypes shared-lib + SWI_HOME_DIR/LIBSWIPL_PATH) PRIMARY, robust subprocess fallback `swipl -s f.pl -g
  goal -t halt` (exit 0/1/2), clingo 5.8.0 ASP as secondary; QCN encoded as edge(E1,E2,RelSet) + algebra-seeded compose/3,converse/2;
  readback |R|==1 emit / |R|>1 ABSTAIN / |R|==0 unsound-flag; CONFIDENT-WRONG = nonabstained-single-relation-mismatch-rate
  on the deduction-required/absent subset, matched-coverage, paired-bootstrap CI, pre-registered MDE, aligned to Logic-LM/LINC
  executable-rate practice. (3) CLUTRR: HF CLUTRR/v1 (14 configs, target 0-20 mapping, fields incl proof_state/f_comb/story_edges/edge_types)
  BUT datasets>=4.0 dropped scripts => load via huggingface_hub snapshot_download of the per-task CSVs (git-LFS) or pin datasets<4.0
  + trust_remote_code; kinship composition table = rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender
  map (no-relation is a native primitive); absent-relation pairs CONSTRUCTED from rob_train_disc disconnected components /
  cross-family pairs; atomic-gold = story_edges+edge_types. (4) STRONGER READER: weak anchor = iter-1 google/gemini-3.1-flash-lite
  ($0.25/$1.50); recommend deepseek/deepseek-v3.2 ($0.2288/$0.3432, cross-family, CHEAPER, gate test ~$1.3) as budget-optimal
  stronger reader, google/gemini-3-flash-preview ($0.50/$3.00 thinking) as the clear capability-jump option on a stratified
  subsample; total two-reader run < $10 with disk cache + prompt caching + hard cost-guard. (5) SEVEN local-regime baselines
  each re-specified to read ONLY local spans with a matched single-relation abstention signal (raw verbalized-confidence,
  CoT, self-consistency vote-margin, LINC formalization-agreement, PoT path-agreement [confirmed per-path INDEPENDENT, no
  cross-path intersection], ILP-commit Eirew M=5, naive single-pass intersection), all thresholded to the SAME coverage object.
  (6) Four recent temporal/logical-consistency citations pinned (arXiv:2510.15513, 2502.11425, 2412.16100, 2409.14065) + a
  crisp novelty statement (disjunction-preserving abstain-on-collapse OUTPUT CONTRACT + gold-free closure CERTIFICATE + redundancy-as-coding-rate,
  NOT the algebra). Includes a consolidated decision table, exact IDs/URLs, and a 12-item gotchas list.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 8 ---
id: art_HS7-lxhZnU9m
type: dataset
title: 'CLUTRR kinship gold graphs: two hop-stratified slices with absent-relation pairs'
summary: |-
  The clean END-TO-END venue for the closure-certificate umbrella, beside the iter-1 temporal corpora (NarrativeTime/TDDMan/MATRES) and the synthetic-QCN backbone. Standardizes CLUTRR (Sinha et al., EMNLP 2019, arXiv:1908.06177) into the aii exp_sel_data_out schema, ONE ROW per story, so iter-3 can deliver — in ONE setting — all four numbers the umbrella names: (i) atomic-extraction precision/recall, (ii) multi-hop deduction accuracy vs chain length, (iii) a human-auditable trace-graph, and (iv) a hallucination-rate reduction on absent-relation queries.

  THE BEST 2 DATASETS (26,676 rows total; target_num_datasets=2): clutrr_gen (gen_train234_test2to10; 16,131 rows; clean; train hops 2-3-4, TEST hops 2..10 → the accuracy-vs-length curve + atomic P/R + trace-graph) and clutrr_disc (rob_train_disc_23_test_all_23; 10,545 rows; disconnected-noise → 10,244 two-component stories yielding 71,684 genuine within-document ABSENT pairs for the hallucination demo; its test split also mixes clean/supporting/irrelevant/disconnected noise, so distractor examples for P/R robustness are present without a 3rd slice). The plan's explicitly-optional 3rd slice clutrr_sup is kept reproducible behind `uv run data.py --include-sup` (off by default).

  PER ROW: input = de-bracketed natural-language story; output = json.dumps(gold_graph) = nodes [{entity_id, surface, gender, mention_spans=[[start,end) into input]}] + typed ATOMIC edges (the directly-stated proof-chain facts: {source,target,kinship_relation gendered surface, relation_type abstract, is_query=false, hop_count=1}; directed: t is source's relation) + noise_edges (extra story_edges CLUTRR does NOT type; structural only) + the held-out query_edge ({source,target,kinship_relation=gold,relation_type,target_int,is_query=true,hop_count}; deduced by composing >=2 atomics) + absent_relation_pairs (entity pairs in DIFFERENT connected components ⇒ provably no kinship path ⇒ 'no-relation'; structural/conservative, capped 20/story). Flat metadata_* per row: fold (train/dev/test), corpus, hop_count, noise_type {none,supporting,irrelevant,disconnected}, task_name, f_comb, query, atomic_facts, gold_proof (backward-chaining decomposition = trace-graph gold), genders, num_entities/num_atomic_edges/num_noise_edges/num_components/absent_pair_count, story_char_len. Top-level metadata emits ONCE the finite kinship COMPOSITION TABLE read verbatim from facebookresearch/clutrr (rules_store.yaml/relations_store.yaml): 11 relation TYPES (+inverse/symmetry flags), (type×gender)→surface map and reverse, composition rules rules[t1][t2]=t3, int↔text label_map 0..20, and a derived gendered surface composition table — explicitly NOT a full relation algebra.

  RECONSTRUCTION (verified on all 26,676 source rows, 0 violations): node_id→name = genders order (verified consistent with proof leaves on every row); atomic edges = story_edges[:len(edge_types)] (the proof chain is always the prefix); noise edges = story_edges[len(edge_types):] (left untyped, NOT fabricated — a word-before-bracket heuristic recovers only ~54% even on known edges). VERIFIED noise_type↔task mapping (config↔task correspondence): {1 none, 2 supporting, 3 irrelevant, 4 disconnected}; label_map matches the canonical 0..20 order; build flags={} (0 span mismatches, 0 missing genders, 0 hop disagreements, 0 proof-leaf inconsistencies).

  DESCRIPTIVE COUNTS ONLY (no composition/closure, no P/R/accuracy/N*/hallucination numbers, no LLM — those are iter-3): 26,676 stories, 124,819 entities, 78,472 typed atomic edges, 10,545 noise edges; folds train 20,144/dev 5,039/test 1,493; hops 2(10,235),3(10,514),4(5,101),5-10(826). HONEST CAVEAT: CLUTRR stories are short — min 39/median 201/MAX 871 chars; NONE reach the umbrella's ~3000-char target (n_ge_3000_chars=0) — reported, not hidden; longer documents must come from the temporal corpora.

  FILES: full corpus split into full_data_out/full_data_out_1.json + full_data_out_2.json (each <100 MB; merge examples of the same dataset name across parts to reconstruct), mini_data_out.json (3 examples/dataset, incl. multi-hop + absent-pair rows), preview_data_out.json (10 examples/dataset, strings truncated; spans hops 2..10 and absent pairs), results/dataset_metadata.json (QA/provenance/data card). Reproduce: `uv run data.py` (downloads CSVs from the kliang5 raw mirror HF CLUTRR/v1 points at + the FB yamls; deterministic, no randomness). License: CLUTRR is research/non-commercial (CC-BY-NC-style; facebookresearch/clutrr LICENSE).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 9 ---
id: art_N0e4pH_C_Cxw
type: experiment
title: Real-LLM Matched-Coverage Closure Showdown on the Synthetic QCN Backbone
summary: |-
  Experiment experiment_iter2_dir3 (tag REAL-LLM-READ-ON-SYNTHETIC). A real OpenRouter LLM (google/gemini-3.1-flash-lite, temp 0) makes LOCAL disjunctive reads of the synthetic QCN NL realizations (gen_art_dataset_2); those reads feed the validated Mackworth PC-2 closure engine; and every baseline is compared at MATCHED single-relation coverage over the SAME networks. OUR METHOD Mode-A = iterated path-consistency closure that answers a deduction-required query (s,t) iff closure narrows it to a singleton (else abstains; empty-collapse = Mode-B inconsistency certificate). BASELINES: naive single-pass (iteration contrast), OFF (coverage 0), raw LLM, chain-of-thought, self-consistency K=5 (vote margin), LINC multi-formalization, Path-of-Thoughts (per-path independent), ILP-commit (Eirew M=5, transitivity ILP via PuLP/CBC).

  HEADLINE RESULT (test fold, 90 networks/cell x 14 cells x 2 algebras = 2520 networks; bite-bearing pool n=900/algebra): H1 CONFIRMED on BOTH algebras (Holm-Bonferroni adjusted, Bonferroni CIs exclude 0). POINT (3-relation convex point algebra, PC-complete/EXACT): Mode-A selective accuracy 1.000 vs PoT 0.957 (gap +0.043, adj-CI [0.024,0.063]) and vs self-consistency 0.854 (gap +0.146, adj-CI [0.114,0.181]). ALLEN (13-relation interval algebra, NP-hard, lower-bound): Mode-A 0.984 vs PoT 0.308 (gap +0.676, adj-CI [0.624,0.728]) and vs SC 0.343 (gap +0.641, adj-CI [0.588,0.691]); Mode-A also dominates CoT/raw/LINC/ILP. CENTRAL FINDING: the closure advantage over neural per-path reasoning SCALES WITH RELATION-ALGEBRA RICHNESS (point gap +0.043 << allen gap +0.676) -- on a simple 3-relation algebra the LLM already composes correctly, but on the rich 13-relation algebra neural chaining collapses while symbolic closure stays robust.

  SECONDARY: H3 iteration -- on a clean GOLD-reads reference, full PC strictly beats naive single-pass on cyclomatic structures (coverage gain +0.30 point / +0.16 allen, where naive single-pass resolves nothing) and on hop>=3, and TIES exactly at length-2 (gap 0.0) -- confirming the pre-registered theorem; the gap survives with REAL reads. C2: Mode-A coverage IS the deduction-required bite (OFF=0). AUDIT: per-edge recall 1.000 point / 0.966 allen (both clear the 0.90/0.85 gates -> operating knob S4_sound frozen on the dev fold); zero-FP-conditional-on-soundness = 1.0 on BOTH (empirical confirmation of PC soundness); silent-wrong only from unsound reads (0.0 point / 0.021 allen); within-doc soundness rho ~ 0; J(E) vs r^E reported; read error-type distribution recorded.

  DELIVERABLES: method.py (full pipeline), engine.py + llm.py (reused from iter-1 gen_art_experiment_3, with a per-call temperature/tag patch on llm.py enabling self-consistency sampling), dataio.py (entity-normalized reads -> 2520 networks collapse to 35 unique cached read prompts, making reads ~free), stats.py (matched-coverage selective accuracy, paired bootstrap fixed-tau primary + rematch sensitivity, Holm-Bonferroni, Page/Jonckheere/Spearman, ICC), tests.py (Stage-0 closure unit tests, all pass). Output method_out.json is schema-valid (exp_gen_sol_out): per-network examples carry predict_modeA/naive/off/raw/cot/sc/linc/pot/ilp; all rich analysis (H1 leaderboards+Holm, H3 hop/cyclomatic tables, C2, audit, per-stratum, worked-example narrowing + Mode-B collapse trace, cross-algebra synthesis, verdict) lives in top-level metadata. 6 figures (H1 leaderboards + H3 hop/cyclomatic per algebra). Total OpenRouter spend across all runs ~$3 (this final run $2.21, 24938 billed calls + 7674 cache hits), well under the $9 hard cap via SHA-256 entity-normalized caching. For the paper: an honest, decisive REAL-LLM-ON-SYNTHETIC win for closure-certified composition, scoped by algebra richness, with a clean zero-FP soundness audit and the iteration theorem confirmed.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 10 ---
id: art_FtN4LBzazO_l
type: experiment
title: >-
  Realism-Matched Synthetic Channel: H3 gap, H4 inverted-U, silent-wrong re-established
summary: |-
  Repairs the two iter-1 synthetic-channel breaches and re-establishes the closure module's three mechanism results under a reader channel CALIBRATED to the iter-1 real-text frontier pilot (experiment_3 metadata.frontier_table, arm TBDense_dense). Zero LLM spend; pure CPU; ~140 s at full scale; schema exp_gen_sol_out validated.

  THE FIX (verified): iter-1's recall and breadth were independent inputs, giving a dead knob (recall flat 0.958) and per-edge error-type TV=0.25. Here the channel is a SINGLE ordinal knob S1-S5 that SAMPLES the per-edge error-type category directly from the calibrated real distribution, so recall = 1 - P(unsound|knob) is an OUTPUT. The real recall ladder is reproduced exactly: real [.572,.599,.625,.783,.796] vs sim [.572,.602,.623,.783,.796] (max err 0.003), with the matching breadth ladder [1.0,1.05,1.96,4.72,5.49].

  REALISM (all pass, realism_matched=True): (i) per-edge error-type TV in the apples-to-apples PROJECTED point ladder {singleton,pair,universal,unsound} = max 0.0065 (the naive 5-cat 0.19 exposes the point-algebra representability gap -- POINT cannot encode ALLEN 'loose'); the ALLEN direct-match arm matches the full 5 categories with TV 0.007. (ii) cross-edge soundness rho is calibrated to the directly-measured within-doc ICC; realism term = max |J2_sim - J2_real| = 0.073 (the real J2/J3 are internally inconsistent with any single exchangeable copula -- J2>p^2 but J3<p^3 on some knobs, a small-sample artifact -> Fallback B, report J(E) vs r^E descriptively). (iii) topology: contributing-edge-count E = minimal-deduction-path hop, cyclo = independent alternative routes; NNLS-matched to the NarrativeTime_point gold graphs (reachable deduction queries); short-range (E<=6) TV_E 0.13 and TV_cyclo 0.14 pass; the full TV_E 0.24 is driven by the long-hop tail outside the synthetic generator's range and is reported descriptively (the frontier pilot itself evaluated E=2 triangles).

  MECHANISM RESULTS (full N=600/cell, B=2000): H3 PASS -- FULL-vs-NAIVE iteration gap per fixed recall slice: length-2 tie (CI includes 0) at every slice, gap grows with hop length and with cyclomatic number, Page trend p ~= 5e-4 (correctly computed, NOT the paper's mis-stated 1e-13). H3 recall-dependence is itself a predicted signal: maxL gap rises 0.21->0.90 as recall 0.57->1.0 (predicted ~0.63 at recall 0.9; got 0.647). H4 PASS -- redundancy gives a recall-dependent inverted-U in Mode-A resolution; interior peak at recall<=0.78, peak shifts outward with recall (3 bins) and under the recall-floor gate, beats both best-single-path and OFF, and J(E)>r^E under rho>0 (frac 1.0 at low recall, centroid shift +1.04). Silent-wrong-vs-recall is monotone-decreasing and stays <= the per-network read-soundness bound 1-J(E) (RIGOROUS, asserted) and the per-edge (1-recall) reference; the E=2 (K=1) stratum is the highest -- redundancy converts over-commitment into DETECTED collapse, not silent error. The zero-FP soundness THEOREM (all-sound contributing edges => gold in Mode-A output with probability 1.0; collapse never co-occurs with all-sound) is verified and reported SEPARATELY (TAG=THEOREM) from the empirical curve (TAG=EMPIRICAL/SYNTHETIC-CHANNEL). C3 reliability: contains-gold slope on J(E)=0.65 (<1, point-algebra absorption -> certificate over-delivers), offset disappears under J(E) (attribution = independence-approximation failure, not soundness failure).

  For downstream GEN_PAPER_TEXT: method_out.json metadata holds realism{...}, recall_ladder_real_vs_sim, H3.by_recall_slice (per-slice Page/Jonckheere/Spearman, length2_tie, maxL_positive, cyclo_trend, recall_dependence), H4 (curves, peaks+CI, net_positive_regions, peak_shift_recall/gate, JE_vs_independence), silent_wrong_vs_recall (with per-edge/per-network bounds and E2 stratum), zero_FP_theorem, C3_reliability, allen arm, and overall_verdict. datasets[] carry worked H3 and H4 reads (predict_full/naive/off, outcome, n_contrib_edges, all_sound) including one Mode-A narrowing and one Mode-B collapse example. Five figures in figures/. Use the page_p_note and projection_note when correcting the paper's earlier claims.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 11 ---
id: art_fil2iJ6xSrYx
type: experiment
title: >-
  LOCAL-reader closure vs PoT/self-consistency on NarrativeTime+TDDMan with Prolog traces
summary: |-
  THE HEADLINE EXPERIMENT (experiment_iter2_dir5) of the Closure-Certified Text-to-Logic Deduction Module. It implements and compares, in ONE pipeline on the FROZEN ACTUAL NarrativeTime (dense host) + TDDMan (non-circular long-distance anchor) gold temporal graphs, our method against four baselines, all reading the SAME span-LOCAL LLM elicitations and resolving to a single coarse temporal relation (the shared coverage object).

  METHOD = Mode-A: iterated path-consistency CLOSURE (engine.pc2_full, Mackworth PC-2) over span-LOCAL reads of the constituent path edges of a deduction-required query, with the query edge HELD OUT (left at universe) so the closure must RECOVER it. BASELINES: (1) naive single-pass intersection (iteration contrast; ties Mode-A on length-2 by theorem); (2) raw local LLM forced-single from the query edge's own local read; (3) Path-of-Thoughts (per-path LLM composition, modal vote, abstain on path disagreement -- isolates the cross-path intersection step Mode-A adds); (4) self-consistency (majority over k paraphrase samples). Closure runs in the convex POINT start-point algebra (PC-COMPLETE, exact); the five coarse labels {before,after,simultaneous,includes,is_included} are exactly the five convex point relations.

  WHAT IT PROVIDES downstream (all numbers in method_out.json, TAGGED REAL-LLM-READ / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / THEOREM):
  * H1 (gateway, Holm-Bonferroni): Mode-A selective accuracy at MATCHED coverage vs PoT and SC, with doc-clustered paired-bootstrap CIs (risk-coverage curves interpolated to a shared coverage grid). Reported gaps vs PoT/SC/raw/naive + AUC + len2-vs-ge3/cyclic strata (Mode-A predicted to TIE naive on len2, dominate on >=3-edge/cyclic).
  * H2 (gateway): end-to-end confident-wrong (hallucination) rate of Mode-A (which abstains on disjunction/collapse) vs the raw LLM (forced single) on deduction-required queries; reduction vs the pre-registered 0.05 floor with doc-clustered bootstrap CI; decomposed into silent-wrong-narrowing (<= 1-recall bound). On the smoke/synthetic evidence Mode-A drives confident-wrong toward ~0 while raw is wrong on a large fraction -- the quantified hallucination-reduction deliverable.
  * Per-edge RECALL vs the 0.90 point gate for BOTH readers (primary google/gemini-3.1-flash-lite; stronger google/gemini-3.5-flash on a bounded NT sample) -- the stronger-reader gate-crossing answer localizes whether the bottleneck is real-text LOCAL read soundness (negative localization) rather than the closure step.
  * applicability: Mode-A singleton-resolution-to-correct rate vs GO-GENERAL(0.10)/GO-MODULE(0.05).
  * GOLD-ONLY-GATE: MATRES yields ~0 multi-path deduction queries (near-empty envelope, gate validation PASS).
  * A $0 fully-powered SYNTHETIC matched-coverage backstop (recall 0.96, 600 networks/cell, point-algebra channel) confirming the mechanism when reads are sound: Mode-A beats raw (~+0.22-0.26), SC, and PoT, ties naive on length-2, and structurally dominates naive/PoT in long-hop families (they cannot reach Mode-A's coverage).
  * A human-auditable Prolog trace deliverable: runnable prog.pl programs (results/worked_modeA.pl narrows to the correct singleton; results/worked_collapse.pl certifies inconsistency -> Mode-B abstain), discharged python-checked (swipl unavailable; H1/H2 are engine-independent) and cross-checked against the engine's Mode-A result.
  * examples[] per query edge with predict_modeA/naive/raw/pot/sc + gold + strata; figures (risk-coverage, synthetic matched-coverage).

  Genuinely NEW code: data_adapter.py (reads gen_art_dataset_1/full_data_out.json, char-offset event marking offset_ok=1.000, deduction-required multi-path query sampling), the span-LOCAL reads, the matched-coverage risk-coverage harness with Holm-adjusted doc-clustered bootstrap, the Prolog discharge, and synth_channel.py's matched-coverage harness. REUSED verbatim from iter-1: engine.py (QCN/pc2_full/naive), llm.py (cached, cost-guarded OpenRouter client), tests.py (blocking closure battery), corpora.py (coarse maps). A GLOBAL budget cap is enforced across all three OpenRouter clients (total < $9 < $10). Verdict policy: CONFIRM (both gateways) / PARTIAL/SCOPE-BOUNDARY (one) / DISCONFIRM/SCOPE-BOUNDARY (neither -> negative-localization + synthetic-mechanism, retargeted to NeSy/findings).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 12 ---
id: art_0a7i481ZRwS1
type: experiment
title: >-
  CLUTRR kinship closure-certificate pipeline: atomic P/R, multi-hop accuracy, Prolog trace
summary: "End-to-end neuro-symbolic experiment on the prepared CLUTRR kinship gold graphs (dependency art_HS7-lxhZnU9m; clutrr_gen\
  \ + clutrr_disc), delivering all four umbrella goal items on real (non-synthetic, non-temporal) text in ONE run with an\
  \ explicit CONFIRM verdict. A cheap LLM (google/gemini-3.1-flash-lite, automatic deepseek-v3.2 fallback on rate-limit) reads\
  \ atomic kinship triples from each de-bracketed story; a finite-composition-table closure engine recovers the held-out query\
  \ relation and emits a certificate.\n\nKEY ENGINEERING RESULT (load-bearing): CLUTRR's kinship table is a finite composition\
  \ table, NOT a relation algebra. Porting the iter-2 PC-2 (Mackworth converse-INTERSECTION) closure is UNSOUND here -- it\
  \ collapses ~13% of GOLD-clean chains to EMPTY. The SOUND closure is a forward least-fixpoint UNION derivation over DEFINED\
  \ compositions only (mirrors CLUTRR's own gold_proof backward-chaining and the emitted Prolog derive/solve predicate). Output\
  \ contract: |D[query]|==1 -> EMIT; >1 -> ABSTAIN (Mode-B conflict); ==0 -> ABSTAIN (no path = absent-relation, hallucination-safe).\
  \ Decisive 0-LLM go/no-go on ALL 16,131 clean gen rows: 100% accuracy on every emitted answer (soundness) at 98.5% singleton-rate;\
  \ the ~1.5% abstentions are a genuine table ambiguity (inv-child vs inv-in-law: the same surface chain 'husband-son-grandmother'\
  \ yields gold 'mother' for one story and 'mother-in-law' for another -> the table provably cannot disambiguate), so Mode-A\
  \ abstains rather than guess.\n\nRESULTS (scored set: 102 present + 180 absent queries spanning hops 2..10; all baselines\
  \ thresholded to the SAME matched-coverage object; doc-clustered paired bootstrap; Holm over {H1_pot,H1_sc,H2}):\n(i) Atomic-extraction\
  \ P/R/F1 = 0.536 / 0.532 / 0.534 (doc-clustered CIs; stable ~0.5 recall across hops; disc by-noise breakdown). \n(ii) H1\
  \ CONFIRMED -- Mode-A selective accuracy 0.886 at matched coverage 0.686 vs Path-of-Thoughts 0.457 (gap +0.429, CI [0.298,0.557],\
  \ p_adj=0.0015), self-consistency 0.557 (gap +0.329, CI [0.205,0.458]), raw-LLM 0.543, naive single-pass 0.229, off 0.0.\
  \ Accuracy-vs-chain-length: Mode-A stays ~1.0 selective accuracy through hop-10 while raw->0.0 / PoT->0.2. H3 CONFIRMED\
  \ -- full-minus-naive coverage gap is ~0 at hop-2 (naive ties full, as predicted) and grows to 0.6-0.9 for hop>=3 (naive\
  \ resolves only hop-2; full PC derives the rest). Gold-read ORACLE (0-LLM upper bound): Mode-A 1.00 selective accuracy at\
  \ 0.951 coverage -> the bottleneck is the neural READ (atomic recall ~0.53), not the symbolic closure (the iter-1 read-soundness\
  \ localization, reproduced on real text).\n(iii) Trace-graph ACTUALLY discharged in SWI-Prolog (v9.0.4): 40/40 sampled queries\
  \ executed in-engine (subprocess; pyswip also verified), 40/40 match the Python reference, 39/40 match gold; a worked 3-entity\
  \ example records the extracted atomics, the Mode-A composition trace (fired t1 o t2 -> t3 steps), the Prolog proof, and\
  \ one Mode-B collapse.\n(iv) H2 CONFIRMED -- absent-relation confident-wrong (hallucination) rate at matched coverage: raw-LLM\
  \ 0.472 vs Mode-A 0.028 = 0.444 absolute reduction (CI [0.317,0.583], meets the pre-registered >=0.20 bar, CI excludes 0);\
  \ full risk-coverage curves reported per method with abstention stated alongside every number, plus a mixed present/absent\
  \ pool so abstain-on-everything cannot win.\n\nCROSS-FAMILY (reader-agnostic): with deepseek-v3.2 as the reader at matched\
  \ per-edge recall (0.51), Mode-A selective accuracy 0.867 vs raw 0.511 -- the closure gain is not an artifact of one reader.\n\
  \nFILES: method.py orchestrator (+ kinship.py forward-closure engine, dataio.py loader/go-no-go, readers.py LLM prompts+parsers,\
  \ baselines.py matched-coverage/risk-coverage stats, prolog.py SWI-Prolog discharge, figures.py, tests.py 0-LLM unit tests;\
  \ engine.py/llm.py/stats.py reused verbatim from iter-2). method_out.json (exp_gen_sol_out, schema-validated) carries per-query\
  \ predict_modeA/modeA_goldread/naive/raw/sc/pot/off + gold and all metadata tables (atomic_pr, deduction_matched_coverage,\
  \ deduction_goldread_oracle, accuracy_vs_hop, absent_relation_h2, risk_coverage curves, holm_family, prolog_discharge, worked_example_3entity,\
  \ cross_family_sensitivity, gold_atomic_engine_sanity, verdict). Four figures in results/.\n\nHONEST CAVEATS: CLUTRR stories\
  \ are short (max 871 chars; none reach the umbrella's ~3000-char target -- longer documents live only in the temporal corpora);\
  \ entity grounding + gender use gold for surface realization (NOT the contribution); a minority of raw/SC/PoT baseline queries\
  \ fell back to deepseek during a gemini rate-limit window (both cheap readers; cross-family confirms reader-agnosticity).\
  \ Total LLM spend well under the $9 hard cap (sha256-cached, cost-guarded). Verdict: CONFIRM (H1, H2, H3)."
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 13 ---
id: art_OETjJkketEVS
type: experiment
title: >-
  Powered closure-certified temporal deduction on real text: H1+H2 CONFIRM at n=600
summary: |-
  Powered, at-scale execution of the iter-2 headline experiment for the Closure-Certified Text-to-Logic Deduction Module, fixing the iter-2 underpowering (n=20 smoke). OUR METHOD (Mode-A) runs iterated path-consistency closure (PC-2, engine.pc2_full) in the PC-complete convex point start-point algebra over SPAN-LOCAL LLM reads of constituent path edges, with the deduction-required query edge HELD OUT; it answers iff closure narrows to one coarse relation, else ABSTAINs. BASELINES in the same pipeline/coverage object: naive single-pass intersection, raw local LLM (forced single), Path-of-Thoughts (per-path composition, modal vote, no cross-path intersection), self-consistency (k=5 paraphrase votes).

  DATA (frozen gold graphs, gen_art_dataset_1): NarrativeTime (36 docs) + TDDMan (34 docs) -> 600 deduction-required multi-path queries scored (300 each); MATRES gate validates with 0 deduction queries (intra/adjacent-only). Readers: PRIMARY google/gemini-3.1-flash-lite (served 3897 reads; 212 fell back to deepseek-v3.2 on rate-limit, ~5%, logged in primary_reader_serving_models); STRONGER deepseek-v4-pro (100% served, max_tokens=8000 so reasoning completes -> non-empty JSON; parse-failed reads are EXCLUDED from recall, not counted as spurious-universe sound).

  HEADLINE VERDICT = CONFIRM (both Holm-gateways clear at powered n>=70). H1: Mode-A selective accuracy at matched coverage beats PoT (gap +0.027, boot_p=0.007) AND self-consistency (gap +0.035, boot_p=0.0185), Holm-adjusted, doc-clustered paired bootstrap (note: raw is higher at this coverage, gap -0.124 - raw is not a gateway). H2: Mode-A confident-wrong (hallucination) rate 0.425 vs raw 0.61 -> reduction 0.185 (CI [0.086,0.282], boot_p~0); reported AT coverage - Mode-A answers 18.8% (81.2% abstain) vs raw 100%, so the FAIR cross-method metric is H1 selective accuracy at matched coverage, not confident-wrong in isolation (h2_risk_coverage.jpg). Applicability GO-GENERAL (singleton-to-correct rate 0.108 >= 0.10 threshold).

  READ-SOUNDNESS RECONCILIATION (per corpus x reader, clustered-bootstrap CI vs the 0.90 point gate = PRIMARY, binomial p = ANTICONSERVATIVE secondary): NarrativeTime primary recall 0.856 (CI_excludes_below_gate), NT strong 0.932 (CI_contains_gate, point estimate crosses), TDDMan primary 0.828 and strong 0.819 (both CI_excludes_below_gate). Framing: gate-crossing is CORPUS/GENRE-specific (dense referential news prose vs discourse-level manual gold), NOT a universal ceiling - the stronger reader crosses the point-gate on NT but not TDDMan, so read soundness is the gating constraint and is partly improvable by a stronger reader on NT yet remains below gate on TDDMan.

  END-TO-END SWI-PROLOG (9.0.4, apt-installed, ACTUALLY executed): both worked programs discharged and cross-checked. worked_modeA.pl -> 'PATHS: [lt] VERDICT: ANSWER(lt)', agrees_with_engine=True, swipl_matches_python_checker=True, gold=before (a correct narrowing certificate). worked_collapse.pl -> Mode-B inconsistency certificate emitting the witnessing inconsistent triangle ('comp(gt,gt)=gt but rel=lt' -> VERDICT: INCONSISTENT, Mode-B ABSTAIN). Worked examples are SCREENED so the runnable 2-hop/triangle trace faithfully reproduces the engine result (two_hop_prolog_faithful=True).

  SYNTHETIC backstop ($0, 600 nets/cell, recall 0.96): mean Mode-A matched-coverage gap vs raw +0.225 -> the closure mechanism works when local reads are sound, isolating real-text read soundness as the binding constraint. H1_stratified (len2 vs ge3_cyclic) kept EXPLORATORY (gold is globally consistent so full==naive on gold; synthetic channel carries H3).

  COST: ~$2.4 realized across staged runs (n=80 then n=300); the final cached re-run is $0 (disk cache keyed by model+temperature+max_tokens). Hard global cap $9 enforced across all clients. Outputs: method.py (+engine/llm/data_adapter/corpora/synth_channel/tests reused), method_out.json (schema exp_gen_sol_out validated; full/mini/preview variants), results/worked_modeA.pl + worked_collapse.pl, figures real_risk_coverage.jpg / synthetic_matched_coverage.jpg / h2_risk_coverage.jpg, every number tagged REAL-LLM-READ / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / THEOREM. HONEST CAVEATS for the paper: matched-coverage H1 gaps are small (~0.03) though significant; primary reader is a 95/5 gemini/deepseek mix; Mode-A coverage is low (18.8%); raw out-accuracies Mode-A at that coverage point.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 14 ---
id: art_QToTkRe6Umb8
type: experiment
title: 'RCC-8 Real-LLM Arm: Third Point on the Closure Algebra-Richness Scaling Curve'
summary: >-
  Adds RCC-8 (8 spatial base relations) as the third real-LLM data point to the closure-certified matched-coverage showdown,
  completing an algebra-richness scaling curve: convex Point algebra (3 relations) -> RCC-8 (8) -> Allen interval (13). The
  iter-2 pipeline is reused verbatim (dataio/llm/stats); engine.py gains build_rcc8_algebra() (built from the dataset's authoritative
  RCC8_Algebra.json, TPPI/NTPPI canonicalised to TPPi/NTPPi, validated by a load-bearing self-test: all 64 composition cells
  + 8 converses + identity reproduced with 0 mismatches), and method.py gains spatial read/answer/PoT prompts and answer-label
  plumbing. A real OpenRouter LLM (google/gemini-3.1-flash-lite, temp 0, same model/seed/knob S4_sound as iter-2) reads the
  synthetic_qcn_rcc8 NL realizations; disjunctive LOCAL reads feed FULL iterated path-consistency closure (Mode-A) plus baselines
  naive single-pass, OFF, raw, CoT, self-consistency, LINC, Path-of-Thoughts, and ILP-commit, all at matched single-relation
  coverage. KEY RESULTS (every number tagged REAL-LLM-READ-ON-SYNTHETIC): (a) the matched-coverage selective-accuracy leaderboard
  with Holm-adjusted paired-bootstrap CIs; RCC-8 read recall = 1.00 (>=0.85 gate) and Mode-A selective accuracy = 1.00 at
  its coverage, while at matched coverage PoT~0.55 and SC~0.38, so Mode-A beats PoT by ~+0.45 and SC by ~+0.62 (both Holm-significant).
  (b) RCC-8 lands MONOTONICALLY between the endpoints on the vs-PoT scaling curve (gap_vs_pot ~0.04 at point -> ~0.45 at RCC-8
  -> ~0.68 at Allen; advantage_grows_with_algebra_richness=True), confirming the pre-registered prediction that the symbolic-closure
  advantage over neural per-path reasoning scales with relation-algebra richness; figure at results/figures/scaling_curve_vs_pot.jpg.
  (c) the iteration-specific full-minus-naive gap, stratified by hop/cyclomatic and decomposed into the INHERITED exact-table-vs-LLM-composition
  component (naive single-pass > PoT) and the NOVEL iterated-closure component (full PC > naive on hop>=3 / cyclomatic>=1);
  a zero-LLM gold-read validation confirms full-minus-naive is exactly 0 on every length-2 cell and positive on deeper strata,
  matching the dataset's own singleton-resolution structure. (d) a zero-FP-conditional-on-soundness audit: on all-sound networks
  Mode-A's committed singleton always contains gold even though RCC-8 PC is sound-but-INCOMPLETE. Because RCC-8 PC is incomplete,
  all coverage / collapse / resolve-to-singleton numbers are TAGGED 'SOUND-LOWER-BOUND'. point/allen are reproduced from iter-2
  (identical model/seed/protocol/cache replay; documented apples-to-apples merge) so the three arms are directly comparable.
  Total OpenRouter spend well under the $9 guard (RCC-8 fresh only; point/allen free via cache). Deliverables: method.py +
  engine.py/dataio.py/llm.py/stats.py, merge_arms.py, schema-valid method_out.json (+ full/mini/preview), and results/figures.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 15 ---
id: art_D0cHQUJ8kY75
type: evaluation
title: >-
  Decompose the +0.676 gap, risk-coverage hallucination, H1-H4 multiplicity re-analysis
summary: |-
  Pure re-analysis EVALUATION over the three iter-2 method_out files (showdown art_N0e4pH_C_Cxw, channel art_FtN4LBzazO_l, real-text art_fil2iJ6xSrYx). ZERO LLM spend (llm_spend_usd=0.0 in metadata and metrics_agg); numpy+scipy only; seed 20260617, paired bootstrap B=10000; runs in ~13s CPU. Output eval_out.json validates against exp_eval_sol_out (all plan-specified keys live under metadata since the schema forbids extra top-level keys); 17/17 sanity checks pass, 0 discrepancies, strict-valid JSON (NaN/Inf->null).

  TASK 1 (decomposition, retires the 'conflates two effects' MAJOR): per algebra and per pool, splits the Mode-A-vs-PoT system gap additively into an INHERITED exact-table-vs-LLM-composition component and a NOVEL iteration component, separating the selective-accuracy axis from the coverage axis. Allen bite pool: system_gap +0.676 = inherited +0.673 + novel_selacc +0.0025 (additivity residual 0.000); point +0.043 = +0.043 + 0.000. So on the selective-accuracy axis the +0.676 is almost entirely the inherited neuro-symbolic premise; iteration adds ~0. The genuine iteration novelty is a COVERAGE gain: full-minus-naive resolve-to-correct gap +0.344 point / +0.144 Allen at L=3 (paired-bootstrap CIs, e.g. Allen L3 [0.078,0.222]), growing with hop and cyclomatic, exact tie at length-2; pooled gold coverage gain +0.114 point / +0.060 Allen. Recomputed Jonckheere-Terpstra z matches F1 exactly (validation). Holm-adjusted family CIs (m=2/m=3), F2 per-recall-slice cross-source corroboration (maxL gap 0.22->0.885 as recall 0.572->1.0), and the corrected Page-p note (1e-13 -> ~5e-4 order; primary slice Page p 0.0036, Jonckheere range 8e-4..1e-118) are all carried.

  TASK 2 (risk-coverage, retires the 'hallucination driven by abstention' MINOR): Mode-A operating point coverage 0.10 (answered 2/20), abstention 0.90, confident-wrong 0.0, selective accuracy 1.0; raw coverage 1.0, confident-wrong 0.65, accuracy 0.35; AUC reused (modeA 1.0, raw 0.549, pot 0.647, sc 0.520; n=20 underpowered). Three mandatory statements embedded: the 0.65->0.0 drop is at ~90% abstention (trivial in isolation), the fair metric is selective accuracy at matched coverage, and at matched coverage 0.10 the advantage is NOT significant at n=20 (boot p vs raw 0.394 / PoT 0.254 / SC 0.175; gap CIs [0,1]). Read-soundness caveat: NT recall 0.743 (n=74) below the 0.90 gate, stronger reader 0.897 (n=39, CI contains 0.90), TDDMan 0.902 (n=41) -> real-text transfer UNRESOLVED.

  TASK 3 (multiplicity): confirmatory family {H1,H2,H3,H4} under Holm-Bonferroni + hierarchical gatekeeping (H1/H2 gateways). Holm step-down: H2 (p~0) clears at 0.0167, H3 (channel Page p 0.0036) clears at 0.025, H1 (p=0.254) FAILS. Conclusion: hallucination-reduction CONFIRMED-but-coverage-conditional (H2); iteration & redundancy CONFIRMED on synthetic (H3/H4 structural); real-text comparative advantage OPEN NEGATIVE (H1). Everything else (per-stratum, H1_stratified, reader-agnosticity, Mode-B, zero-FP audit/THEOREM, C3, silent-wrong, synthetic backstop, secondary corpora, real-text H3 stratum) tagged EXPLORATORY.

  Deliverables for GEN_PAPER_TEXT: eval_out.json (metadata.decomposition / risk_coverage / multiplicity / summary_for_paper / provenance; 45 flat metrics_agg numbers; datasets as schema-valid decomposition/risk-coverage/multiplicity tables), full/mini/preview variants, and eval_digest.md mirroring summary_for_paper with the headline-rewrite guidance, inherited-vs-novel framing, risk-coverage caveats, and corrected Page-p note. Every value is traceable to a source field or documented recomputation; provenance lists fields reused verbatim vs recomputed and the PoT matched-coverage reuse note.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 16 ---
id: art_fFOG-OJakRw-
type: research
title: Pinned & Differentiated 4 Closest Neuro-Symbolic Temporal/Abstention Neighbors
summary: >-
  Citation-verification bundle retiring the iter-2 reviewer MINOR 'closest recent neighbors not cited'. Independently re-verified
  and BibTeX-pinned four 2025-2026 neighbors -- NeSTR (Liang2026, AAAI 2026, arXiv:2512.07218; generate-then-abductively-REPAIR),
  TReMu (Ge2025, Findings-ACL 2025, 2025.findings-acl.972, arXiv:2502.01630; neuro-symbolic CODE-GEN/COMMIT over dialogue
  memory), Consistent Discourse-level TRE (Fan2025, Findings-EMNLP 2025, 2025.findings-emnlp.1010; single-label F1 COMMIT
  we invert), and When Silence Is Golden (Zhou2026, ICLR 2026, arXiv:2602.04755; LEARNED/TRAINED abstention). Provides per-paper
  objective_summary, output_contract, one_sentence_differentiation, verified BibTeX in AuthorYYYY project key style, a drop-in
  differentiation_paragraph, two ID corrections (TReMu full name/setting; TReMu pages 18974-18988 not 18605-18622), and an
  adversarial novelty-scout result confirming NO exact-match competitor preserves a relation-algebra disjunction AND abstains
  on closure-collapse (near-but-non-matching GDLLM 2508.20828 and BeDiscovER 2511.13095 noted). $0, pure-web, ready for GEN_PAPER_TEXT
  related work.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 17 ---
id: art_0AIWMhwc1pJM
type: experiment
title: 'Decisive real-text test: cross-path Allen-13 intersection vs best-single-path'
summary: |-
  THE decisive iter-4 experiment retiring reviewer MAJOR #1 (the cross-path-intersection mechanism was synthetic-only in iter-3). It tests, at statistical power on frozen real temporal gold graphs (NarrativeTime + TDDMan + MATRES), whether the cross-path full-PC INTERSECTION of disjunctive LLM Allen-interval reads narrows deduction-required queries strictly BEYOND the best-single-path composition, using the FULL Allen-13 algebra (not iter-3's coarse point projection that made full==naive).

  VERDICT = SCOPE-BOUNDARY (powered, n=125 TDDMan gold-singleton headline queries; ~$0.94 LLM spend, hard-guarded <$9). Three converging, pre-registered results:
  (1) STEP-1 a-priori GATE = GO (zero-LLM): the coding STRUCTURE exists in gold — combined gold-singleton multi-path-with-bite N=125 (TDDMan; NarrativeTime 0 because its dense start-point gold is structurally DISJUNCTIVE — explaining iter-3's full==naive; MATRES 0, confirming the gate is discriminative). Gold bite hist {2:62, 4:63}; power/MDE table included.
  (2) Synthetic Allen POSITIVE CONTROL: on consistent-by-construction Allen QCNs with a noisy reader channel, intersection beats best-single at reader-recall 0.95 — the comparison code detects a true effect when reads are sound.
  (3) REAL TEXT fails for a sharply localized reason: LLM Allen reads of constituent edges are near-universe/underdetermined across BOTH read regimes (event-local AND wider inter-event window) and BOTH readers (gemini-3.1-flash-lite underdet-rate 0.79; the STRONGER cross-family deepseek-v3.2 underdet-rate 0.99, breadth 12.9/13 — MORE conservative, so NOT a weak-model artifact). Composition of near-universe sets stays at the universe -> zero realized bite -> intersection/best-single/naive all resolve 0/125. Per-edge Allen recall 0.90 clears the 0.85 gate, but only because near-universe reads trivially contain gold (breadth, not soundness, is the issue).

  KEY INSIGHT (precision/recall impossibility): high-recall disjunctive reads are SOUND but bite-free; forcing a single tight Allen relation (the raw baseline) is tight but only ~3% correct (UNSOUND). Text underdetermines interval endpoints, so no reader operating point yields tight-AND-sound Allen reads — the richer algebra that ENABLES intersection bite (gate GO) is exactly the one LLMs cannot read informatively. This extends iter-3's read-soundness finding to the Allen setting. The few times intersection committed to a singleton it was wrong (confident-wrong=1.0): an auditable silent-wrong-narrowing failure mode, shown in runnable Prolog trace-graphs (python-checker fallback; swipl absent here, reported truthfully; traces reproduce the engine intersection exactly).

  DELIVERABLES for GEN_PAPER_TEXT: method.py (driver: gate->reads->matched-coverage comparison with the R1 BRACKETING-CI fix that flags any CI excluding its own point, Holm-adjusted over {intersection_vs_best_single, intersection_vs_naive, intersection_vs_PoT}); gate.py (a-priori multi-path gate, cached); allen_layer.py (Allen-13 token map, prompts, parser); synth_allen.py (positive control). method_out.json (schema exp_gen_sol_out, validated) carries: a_priori_gate (per-corpus N, prevalence, bite_hist, gold-singleton, singleton-resolvable, ge3-stratum, power_MDE, MATRES validation, gate_decision), read_conditions + read_informativeness_localization (3 conditions), per_edge_recall (recall/CI/rho/breadth/gate_verdict), leaderboard (5 contrasts with gap_point/gap_ci95/gap_bootstrap_median/brackets/boot_p), holm, singleton_resolution_rates, set_tightening_secondary, precision_recall_impossibility, cross_family_sensitivity, narrativetime_descriptive, synthetic_allen_control, worked_examples_prolog, stratified_exploratory, cost, verdict + rationale + honesty_caveats; datasets carry 125 TDDMan + 40 NarrativeTime per-query examples with predict_* and metadata_* fields. 3 figures (intersection-vs-best-single risk-coverage, gold-gate bite histogram, realized-bite-vs-paths). Transferable contribution surviving the negative: inherited exact-table composition + the gold-free abstain-on-collapse certificate; the cross-path coding mechanism is honestly synthetic-channel-only on these temporal corpora, with the multi-path-richer RCC-8 spatial venue recommended for iter-5.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 18 ---
id: art_f-ofxduZjwSM
type: dataset
title: 'Spatial multi-path-redundancy gold-QCN corpus: iter-5 prevalence gate'
summary: |-
  A SPATIAL multi-path-redundant gold-QCN corpus that serves as an a-priori, descriptive prevalence gate for iter-5's second real-venue cross-path-intersection test (the spatial analog of the temporal N* gate). Strictly $0, no LLM, descriptive-only: no closure, no derived P/R. From each published spatial-QA scene the pipeline reconstructs a GOLD relation-graph (nodes=objects/blocks with surface forms + char-offset spans where the source provides them; edges=stated native relations split into rcc8 {DC,EC,PO,EQ,TPP,NTPP,TPPI,NTPPI} — engine-validated — vs cardinal_direction {N/S/E/W + diagonals + near/far distance + front/behind out-of-2D-CDC depth}; a held-out query edge) and annotates each query with networkx structural metrics: hop_length, num_edge_disjoint_paths (Menger), cyclomatic_number, deduction_required, genuine_multipath_with_bite (deduction-required AND >=2 edge-disjoint paths each len>=2 = the spatial N* analog), and genuine_multipath_with_bite_TIGHT (additionally requiring >=2 of those paths to be short, len<=4 — the deductively meaningful redundancy, since long cardinal compositions decay to the universal relation). The world/image-container root node (id '-1') is excluded from the primary graph (non-constraining containment).

  Six corpora were EVALUATED; the FOUR STANDARDIZED corpora are emitted into datasets[] (full_data_out.json): SpaRP-PS1 (SpaRTUN; dense templated RCC-8+directional; symbolic_context=stated graph), SpartQA-Human (semi-natural human SpRL annotation), StepGame-clean (single-chain cardinal contrast), ReSQ (genuinely-natural anchor, no recoverable scene graph). Two EVALUATED EXTRAS appear only in the prevalence table (role=evaluated_extra, not emitted): SpaRP-PS2 (StepGame-Ext) and SpartQA-Auto.

  GO/NO-GO VERDICT (tight-bite fraction of deduction-required queries; bands >=10% general / 5-10% useful module / <5% niche): SpaRP-PS1 = 27.4% GENERAL — the recommended high-redundancy synthetic-but-realistic-text venue for iter-5, with RCC-8 edges immediately usable by the engine; SpartQA-Human = 4.5% (semi-natural text hosts modest but real redundancy, niche/useful boundary); SpaRP-PS2 = 10.4% raw but only 0.9% TIGHT (its redundancy is mostly long loose paths — empirically vindicates the plan's 'verify, don't trust noise labels'); SpartQA-Auto = 3.5%; StepGame-clean and ReSQ = 0 (single-chain by construction / no recoverable graph = the honest scope boundary). Caveats reported in the card: all spatial corpora fall far short of the ~3000-char target (130–1338 chars); SpaRP uses symbolic entity ids (char_spans=[]); SpartQA queries are enumerated deduction pairs (gold not derived) since FR descriptions are unresolvable without an LLM; ReSQ ships no reusable scene-graph triples; front/behind is out-of-standard-CDC; relation-vocab coverage = 0 unmapped after mapping.

  DELIVERABLES: data.py (+src/algebra.py, graphmetrics.py, loaders.py, make_variants.py) — deterministic, idempotent, reads cached raw downloads under temp/; full_data_out.json (4 datasets grouped, exp_sel_data_out schema, one example per (scene,query) row: input=story text, output=JSON {nodes,edges,query_edge}, flat metadata_* incl. all structural metrics; ~40MB < 100MB, not split); mini_data_out.json (3 rows/dataset); preview_data_out.json (10 rows/dataset, truncated); analysis_out.json (full 6-corpus prevalence table + relation-vocab ledger); dataset_card.md (prevalence table, provenance/licenses/commits, templated-vs-natural ledger, doc-length-vs-3000-char, per-algebra vocab coverage, caveats). All three data files validate against exp_sel_data_out.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 19 ---
id: art_OvidVcsfr5HM
type: experiment
title: >-
  LLM fuzzy-unification composition-cell gap-filling on Allen/RCC-8/Point and CLUTRR kinship
summary: |-
  Experiment substantiating the neuro-symbolic 'fuzzy unification' framing (reviewer MAJOR #3) WITHOUT overclaiming OpenCyc/general-fuzzy-unification: it scopes the claim to composition-CELL gap-filling (a missing/ambiguous cell of an EXACT qualitative or kinship composition table filled by a probabilistic LLM read). Real reader google/gemini-3.1-flash-lite, temp 0, sha256-cached; TOTAL api spend $0.28 (1797 calls), hard cap $9.

  Setting 1a (242 cells): LLM exact-match composition accuracy DEGRADES MONOTONICALLY with algebra richness — point 0.67 (3 rels) > rcc8 0.52 (8) > allen 0.38 (13); soundness falls 0.78->0.78->0.44 (on Allen the LLM drops feasible relations 56% of the time = the silent-wrong-narrowing hazard). The LLM knows the CLUTRR kinship calculus PERFECTLY (16/16 cells = 1.00) — common-sense calculi are where its implicit knowledge shines.

  Setting 1b ($0 extra, reuses cached cells; path-recompose sanity 100%): synthetic end-to-end gap-fill recovered-precision tracks richness/ablation — point & rcc8 = 1.0 with 0 hallucination at every K; allen degrades 0.52->0.45->0.30 (confident-wrong 0.02->0.06->0.17) as K=0.10->0.20->0.30.

  Setting 2 (HEADLINE, CLUTRR, mixed pool 663): under a converse-closed ablated kinship table the symbolic engine is PROVABLY hallucination-safe (D_abl subset of {gold} => 0 confident-wrong, verified). 391 manufactured no-path gaps + 244 natural inv-child/inv-in-law conflict gaps. Two gap-fill modes vs two baselines at full coverage: symbolic-abstain (cov 0.47, acc 1.00, cw 0.000); Mode-P CELL-fill, neuro-symbolic (cov 1.00, acc 1.00, cw 0.000); Mode-S STORY-fill (cov 0.99, acc 0.65, cw 0.343); raw_llm CoT pure-neural (cov 1.00, acc 0.54, cw 0.522). VERDICT=YES: Mode-P (LLM supplies only the missing ATOMIC rule, symbolic does the multi-hop chaining) recovers 100% of gaps at precision 1.00 (net +391) and CUTS the confident-wrong hallucination rate 100% (0.522->0.000) vs raw LLM at full coverage — the right neuro-symbolic division of labour. HONEST NEGATIVE: naive STORY-level filling is NOT net-faithful (precision 0.33, net -133), because asking the weak LLM to do the multi-hop read inherits its chain errors. K-sweep on CLUTRR: precision 1.0 / cw 0.0 at all K. Source-tagged auditable trace-graphs flag each LLM-resolved (fuzzy) step vs exact-table steps (incl. one honest mother-vs-mother-in-law failure). doc-clustered bootstrap CIs reported.

  Output method_out.json (aii exp_gen_sol_out, schema-validated): metadata holds composition_accuracy_by_algebra/by_true_cell_size, composition_richness_curve, kinship_composition_cell_accuracy, end_to_end_synthetic_gapfill, clutrr_gap_pool_counts, clutrr_gapfill_risk_coverage, clutrr_manufactured_K_sweep, clutrr_gapfill_mixed_pool_curve, clutrr_full_coverage_point, clutrr_hallucination_reduction, llm_resolved_step_accuracy (Mode-P cells + Mode-S manufactured/natural arms), bootstrap_cis, flagged_fuzzy_step_traces, honesty_caveats, budget, verdict. Two datasets: synthetic_composition_cells (242, predict_llm) and clutrr_gapfill (663; predict_symbolic/gapfill_P/gapfill_S/raw_llm). 4 figures in results/. Reuses kinship.py/llm.py/stats.py/dataio.py/qcn/ from sibling artifacts; --no-llm and --mini paths run symbolic-only at $0.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 20 ---
id: art_Vc1UBGIVSi0T
type: evaluation
title: 'Zero-spend re-analysis: bracketing CIs, CLUTRR coverage, contribution split'
summary: >-
  Pure re-analysis ($0 LLM; numpy+scipy only; seed=20260617, B=10000, doc/story-clustered paired bootstrap) of the two iter-3
  source experiments: temporal point-algebra natural text [art_OETjJkketEVS] and CLUTRR templated-kinship end-to-end [art_0a7i481ZRwS1].
  Temporal per-query (conf,correct,answered) records were rebuilt by a $0 CACHED re-run of the experiment's own pipeline (symlinked
  cache/, dummy key, --skip-strong): total_cache_misses=0, primary_cost=0.0, 600 records; every reproduced point estimate
  matches the source files (0 mismatches). Deliverables for GEN_PAPER_TEXT: (R1) Root-caused the matched_coverage_gap bootstrap
  bug (it re-derived the target coverage INSIDE each resample, making the gap distribution a different estimator than the
  headline gap); the corrected FIXED-operating-point CIs BRACKET the point gaps (vs-PoT new CI [-0.088,0.140] brackets +0.0265;
  published [0.045,0.315] did not). CRITICAL HONEST FINDING: once correctly centered, the vs-PoT and vs-SC CIs INCLUDE 0 (boot_p
  0.33 / 0.26) and neither H1 gateway clears Holm after correction; the published boot_p 0.007/0.0185 significance was a bootstrap
  ARTIFACT. So the temporal natural-text comparative win is MARGINAL/not-robustly-significant, and the transferable temporal
  contribution is the gold-free abstain-on-collapse CERTIFICATE, not selective-accuracy dominance. (R2) Recomputed CLUTRR
  naive NATURAL-coverage (0.216 cov, 22/102; selacc 0.727) beside the FORCE-EXTENDED matched value (0.686 cov, 0.229) and
  flagged the force-extension; routed the iteration (H3) claim through the COVERAGE axis (full-minus-naive coverage gap 0.0@hop2
  -> 0.586@hop3 -> 0.875@hop9), keeping the legitimate selacc leaderboard (Mode-A 0.886 vs PoT 0.457/SC 0.557/raw 0.543, Holm
  p_adj 0.0015; corrected fixed-set CIs reproduce the gaps). (42.5% block) Surfaced confident-wrong-among-answered = 0.425
  (48/113), ALL silent-wrong-narrowing (undetectable by Mode-B), with the read-soundness frontier (NT primary 0.856, strong
  0.932; TDDMan 0.828/0.819; rho 0.003-0.167) and the $0 synthetic backstop (+0.225 vs raw at recall 0.96) localizing the
  real-text bottleneck to the NEURAL READ, not closure. (Decomposition) Recomputed INHERITED-vs-NOVEL on both venues: NOVEL-on-selective-accuracy
  ~0 on the covered-by-both subset for both algebras (temporal +0.009; iter-2 Allen recomputed ~0, carried +0.673 inherited
  / +0.0025 novel); CLUTRR's additive split is force-extension-distorted and flagged. (Contribution split) One table separating
  TRANSFERABLE-AT-POWER (CLUTRR vs-PoT +0.429 [0.299,0.563], H2 absent-relation reduction +0.444 [0.317,0.583], gold-read
  oracle 1.00@0.951, multi-hop to hop-10, SWI-Prolog 40/40, and the portable certificate) from MARGINAL-NATURAL-TEXT (temporal,
  not significant after correction) from SYNTHETIC-CHANNEL-ONLY (cross-path INTERSECTION coding mechanism + inverted-U, +0.225
  backstop) -- with the explicit note that the reviewer's 'synthetic-only central contribution' concern is RECAST, not retired.
  (Scope) Re-tags CLUTRR as a templated kinship benchmark (max 871 chars), foregrounds the deduction-sub-module scope (~0.53
  atomic recall -> ~19% Mode-A coverage; OpenCyc/fuzzy-unification out of scope), re-affirms the H1-H4 Holm gatekeeping, and
  recommends re-titling around a 'closure-certified deduction sub-module'. Outputs: eval.py, eval_out.json (+full/mini/preview,
  schema-validated against exp_eval_sol_out), eval_digest.md (paper-facing), per_query_records_temporal.json (the $0 R1 input),
  and rerun_temporal/ (the cached re-run harness). Every number carries an evidence tag.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 21 ---
id: art_2Xp7DiYUxoNo
type: research
title: GDLLM/BeDiscovER citation+novelty pin and spatial composition-table de-risk
summary: >-
  Two-part $0 web dossier. PART A retires reviewer MINOR #6 by pinning the two near-neighbor citations -- GDLLM (Zhao et al.,
  EMNLP 2025 Findings; a fine-tuned LLM+GAT single-label COMMIT classifier) and BeDiscovER (Li & Carenini, EACL 2026; a 52-dataset
  EVALUATION benchmark) -- with verified BibTeX, objective+output-contract per paper, a drop-in differentiation paragraph
  folding them alongside the iter-3 four, and a sharpened one-sentence novelty (training-free/per-edge/gold-free abstain-on-collapse
  certificate) cleanly separated from the synthetic-only cross-path coding-rate thesis; corrects the iter-3 GDLLM key (Zhao
  not Mu). PART B/C de-risk the decisive spatial experiment: a verified corpus table (SpaRTUN/SpartQA/ReSQ/StepGame/SpaRP
  -- sizes, licenses, relation vocabularies, doc-lengths), a multi-path-redundancy verdict (StepGame single-chain; ReSQ/SpartQA-Human
  too shallow/small; SpaRTUN the strongest LIKELY-HOSTS candidate pending an edge-disjoint-paths audit on the STORY-stated
  subgraph; fallback = synthetic QCN host + SpaRTUN realism anchor), a corpus->algebra map, and EXACT composition tables.
  The key engine insight is VERIFIED: the projection-based cardinal calculus = product of two point algebras (an independent
  reconstruction reproduced GQR's cd.comp cell-for-cell), so the team's validated point engine generates the cardinal table
  for free; machine-readable GQR cd.comp/rcc8.comp/point.comp URLs are pinned.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
</supplementary_materials>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (evidence) The paper's signature novel mechanism — multi-path redundancy as an error-correcting code, where cross-path INTERSECTION of disjunctive LLM reads narrows the query toward gold (Mode A), with an inverted-U coding rate — is demonstrated at statistical power ONLY on the synthetic channel, whose recall and within-document correlation are controlled inputs. Neither real-text venue actually tests it. (1) CLUTRR uses a DIFFERENT algorithm: a forward least-fixpoint UNION derivation over single chains (kinship.py:109,134), with near-singleton kinship reads and no redundant constraining paths — the worked example (Lena->Irvin->James->Lynn) is sequential transitive composition, never a cross-path intersection. So the CLUTRR win is the inherited 'exact-table composition over LLM atoms' premise plus basic multi-hop closure, not the novel mechanism. (2) On the natural-text temporal corpora the iteration signature is absent at power: Mode-A-vs-naive single-pass gap is +0.027 with p=0.079 (NOT significant); the >=3-edge/cyclic full-vs-naive stratum is +0.042, p=0.061 (NOT significant, explicitly labeled EXPLORATORY, with 'the synthetic channel carries H3'); and the raw LLM out-accuracies Mode A by 0.124. The prior reviewer's 'central comparative contribution is synthetic-only' concern is therefore not retired — it is recast: the inherited premise transfers to a templated benchmark, but the novel coding mechanism does not.
  Action: Run the one decisive experiment: identify/construct real-text deduction queries with genuine multi-path redundancy (entity pairs reachable via >=2 disjoint constraining paths) and show at power that cross-path intersection narrows beyond single-path composition. If infeasible this round, restructure the headline so the real-text contribution is honestly 'inherited exact-table multi-hop composition + a gold-free abstain-on-collapse certificate,' and explicitly label the redundancy/intersection coding result as a synthetic-channel mechanism finding. Do NOT present 'on CLUTRR the iteration term is large and load-bearing' without stating that CLUTRR's 'iteration' is single-chain transitive composition under a UNION fixpoint, not the cross-path intersection that is the paper's claimed novelty.
- [MAJOR] (scope) CLUTRR is repeatedly framed as 'real, non-synthetic text' and the abstract claims confirmation on 'two non-synthetic venues.' CLUTRR stories are template-generated from kinship graphs (semi-synthetic), max 871 characters (none reach the ~3000-char target), and entity grounding uses gold surface forms; crucially, the composition knowledge is a hand-supplied table (rules_store.yaml), so the LLM never resolves implicit/common-sense composition — it only extracts atomic facts. The only genuinely natural text in the paper is the news-derived temporal corpora, and that is precisely where the contribution is marginal (+0.027, raw LLM wins, 18.8% coverage). This makes 'two non-synthetic venues' an overclaim and obscures that the natural-text result is weak.
  Action: Replace 'non-synthetic' with accurate language: CLUTRR is 'an established but templated kinship benchmark,' and the temporal corpora are 'natural news text.' State plainly that the decisive end-to-end win is on a templated benchmark and the natural-text result is marginal. Acknowledge that because the kinship/temporal composition tables are supplied, the goal's 'LLM as probabilistic reasoning engine for fuzzy unification / implicit common-sense composition' is out of scope here.
- [MAJOR] (scope) Measured against the project goal (an operational text->FOL pipeline that uses OpenCyc/upper-ontology grounding, an LLM as a probabilistic reasoner for fuzzy unification, SWI-Prolog execution, and quantified hallucination reduction on ~3000-char professional documents), the delivered contribution is a narrow deduction sub-module. OpenCyc grounding and LLM fuzzy unification are out of scope; atomic extraction is now measured but poor (P/R/F1 ~0.536/0.532/0.534) and held fixed; the longest real documents appear only in the weak temporal arm. The real-text utility is structurally capped by ~0.53 atomic recall, which is why Mode A operates at only 18.8% coverage on temporal text. This is acceptable as a focused contribution but the framing should make the ceiling unmistakable.
  Action: Foreground in the abstract and intro (not only the discussion) that this is the deduction sub-module only and that real-text utility is currently extraction-limited (0.53 atomic recall -> heavy abstention). Consider re-titling to center 'closure-certified deduction sub-module' rather than the full pipeline. If possible, add even a minimal demonstration of one missing goal element (e.g., an LLM-resolved composition step where the symbolic table has a gap) to substantiate the neuro-symbolic 'fuzzy unification' framing the motivation invokes.
- [MINOR] (evidence) On real temporal text the abstention certificate is weakly protective: among the 18.8% of queries Mode A actually commits to, it is confident-wrong 42.5% of the time (48/113). The paper frames Mode A's temporal value as 'the abstention-backed certificate,' but a 42.5% silent-wrong rate among answered queries means the certificate does not reliably protect on dense temporal prose at ~0.85 recall. This is a direct consequence of the silent-wrong-narrowing failure mode the method cannot detect.
  Action: Report the 42.5% confident-wrong-among-answered figure prominently next to the temporal claims, and temper 'faithfulness-by-abstention' to note that on real temporal text the certificate's protective value is limited because recall-failure-driven silent narrowing is undetectable. This strengthens credibility and pre-empts a skeptical reader.
- [MINOR] (rigor) Two reporting issues. (a) The temporal H1 modeA_vs_pot gap is +0.0265 but its reported 95% CI is [0.045, 0.315], which does not contain the point estimate — an artifact of re-matching coverage inside the bootstrap. (b) The naive baseline on CLUTRR is force-extended from its natural coverage (0.216) up to the matched 0.686 with 'representative surface' answers (baselines.py:33), so the 0.229 matched-coverage selective accuracy that anchors the '0.229 -> 0.886 iteration' headline is partly a forced-up artifact rather than a like-for-like comparison.
  Action: (a) Report a bootstrap CI that brackets the observed gap (percentile of the matched-gap distribution) or fix the matching procedure. (b) In the CLUTRR table, add naive's natural-coverage selective accuracy and flag force-extension in the caption; route the iteration claim through the coverage axis (which the data genuinely support) rather than the forced selective-accuracy contrast.
- [MINOR] (novelty) The technical machinery (path consistency over relation algebras, abstention on non-singleton query edges) is classical qualitative spatial/temporal reasoning (Allen, Mackworth, GQR, SputLink). The novelty is the combination/framing: a disjunction-preserving high-recall LLM reader feeding exact composition tables, with a gold-free abstain-on-collapse certificate and a coding-theory lens. This is a reasonable but incremental novelty, and as currently demonstrated on real text it reduces largely to the standard neuro-symbolic premise (compose with the table, not the LLM) plus structural abstention. The 'error-correcting code / coding rate' lens, while elegant, is exercised only synthetically.
  Action: Sharpen the one-sentence novelty to what is uniquely demonstrated end-to-end on a real benchmark (training-free, per-edge, gold-free abstain-on-collapse certificate over LLM-extracted relational facts) and clearly separate it from the coding-rate thesis (synthetic). Cite GDLLM (2508.20828) and BeDiscovER (2511.13095) as nearest non-matching neighbors to preempt 'incomplete positioning,' since the novelty scout already flagged them.
</previous_review>

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

### [2] HUMAN-USER prompt · 2026-06-17 22:10:54 UTC

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

### [3] SKILL-INPUT — aii-web-tools · 2026-06-17 22:13:43 UTC

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
