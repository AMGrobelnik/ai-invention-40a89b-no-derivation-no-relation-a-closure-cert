# gen_paper_text — test_idea

> Phase: `invention_loop` · round 7 · Substep: `gen_paper_text`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave the agent(s) in this substep — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-18 03:23:19 UTC

````
<system-prompt>
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A research paper writer (Step 3.4: GEN_PAPER_TEXT in the invention loop)

You received the hypothesis, all artifacts, the previous paper draft (if any), and reviewer feedback.
Write a complete paper draft with figure placeholders.

Publication-quality paper → strong contribution. Weak paper → wasted iteration.
</your_role>
</ai_inventor_context>

<research_methodology>
Write like a researcher drafting a paper, not a chatbot summarizing bullet points.

- Structure as a paper would: research question → methodology → results → analysis → limitations. Not a list of "we did X, then Y."
- Ground every claim in specific artifacts and specific numbers. "Results show improvement" is empty — state effect sizes, baselines, and conditions.
- Be honest about what worked, what didn't, and why. Don't spin failures as "future work."
- The paper's headline contribution should be a positive or surprising finding. Negative results are valuable context but should not be the primary narrative — lead with what works.
- Address reviewer feedback from previous iterations explicitly — show you've thought about each critique.
</research_methodology>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

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
</system-prompt>

<prompt>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# Introduction
\label{sec:intro}

A growing class of systems reads a short, professionally written document---a news report, a contract clause, a biography---into a formal representation (first-order-logic predicates, Prolog facts) that a symbolic reasoner can execute, with a large language model (LLM) resolving the terminology, concepts, and relations the surface text leaves implicit \citep{Pan2023, Olausson2023}. Such a pipeline promises auditable, replayable reasoning over text, but it has a structurally identifiable weak link. Atomic extraction---naming the entities and the relations that hold between locally co-occurring mentions---is by now something LLMs do competently, if imperfectly. The \emph{deduction} step is where faithfulness breaks: synthesizing the explicitly stated facts with implicit composition knowledge to answer a query about a pair of entities that never co-occur in any single span. This multi-hop relational reasoning is what the user ultimately cares about, and it is exactly where hallucination is most damaging and hardest to detect. We therefore scope this paper, deliberately and up front, to the \emph{deduction sub-module}: we measure atomic-extraction quality but do not try to improve it, we leave upper-ontology grounding \citep{Lenat1995} out of scope, and in every venue the composition table is \emph{hand-supplied}.

\textbf{One thesis, stated first and alone.} The contribution of this paper is a single, repeatable advance: \emph{a structural, label-free certificate that catches confident relational hallucinations that a confidence threshold cannot see.} Concretely, it is a training-free, gold-free, per-edge \textbf{abstain-on-collapse certificate} over LLM-extracted relational facts. The LLM is kept as a high-recall disjunctive reader; composition flows only through the exact relation-algebra table; the system \emph{emits} a singleton, \emph{abstains} on a residual disjunction, and \emph{flags an unsound read} when iterated closure collapses to the empty set. Its distinctive, non-incremental value is precise: it reduces confident-wrong hallucination exactly where a confidence-thresholded neural abstainer structurally \emph{cannot}---on \emph{no-derivation / absent-relation} queries, where the LLM hallucinates a relation at \emph{high} confidence (so no confidence threshold abstains on it) yet the certificate abstains because no derivation path exists, and on \emph{sound-violating} reads (Mode-B collapse). Everything else in this paper---a cross-path coding thesis, an algebra-richness scaling law, an inherited-vs-novel decomposition, a redundancy optimum, a zero-false-positive theorem---is \emph{supporting} material, demoted to one subsection or a compact appendix, not a co-equal contribution.

The deduction step is hard because the obvious ways of using an LLM fail in characteristic ways. Composing freely, the LLM is locally fluent but globally inconsistent: it can assign more than one relation to the same pair and violate transitivity, producing silent errors that an answer-level vote \citep{Wang2022} or a solver-crash signal \citep{Pan2023} cannot see. Reasoning each path in isolation---the strategy of backward chaining \citep{Kazemi2022} and Path-of-Thoughts \citep{Zhang2024}---deliberately avoids the global check. Hand-crafting composition rules (the kinship rules behind CLUTRR \citep{Sinha2019}) does not scale, and inducing rules to fit task accuracy \citep{Zhang2023, Zhu2023} optimizes data fit rather than the algebraic laws needed for soundness. And crucially for our thesis, the natural defense against hallucination---\emph{abstain when the model is uncertain}---fails on the very errors that matter most: an absent-relation hallucination is typically \emph{confident}, so every member of the confidence/uncertainty family (verbalized confidence \citep{Lin2022, Tian2023}, self-consistency vote-margin \citep{Wang2022}, Kadavath's P(True) \citep{Kadavath2022}, semantic entropy \citep{Kuhn2023, Farquhar2024}, SelfCheckGPT \citep{Manakul2023}) keeps it. Each such signal is a monotone function of prediction \emph{dispersion} or self-assessed confidence \citep{Wen2024}, so a confident, self-consistent fabrication reads as ``certain'' and survives. Even internal-state probes are reported ineffective on logic-intensive tasks ``where models are confidently wrong'' \citep{Song2025}.

Why has the consistency angle not already solved this? Because the recent lineage attacks it under the wrong \emph{output contract}. A zero-shot study finds LLMs assign multiple relations to over half (up to $97\%$) of temporal pairs and violate transitivity, then enforces consistency with integer linear programming (ILP) and reports that consistency enforcement \emph{does not improve} F1 \citep{Kougia2024}; the most recent global temporal-graph generator still aggregates generations and ILP-commits to a single label per pair, preserving no disjunction, issuing no certificate, offering no abstention \citep{Eirew2025}. Classical temporal closure \citep{Verhagen2005, Chambers2014, Ning2017} and the newest neuro-symbolic temporal work \citep{Liang2025, Ge2025, Fan2025, Zhao2025} share this \emph{commit-for-F1} contract. We invert it: the LLM's native multi-relation output is not noise to be collapsed but a \emph{sound disjunction} to be preserved and narrowed, and the right objective is faithfulness-by-abstention. The relations involved---temporal order, kinship, spatial containment---are precisely those for which mathematics has supplied exact \emph{composition laws} for forty years: Allen's interval algebra \citep{Allen1983}, the convex point algebra \citep{Vilain1986}, the region connection calculus RCC-8 \citep{Randell1992}, and path-consistency constraint propagation \citep{Mackworth1977}. If a document says $A$ is before $B$ and $B$ before $C$, the relation between $A$ and $C$ is fixed by an exact table, not a matter of opinion to be guessed.

\textbf{What we show, and its boundary.} (1) On the no-derivation regime the certificate beats not a strawman but the \emph{best available} confidence/uncertainty battery---four signals (verbalized, self-consistency, P(True), semantic entropy)---at matched coverage: the raw LLM hallucinates a kinship on $47.2\%$ of CLUTRR absent pairs, no signal removes them at the LLM's natural coverage, and on the mixed pool the certificate's selective accuracy ($0.827$) roughly doubles every signal ($0.37$--$0.44$), with Holm-adjusted confident-wrong reductions whose CIs exclude zero (Section~\ref{sec:fairbaseline}). (2) The same edge holds for genuinely fuzzy LLM reads, against a \emph{confidence-thresholded} abstainer (not just an always-answer commit), in both a vague-spatial and an ambiguous-kinship setting (Section~\ref{sec:fuzzy}). (3) We honestly bound where the certificate does \emph{not} help: on ordinary single-path deduction a confidence threshold is already well-calibrated and the certificate ties or loses (Section~\ref{sec:fairbaseline}); the signature cross-path-intersection coding mechanism is synthetic-channel-only on both real venues we could a-priori-gate (Section~\ref{sec:decisive}); and on dense natural temporal prose the certificate is only weakly protective (Section~\ref{sec:temporal}). The operational ceiling is the deduction sub-module: atomic extraction is measured ($\approx 0.534$ F1), not improved; real-text utility is extraction-limited; and no benchmark document reaches the $\sim$3000-character target. We tag every number by evidence class in \emph{table columns}, not inline hedging, and---because the contribution is deduction/consistency rather than extraction---we target a neuro-symbolic / qualitative-reasoning (NeSy) venue rather than a knowledge-extraction track.

[FIGURE:fig1]

\begin{table}[t]
\centering
\small
\begin{tabular}{p{2.35cm}p{1.7cm}p{1.55cm}p{1.15cm}}
\hline
Claim & Evidence & Where & Status \\
\hline
\textbf{(Spine) Abstain-on-collapse certificate: cuts confident-wrong on no-derivation queries that confidence cannot abstain on} & \textsc{real-read} $+$ \textsc{theorem} & CLUTRR; fuzzy RCC-8/kinship & \textbf{Confirmed vs.\ a 4-signal confidence battery} \\
(Supporting) Cross-path coding is synthetic-channel-only & \textsc{real-read} $+$ \textsc{gold-gate} $+$ \textsc{synth} & temporal Allen; spatial RCC-8 & Resolved negative (Sec.~\ref{sec:decisive}) \\
(Appendix) Algebra-richness scaling; inverted-U; zero-FP theorem & \textsc{real-on-synth} / \textsc{synth} / \textsc{theorem} & synthetic & Inherited / textbook (App.~\ref{sec:mechanism}) \\
(Ceiling) Marginal on natural temporal text; extraction-limited & \textsc{real-read} & temporal; all venues & Honest scope \\
\hline
\end{tabular}
\caption{The paper's spine: one load-bearing contribution (the certificate), with everything else explicitly subordinate. Evidence-class tags are columns, not inline hedging. \textsc{real-read}: a real LLM reads natural(istic) text. \textsc{gold-gate}: zero-LLM structural gate over verified gold. \textsc{synth}: synthetic channel. \textsc{theorem}: a path-consistency invariant.}
\label{tab:spine}
\end{table}

## Summary of Contributions

\begin{itemize}
\item \textbf{The certificate beats the best confidence/uncertainty signals where they structurally cannot help} (Section~\ref{sec:fairbaseline}). Against a four-signal battery (verbalized confidence, self-consistency vote-margin, P(True), semantic entropy) at matched coverage, the certificate removes the high-confidence absent-relation hallucinations that survive every signal: on CLUTRR absent pairs the raw LLM is confidently wrong $47.2\%$ of the time and the certificate $2.8\%$ (reduction $0.444$, $95\%$ CI $[0.317,0.583]$); on the mixed pool the certificate's selective accuracy is $0.827$ vs $0.37$--$0.44$ for every signal (confident-wrong reductions $0.10$--$0.12$, Holm-adjusted CIs exclude $0$); cross-family (\texttt{deepseek-v3.2}) reproduces it [ARTIFACT:art_LeRQRGHJZcdQ].
\item \textbf{The same edge over a fair confidence abstainer on genuinely fuzzy reads} (Section~\ref{sec:fuzzy}). When the LLM resolves a \emph{vague} preposition or an \emph{informal} kinship term at calibrated sub-$1.0$ confidence, the certificate's confident-wrong rate is $0.000$ at coverage $0.535$/$0.314$, strictly below a confidence-thresholded top-1 abstainer at matched coverage ($0.415$/$0.346$, CIs exclude $0$); its strictly distinctive, same-object edge is catching $5/5$ sound-violating spatial reads at ordinary confidence [ARTIFACT:art_0MDLD-w-RXOu] [ARTIFACT:art_I22c-J7-OcXl].
\item \textbf{An end-to-end, SWI-Prolog-executed pipeline delivering all four umbrella goal items on CLUTRR} (Section~\ref{sec:clutrr}): measured atomic P/R/F1 $0.536/0.532/0.534$; multi-hop selective accuracy $0.75$--$1.00$ through 10-hop chains; $40/40$ executed Prolog traces ($39/40$ match gold); and the $0.444$ absent-relation hallucination reduction. A gold-read oracle ($1.00$ at coverage $0.951$) localizes the bottleneck to the neural read, not the symbolic closure [ARTIFACT:art_0a7i481ZRwS1].
\item \textbf{An honest negative and an honest ceiling.} The cross-path-intersection coding mechanism is synthetic-channel-only, for two conditions each independently violated in the two real venues we could a-priori-gate (Section~\ref{sec:decisive}); on natural temporal text the comparative advantage is marginal under a corrected bootstrap (Section~\ref{sec:temporal}); and a genuinely natural absent-relation corpus (Re-DocRED) is constructed and gold-verified for the immediate next step (Section~\ref{sec:natural}) [ARTIFACT:art_i53dBKgGY3Ig] [ARTIFACT:art_NUWTxBVWENIJ].
\end{itemize}

# Related Work
\label{sec:related}

\textbf{What is new, in one sentence.} Path consistency over relation algebras and consistency enforcement over machine-extracted relations are both well established; our contribution is a \emph{training-free, per-edge, gold-free abstain-on-collapse certificate} that inverts the F1-maximizing commit contract and---its distinctive, empirically isolated property---abstains on the \emph{confident} relational hallucinations that the entire confidence/uncertainty family keeps.

\textbf{Abstention by confidence vs.\ abstention by structure.} The dominant defense against LLM error is selective prediction: abstain when an uncertainty signal is low. The family spans verbalized confidence \citep{Lin2022, Tian2023}, self-consistency / vote-margin \citep{Wang2022}, P(True) and P(IK) \citep{Kadavath2022}, semantic entropy over meaning-clustered samples \citep{Kuhn2023, Farquhar2024}, and SelfCheckGPT sampling consistency \citep{Manakul2023}; surveys frame the whole family as a confidence-threshold decision \citep{Wen2024}. Every one of these signals is a monotone function of prediction dispersion or self-assessed confidence, so \emph{by construction} it reads ``certain'' on a confident, self-consistent absent-relation hallucination---samples agree, verbalized confidence is high, P(True) is high, semantic entropy is low---and keeps it. Even internal-state probing is reported ineffective ``on logic-intensive tasks \dots where models are confidently wrong'' \citep{Song2025}. Our certificate is orthogonal: it abstains because no derivation path exists after composing per-edge reads through the exact algebra---confidence-independent, gold-free, training-free. We make this the empirical centerpiece (Section~\ref{sec:fairbaseline}) rather than an assertion, and we keep the scope honest: on ordinary uncertain deduction, where the model's dispersion \emph{is} informative, the confidence baselines tie the certificate.

\textbf{Consistency enforcement and abstention under the commit contract.} A zero-shot study reports ILP consistency enforcement does not raise F1 \citep{Kougia2024}; the most recent global temporal-graph generator still ILP-commits \citep{Eirew2025}. Our closest neuro-symbolic neighbors all retain a commit objective: NeSTR repairs detected inconsistencies toward a single committed conclusion \citep{Liang2025}; TReMu generates and commits Python over dialogue memory \citep{Ge2025}; Fan and Strube's discourse-level extractor---the contract we most directly invert---pairs Allen-algebra prompts with reflection to commit to one F1-maximizing label per pair \citep{Fan2025}; GDLLM fine-tunes an LLM whose soft distribution feeds a graph network to \emph{classify} one relation per pair \citep{Zhao2025}. METRE trains a multi-label head to model ambiguity \citep{Hu2024} but is F1-trained, carries no set through a composition table across paths, and does not abstain. ``When Silence Is Golden'' targets temporal abstention but \emph{trains} it via chain-of-thought supervision and abstention-aware rewards at the answer level \citep{Zhou2026}; ours is structural, training-free, and per-edge. BeDiscovER is a recent discourse \emph{evaluation} suite \citep{Li2025} with no reasoning mechanism. None preserves a relation-algebra disjunction \emph{and} abstains on closure-collapse with a gold-free, training-free, per-edge certificate.

\textbf{Closure over machine-extracted relations.} SputLink computes temporal closure to densify TimeBank \citep{Verhagen2005}; CAEVO does global inference by cascaded sieves \citep{Chambers2014}; structured learning enforces transitivity \citep{Ning2017}. All commit to one consistent labeling to maximize F1, preserve no disjunction, certify no reading error, and do not abstain. SputLink-style closure \emph{produces} the non-adjacent gold whose circularity we avoid by evaluating against direct human-timeline gold \citep{Rogers2019} and manual long-distance gold \citep{Naik2019}.

\textbf{Qualitative reasoning, LLM reasoning, and abstention.} Allen's interval algebra \citep{Allen1983}, the convex point algebra \citep{Vilain1986}, RCC-8 \citep{Randell1992}, and the cardinal-direction calculus \citep{Frank1996, Ligozat1998} supply exact tables; Mackworth's path consistency \citep{Mackworth1977} iterates length-2 intersections to a fixpoint. Path consistency is \emph{complete} for the convex point algebra and the ORD-Horn fragment \citep{Nebel1994} but only \emph{sound-but-incomplete} for full Allen IA and RCC-8 \citep{Renz1999}; we import the algorithms and inherit these facts (our point arm is exact; Allen and RCC-8 arms are sound lower bounds). Chain-of-thought \citep{Wei2022} and self-consistency \citep{Wang2022} operate at the answer level; Logic-LM self-refines on solver crashes \citep{Pan2023} and LINC majority-votes formalizations \citep{Olausson2023}, but none maintains a positive global invariant over relational knowledge. Path-of-Thoughts reasons each extracted path independently \citep{Zhang2024}. The discourse-level reading prompts of \citet{Wei2024} ground our span-local protocol. Selective prediction \citep{Geifman2017} abstains on generic uncertainty; RuleTaker \citep{Clark2020} targets propositional entailment; Reiter's model-based diagnosis \citep{Reiter1987} supplies the minimal-hitting-set machinery for the Mode-B repair we scope as future work. Hallucination in generation is a broad concern \citep{Ji2022}; ours is a per-edge, certificate-backed reduction. For the spatial venue we use SpaRTUN-style RCC-8 scenes \citep{Mirzaee2022}, alongside SpartQA \citep{Mirzaee2021} and StepGame \citep{Shi2022} as structural contrasts; the natural absent-relation corpus is built from Re-DocRED \citep{Tan2022}, the completeness-corrected re-annotation of DocRED \citep{Yao2019}.

# Method
\label{sec:method}

## The inverted output contract

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
no-derivation & query unreachable by any composition path \\
Mode~A & narrowing/no-derivation abstention (primary) \\
Mode~B & empty closure certifies an unsound read \\
\textsc{ct}-$s$ & confidence-thresholded raw-abstain baseline on signal $s$ \\
matched cov. & every method scored at the same resolution rate \\
confident-wrong & a committed (non-abstained) answer $\neq$ gold \\
\hline
\end{tabular}
\caption{Notation and metrics used throughout.}
\label{tab:notation}
\end{table}

## Two value modes, and the behavior confidence cannot replicate

\textbf{Mode~A (sound narrowing and no-derivation abstention).} Composing the LLM's per-edge sets through the exact table and intersecting at the query pair, the system emits iff the result is a singleton, abstains iff it remains a disjunction, and---the load-bearing case---abstains with ``no relation'' iff \emph{no} composition path reaches the query at all. The intersection of sound sets is always sound, so under all-sound inputs Mode~A's output contains gold with probability exactly $1.0$; this survives path-consistency incompleteness. \textbf{Mode~B (detection).} An empty closure is a deductive certificate that some contributing read is unsound, with no gold labels; it fires when an over-committed or recall-failed edge is present. Both modes carry the \emph{silent-wrong-narrowing} dual: if gold is \emph{omitted} from a contributing set (recall failure), closure can narrow to a confident wrong singleton with no collapse---the failure we bound per-edge by $(1-r)$ and which dominates the natural-text errors (Section~\ref{sec:temporal}).

The crucial point for the thesis is \emph{why a confidence threshold cannot replicate the no-derivation behavior.} An absent-relation query is one where the truthful answer is ``no relation.'' A raw LLM asked for the relation will typically name one anyway, and---because the named relation is locally plausible---it names it at \emph{high} confidence, with samples agreeing. Every confidence/uncertainty signal therefore reads ``certain'' and commits the fabrication. The certificate abstains for a reason orthogonal to confidence: there is no path through the composition table that derives \emph{any} relation for that pair. This is not a better-calibrated abstention signal; it is a different \emph{kind} of signal, and Section~\ref{sec:fairbaseline} measures the gap directly.

## Two worked examples

\textbf{Mode~A no-derivation abstention.} In a CLUTRR story, two entities $X,Y$ lie in disconnected family components. The raw reader, asked ``what is $Y$ to $X$?'', answers ``\textsf{nephew}'' at confidence $0.8$ with $9/10$ self-consistency samples agreeing---a textbook high-confidence hallucination that no confidence threshold removes. The certificate composes the extracted atomic kinship edges, finds no derivation reaching $(X,Y)$, and abstains ``no relation''---the correct, faithful output. \textbf{Mode~B collapse.} A vague spatial read renders \textsf{around} as $\{\textsf{NTPPi},\textsf{TPPi}\}$, dropping the gold \textsf{EC}; composing this against another constituent yields the empty set, so the certificate flags an unsound read and abstains rather than committing the wrong \textsf{DC}---a catch a confidence threshold (which would have committed the high-confidence \textsf{DC}) cannot make.

## The fair baseline: a confidence-thresholded raw-abstain abstainer

Throughout, the certificate is benchmarked not only against always-answer baselines (commit-the-argmax, raw forced-single) but against a \emph{confidence-thresholded raw-abstain} baseline \textsc{ct}-$s$: commit the raw LLM's top-1 answer iff signal $s\ge\tau$, else abstain, with $\tau$ swept so every method reports at the \emph{same} coverage. We instantiate $s$ with the best available battery: (a) \emph{verbalized} self-reported confidence; (b) \emph{sc\_margin}, the self-consistency vote-margin over $k{=}10$ temperature-$0.7$ samples; (c) \emph{ptrue}, Kadavath's P(True); and (d) \emph{negent}, semantic-entropy negentropy over the $k{=}10$ samples clustered by relation [ARTIFACT:art_LeRQRGHJZcdQ]. The certificate's claim is specifically that it beats \textsc{ct}-$s$ on the no-derivation stratum, while honestly tying or losing on ordinary single-path deduction.

## Genuine fuzzy unification, bounded by the certificate
\label{sec:method-fuzzy}

The umbrella goal invokes the LLM as a probabilistic engine ``to handle fuzzy unifications \dots where strict symbolic matching fails.'' We substantiate this without circularity: a known relation is rendered with a \emph{vague} preposition (\textsf{near}, \textsf{touching}, \textsf{around}) or an \emph{informal} kinship term (\textsf{guardian}, \textsf{family elder}, \textsf{relative by marriage}) that has \emph{no single} table answer, and the LLM must emit a calibrated disjunction over base relations. The abstain-on-collapse certificate then runs unchanged. This is explicitly \emph{not} upper-ontology grounding and \emph{not} general fuzzy unification over arbitrary predicates, both out of scope.

## Datasets, baselines, and metrics

\textbf{End-to-end venue (templated).} CLUTRR kinship \citep{Sinha2019}, standardized to gold graphs with typed atomic edges, held-out multi-hop queries (hops $2$--$10$), and within-document absent-relation pairs [ARTIFACT:art_HS7-lxhZnU9m]. CLUTRR is template-generated (semi-synthetic), short (max $871$ characters), and its composition table is hand-supplied. \textbf{Genuinely natural absent-relation corpus.} Re-DocRED \citep{Tan2022}, completeness-corrected Wikipedia prose, built and gold-verified for the no-derivation regime [ARTIFACT:art_NUWTxBVWENIJ]. \textbf{Natural-text temporal corpora.} NarrativeTime (a timeline-based full-coverage human re-annotation of TimeBank-Dense) \citep{Rogers2019, Cassidy2014}, TDDMan (manual long-distance pairs) \citep{Naik2019}, and MATRES (intra/adjacent only, the gate-validation control) \citep{Ning2018} [ARTIFACT:art_PNrS9T8JeATf]. \textbf{Spatial venue.} SpaRP-PS1 (SpaRTUN-style RCC-8 scenes) \citep{Mirzaee2022} [ARTIFACT:art_f-ofxduZjwSM]. \textbf{Synthetic backbone.} Globally-consistent QCNs over the convex point, Allen, and RCC-8 algebras [ARTIFACT:art_ghVQmxVlmOJJ]. \textbf{Baselines}: the confidence-thresholded \textsc{ct}-$s$ battery (primary); always-answer commit-the-argmax and raw forced-single; chain-of-thought \citep{Wei2022}; self-consistency \citep{Wang2022}; LINC-style voting \citep{Olausson2023}; Path-of-Thoughts \citep{Zhang2024}; the ILP-commit contract \citep{Eirew2025}; and a best-single-path composition baseline for the cross-path test. \textbf{Metrics}: confident-wrong (hallucination) rate \emph{always reported with coverage}; selective accuracy at matched coverage; the crux survival fraction (fraction of absent hallucinations a confidence rule keeps at the certificate's coverage); atomic P/R (held-fixed control); per-edge recall; and, for fuzzy reads, expected calibration error (ECE).

# Experimental Setup
\label{sec:setup}

Readers are \texttt{google/gemini-3.1-flash-lite} (primary, temperature $0$) and a stronger cross-family reader (\texttt{deepseek/deepseek-v3.2}); all LLM calls use a SHA-256 disk cache and a hard cost guard. The fair-baseline experiment (Section~\ref{sec:fairbaseline}) re-uses the exact cached CLUTRR pool ($180$ absent $+$ $102$ present) and spatial RCC-8 pool ($228$ single-path queries); a reproduction gate confirms the rebuilt certificate/raw/self-consistency/Path-of-Thoughts predictions are identical to the published pool ($0$ mismatches, \$0), and the new four-signal battery cost \$0.30 once [ARTIFACT:art_LeRQRGHJZcdQ]. Story-clustered paired bootstrap uses $B{=}10000$, Holm-adjusted over the four signals. The QCN engine is gated by a unit-test suite: the Allen $169$-cell and RCC-8 $64$-cell tables match the published cells with $0$ failures, convex-point completeness is confirmed against brute force, and the iteration-isolation test confirms \textsc{full}$=$\textsc{naive} at length $2$ and \textsc{full}$\neq$\textsc{naive} on $3$-hop chains. Realized spend is small throughout: the CLUTRR end-to-end run and the two decisive tests together $\sim$\$1.2; the fuzzy-unification cache \$0.003; the powered temporal study $\sim$\$2.4; the operational study \$0.31; the fair-baseline battery \$0.30; cached re-runs \$0.

# Results

## The certificate catches confident hallucinations that confidence cannot see (\textsc{real-llm-read})
\label{sec:fairbaseline}

This is the paper's load-bearing result and the direct answer to the reviewer's question: is the certificate's hallucination safety on absent-relation queries merely a re-skin of an uncertainty signal the LLM already has? It is not. We pit the certificate against the best available confidence/uncertainty battery at matched coverage and show it removes exactly the high-confidence absent-relation hallucinations that \emph{no} confidence rule removes [ARTIFACT:art_LeRQRGHJZcdQ].

[FIGURE:fig2]

\textbf{The LLM is confidently wrong on absent relations.} On the $180$ CLUTRR absent pairs the raw LLM commits a kinship on $47.2\%$ of them; the certificate's confident-wrong rate is $2.8\%$ (reduction $0.444$, $95\%$ CI $[0.317,0.583]$, clearing the pre-registered $0.20$ bar). At the LLM's \emph{natural} coverage, no confidence signal removes a single one of these hallucinations---they are all confident, so every threshold commits them.

\textbf{Crux: confidence is blind to absent hallucinations.} Calibrate each signal's threshold to the certificate's coverage and measure the fraction of the $85$ absent hallucinations that \emph{survive} (Table~\ref{tab:fairbaseline}, Figure~\ref{fig:fig2}): verbalized $0.435$, sc\_margin $0.718$, P(True) $0.247$, semantic-entropy $0.718$. Verbalized confidence is $\ge 0.5$ on $100\%$ of the hallucinations; only P(True) partially separates them (median P(True) $=0.0$ on hallucinations) yet $24.7\%$ still survive. A confident, self-consistent fabrication is invisible to dispersion-based signals by construction.

\textbf{Decisive mixed-pool showdown.} On a mixed present/absent pool ($n{=}282$) so that abstaining on everything cannot win, at matched coverage $0.266$ the certificate's selective accuracy is $0.827$ versus verbalized $0.413$, sc\_margin $0.373$, P(True) $0.440$, and semantic-entropy $0.373$---roughly double every signal. The certificate's confident-wrong rate ($0.046$) is strictly below each signal's ($0.16$--$0.17$); reductions are $0.110$ (vs verbalized, Holm $p_{\text{adj}}{=}0.0004$), $0.121$ (sc\_margin, $0.0027$), $0.103$ (P(True), $0.0027$), and $0.121$ (semantic-entropy, $0.0027$), all Holm-adjusted CIs excluding $0$. A single neural threshold cannot simultaneously abstain on absent pairs and cover present ones; the certificate does both, because its signal is structural. Cross-family (\texttt{deepseek-v3.2}) reproduces the edge: $48.3\%$ absent hallucination, survival fractions $0.672$/$0.224$/$0.103$/$0.224$, certificate still structurally abstaining---so this is not a weak-reader artifact.

\textbf{Honest scope boundary.} On the genuine ordinary \emph{single-path} stratum (spatial RCC-8, $228$ queries) the certificate \emph{ties or loses}: confident-wrong $0.022$ vs raw-abstain $0.035$ (reduction CI includes $0$), and the matched-coverage selective-accuracy gap is $-0.088$ ($95\%$ CI $[-0.222,0.040]$, favoring the baseline). When one short chain suffices, the model's dispersion \emph{is} an informative uncertainty signal, well-calibrated, and the sound-but-incomplete closure only sacrifices coverage. The certificate's distinctive value is therefore localized---sharply---to the no-derivation regime and to multi-hop deduction (where, on CLUTRR-present, it again wins: $0.886$ vs $0.543$ for every confidence baseline at matched coverage $0.686$), not to ordinary single-hop deduction.

\begin{table}[t]
\centering
\small
\begin{tabular}{lcccc}
\hline
Signal $s$ & \multicolumn{2}{c}{Crux: survive$^\dagger$} & Mixed sel.\ & Mixed CW \\
 & gemini & deepseek & acc.$^\ddagger$ & redux$^\ddagger$ \\
\hline
verbalized & 0.435 & 0.672 & 0.413 & 0.110 \\
sc\_margin & 0.718 & 0.224 & 0.373 & 0.121 \\
P(True) & 0.247 & 0.103 & 0.440 & 0.103 \\
semantic-entropy & 0.718 & 0.224 & 0.373 & 0.121 \\
\hline
\textbf{Certificate} & \textbf{structural} & \textbf{structural} & \textbf{0.827} & --- \\
\hline
\end{tabular}
\caption{The certificate vs.\ a four-signal confidence/uncertainty battery (\textsc{real-llm-read}). $^\dagger$Fraction of the $85$ absent hallucinations that survive each signal's rule at the certificate's coverage---confidence keeps the confident fabrications. $^\ddagger$Mixed-pool ($n{=}282$) selective accuracy at matched coverage $0.266$ and certificate-vs-signal confident-wrong (CW) reduction (all Holm-adjusted CIs exclude $0$). On absent queries the raw LLM is confidently wrong $47.2\%$ of the time; the certificate $2.8\%$.}
\label{tab:fairbaseline}
\end{table}

## End-to-end on CLUTRR: all four goal items, executed in Prolog (\textsc{real-llm-read})
\label{sec:clutrr}

The certificate runs end-to-end on real (templated) CLUTRR text: a real LLM reads atomic kinship triples span-by-span; a forward-union least-fixpoint engine recovers the held-out query and emits a certificate [ARTIFACT:art_0a7i481ZRwS1]. As a $0$-LLM go/no-go, the gold-atomic engine on all $16{,}131$ clean stories is $100\%$ accurate on every emitted answer at a $98.5\%$ singleton rate; the $1.5\%$ abstentions are genuine table ambiguities, so the engine declines to guess.

[FIGURE:fig3]

\textbf{All four umbrella goal items.} (i) \emph{Atomic extraction}: the span-local reader extracts typed kinship triples at P/R/F1 $=0.536/0.532/0.534$ (doc-clustered CIs precision $[0.486,0.589]$, recall $[0.483,0.583]$), reported as a held-fixed control. (ii) \emph{Multi-hop accuracy}: Mode~A's selective accuracy stays between $0.75$ and $1.00$ from hop-2 through hop-10, while the raw LLM collapses (hop-3 $0.444 \rightarrow$ hop-10 $0.0$) and Path-of-Thoughts degrades (hop-3 $0.357 \rightarrow$ hop-10 $0.20$); at matched coverage $0.686$ Mode~A reaches selective accuracy $0.886$ versus Path-of-Thoughts $0.457$ (gap $+0.429$, $95\%$ CI $[0.299,0.563]$, Holm $p_{\text{adj}}{=}0.0015$) and every confidence baseline $0.543$ (Table~\ref{tab:clutrr}). We are explicit that this selective-accuracy win is the \emph{inherited} neuro-symbolic premise (compose with the exact table, not the LLM), not our distinctive contribution---on rich Allen the analogous $+0.676$ system gap decomposes into $+0.673$ inherited and only $+0.0025$ novel (Appendix~\ref{sec:mechanism}). (iii) \emph{Auditable, executed trace}: the closed network is emitted as a runnable SWI-Prolog program; we install SWI-Prolog $9.0.4$ and \emph{execute} $40$ sampled query programs---$40/40$ run to exit $0$, $40/40$ match the Python engine, $39/40$ match gold (the one miss is a read recall failure, not a closure error). (iv) \emph{Hallucination reduction}: the $0.444$ absent-relation reduction of Section~\ref{sec:fairbaseline}. A gold-read oracle isolates the bottleneck: given gold atomic reads, Mode~A is $1.00$ accurate at coverage $0.951$ versus $0.433$ for raw and Path-of-Thoughts, so the symbolic closure is not the limiting factor---the neural read is (atomic recall $\sim 0.53$).

\begin{table}[t]
\centering
\small
\begin{tabular}{lccc}
\hline
Method (matched cov.\ $0.686$) & Sel.\ acc. & Nat.\ cov. & Gap \\
\hline
\textbf{Mode~A (certificate)} & \textbf{0.886} & 0.686 & --- \\
Confidence baselines (\textsc{ct}-$s$) & 0.543 & 0.794 & $+0.343$ \\
Self-consistency \citep{Wang2022} & 0.557 & 0.794 & $+0.329$ \\
Path-of-Thoughts \citep{Zhang2024} & 0.457 & 0.882 & $+0.429$ \\
\textsc{off} (no propagation) & 0.000 & 0.000 & --- \\
\hline
Gold-read oracle (Mode~A) & 1.000 & 0.951 & --- \\
\hline
\end{tabular}
\caption{CLUTRR end-to-end selective accuracy on present multi-hop deduction queries (\textsc{real-llm-read}, $n{=}102$, hops $2$--$10$). The selective-accuracy win is the inherited neuro-symbolic premise; the distinctive certificate value is the absent-relation result of Table~\ref{tab:fairbaseline}. The gold-read oracle shows closure is not the bottleneck.}
\label{tab:clutrr}
\end{table}

## Genuine fuzzy unification, against a fair confidence abstainer (\textsc{real-llm-read})
\label{sec:fuzzy}

In two labeled settings a known relation is rendered with a vague or out-of-table phrase and a real LLM emits a calibrated disjunction: \emph{(1) vague spatial RCC-8}---\textsf{near}/\textsf{touching}/\textsf{around}/\textsf{inside}/\textsf{overlapping} over $8$ base relations; \emph{(2) ambiguous kinship}---\textsf{guardian}/\textsf{family elder}/\textsf{relative by marriage}/\dots\ mapping to a type-disjunction [ARTIFACT:art_I22c-J7-OcXl]. The reads are genuinely fuzzy and calibrated (fraction at confidence $1.0$ is $0.00$ in both, versus $1.00$ for the memorized-table recall a prior version mislabeled fuzzy unification; per-candidate ECE $0.142$ spatial / $0.111$ kinship).

\textbf{The certificate beats a confidence-thresholded abstainer, not just an always-answer commit} (correcting a reviewer concern about the earlier $0.000$-vs-always-answer comparison) [ARTIFACT:art_0MDLD-w-RXOu]. Replacing the always-answer comparator with a confidence-thresholded top-1 abstainer at matched coverage, the certificate's confident-wrong rate is $0.000$ at coverage $0.535$ (spatial) / $0.314$ (kinship) versus the confidence baseline's $0.415$ ($95\%$ CI $[0.376,0.457]$) and $0.346$ ($[0.293,0.413]$) (Table~\ref{tab:fuzzy}; both bootstrap lower bounds exclude $0$). Notably the certificate beats the baseline \emph{even when the reads are well-calibrated} (kinship ECE $0.051$): a threshold cannot reach $0$ confident-wrong when the maximum emitted top-1 confidence is only $0.8$ and underlying read accuracy is modest, however well-calibrated. \textbf{The strictly distinctive, same-object edge is the Mode-B catch}: on the spatial arm all $5$ genuinely sound-violating reads were caught (e.g.\ \textsf{around}$\rightarrow\{\textsf{NTPPi},\textsf{TPPi}\}$ drops gold \textsf{EC}, so closure collapses and the certificate abstains rather than committing the wrong \textsf{DC}), with $0$ silent-wrong missed; of $100$ unsound calibration reads, all sit at top-1 confidence $0.7$--$0.8$ and $88$ fall in a region a threshold would commit wrong. We frame the contribution honestly as \emph{auditable, faithful abstention that additionally catches sound-violations confidence cannot see}---$5/5$ on spatial, untested on kinship ($0$ unsound reads)---rather than letting the headline rest on the always-answer contrast. \emph{Unit-of-analysis caveat}: the certificate's confident-wrong is measured on closure \emph{queries} while the confidence baseline's is at the edge-\emph{read} level (matched on coverage fraction); a query-level confidence abstainer on this exact pool is the Section~\ref{sec:fairbaseline} experiment, run on CLUTRR/spatial.

\begin{table}[t]
\centering
\small
\begin{tabular}{lcc}
\hline
Quantity & Vague RCC-8 & Amb.\ kinship \\
\hline
read ECE (cand.) & 0.142 & 0.111 \\
frac.\ at conf.\ $1.0$ & 0.00 & 0.00 \\
\hline
certificate cov. & 0.535 & 0.314 \\
\textbf{certificate confident-wrong} & \textbf{0.000} & \textbf{0.000} \\
\textsc{ct}-top1 conf.-wrong @matched cov. & 0.415 & 0.346 \\
\quad $95\%$ CI & {\scriptsize$[.376,.457]$} & {\scriptsize$[.293,.413]$} \\
Mode-B sound-violation catches & 5/5 & 0/0 (untested) \\
\hline
\end{tabular}
\caption{Genuine fuzzy unification against a \emph{fair} confidence-thresholded abstainer (\textsc{real-llm-read}). The certificate's confident-wrong is strictly below a confidence-thresholded top-1 abstainer at matched coverage in both settings; its distinctive same-object edge is the $5/5$ Mode-B catch of sound-violating spatial reads.}
\label{tab:fuzzy}
\end{table}

## A genuinely natural absent-relation corpus, built and gold-verified (\textsc{gold-only})
\label{sec:natural}

The reviewer rightly asked for the certificate's value on a \emph{genuinely natural} corpus, not templated CLUTRR or symbolic-id spatial scenes. We constructed one: a document-level kinship corpus from completeness-corrected Re-DocRED \citep{Tan2022} Wikipedia introductory prose (no templating, no concatenation), drop-in compatible with the same finite kinship table and forward-closure engine [ARTIFACT:art_NUWTxBVWENIJ]. Re-DocRED is load-bearing because vanilla DocRED is $\sim$$64.6\%$ false-negative, which would corrupt ``absent $=$ no relation'' gold; on the $400$ shared documents Re-DocRED carries $3{,}087$ family edges versus DocRED's $1{,}716$ ($+1{,}371$, $+80\%$), so only the corrected slice yields a defensible within-document absent label. The primary slice gives $575$ family-bearing documents, $360$ present multi-hop queries ($222$ \emph{composed-only}, whose relation types---\textsf{grand}/\textsf{uncle}/\textsf{in-law}---lie outside DocRED's inventory and are therefore provably non-circular), and $368$ absent pairs (disconnected family components). The drop-in engine is gold-verified: it reproduces $476/476$ emitted present golds and derives the empty set for $577/577$ absent pairs.

We report honestly that this iteration delivers the corpus \emph{built and gold-verified}; the full LLM-read run of the certificate versus a confidence-thresholded abstainer on its no-derivation stratum is the immediate next step. The corpus establishes that the no-derivation regime---high-confidence absent-relation hallucination over real prose with recoverable, non-circular gold---exists outside templated benchmarks, and (per the structural argument of Section~\ref{sec:fairbaseline}, which is corpus-independent) is exactly the regime where confidence signals are blind. Char-length honesty: Wikipedia intros at this annotation density average $\sim$$1{,}020$ characters; no family-bearing document reaches $3{,}000$ and only $\sim$$2.6\%$ reach $2{,}000$. We do not pad or concatenate; the natural-text $+$ absent-relation regime is the load-bearing property, not the $3{,}000$-character target.

## Cross-path coding is synthetic-channel-only: a bounded negative (\textsc{real-read}/\textsc{gold-gate}/\textsc{synth})
\label{sec:decisive}

We are explicit that the most \emph{novel} mechanism we explored---cross-path intersection of disjunctive reads as an error-correcting code over LLM extractions---does not transfer to real text, and we present this as an explanatory account of two negatives, \emph{not} a predictive law. The mechanism needs two conditions to hold jointly: (i) per-edge reads must be \emph{informative} (sound but sub-universal, so intersection has bite), and (ii) the document must offer \emph{same-algebra} structural redundancy ($\ge 2$ edge-disjoint paths whose compositions land in one calculus). Across the two real venues we could a-priori-gate before any LLM spend, each condition was \emph{independently} violated, for opposite reasons.

[FIGURE:fig4]

\textbf{Temporal Allen violates (i).} The a-priori gate is GO---the structure exists in gold ($N{=}125$ gold-singleton multi-path-with-bite queries on TDDMan)---but LLM Allen reads of constituent edges are near-universe (event-local underdetermined-rate $0.87$, breadth $11.5$ of $13$; the stronger \texttt{deepseek-v3.2} is \emph{more} conservative at $0.99$, breadth $12.9$, so not a weak-model artifact), so intersection, best-single, and naive all resolve $0/125$ [ARTIFACT:art_0AIWMhwc1pJM]. Text underdetermines interval endpoints. \textbf{Spatial RCC-8 violates (ii).} Reads are informative (breadth $2.1$ of $8$, underdetermined $0.036$), but a zero-LLM gate over the \emph{verified} gold shows no same-algebra multi-path bite: the RCC-8 subgraph is a containment tree (all $228$ deduction queries have one edge-disjoint path) and the cardinal subgraph already composes to a singleton on the best single path, so the corpus's $27.4\%$ ``tight-multipath'' flag is purely structural and the genuine redundancy is \emph{cross-algebra} (topology $\perp$ direction), not intersectable in one calculus [ARTIFACT:art_i53dBKgGY3Ig]. \textbf{Synthetic controls satisfying both conditions confirm the mechanism is real}: on Allen at reader-recall $0.95$, intersection selective accuracy $0.976$ vs best-single $0.717$ ($+0.259$, $95\%$ CI $[0.177,0.349]$); on RCC-8, $0.890$ vs $0.797$. We therefore claim only that these two conditions were each independently violated in the two venues we could gate, with synthetic controls localizing the cause---not a sharp, general characterization (the conditions are close to definitionally necessary, so their joint absence across two venues is an explanation, not a validated law). Even where it works, the realized cross-path \emph{coverage} bite is tiny ($+0.024$ over best-single, CI includes $0$); the value is precision of committed answers ($+0.259$ selective accuracy), not coverage. Separately, on the $228$ single-path RCC-8 queries SpaRP-PS1 \emph{does} host, the certificate cuts confident-wrong from raw-LLM $0.193$/CoT $0.123$ to $0.022$, but as Section~\ref{sec:fairbaseline} reported this is abstention-driven and ties a confidence-thresholded baseline---consistent with the no-derivation/ordinary-deduction boundary.

## Natural temporal text: the certificate is only weakly protective (\textsc{real-llm-read})
\label{sec:temporal}

On dense natural temporal prose we report the certificate's limits without spin. Scaling the temporal head-to-head to $600$ deduction-required queries ($300$ NarrativeTime, $300$ TDDMan) in the PC-complete convex point algebra and re-analyzing with a corrected fixed-operating-point bootstrap [ARTIFACT:art_OETjJkketEVS] [ARTIFACT:art_Vc1UBGIVSi0T]: the previously published temporal CIs were a bootstrap artifact (the gap was re-derived inside each resample, recentering on the volatile low-coverage baseline). Holding the operating point fixed, the Mode-A advantage is marginal and not robustly significant---vs Path-of-Thoughts $+0.027$, CI $[-0.088,0.140]$, $p{=}0.33$; vs self-consistency $+0.035$, CI $[-0.061,0.135]$, $p{=}0.26$; neither clears Holm; the raw LLM is in fact \emph{more} accurate than Mode~A at this coverage ($0.699$ vs $0.575$). The certificate is \emph{weakly protective}: among the $18.8\%$ of queries Mode~A commits to, it is confident-wrong $42.5\%$ of the time ($48/113$), and all $48$ are silent-wrong-narrowing (gold omitted from a contributing read, so closure narrowed to a wrong singleton with no collapse, which Mode~B cannot flag). The end-to-end reduction vs raw ($0.61 \rightarrow 0.425$, i.e.\ $0.185$, CI $[0.087,0.280]$) is real but must be read alongside Mode~A's $0.188$ coverage versus raw's $1.0$. Read-soundness is the binding, corpus-specific constraint: the stronger reader reaches recall $0.932$ on NarrativeTime (CI $[0.888,0.967]$, straddling the $0.90$ gate) but stays below it on discourse-level TDDMan ($0.819$). A \$0 synthetic backstop closes the loop: when reads are sound (recall $0.96$), Mode~A beats raw by $+0.225$ at matched coverage [ARTIFACT:art_FtN4LBzazO_l]---isolating read-soundness, not closure, as the real-text gate.

## An operational $\sim$3000-character case study (\textsc{real-llm-read})
\label{sec:operational}

To probe operation at the umbrella's goal length we ran the full pipeline---span-local read $\to$ QCN closure $\to$ executed SWI-Prolog trace-graph $\to$ quantified hallucination reduction---as an \emph{operational case study} (per-document operating points, not a powered test), with the documents \emph{honestly labeled} as constructed [ARTIFACT:art_WQoePKrpsTPo]. The temporal arm uses $5$ NarrativeTime news articles \emph{bracket-selected} around $3000$ characters (mean $3050$, range $2197$--$4293$; \emph{no} single article falls in $[2500,3500]$, reported); the kinship arm uses $3$ documents each \emph{concatenated} from disjoint-entity CLUTRR sub-stories (cross-story pairs absent-by-construction, hence trivially abstained). On the temporal arm the pipeline emits $22$, abstains $126$, and flags $2$ Mode-B collapses over $150$ queries, yielding a confident-wrong reduction of $0.27$--$0.60$ (mean $0.45$) versus whole-document raw generation, at Mode-A coverage $0$--$0.33$ versus raw coverage $1.0$. On the kinship arm atomic recall is $0.39$--$0.56$ (mean $0.49$, the binding ceiling), within-story multi-hop selective accuracy is $0.75$ ($6/8$ emitted correct), and all $56$ cross-story absent pairs are abstained with $0$ confident-wrong. Across both arms $95$ Prolog programs were discharged and executed in SWI-Prolog $9.0.4$. The study confirms the pipeline is operational on goal-length documents and that the binding constraint is atomic extraction, not the certified closure.

# Discussion
\label{sec:discussion}

\textbf{What the evidence supports.} The single thesis holds: a training-free, gold-free, per-edge abstain-on-collapse certificate catches confident relational hallucinations that a confidence threshold cannot see. Against the best four-signal uncertainty battery at matched coverage, the certificate removes the absent-relation hallucinations that survive every signal (mixed-pool selective accuracy $0.827$ vs $0.37$--$0.44$; Holm-significant confident-wrong reductions), and the edge reproduces cross-family and against a fair confidence abstainer on genuinely fuzzy reads. This is a capability gap, not a calibration gap: a confident, self-consistent fabrication is invisible to dispersion by construction \citep{Wen2024, Song2025}, whereas the certificate's signal is structural (no derivation path). The CLUTRR pipeline delivers all four umbrella goal items with SWI-Prolog-executed traces, and a gold-read oracle localizes the remaining error to the neural read, not the closure.

\textbf{What it does not support, stated without spin.} The certificate's distinctive value is \emph{localized}, not universal. On ordinary single-path deduction, where dispersion is informative, a confidence threshold ties or beats it. The signature cross-path-intersection coding mechanism is synthetic-channel-only---it needs informative reads \emph{and} same-algebra redundancy, each independently violated in the two real venues we gated. The natural-text temporal advantage is marginal and the certificate weakly protective there, because recall-driven silent narrowing is undetectable. And the load-bearing fair-baseline result is on templated CLUTRR plus semi-natural spatial and fuzzy settings; the genuinely natural Re-DocRED corpus is built and gold-verified but its LLM-read run is the immediate next step.

\textbf{Where to deploy, and why.} Deploy the certificate wherever no-derivation / absent-relation queries carry real cost---an entity pair the document does not connect, a query the facts cannot answer---because that is exactly where a confidence threshold fails and the structural signal succeeds. The two-condition account also explains the long-standing puzzle that consistency enforcement does not improve F1 \citep{Kougia2024, Eirew2025}: on coarse algebras there is little to fix; on rich algebras the headroom is real but the same richness defeats the reader or the available structure. Per-edge read-soundness, not more consistency post-processing, is the lever to invest in.

\textbf{Limitations.} (1) The fair-baseline edge is demonstrated on templated CLUTRR, semi-natural spatial, and fuzzy settings; the natural-corpus LLM-read run is future work (the corpus is delivered and gold-verified). (2) The cross-path coding mechanism is synthetic-only. (3) Path consistency is complete only for the convex point algebra; Allen and RCC-8 numbers are sound lower bounds. (4) CLUTRR is templated, short ($\le 871$ characters), with gold entity grounding and a hand-supplied table; no benchmark document reaches $\sim$3000 characters, and the operational study's documents are bracket-selected / concatenation-constructed. (5) Upper-ontology grounding, atomic re-extraction, and general fuzzy unification are out of scope; the fuzzy result is scoped to disjunctions over a known base vocabulary and its reads are term-conditioned. (6) The Mode-B fuzzy edge rests on $5$ caught spatial reads ($0$ testable on kinship). (7) Mode-B repair quality and a trained-reader ablation are future work.

# Conclusion
\label{sec:conclusion}

We treated the deduction sub-module of a text-to-logic pipeline as a faithfulness problem and contributed one thing a reader can carry away in a sentence: \emph{a structural, label-free certificate that catches confident relational hallucinations that confidence cannot see.} Keep the LLM a high-recall disjunctive reader, compose only through exact relation-algebra tables, and abstain when iterated closure leaves a disjunction, collapses to empty, or---the load-bearing case---finds no derivation path at all. Against the best available confidence/uncertainty battery at matched coverage, the certificate removes the high-confidence absent-relation hallucinations that every signal keeps (CLUTRR absent reduction $0.444$; mixed-pool selective accuracy $0.827$ vs $0.37$--$0.44$; cross-family reproduced; the same edge over a fair confidence abstainer on fuzzy reads), while honestly tying on ordinary single-path deduction and remaining only weakly protective on dense natural temporal prose. We are equally explicit about the boundary: the cross-path-intersection coding mechanism is synthetic-channel-only, an explanatory account of two independently-violated conditions, not a law. Three concrete next steps follow: (1) run the certificate-versus-confidence comparison on the delivered natural Re-DocRED absent-relation corpus; (2) raise per-edge read recall on discourse-level gold into the $0.90$ regime; and (3) integrate the validated certificate into the full pipeline with upper-ontology grounding.

\appendix
# Appendix: Mechanism analysis (\textsc{real-on-synth} / \textsc{synth} / \textsc{theorem})
\label{sec:mechanism}

We collect the inherited and synthetic mechanism results that explain---but do not compete with---the certificate headline.

[FIGURE:fig5]

\textbf{Algebra-richness scaling (inherited).} With real LLM reads on synthetic NL, the matched-coverage advantage over Path-of-Thoughts grows monotonically with base-relation count: point ($3$) $+0.043 \rightarrow$ RCC-8 ($8$) $+0.448 \rightarrow$ Allen ($13$) $+0.676$ (all Holm-significant) [ARTIFACT:art_N0e4pH_C_Cxw] [ARTIFACT:art_QToTkRe6Umb8]. On a coarse algebra the LLM rarely has more than one plausible composition; as branching grows, free neural composition accumulates locally-fluent but globally-inconsistent steps that exact intersection eliminates. This is the standard table-vs-LLM-composition effect at recall $\sim1.0$ on templated NL---not our discovery---and indeed the $+0.676$ Allen system gap decomposes into an inherited $+0.673$ and a novel-on-selective-accuracy $+0.0025$ [ARTIFACT:art_D0cHQUJ8kY75]. Because PC is incomplete for RCC-8 and Allen, those numbers are sound lower bounds.

\textbf{Redundancy inverted-U (synthetic).} On a channel calibrated to the real-text frontier, iterated closure error-corrects per recall slice: the full-minus-naive gap is a structural $0.0$ at hop length $2$ and grows with hop length and cyclomatic number (Page trend $p\approx 5\times 10^{-4}$, correcting a prior draft's mis-stated $10^{-13}$) [ARTIFACT:art_FtN4LBzazO_l]. Net Mode-A resolution is an inverted-U in path redundancy $K$, with the optimum moving outward with recall (peak $K^\ast = 2,4,7,10,16$ for recall $0.5,0.625,0.78,0.90,0.95$) and silent-wrong rising $0.006\rightarrow0.146$, always below the bound $(1-r)$ [ARTIFACT:art_N8G6ZlQTONfk]. Even synthetically the realized coverage bite is small ($+0.024$ over best-single); the value is precision, not coverage.

\textbf{Zero-false-positive theorem.} On all-sound contributing edges the Mode-A output contains gold with probability exactly $1.0$, and a collapse never co-occurs with all-sound reads---the soundness invariant of path consistency, verified on $100{,}296$ all-sound networks. Recall is an \emph{input} here, so this characterizes the mechanism rather than predicting a real-text operating point; its empirical content is the conditionality (silent-wrong rises as recall falls), and Section~\ref{sec:decisive} shows the operating point is not reached on the rich-algebra real venues we tested.

\bibliographystyle{plainnat}
\bibliography{references}

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (evidence) The single highest-leverage gap: the load-bearing fair-baseline result remains on TEMPLATED CLUTRR (plus semi-natural spatial/fuzzy). The genuinely natural absent-relation corpus (Re-DocRED) is built and gold-verified (575 docs, 360 present / 368 absent, drop-in engine reproduces present and absent golds), but the decisive certificate-vs-confidence LLM-read experiment on it is explicitly deferred to 'the immediate next step.' This is exactly the action I requested last round, now half-completed (corpus built, experiment not run). The artifact for the analogous CLUTRR battery cost ~$0.30 and the Re-DocRED corpus is engine-compatible, so this is a cheap, in-scope experiment whose absence is the main thing keeping the central claim on templated data. As-is, the paper relies on a corpus-independent structural argument to assert the edge transfers, which a skeptical reviewer will not accept as a substitute for the measurement.
  Action: Run the four-signal fair-baseline experiment (verbalized, sc_margin, P(True), semantic entropy) on the Re-DocRED present/absent pools at matched coverage. Report the crux-survival table, the mixed-pool selective-accuracy showdown, and the Holm-adjusted confident-wrong reductions exactly as in Section 6.1, on a stronger reader if possible. If the edge holds on natural Wikipedia prose, make THAT the headline result and demote CLUTRR to a templated companion; if it is weaker on natural prose, report it honestly — either outcome is more valuable than deferral.
- [MAJOR] (rigor) The certificate's win on the absent-relation stratum is close to structural-by-construction and this is not flagged. CLUTRR absent pairs are DEFINED as entities in different connected components; a sound forward-closure over the extracted graph will derive the empty set (and abstain) on disconnected pairs almost by definition, and imperfect extraction (recall ~0.53) only increases apparent disconnection, so the certificate's 2.8% confident-wrong on absent pairs is near-tautological given the setup. The genuinely non-circular empirical content is (a) the LLM hallucinates a relation on 47% of disconnected pairs at high confidence and (b) the confidence/uncertainty family cannot filter these. The paper currently lets the certificate's abstention rate (2.8% vs 47.2%) and the 0.827-vs-0.37 mixed-pool contrast carry the section without acknowledging that one side of the comparison is handed the structural answer by construction.
  Action: Add an explicit paragraph stating that closure-abstention on disconnected pairs is structural-by-construction, and reframe the load-bearing claim around the two non-circular facts: the measured 47% high-confidence hallucination rate and the measured confidence-blindness (crux-survival). Tie this directly to why extraction recall and the natural-corpus run are load-bearing — on a natural corpus the extracted graph (and hence the absent-detection) is no longer trivially correct, which is precisely what makes that experiment decisive rather than confirmatory.
- [MAJOR] (novelty) Contribution magnitude remains the binding constraint. By the paper's own inherited/novel decomposition, the transferable mechanism (compose through the exact table, abstain on collapse) is the standard neuro-symbolic premise (+0.673 inherited vs +0.0025 novel on selective accuracy), and the one genuinely novel mechanism explored (cross-path intersection as an error-correcting code) is synthetic-only and presented as a double negative. 'A sound logic reasoner abstains when it cannot derive an answer' is the default behavior of any sound NeSy system, so a NeSy-audience reviewer may read the core finding as expected. The defensible, valuable novelty is the EMPIRICAL ISOLATION against the best confidence battery — but that needs to be positioned as such and strengthened, not presented as if the certificate mechanism itself were the new idea.
  Action: Position the paper unambiguously as an empirical/diagnostic contribution: the new knowledge is that the entire confidence/uncertainty family is structurally blind to confident absent-relation hallucinations while a gold-free structural signal is not. Strengthen it by (i) the natural-corpus run (critique 1) and (ii) at least a second relation domain or reader to show the confidence-blindness finding is not kinship-specific. Avoid any phrasing that implies the closure/abstention mechanism is itself the novelty — the paper already concedes it is inherited, so make that concession the framing rather than a footnote.
- [MINOR] (evidence) The fuzzy-unification comparison (Section 7, Table 3) has a unit-of-analysis mismatch the paper honestly flags but does not resolve: the certificate's confident-wrong (0.000) is measured at the closure-QUERY level, while the confidence-thresholded baseline's (0.415 spatial / 0.346 kinship) is measured at the edge-READ level, matched only on coverage fraction. This weakens the otherwise-clean '0.000 vs 0.415' claim, and the strictly-distinctive Mode-B edge still rests on only 5 caught spatial reads (0 on kinship, untested). After the much stronger query-level Section 6.1, the fuzzy section is now a secondary support whose headline contrast is the least apples-to-apples in the paper.
  Action: Either build a true query-level confidence abstainer on the fuzzy pools (mirroring Section 6.1) so the comparison is apples-to-apples, or further downweight the fuzzy section relative to Section 6.1 and lead its framing with the honestly-quantified 5/5 Mode-B sound-violation catch as the distinctive contribution rather than the 0.000-vs-0.415 number. Keep the unit-of-analysis caveat but make sure it does not undercut a headline table.
- [MINOR] (scope) The paper delivers a closure-certified DEDUCTION SUB-MODULE, not the umbrella's operational pipeline: upper-ontology/OpenCyc grounding, general fuzzy unification over arbitrary predicates, atomic re-extraction, and genuine ~3000-char natural professional documents are all scoped out. The operational case study is bracket-selected (temporal; no doc in [2500,3500]) and concatenation-constructed (kinship; the 56/56 cross-story absent pairs are trivially abstained by construction), so it demonstrates the pipeline runs at length rather than that it is useful at length. This is honestly disclosed and the venue is repositioned to NeSy, but a reviewer aligned with the originally-named ACL Knowledge Extraction track would see a significant goal-vs-delivery gap.
  Action: Keep the honest scoping and ensure the first paragraph of the abstract states up-front that this is a deduction sub-module (extraction/grounding/long-document/probabilistic-unification out of scope). Consider compressing the operational case study (its concatenated kinship arm and bracket-selected temporal arm add little beyond 'it runs') to buy space for the natural-corpus result, and state plainly that the umbrella's OpenCyc-grounded, 3000-char-natural-document pipeline is future work this paper does not claim to deliver.
- [MINOR] (clarity) The Re-DocRED verification counts are presented in a way that conflates the two datasets. The paper writes that the 'primary slice gives 575 family-bearing documents, 360 present multi-hop queries ... and 368 absent pairs ... it reproduces 476/476 emitted present golds and derives the empty set for 577/577 absent pairs.' But 476 = re-docred 360 + docred 116 and 577 = re-docred 368 + docred 209, i.e. the round-trip spans both datasets, not the primary slice alone. A careful reader will be confused by 360 != 476 and 368 != 577.
  Action: State the per-dataset breakdown explicitly: the re-docred primary slice is 360 present / 368 absent, and the 476/577 engine round-trip is the combined re-docred + docred verification. One added clause removes the apparent inconsistency.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

kind: hypothesis
title: >-
  The Confidence/Uncertainty Family Is Structurally Blind to Confident Absent-Relation Hallucinations, but a Gold-Free Structural
  Certificate Is Not: An Empirical Isolation in the Deduction Sub-Module of Text-to-Logic Pipelines (the natural-corpus run
  is the decisive open test; closure-abstention on disconnected pairs is conceded structural-by-construction; cross-path qualitative-algebra
  coding is synthetic-channel-only)
hypothesis: |-
  ONE THESIS, REFRAMED AS AN EMPIRICAL / DIAGNOSTIC CONTRIBUTION (reviewer novelty MAJOR + rigor MAJOR, both this round). We STOP positioning the certificate's machinery as the novelty and concede this up-front, as the paper's FRAMING rather than a footnote: keeping the LLM a high-recall disjunctive reader, composing ONLY through exact relation-algebra tables, EMITting a singleton / ABSTAINing on a residual disjunction / FLAGging an unsound read on empty collapse is the STANDARD neuro-symbolic premise -- 'a sound reasoner abstains when it cannot derive an answer' is the default behavior of any sound NeSy system, worth +0.673 inherited vs only +0.0025 novel on selective accuracy (art_D0cHQUJ8kY75). The genuine, defensible, NON-INCREMENTAL new KNOWLEDGE is an EMPIRICAL ISOLATION, not a mechanism: the ENTIRE confidence/uncertainty selective-prediction family -- verbalized confidence, self-consistency vote-margin, Kadavath P(True), semantic-entropy negentropy -- is STRUCTURALLY BLIND to a confident, self-consistent ABSENT-RELATION hallucination (a fabricated relation between entities the document does not connect), whereas a gold-free, training-free STRUCTURAL signal ('no derivation path => abstain') is not, because the absent-relation hallucination is HIGH-confidence and low-dispersion by construction. One sentence a reader repeats: 'The confidence family cannot see the relational hallucinations that matter most -- confident fabrications of relations that do not exist -- but a structural no-derivation certificate can.' Keep evidence-class tags in TABLE COLUMNS, not inline hedging. Everything else (cross-path coding thesis, algebra-richness scaling, inherited/novel decomposition, redundancy inverted-U, zero-FP theorem, fuzzy unification, operational case study, marginal natural-temporal result) is SUPPORTING, demoted to one subsection or a compact appendix.

      THE LOAD-BEARING CLAIM IS THE TWO NON-CIRCULAR FACTS, NOT THE CERTIFICATE'S ABSTENTION RATE (reviewer rigor MAJOR, accepted in full). We now state explicitly, in its own paragraph, that the certificate's near-zero confident-wrong on the ABSENT stratum is LARGELY STRUCTURAL-BY-CONSTRUCTION and must NOT be allowed to carry the section: CLUTRR absent pairs are DEFINED as entities in different connected components, so a sound forward-closure over the extracted graph derives the empty set (and abstains) on disconnected pairs almost by definition, and imperfect extraction (recall ~0.53) only INCREASES apparent disconnection, so the certificate's 2.8% confident-wrong on CLUTRR absent pairs (art_LeRQRGHJZcdQ) is near-tautological given the setup -- one side of the comparison is handed the answer. The genuinely non-circular empirical content, which becomes the headline, is two measured facts about the RAW LLM and the confidence family (both independent of the certificate): (FACT A) the raw LLM fabricates a relation on 47.2% of disconnected/absent CLUTRR pairs (cross-family deepseek-v3.2 48.3%) at HIGH confidence; and (FACT B) NO member of the best four-signal confidence/uncertainty battery removes these at the LLM's natural coverage, and at matched coverage 0.435/0.718/0.247/0.718 of them SURVIVE (verbalized/sc_margin/P(True)/negent; deepseek 0.672/0.224/0.103/0.224), so >=2 signals keep a strong majority -- a confident self-consistent fabrication is invisible to dispersion by construction. These two facts are what make the structural certificate's success informative; we tie this DIRECTLY to why extraction recall and the natural-corpus run are LOAD-BEARING: on a NATURAL corpus the extracted graph (and hence absent-detection) is no longer trivially correct -- extraction errors can make the certificate OVER-abstain on PRESENT pairs -- which is precisely what converts the natural-corpus experiment from confirmatory to DECISIVE.

      OPERATIONAL CEILING + VENUE, IN THE FIRST PARAGRAPH OF THE ABSTRACT (reviewer scope MINOR). State up-front: this is a closure-certified DEDUCTION SUB-MODULE, NOT the umbrella's operational pipeline. Explicitly OUT OF SCOPE and named as FUTURE WORK THIS PAPER DOES NOT CLAIM TO DELIVER: (a) upper-ontology / OpenCyc grounding; (b) general fuzzy unification over arbitrary predicates (we scope fuzzy to disjunctions over a KNOWN base vocabulary); (c) atomic re-extraction (extraction is MEASURED not improved: CLUTRR P/R/F1 ~= 0.536/0.532/0.534); (d) genuine ~3000-char NATURAL professional documents (no benchmark doc reaches it; the operational ~3000-char study is bracket-selected (temporal; none in [2500,3500]) and concatenation-constructed (kinship; 56/56 cross-story absent pairs trivially abstained by construction), so it shows the pipeline RUNS at length, not that it is USEFUL at length). RE-TARGET the primary venue from ACL Knowledge Extraction to a NeSy / temporal-and-qualitative-reasoning track and SAY SO; report real-text utility as structurally EXTRACTION-LIMITED (~0.53 atomic recall => ~19% Mode-A coverage on dense prose).

      ----- CLAIM 1 (THE SINGLE HEADLINE, EMPIRICAL ISOLATION): CONFIDENCE-BLINDNESS TO CONFIDENT ABSENT-RELATION HALLUCINATION, vs THE BEST 4-SIGNAL BATTERY. TAG: REAL-LLM-READ. -----
      The portable, demonstrated-at-power result, now stated as a DIAGNOSTIC about the confidence family (FACT A + FACT B) rather than as a property of the certificate mechanism. STEP A is EXECUTED (art_LeRQRGHJZcdQ, VERDICT=CONFIRM, ~$0.30): against verbalized confidence, self-consistency vote-margin@k=10, Kadavath P(True), and semantic-entropy negentropy -- the BEST available battery, not a strawman -- the raw LLM is confidently wrong on 47.2% of CLUTRR absent pairs and the certificate 2.8% (reduction 0.444, CI [0.317,0.583]); at the LLM's natural coverage NO signal removes any of these; the crux-survival table shows 0.435/0.718/0.247/0.718 surviving at matched coverage (only P(True) partially separates, median 0.0, yet 24.7% survive). The DECISIVE mixed present/absent pool (n=282, so abstain-on-everything cannot win) at matched coverage 0.266: certificate selective accuracy 0.827 vs every signal 0.37-0.44 (~2x); Holm-adjusted confident-wrong reductions 0.103-0.121, all CIs exclude 0; cross-family deepseek-v3.2 reproduces the edge. HONESTY, FOREGROUNDED: the CLUTRR-absent abstention is structural-by-construction (above); the non-circular content is FACT A and FACT B; the multi-hop PRESENT selective-accuracy win (CLUTRR 0.886 vs 0.543 at matched coverage 0.686) is the INHERITED NeSy premise, labeled as such wherever it appears.

      ----- CLAIM 2 (THE SINGLE DECISIVE OPEN EXPERIMENT for iter-7 = RUN STEP B ON THE BUILT NATURAL CORPUS). TAG: REAL-LLM-READ. -----
      This is the reviewer's #1 action (evidence MAJOR) and the paper's path above the bar; the corpus is ALREADY built and gold-verified (art_NUWTxBVWENIJ), the analogous CLUTRR battery cost ~$0.30, and the corpus is drop-in engine-compatible, so this is a cheap, in-scope experiment whose ABSENCE is the only thing keeping the central claim on templated data. iter-7 MUST run the four-signal fair-baseline experiment (verbalized, sc_margin, P(True), semantic entropy) on the Re-DocRED natural Wikipedia present/absent pools at matched coverage, reporting -- exactly as in the CLUTRR section -- (i) the raw-LLM absent-hallucination rate (FACT A), (ii) the crux-survival table (FACT B), (iii) the mixed-pool selective-accuracy showdown, and (iv) the Holm-adjusted confident-wrong reductions, on a STRONGER reader if affordable, and including >=1 ADDITIONAL relation DOMAIN or reader (reviewer novelty MAJOR-ii) -- e.g. confirm FACT A/FACT B on natural spatial-containment absent pairs or temporal no-relation queries -- to show the confidence-blindness finding is NOT kinship-specific (cross-family deepseek already supplies reader diversity). CRITICAL NATURAL-CORPUS NUANCE (ties CLAIM 2 to the rigor MAJOR): on Re-DocRED the certificate is NO LONGER handed the structural answer -- because extraction recall is imperfect, the certificate can over-abstain on PRESENT multi-hop pairs (missing connecting edges look disconnected), so the genuine test is whether it STILL answers present pairs while abstaining on absent ones in the MIXED regime. FORK (both publishable): IF the certificate beats the four-signal battery on the Re-DocRED MIXED pool at matched coverage with Holm-adjusted CIs excluding 0 -> MAKE THAT THE HEADLINE and demote CLUTRR to a TEMPLATED companion; IF extraction recall on natural prose is so low that the certificate over-abstains and TIES/LOSES the mixed-pool showdown -> report it HONESTLY as the extraction-limited boundary, while preserving the DIAGNOSTIC contribution (FACT A + FACT B are properties of the raw LLM and the confidence signals, NOT the certificate, and are expected to reproduce on natural prose regardless of the certificate's net utility) -- i.e. confidence-blindness is corpus-robust even where the certificate's net utility is gated by extraction. EITHER outcome is more valuable than the current deferral.

      ----- CLAIM 3 (GENUINE FUZZY UNIFICATION, SUPPORTING, NOW DOWNWEIGHTED; reviewer evidence MINOR). TAG: REAL-LLM-READ. -----
      The genuine fuzzy-unification experiment (art_I22c-J7-OcXl) retired the iter-4 circular Mode-P: rendering a known relation with a VAGUE preposition (near/touching/around) or an INFORMAL kinship term (guardian/family elder/relative by marriage) yields CALIBRATED sub-1.0 disjunctions (fraction-at-1.0 = 0.00 in both vs Mode-P's 1.00; per-candidate ECE 0.142 spatial / 0.111 kinship). The certificate's confident-wrong is 0.000 at coverage 0.535/0.314 vs a confidence-thresholded top-1 abstainer 0.415 [0.376,0.457] / 0.346 [0.293,0.413] (art_0MDLD-w-RXOu). UNIT-OF-ANALYSIS FIX (reviewer evidence MINOR): the 0.000-vs-0.415 contrast is APPLES-TO-ORANGES -- certificate confident-wrong is measured at the closure-QUERY level while the confidence baseline is at the edge-READ level, matched only on coverage fraction. iter-7 SHOULD either build a TRUE query-level confidence abstainer on the fuzzy pools (mirroring CLAIM 1) so the comparison is apples-to-apples, OR FURTHER downweight the fuzzy section relative to CLAIM 1 and LEAD its framing with the honestly-quantified Mode-B sound-violation catch as the distinctive contribution rather than the 0.000-vs-0.415 number. Keep the caveat but do NOT let it undercut a headline table. The DISTINCTIVE same-object edge is the Mode-B catch (around -> {NTPPi,TPPi} drops gold EC => collapse => abstain instead of committing wrong DC): 5/5 sound-violating spatial reads caught, 0 silent-wrong missed; kinship UNTESTED (0 unsound reads -- the catch holds trivially). This is a SUPPORTING subsection under the CLAIM 1 headline.

      ----- CLAIM 4 (SUPPORTING NEGATIVE, ONE SUBSECTION): CROSS-PATH CODING IS SYNTHETIC-CHANNEL-ONLY. TAG: REAL-LLM-READ + GOLD-ONLY-GATE + SYNTHETIC-CONTROL. -----
      The signature cross-path-intersection mechanism (multi-path redundancy as an error-correcting code over LLM reads) is established at power ONLY on synthetic channels, and FAILED on BOTH a-priori-gated real venues for OPPOSITE reasons: temporal Allen reads are near-universe (event-local underdetermined 0.87; intersection/best-single/naive all resolve 0/125; stronger deepseek-v3.2 MORE conservative at 0.99 -- not a weak-model artifact, art_0AIWMhwc1pJM), and spatial RCC-8 reads informatively (breadth 2.1/8, underdetermined 0.036) but its gold is a containment TREE (all 228 deduction queries have exactly one edge-disjoint path; the cardinal subgraph composes to a singleton on the best single path), so the corpus's 27.4% 'tight-multipath' flag was purely STRUCTURAL and the genuine redundancy is CROSS-algebra, not intersectable in one calculus (art_i53dBKgGY3Ig, a $0 gold-structural negative). Synthetic positive controls satisfying both conditions confirm the mechanism is real (Allen recall_95 selective accuracy 0.976 vs best-single 0.717, +0.259, CI [0.177,0.349]; RCC-8 0.890 vs 0.797). TEMPER (reviewer rigor, carried): present as 'two conditions -- informative sub-universal reads AND same-algebra structural redundancy -- each INDEPENDENTLY violated in the two real venues we could a-priori-gate, with synthetic controls confirming the mechanism when both hold' -- an EXPLANATORY ACCOUNT of two negatives, NOT a predictive law. Even where it works the realized cross-path COVERAGE bite is tiny (+0.024 over best-single, CI includes 0); the gain is precision-of-commitments (+0.259), not coverage. ONE honestly-bounded subsection, explicitly subordinate to the certificate headline; do NOT re-run RCC-8 (the negative is clean and needs no LLM).

      ----- CLAIM 5 (NATURAL TEMPORAL TEXT: certificate only WEAKLY protective; corrected statistics). TAG: REAL-LLM-READ. -----
      On natural temporal text the raw LLM OUT-ACCURACIES Mode-A at matched coverage (0.699 vs 0.575, gap -0.124); among ~19% Mode-A commits it is CONFIDENT-WRONG 42.5% (48/113), ALL silent-wrong-narrowing (gold omitted from a contributing read => confident wrong singleton with NO collapse, UNDETECTABLE at ~0.85 recall). The corrected FIXED-operating-point H1 CIs INCLUDE ZERO (vs PoT +0.027 [-0.088,0.140] p=0.33; vs SC +0.035 [-0.061,0.135] p=0.26; neither clears Holm; the earlier CONFIRM was a bootstrap artifact, art_Vc1UBGIVSi0T). State plainly: the natural-text temporal comparative advantage is MARGINAL and not robustly significant; the certificate's value there is the gold-free certificate + abstention-as-an-OPTION, bounded by read recall (end-to-end confident-wrong reduction 0.61->0.425 = 0.185, CI [0.087,0.280], read alongside Mode-A's 0.188 coverage vs raw 1.0). Read-soundness is the binding, CORPUS-SPECIFIC constraint (NarrativeTime stronger reader 0.932, CI [0.888,0.967] straddles the 0.90 gate; TDDMan below). A $0 synthetic backstop (recall 0.96) gives Mode-A +0.225 over raw, isolating read-soundness, not closure, as the gate. Supporting, not a headline.

      ----- CLAIM 6 (OPERATIONAL CASE STUDY, SUPPORTING, COMPRESSED; reviewer scope MINOR). TAG: REAL-LLM-READ. -----
      COMPRESS this section (its concatenated kinship arm and bracket-selected temporal arm add little beyond 'it runs') to buy space for the natural-corpus result (CLAIM 2). The first end-to-end ~3000-char run (art_WQoePKrpsTPo) is an OPERATIONAL CASE STUDY (per-document operating points, not a powered test): temporal arm = 5 NarrativeTime news articles BRACKET-selected around 3000 chars (NONE in [2500,3500]; mean 3050, range 2197-4293), kinship arm = 3 docs CONCATENATED from disjoint-entity CLUTRR sub-stories (cross-story pairs absent-by-construction => trivially abstained). 95 Prolog programs discharged AND executed in swipl 9.0.4; hallucination reduction vs whole-document raw 0.27-0.60 (mean 0.45) at Mode-A coverage 0-0.33 vs raw 1.0; atomic recall ~0.49 isolated as the binding ceiling. LABEL the documents bracket-selected/concatenation-constructed; keep as a short demonstration that the pipeline is operational at length and that EXTRACTION (not closure) is the ceiling.

      ----- CLAIM 7 (MECHANISM ANALYSIS / APPENDIX, DEMOTED). TAG: REAL-LLM-READ-ON-SYNTHETIC + SYNTHETIC-CHANNEL + THEOREM. -----
      Compress into a COMPACT half-page/APPENDIX, labeled inherited/synthetic/textbook: (7a) ALGEBRA-RICHNESS SCALING with real LLM reads on synthetic NL (point(3) +0.043 -> RCC-8(8) +0.448 -> Allen(13) +0.676; INHERITED table-vs-LLM-composition at recall ~1.0); (7b) the REDUNDANCY INVERTED-U on a realism-matched channel (Page p ~= 5e-4 corrected from the paper's mis-stated 1e-13; peak K* = 2,4,7,10,16 for recall 0.5->0.95; silent-wrong 0.006->0.146 bounded by (1-r)) with the small-bite caveat (+0.024 coverage); (7c) the ZERO-FP soundness THEOREM (all-sound contributing edges => gold in Mode-A output with probability 1.0; verified on 100,296 networks) -- a textbook PC invariant; recall and rho are INPUTS so it characterizes, not predicts a real-text operating point. None competes with the certificate headline.

      ----- CLARITY FIX (reviewer clarity MINOR): RE-DOCRED COUNTS PER-DATASET. -----
      State the per-dataset breakdown explicitly to remove the 360!=476 / 368!=577 apparent inconsistency: the re-docred PRIMARY slice is 360 present multi-hop queries (222 composed-only / non-circular) and 368 absent pairs; the 476/476 present and 577/577 absent engine round-trip is the COMBINED re-docred (360 present / 368 absent) + docred (116 present / 209 absent) verification (docred absent gold DOWNGRADED due to ~64.6% false-negatives; only the re-docred slice yields a defensible within-document absent label). One added clause removes the confusion.

      ----- METHOD CORE (unchanged in substance; re-scoped). -----
      MODE A (SOUND NARROWING / no-derivation abstention, PRIMARY, READ-SOUNDNESS-CONDITIONAL zero-FP). The local reader emits per span a high-recall sub-universal disjunction; composing+intersecting through the EXACT table either resolves a singleton (EMIT), leaves a disjunction (ABSTAIN), or finds NO derivation path (ABSTAIN 'no relation' -- the absent-relation behavior, conceded structural-by-construction on disconnected pairs). zero-FP survives PC incompleteness but is CONDITIONAL on every contributing read being sound. The cross-path-INTERSECTION variant is SYNTHETIC-ONLY-at-power (CLAIM 4); CLUTRR uses a union-fixpoint, not intersection.
      MODE B (DETECTION/REPAIR, SECONDARY). An empty closure certifies an UNSOUND read -- a gold-free, zero-FP DETECTION flag (conditional on recall) -- carrying the SILENT-WRONG-NARROWING dual (an unsound set OMITTING gold drives a confident WRONG singleton with no collapse; CLAIM 5's 42.5%). The fuzzy Mode-B catches (5/5 spatial) are the certificate's distinctive edge over a fair neural abstainer (CLAIM 3). Reiter-style minimal-hitting-set repair is future work.
      BASELINES: every certificate comparison includes the CONFIDENCE-THRESHOLDED RAW-ABSTAIN battery (verbalized + sc_margin + P(True) + semantic-entropy negentropy) thresholded to MATCHED coverage, alongside always-answer commit-the-argmax/raw-forced-single, PoT, and self-consistency. The claim is specifically that the confidence FAMILY is blind on the NO-DERIVATION/absent stratum.
      GENERALITY, TEMPERED. EXACT only on the convex point algebra (PC complete); Allen IA and RCC-8 are SOUND LOWER BOUNDS; CLUTRR kinship is a finite UNION composition table, NOT a relation algebra, NOT a cross-path-intersection venue.

      ----- HONESTY COMMITMENTS. -----
      (1) TAG every number THEOREM / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / REAL-LLM-READ / REAL-LLM-READ-ON-SYNTHETIC in TABLE COLUMNS. (2) Do NOT call CLUTRR natural -- it is TEMPLATED (<=871 chars, gold surface forms, hand-supplied table). (3) The certificate MECHANISM is the INHERITED NeSy premise (+0.673 inherited / +0.0025 novel); the NOVELTY is the EMPIRICAL ISOLATION (confidence-blindness), not the closure/abstention mechanism -- make the concession the framing. (4) The CLUTRR-absent abstention is STRUCTURAL-BY-CONSTRUCTION (disconnected components); the non-circular content is FACT A (47% high-confidence hallucination) + FACT B (confidence-blindness); the natural-corpus run is DECISIVE because there the extracted graph is not trivially correct. (5) Cross-path coding is SYNTHETIC-CHANNEL-ONLY -- one bounded negative subsection, an explanatory account of two gated-venue negatives, NOT a 'law'. (6) zero-FP is READ-SOUNDNESS-CONDITIONAL. (7) The fuzzy-unification certificate edge has a unit-of-analysis mismatch (query-level vs edge-read level); fix it with a query-level abstainer or lead with the 5/5 Mode-B catch; the kinship catch is untested (0 unsound reads). (8) Report every hallucination number WITH coverage/abstention. (9) SWI-Prolog execution reported truthfully (40/40 engine, 39/40 gold; 95 programs in the operational study). (10) DEDUCTION SUB-MODULE only -- OpenCyc grounding, atomic re-extraction, general fuzzy unification, and genuine ~3000-char natural professional documents are explicitly FUTURE WORK THIS PAPER DOES NOT CLAIM TO DELIVER; extraction-limited (~0.53 recall => ~19% coverage). (11) RE-TARGET venue to NeSy / temporal-and-qualitative-reasoning, with the deduction-sub-module scope stated in the FIRST paragraph of the abstract. (12) Include one worked Mode-A no-derivation abstention + one Mode-B collapse + a compact notation/metric table.

      SUCCESS / DISCONFIRM (re-centered on the empirical isolation + the natural-corpus run). CONFIRM if: (i) FACT A and FACT B reproduce on the natural Re-DocRED corpus and >=1 additional relation domain/reader (the raw LLM confidently hallucinates absent relations and the four-signal battery cannot filter them, crux-survival high) -- this is the corpus-robust DIAGNOSTIC contribution; AND (ii) the certificate beats the four-signal battery on the Re-DocRED MIXED pool at matched coverage with Holm-adjusted CIs excluding 0 (MET on CLUTRR + suggestive; the natural-corpus version is the iter-7 test), with the CLUTRR-absent structural-by-construction caveat stated; AND a SWI-Prolog-executed pipeline reports atomic P/R, multi-hop accuracy, trace-graphs, and abstention beside every hallucination number. DISCONFIRM / SCOPE-BOUNDARY (each publishable): FACT B fails (some confidence signal DOES filter confident absent hallucinations at matched coverage on a real venue => the empirical isolation is weaker than claimed -- an honest negative); OR the certificate ties/loses the Re-DocRED mixed-pool showdown because extraction recall is too low (=> certificate net utility is extraction-limited on natural text, while the DIAGNOSTIC FACT A+B survives); OR cross-path intersection never beats single-path on any real multi-path stratum at power (already observed on both gated venues => coding mechanism honestly synthetic-only).
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
  no over-commitment and no labels, and multi-path redundancy becomes an ERROR-CORRECTING CODE over LLM extractions. SECOND,
  the coding-theory lens predicts an OPTIMAL RATE: narrowing stays zero-FP only while all contributing edges are sound and
  that JOINT probability (measured EMPIRICALLY as J(E), not assumed independent) decays with redundancy, so net benefit is
  an INVERTED-U whose peak we predict from measured recall and the measured cross-edge error correlation and shift with a
  recall-floor gate. THIRD, the objective inverts F1 -- we preserve disjunctive uncertainty and ABSTAIN, trading coverage
  for faithfulness, and we measure the ACTIONABLE yield (intersection-to-correct-singleton at matched coverage) and the DOWNSTREAM
  hallucination-rate reduction, not whether a set merely shrank. The decisive realism move this iteration is choosing the
  corpus that can ACTUALLY host the claim: MATRES annotates only same/adjacent-sentence pairs, so its deduction-required envelope
  is empty BY CONSTRUCTION; the headline must live on a DENSE, direct-human-gold corpus (NarrativeTime, full TLink coverage,
  human-timeline gold) and be corroborated where gold is provably non-closure-derived (TDDMan long-distance manual pairs).
  If it works, this is a general, training-free recipe for trustworthy relational deduction over text with quantified, certificate-backed
  hallucination reduction and replayable trace-graphs; if it fails (intersection rarely resolves correct singletons because
  real sets are near-universal; the redundancy peak sits at trivially low redundancy; recall failures dominate the joint-soundness
  bound; or even the dense corpus's deduction-required multi-path-with-bite slice is below the pre-registered applicability
  number), each is itself a publishable scope boundary on repairing LLM-read relational knowledge.
assumptions:
- >-
  ARM-SCOPED CLAIMS + DENSE-CORPUS RELOCATION (resolves the prior contradiction AND the MATRES-locality problem). The real-text
  narrowing/hallucination win is claimed on a DENSE direct-human-gold corpus's deduction-required multi-path subset (NarrativeTime
  CO-PRIMARY; TDDMan non-circularity corroboration), NOT on MATRES, which is EXPECTED TO FAIL the deduction-required gate
  by construction (same/adjacent-sentence annotation -> all gold local). Mode A beats path-isolated Path-of-Thoughts and answer-voting;
  it TIES naive single-pass intersection on length-2 queries; FULL ITERATED closure beats naive ONLY where >=3-edge/cyclic
  structure exists -- now demonstrated on synthetic AND, where T0 finds a usable real-text stratum, on real text.
- >-
  CORPUS ALGEBRA & NON-CIRCULARITY CHARACTERIZED A-PRIORI FOR ALL CORPORA (before any LLM spend). NarrativeTime gold = HUMAN
  TIMELINE placement (manual, full TLink coverage, IAA alpha ~0.68), restrictable to START-POINTS -> CONVEX POINT ALGEBRA
  where PC is COMPLETE and the table exact (full-interval Allen scored as a lower-bound detector); its non-local gold is human-holistic,
  NOT algorithmic-closure output, so closure recovery over independently-read edges is non-circular -- quantified by the LOCALLY-JUSTIFIABLE
  vs PURELY-TIMELINE-IMPLIED fraction. TDDMan gold = direct human annotation of long-distance pairs explicitly NOT auto-inferable
  -> a structurally non-circular anchor whose win moots the timeline-circularity worry. Mode A's zero-FP soundness SURVIVES
  PC incompleteness (intersection of sound sets is always sound), so the mechanism is not lost where completeness fails.
- >-
  REDUNDANCY IS DOUBLE-EDGED, AUDITED ON EMPIRICAL JOINT SOUNDNESS (no independence assumption). Mode A's zero-FP narrowing
  holds only when ALL contributing edges are sound. We MEASURE the empirical joint soundness J(E) and report the within-document
  cross-edge reading-error correlation rho. Net Mode-A gain is an INVERTED-U in redundancy at fixed recall, cost term 1 -
  J(E), peak located using empirical J(E); positive rho pushes the peak outward. A flat/non-monotone curve is the predicted
  recall x redundancy interaction, not a disconfirmation.
- >-
  A-PRIORI ENVELOPE GATE EXTENDED TO ALL CORPORA + CONCRETE APPLICABILITY THRESHOLD. From each gold graph alone (zero LLM
  spend) we count N* (deduction-required AND >=2-path AND bite-after-widening AND singleton-resolving) AND the >=3-edge/cyclic
  prevalence (the real-text iteration envelope), with a paired-bootstrap power calc, for NarrativeTime, TDDMan AND MATRES;
  we report widening-induced bite loss; and we pre-register the applicability-envelope threshold as a NUMBER (deduction-required
  multi-path-with-bite fraction >=10% of evaluable held-out edges = 'general mechanism'; 5-10% = 'useful module'; <5% = 'niche
  safety-net'). The headline is never contingent on an unmeasured quantity.
- >-
  ACTIONABLE YIELD = SINGLETON-RESOLUTION-TO-CORRECT + DOWNSTREAM HALLUCINATION REDUCTION, AND RECALL-AND-RHO-MATCHED READER-AGNOSTICITY.
  The matched-coverage win and the hallucination-rate drop are both driven by intersection-to-correct-SINGLETON (strict-tightening
  reported separately, stated non-load-bearing); the coverage axis (single-relation resolution) is applied IDENTICALLY to
  closure and every baseline. The gain is attributable to the ALGEBRA: swapping the disjunctive edge-reader preserves the
  gain when each alternative reader is tuned to MATCHED per-edge recall AND its rho is reported (conditioned on rho if it
  differs materially), so reader-specific error correlation cannot confound the conclusion.
investigation_approach: |-
  TIERING (pre-committed; T0 then Tier-1 must COMPLETE before Tier-2; a fully-executed T0+Tier-1 with a thin Tier-2 is the acceptable minimum publishable unit). T0 -- A-PRIORI ENVELOPE GATE FOR ALL CORPORA (zero LLM spend): from each gold graph compute N* (deduction-required AND >=2-path AND bite-after-widening AND singleton-resolving), the >=3-edge/cyclic prevalence, the widening-induced bite loss, and a paired-bootstrap power calc, for NarrativeTime, TDDMan AND MATRES; for NarrativeTime also compute the locally-justifiable vs purely-timeline-implied split (non-circularity audit, structural proxy only). Decide hosting via the pre-registered applicability NUMBER; the expected MATRES N* ~ 0 vs NarrativeTime/TDDMan N* >> 0 is reported as gate validation. TIER-1 (headline-critical, on the dense co-primary): (T1) the RECALL-BITE FRONTIER map + pre-registered go/no-go; (T2) the real-text Mode-A comparison vs Path-of-Thoughts and self-consistency at MATCHED COVERAGE with paired-bootstrap CIs, stratified by deduction-required vs directly-readable; (T2b) the END-TO-END HALLUCINATION-REDUCTION on the deduction-required/absent-relation subset vs a raw LLM, with a PRE-REGISTERED minimum effect size; (T3) the SYNTHETIC long-hop/cyclic redundancy-scaling DECOMPOSITION separating Mode-A BENEFIT from silent-narrowing COST, locating the inverted-U peak, conditioning the zero-FP audit on EMPIRICAL J(E), PLUS a coarse REAL-TEXT decomposition anchor binned by contributing-edge count; (T4) the isolating ablations -- closure ON/OFF table-held-fixed, Mode-A-only, and NAIVE-INTERSECTION vs FULL ITERATED closure with hop/cyclomatic stratification ON BOTH synthetic AND the dense corpus's real >=3-edge/cyclic stratum (the iteration claim). TIER-2 (runs only after Tier-1): TDDMan non-circularity replication, RCC-8 second algebra, CLUTRR elicited-table ablation + absent-relation end-to-end demo, TimeBank-Dense (framed noisy-read-vs-clean-read), Mode-B repair quality, the METRE-style alternative-reader ablation, exploratory semiring variant.

  MULTIPLICITY POLICY (pre-registered; inoculates against a garden-of-forking-paths objection). CONFIRMATORY FAMILY (Holm-Bonferroni / hierarchical gatekeeping across the family; report ADJUSTED CIs): (H1) real-text Mode-A selective-accuracy gap vs PoT & voting; (H2) end-to-end hallucination-rate reduction vs raw LLM; (H3) full-minus-naive iteration gap growing with hop/cyclomatic; (H4) the single redundancy inverted-U disconfirmer. H1 and H2 are the gateway tests; H3/H4 are tested only if a gateway clears. EVERYTHING ELSE -- per-stratum splits, per-bin curves, reader-agnosticity, Mode-B repair, RCC-8/CLUTRR/TB-Dense, the real-text iteration stratum (corroborative) -- is EXPLORATORY, reported with nominal CIs and labelled as such.

  EMPIRICAL-J(E) ATTRIBUTION RULE (stated ONCE here): a reliability-slope offset that DISAPPEARS when the predictor is switched from the independence product r^E to empirical J(E) is the independence approximation failing (NOT a disconfirmation); an offset that PERSISTS under empirical J(E) is a genuine soundness failure. ESCALATION LADDER (stated ONCE here): the dense direct-human-gold CO-PRIMARY is NarrativeTime if its T0 N* clears the applicability number; TDDMan corroborates and supplies a non-circularity-clean (and harder) arm; MATRES is the gate-validation control; if NO real corpus clears the number even after these, the synthetic arm becomes the headline and real text is demoted to an honestly-scoped niche-safety-net boundary -- but T0 makes that decision before LLM spend.

  COMPACT LOGICAL STRUCTURE (claim -> precondition -> metric -> baseline -> CI test). [H1 REAL-TEXT NARROWING] Mode-A singleton-resolution-to-correct > PoT & self-consistency (ties naive-intersection) -> precondition: dense-corpus deduction-required multi-path-with-bite subset with N* powering the CI (from T0) -> metric: selective accuracy at matched coverage -> baselines: PoT (path-agreement abstain), self-consistency (vote margin) -> paired-bootstrap adjusted CI on the gap, separated from 0. [H2 HALLUCINATION REDUCTION] closure pipeline confident-wrong rate < raw-LLM on the absent-relation subset -> precondition: same subset -> metric: confident-wrong (non-abstained gold-mismatch) rate -> baseline: raw LLM forced to a single relation -> paired-bootstrap adjusted CI meeting the pre-registered minimum effect. [H3 ITERATION] full closure > naive-intersection, gap grows with hop/cyclomatic -> precondition: paths longer than 2 / cycles present (synthetic; real >=3-edge/cyclic stratum) -> metric: selective-accuracy gap vs hop-count bin -> baseline: naive single-pass intersection -> per-bin adjusted CI + monotone-trend test. [H4 REDUNDANCY OPTIMUM] net gain inverted-U with located peak; peak increases with recall; gate shifts it -> precondition: >=4 fixed per-edge-recall arms + estimation-precision pre-reg -> metric: separate benefit and cost curves vs redundancy (synthetic + coarse real anchor) -> peak-detection meeting the >=1-bin shift bar. [C2 PATH-CONSISTENCY] closure ON > OFF, table held FIXED -> paired bootstrap (exploratory). [C3 ZERO-FP AUDIT] realized fraction-still-contains-gold tracks EMPIRICAL J(E), slope ~1 (exploratory). [C5 READER-AGNOSTIC] gain persists under swapped reader at matched recall AND reported rho (exploratory). [C6 MODE-B] zero-FP DETECTION; repair toward gold (exploratory).

  PILOT AS A FRONTIER MAP (after T0, before main runs). On synthetic and real edges, SWEEP a prompt-elicited breadth knob across >=5 settings from 'name THE relation' to 'name the maximal SOUND set the text does not exclude.' At each setting MEASURE: per-edge RECALL = P(gold in emitted set); breadth distribution; over-commitment vs under-specification rate; raw closure-collapse rate; strict-tightening AND singleton-resolution-to-correct yields; local-only-reader accuracy defining the deduction-required fraction; and the within-document cross-edge reading-error correlation rho. PLOT the RECALL-BITE FRONTIER as a primary deliverable and pre-register go/no-go (a region clearing a recall gate AND non-trivial singleton-resolution-to-correct) BEFORE any main run. PRE-REGISTER the EXTENDED REALISM-MATCHING STATISTIC for the synthetic NL-realization: total-variation distance between real and synthetic per-edge error-type distributions PLUS a cross-edge error-CORRELATION (rho) match term PLUS a redundancy/path-topology match (contributing-edge-count and cycle-structure histograms), thresholds FIXED before generating the redundancy curve.

  PIPELINE (four stages). (1) NEURAL READING -- prompt the LLM (via OpenRouter, cheap model, short docs, caching; well under $10) to map each surface relation phrase onto a SOUND DISJUNCTION of canonical base relations at the pre-registered frontier operating point; for the NarrativeTime point-algebra arm restrict emitted vocabulary to CONVEX point relations on start-points (widen non-convex {<,>} to VAGUE) so PC stays COMPLETE, and MEASURE the bite lost. (2) ALGEBRA -- use the EXACT published composition table (Allen 13-relation, point algebra, RCC-8; the convex table for the coarse interval label sets); seed converses/identity from the algebra, never from an LLM. (3) SYMBOLIC CLOSURE -- build a QCN (nodes=events/entities, edges=relation SETS; query/held-out edge starts universal), run path-consistency to a FIXPOINT. Three instrumented variants: FULL iterated PC; NAIVE single-pass intersection at the query node (no fixpoint, no converse seeding); closure-OFF (table fixed). MODE A narrows by cross-path intersection and emits an answer ONLY when the query resolves to a single relation (coverage axis), else ABSTAINS. MODE B (Tier-2): an empty collapse CERTIFIES a reading error; compute a minimal Reiter-style hitting-set/MaxSAT repair preferring lowest-confidence edges, recording the diagnosis and flagging possible mislocalization. (4) AUDIT -- emit the QCN, which compositions fired on which paths, and repairs as a TRACE-GRAPH, optionally discharged in SWI-Prolog/ASP from the closed table for a replayable proof (connective tissue to the umbrella pipeline's auditability + quantified-hallucination-reduction requirements).

  DATASETS. DENSE REAL-TEXT CO-PRIMARY: NarrativeTime / TimeBankNT (Rogers et al., LREC-COLING 2024; arXiv:1908.11443) -- timeline-based FULL-coverage human re-annotation of TimeBank-Dense (news), IAA alpha ~0.68; start-point restriction -> convex point algebra (PC COMPLETE), full-interval arm as lower-bound detector; non-local gold is HUMAN-timeline-placed (non-circular vs algorithmic PC). NON-CIRCULARITY ANCHOR: TDDMan (Naik et al., TDDiscourse 2019; aclanthology W19-5929) -- MANUAL long-distance (>1-sentence-apart) pairs that 'cannot be inferred automatically from existing annotations'; relation set {before, after, simultaneous, includes, is_included}, mutually exclusive (no VAGUE), coarse interval algebra; cleanest non-circularity, used to replicate the narrowing win where gold is provably not a closure artifact. GATE-VALIDATION CONTROL: MATRES (Ning, Wu & Roth 2018) -- same/adjacent-sentence annotation, expected N* ~ 0 on the deduction-required gate, demonstrating the gate discriminates. SYNTHETIC PRIMARY (clean ground truth, controlled redundancy): a Renz-Nebel-style random consistent Allen/point QCN generator GUARANTEEING redundant paths/cycles and sweeping redundancy/density/hop-count INDEPENDENTLY; the NL-realization protocol is VALIDATED to clear the EXTENDED realism statistic; the redundancy DECOMPOSITION is reported at >=4 FIXED per-edge-recall levels with >=500 networks per cell. SECOND ALGEBRA: RCC-8 synthetic. ELICITED-TABLE VENUE: CLUTRR kinship (LLM-elicited table vs gold) doubling as an end-to-end hallucination-reduction-on-ABSENT-relation demo. TimeBank-Dense as a Tier-2 noisy-read-vs-clean-read arm; RuleTaker an out-of-scope propositional contrast.

  KEY ABLATIONS: (i) closure/intersection ON vs OFF with the table HELD FIXED; (ii) NAIVE single-pass vs FULL iterated closure with hop/cyclomatic stratification (synthetic + real); (iii) Mode A ONLY vs Mode A+B; (iv) disjunction OFF (force singletons); (v) exact-table vs LLM-elicited-table (kinship); (vi) recall-floor gate ON vs OFF; (vii) ALTERNATIVE EDGE-READER (METRE-style multi-label head + a second LLM into the SAME closure pipeline -- recall-AND-rho-matched). BASELINES, EACH WITH A MATCHED ABSTENTION SIGNAL thresholded to the SAME coverage object: raw LLM (verbalized confidence), CoT, self-consistency (vote margin), LINC-style multi-formalization vote, DSR-LM-style induced-rule Prolog (no closure), Path-of-Thoughts (PRIMARY real-text baseline; path-agreement abstain), NAIVE single-pass intersection (iteration contrast), a TempRel-style COMMIT baseline, and a soft-unification neural theorem prover.

  METRICS, per-regime and STRATIFIED: (1) SINGLETON-RESOLUTION-TO-CORRECT yield + risk-coverage/selective accuracy AT MATCHED COVERAGE (HEADLINE H1) with paired-bootstrap adjusted CIs, reported alongside strict-tightening yield (stated non-load-bearing); (2) END-TO-END hallucination-rate reduction vs raw LLM on the deduction-required/absent-relation subset (HEADLINE H2) with a pre-registered minimum effect; (3) empirical zero-FP audit CONDITIONED on EMPIRICAL J(E) (reliability curve slope ~1; rho reported); (4) REDUNDANCY DECOMPOSITION (benefit vs silent-narrowing cost, located peak, gate shift) on SYNTHETIC + coarse REAL anchor; (5) full-minus-naive gap vs hop/cyclomatic on SYNTHETIC and the real >=3-edge/cyclic stratum; (6) Mode-B detection (lower bound on Allen IA/RCC-8, exact on the point-algebra arm) + repair quality; (7) reader-agnostic closure delta at matched recall and reported rho; (8) APPLICABILITY ENVELOPE -- relation-composable, multi-path-with-bite, deduction-required, AND >=3-edge/cyclic fractions per corpus (N* up front), scored against the pre-registered NUMBER; (9) atomic extraction P/R as a HELD-FIXED control; (10) the non-circularity audit (locally-justifiable vs purely-timeline-implied fraction on NarrativeTime). Closure and repair run in milliseconds per network on a laptop.
success_criteria: |-
  THREE ARM-SCOPED HEADLINE PREDICTIONS (stated before all qualifiers; the confirmatory family H1-H4 is Holm-Bonferroni-adjusted, H1/H2 are gateways). CONFIRM lines: (REAL-TEXT) On the dense co-primary's deduction-required multi-path-with-bite subset at the pre-registered frontier operating point, Mode A achieves strictly higher SELECTIVE ACCURACY AT MATCHED COVERAGE than Path-of-Thoughts AND self-consistency (H1), AND cuts the CONFIDENT-WRONG (hallucination) rate versus a raw LLM on the same absent-relation pairs by at least the pre-registered minimum effect (H2) -- both adjusted-CI-separated from zero, driven by singleton-resolution-to-correct; Mode A is PREDICTED TO TIE naive single-pass intersection on the length-2 stratum and that tie is reported as confirmation, not failure. (ITERATION) FULL ITERATED closure beats NAIVE single-pass intersection with the gap GROWING in hop-count/cyclomatic number (and ~0 on length-2) on synthetic QCNs AND, where T0 found a usable real >=3-edge/cyclic stratum, on real text (H3). (REDUNDANCY) Net Mode-A gain is an INVERTED-U whose peak increases with recall and shifts outward under the recall-floor gate, at the pre-registered estimation precision (>=4 recall levels, >=500 networks/cell, >=1-bin minimum-detectable peak shift, peak bin CI-above both neighbors) (H4). Additionally CONFIRMS if: T0 reports N* clearing the applicability NUMBER on >=1 real corpus (NarrativeTime preferred, TDDMan corroborating) so the headline is genuine deduction not re-reading; the empirical zero-FP audit tracks J(E) (slope ~1, rho reported, slope-offset correctly attributed); the coarse real-text redundancy anchor matches the synthetic inverted-U sign; disjunction-ON beats commit-to-singleton; and the gain is reader-agnostic at matched recall+rho. DISCONFIRM lines: (REAL-TEXT) NEITHER a singleton-resolution advantage over PoT/voting NOR a hallucination-rate drop vs raw LLM exists on the deduction-required multi-path-with-bite subset even when sound sets are sub-universal and bite exists; (ITERATION) the full-minus-naive gap is ~0 even on multi-hop/cyclic queries (the win is 'any intersection,' not iteration); (REDUNDANCY) the SINGLE genuine disconfirmer -- the ABSENCE of any net-positive redundancy region beating BOTH best-single-path and naive-intersection (a flat/turned-over curve ALONE is NOT a disconfirmation); or T0 shows NO corpus clears the applicability NUMBER (then honestly scoped to synthetic + niche-safety-net).

  PRE-REGISTERED FAILURE MODES (each a publishable scope boundary): [NEAR-UNIVERSAL UNDER-SPECIFICATION | precondition: sets effectively universal | bound: Mode A inert, intersection cannot resolve singletons | the ONLY under-specification outcome that disconfirms Mode A]. [SILENT WRONG NARROWING | precondition: a contributing set OMITS gold (unsound) | bound: rate <= (1-recall) per-edge and (1 - J(E)) per-network | suppressed by the recall-floor gate, which also shifts the redundancy peak]. [CONSISTENT-BUT-WRONG ELICITED TABLE | precondition: LLM supplies the composition table | bound: quantified vs gold in kinship only | shown NOT to arise in exact-table settings]. [INVISIBLE SINGLE-CHAIN HALLUCINATION | precondition: confident self-consistent single chain | bound: closure cannot see it | scopes Mode B to multi-path collapse only]. [TINY/CIRCULAR ENVELOPE | precondition: N* below the applicability NUMBER even on the dense corpus, or gold purely-timeline-implied with no non-circular replication on TDDMan | bound: contribution scoped to synthetic + niche safety-net | decided a-priori by T0, not after spend]. Throughout, 'zero false-positive' is stated separately for Mode A (intersected set still contains gold under JOINT-sound inputs, audited against EMPIRICAL J(E)) and Mode B (DETECTION only); the closure-detectable hallucination rate is a LOWER BOUND because PC is incomplete for Allen IA/RCC-8 (complete only on the NarrativeTime start-point convex-point-algebra arm). Atomic extraction P/R must remain comparable to baselines, the per-corpus fractions (including a-priori N* and the >=3-edge/cyclic prevalence) must be reported up front, and trace-graphs must be judged human-auditable.
related_works:
- >-
  NarrativeTime / TimeBankNT (Rogers et al., LREC-COLING 2024; arXiv:1908.11443): the FIRST timeline-based annotation achieving
  FULL coverage of all possible TLinks, a human re-annotation of TimeBank-Dense (news) with IAA Krippendorff alpha ~0.68 and
  significantly higher density, plus tools converting to TimeML. We USE it as the dense real-text CO-PRIMARY because (unlike
  MATRES) it has direct human gold for NON-LOCAL pairs and (unlike TimeBank-Dense) its dense relations are HUMAN-timeline-backed
  rather than SputLink-inferred. Difference from our work: NarrativeTime is a DATASET/annotation scheme producing a single
  consistent labeling for extraction evaluation; it neither preserves LLM disjunction, intersects compositions across paths,
  certifies reading errors, nor abstains. We restrict its start-points to the convex point algebra (PC COMPLETE) and audit
  the locally-justifiable vs purely-timeline-implied fraction to neutralise residual circularity.
- >-
  TDDiscourse / TDDMan (Naik, Breitfeller et al., 2019; aclanthology W19-5929): the first dataset of DISCOURSE-LEVEL temporal
  links between events MORE THAN ONE SENTENCE APART, MANUALLY annotating global pairs that 'cannot be inferred automatically
  from existing annotations,' doubling TimeBank-Dense's links; relation set {before, after, simultaneous, includes, is_included},
  mutually exclusive, no VAGUE. We USE TDDMan as the NON-CIRCULARITY anchor: its gold is provably NOT the output of the closure
  algorithm we test, so a Mode-A narrowing win there cannot be a closure artifact. Difference: TDDiscourse is a benchmark
  for committed single-label discourse-level extraction; it preserves no disjunction, performs no cross-path intersection,
  issues no certificate, and does not abstain.
- >-
  Global Zero-shot Temporal Graph Generation (2025, arXiv:2502.11114; EMNLP 2025 main): prompts an LLM to generate a whole
  temporal graph, aggregates M=5 generations, then enforces uniqueness/symmetry/transitivity with ILP using Allen's laws.
  MOST RECENT directly-relevant prior art. Difference: it COMMITS to a single deterministic label per pair, preserves NO disjunction,
  intersects NO compositions across paths, issues NO gold-free certificate, and does NOT abstain -- the same F1-maximizing
  COMMIT contract we invert.
- >-
  Knez & Sun 2024 (arXiv:2406.11486): zero-shot LLMs assign MORE THAN ONE relation to a pair for >=50% (up to 97%) of pairs
  and violate uniqueness/transitivity; the authors ENFORCE consistency with ILP and find it DOES NOT improve F1. Difference:
  it enforces consistency under the F1-maximizing COMMIT contract (which it shows fails); no closure-a
  TWO READERS: PRIMARY google/gemini-3.1-flash-lite on FULL re-docred (360 present deduction-required + 368 absent no-derivation); CROSS-FAMILY deepseek/deepseek-v3.2 spot-check (25 docs: 67 present + 107 absent) with a reader-specific certificate (re-extract + re-ground). docred present-stratum (116) corroborates (its absent gold is DOWNGRADED).

  PRE-REGISTERED VERDICT = EXTRACTION-LIMITED-BOUNDARY. (1) FACT A TRANSFERS to natural prose AND across readers: the raw LLM commits a confident kinship on 32.6% of absent pairs (120/368, gemini) and 31.8% (deepseek) -- both well above the synthetic-vs-real bar. (2) FACT B (confidence blindness) holds on gemini: those absent hallucinations carry mean signal verbalized 0.95 / sc_margin 0.95 / negent 0.96, with only P(True) partly separating (mean 0.51, the best signal); >=2 of 4 signals still COMMIT >=50% of them at a global threshold matched to the certificate's coverage (frac_surviving 0.51/0.85/0.48/0.85). It is weaker under deepseek (top signal verbalized 0.41). (3) The certificate does NOT win the MIXED pool on natural prose: confident-wrong reductions vs every signal are slightly NEGATIVE (-0.034..-0.055, doc-clustered paired bootstrap B=10000 CIs all include 0, Holm not rejected) and mixed selective accuracy is certificate 0.475 vs signals 0.60-0.675 -- because natural-prose extraction is noisy (precision 0.62 propagates to wrong derivations -> certificate present selective accuracy only 0.55) and incomplete.

  The boundary is QUANTIFIED, not asserted: certificate present coverage 0.48 (LLM-read) vs 1.0 (gold-read ceiling, which reproduces 100% present / abstains 100% absent by construction); over-abstain-present 0.52; atomic recall 0.376 (converse-invariant primitive), 0.46 vs the locally-justifiable span-extractable subset, 0.20 strict-direction; certificate absent confident-wrong only 0.07 (near-perfect STRUCTURAL abstention). So on absent the certificate stays hallucination-safe; the mixed-pool advantage is erased by extraction RECALL, not by the certificate's logic.

  OUTPUT (exp_gen_sol_out, validated): 844 per-query rows across re-docred_present(360) / re-docred_absent(368) / docred_present(116) with predict_certificate (+ goldread), predict_conf_thresh_{verbalized,sc_margin,ptrue,negent}, predict_commit_argmax/pot/sc, and rich metadata. metadata.headline_summary carries FACT A, FACT B crux table, mixed leaderboard + Holm CIs, abstention decomposition, natural atomic P/R, cross-reader generality, and the fork verdict. Auditability: worked no-derivation abstention, over-abstain-present, and present-composition traces, each Prolog-discharged (python-checked: SWI-Prolog unavailable, labelled truthfully; 40 queries discharged, program comp/3,conv/2,rel/3,solve_/4 emitted + cross-checked).

  HONEST CAVEATS (downstream paper): natural prose averages ~1020 chars (no 3000-char doc; not padded); absent pairs are STRUCTURAL (different components) so absent abstention is structural-by-construction (conceded); docred absent gold downgraded; primitive-level scoring (surface secondary); extraction MEASURED not improved. Total OpenRouter spend ~$1.5 (final run replays primary at $0 from the sha256 cache; cross-family tail $0.19), far under the $9 cap. IMPLICATION: the diagnostic (confident absent hallucination invisible to confidence) is corpus-robust and reader-diverse, but the certificate's safety advantage is extraction-recall-limited on real prose -- CLUTRR stays the templated power demo; the natural contribution is the honest, quantified boundary plus the gold-read ceiling isolating extraction as the binding constraint.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 31 ---
id: art_RfjDpsGkBXDG
type: dataset
title: Natural-Text Located-In Absent-Relation Corpus from Re-DocRED + DocRED
summary: |-
  A document-level GEOGRAPHIC / ADMINISTRATIVE CONTAINMENT ('located-in') corpus over genuinely-natural Wikipedia introductory prose (Re-DocRED, the completeness-corrected re-annotation of DocRED; vanilla DocRED kept as a downgraded secondary slice). It is the STRUCTURAL TWIN of the iter-6 natural-kinship corpus and a SECOND genuinely-natural absent-relation domain, built to show the closure-certificate confidence-blindness diagnostic is NOT kinship-specific. Consumed by iter-8's domain-generality experiment. Built $0 LLM (deterministic cue check passes 100%, judge skipped).

  FORMAT: exp_sel_data_out, ONE ROW PER DOCUMENT, grouped by dataset. datasets=[{dataset:'re-docred', examples:[...]}, {dataset:'docred', examples:[...]}]. Each example: input=detokenized Wikipedia prose; output=json.dumps(gold_graph) with {doc_id, source, split, nodes, atomic_edges, query_edges, absent_relation_pairs, absent_pairs_source='structural_closure', contradiction_pairs}; plus flat metadata_* columns. Counts re-docred 2604 docs / docred 2080.

  ENGINE (drop-in): kinship.py forward least-fixpoint UNION closure is REUSED VERBATIM, parameterized by containment_composition_table.json — a DEGENERATE single-relation TRANSITIVE table (located_in∘located_in=located_in; contains∘contains=contains; ALL else UNDEFINED). NOT a relation algebra. Map each atomic edge to {a:source, b:target, type:primitive}; D[(s,t)]={located_in} EMIT, ∅ both directions ABSTAIN (absent), |D|>1 Mode-B conflict (0 here). Direction: source located_in target; P131/P17/P1376/P276 src=h tgt=t, P150/P36 INVERT.

  THREE STRATA. (1) Atomic located_in edges (LOC-LOC NER filter, deduped, true 2-cycles dropped), each flagged locally_justifiable (adjacent-sentence locality + surface cue); re-docred 20,825 edges, locally_justifiable_frac 0.588. (2) PRESENT deduction-required queries (re-docred 3,510), gold certain, TWO honest sub-types: never_annotated (118; pair never a direct edge, composed_only=true, provably non-circular — RARE because DocRED annotates geography near-transitively, a measured domain difference) and held_out (3,392; a directly-annotated located_in edge that is ALSO derivable via an alternative ≥2-hop path and is non-local — consumer MUST drop the single (source,target) atomic edge before querying, then the engine deduces it; SOUND because removing a redundant edge preserves the full transitive closure). (3) ABSENT no-derivation pairs (re-docred 24,088), two regimes: different_component (3,274; unrelated places, clean kinship-analog) and same_component_sibling (20,814; co-component, neither inside the other — the reviewer-named containment-specific regime). Per-doc caps present_cap=40, absent_cap=30 (stratified), atomic_cap=80; *_truncated flagged.

  QUALITY. Round-trip gate (verify.py) PASSES: never_annotated 367/367, held_out 4357/4357 (deduced after ablation), absent 41100/41100 empty in BOTH directions, every derivation_path a valid DIRECTED located_in chain, cue-present 19885/19885, Mode-B 0. offset_ok 0.988/0.990. Schema-validated 3/3 (full/mini/preview). Completeness correction (2079 shared titles): Re-DocRED +67.5% located-in edges and 2.8x present queries vs DocRED — so absent gold is TRUSTWORTHY only on re-docred; docred absent is DOWNGRADED. Char honesty: mean ~1025 chars, max 2969, NO doc reaches 3000 (no padding/concatenation — natural-text + absent-relation is the load-bearing property). Caveats: closed-world absent; composed_only is pair-level (not type-level as kinship); multi-parent DAG; admin_level node tag best-effort/non-load-bearing; P276 lower precision (~0 LOC-LOC on re-docred). See dataset_card.md / README.md.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 32 ---
id: art_5zL3Idms1neE
type: evaluation
title: >-
  Zero-spend empirical-isolation reframe: non-circular FACT-A/FACT-B ledger + scaffold
summary: >-
  Pure $0 re-analysis (numpy/scipy/json only; no LLM, no network; eval.py hard-asserts cumulative spend == $0 and that no
  OpenRouter/network module is imported). It reconstructs the 282-record CLUTRR pool (180 absent + 102 present) from art_LeRQRGHJZcdQ
  IN THE ORIGINAL iter-3 order (load_stored_iter3 ordering, restored via the iter-3 key sequence so index-tie-broken matched_coverage_mask
  and the by_doc story-clustered bootstrap reproduce exactly) and re-derives every carried literal with the source's verbatim
  helper functions (seed=20260617, B=10000). STEP-0 reproduce-verify gate: 38/38 checks PASS, reproduction_ok=True — FACT
  A raw absent-hallucination 0.4722 (deepseek 0.4833), FACT B crux survival 0.4353/0.7176/0.2471/0.7176 (deepseek 0.6724/0.2241/0.1034/0.2241),
  certificate absent CW 0.0278 (reduction 0.4444), mixed-pool selective accuracy 0.8267 vs 0.4133/0.3733/0.44/0.3733 @c*=0.266,
  mixed CW reductions 0.1099/0.1206/0.1028/0.1206 with Holm p_adj 0.0004/0.0027/0.0027/0.0027 and CIs excluding 0, spatial
  boundary cert CW 0.0219 vs raw-abstain 0.0351, multi-hop present win 0.8857 vs 0.5429 @0.6863, atomic P/R/F1 0.5361/0.5324/0.5343.
  Count arithmetic hard-asserted: re-docred 360/368 + docred 116/209 = 476/577. Deliverables: eval.py (+prose.py), eval_out.json
  (exp_eval_sol_out-VALID; full/mini/preview) carrying metadata.structural_by_construction_paragraph, a 48-row non_circular_vs_structural
  ledger (every number tagged side in {NON_CIRCULAR, STRUCTURAL_BY_CONSTRUCTION, INHERITED, NON_CIRCULAR_CONDITIONAL, MEASURED,
  PENDING} + evidence_tag + source_artifact + recomputed/matches flags), count_breakdown+fix sentence, abstract_front_matter
  (OpenCyc/general-fuzzy/atomic-re-extraction/3000-char OUT OF SCOPE; NeSy venue), operational compression recommendation,
  fuzzy_reframe (LEAD with spatial 5/5 Mode-B sound-violation catch; demoted query-vs-edge unit caveat; supporting cert CW
  0.000 vs commit-argmax 0.364/0.216), a 7-row one_thesis_table with evidence-class tags as COLUMNS and a clearly-labeled
  PENDING natural-corpus slot, and headline_structure_guidance. eval_digest.md mirrors all of it paper-facing. Three schema-valid
  datasets (non_circular_facts_ledger 48, one_thesis_contribution_table 7, reproduction_gate 38). Tells GEN_PAPER_TEXT to
  LEAD with confidence-blindness isolation, concede the closure mechanism INHERITED (+0.673 inherited / +0.0025 novel) up
  front, and never re-center on the structural-by-construction 2.8%.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

id: art_htcr8yOZLCQy
title: Closure Certificate vs 4-Signal Confidence Battery on Natural Re-DocRED Kinship
summary: |-
  STEP-B (iter-7): the iter-6 CLUTRR fair-baseline experiment re-run VERBATIM on the GENUINELY-NATURAL Re-DocRED/DocRED Wikipedia kinship corpus (art_NUWTxBVWENIJ). It moves the load-bearing diagnostic off templated text onto real prose: a closure CERTIFICATE (forward least-fixpoint UNION over LLM-extracted kinship edges -> abstain when no derivation path) vs the strongest confidence/uncertainty BATTERY on the raw LLM answerer (verbalized, self-consistency vote-margin@k=10, Kadavath P(True), semantic-entropy negentropy).

  REUSE vs NEW: readers.py / kinship.py (forward-UNION engine, the correct one for the finite kinship table) / baselines.py / stats.py / llm.py / prolog.py are copied VERBATIM from iter-6. New code: dataio_redocred.py (natural-corpus loader + entity-name GROUNDING of LLM names to gold entity_ids via mention-span aliases; measured grounding recall ~0.99) and method.py orchestration (PRIMITIVE-level scoring since gender is best-effort, natural-prose atomic P/R, certificate-abstention DECOMPOSITION, gold-read ceiling, pre-registered FORK verdict).

  TWO READERS: PRIMARY google/gemini-3.1-flash-lite on FULL re-docred (360 present deduction-required + 368 absent no-derivation); CROSS-FAMILY deepseek/deepseek-v3.2 spot-check (25 docs: 67 present + 107 absent) with a reader-specific certificate (re-extract + re-ground). docred present-stratum (116) corroborates (its absent gold is DOWNGRADED).

  PRE-REGISTERED VERDICT = EXTRACTION-LIMITED-BOUNDARY. (1) FACT A TRANSFERS to natural prose AND across readers: the raw LLM commits a confident kinship on 32.6% of absent pairs (120/368, gemini) and 31.8% (deepseek) -- both well above the synthetic-vs-real bar. (2) FACT B (confidence blindness) holds on gemini: those absent hallucinations carry mean signal verbalized 0.95 / sc_margin 0.95 / negent 0.96, with only P(True) partly separating (mean 0.51, the best signal); >=2 of 4 signals still COMMIT >=50% of them at a global threshold matched to the certificate's coverage (frac_surviving 0.51/0.85/0.48/0.85). It is weaker under deepseek (top signal verbalized 0.41). (3) The certificate does NOT win the MIXED pool on natural prose: confident-wrong reductions vs every signal are slightly NEGATIVE (-0.034..-0.055, doc-clustered paired bootstrap B=10000 CIs all include 0, Holm not rejected) and mixed selective accuracy is certificate 0.475 vs signals 0.60-0.675 -- because natural-prose extraction is noisy (precision 0.62 propagates to wrong derivations -> certificate present selective accuracy only 0.55) and incomplete.

  The boundary is QUANTIFIED, not asserted: certificate present coverage 0.48 (LLM-read) vs 1.0 (gold-read ceiling, which reproduces 100% present / abstains 100% absent by construction); over-abstain-present 0.52; atomic recall 0.376 (converse-invariant primitive), 0.46 vs the locally-justifiable span-extractable subset, 0.20 strict-direction; certificate absent confident-wrong only 0.07 (near-perfect STRUCTURAL abstention). So on absent the certificate stays hallucination-safe; the mixed-pool advantage is erased by extraction RECALL, not by the certificate's logic.

  OUTPUT (exp_gen_sol_out, validated): 844 per-query rows across re-docred_present(360) / re-docred_absent(368) / docred_present(116) with predict_certificate (+ goldread), predict_conf_thresh_{verbalized,sc_margin,ptrue,negent}, predict_commit_argmax/pot/sc, and rich metadata. metadata.headline_summary carries FACT A, FACT B crux table, mixed leaderboard + Holm CIs, abstention decomposition, natural atomic P/R, cross-reader generality, and the fork verdict. Auditability: worked no-derivation abstention, over-abstain-present, and present-composition traces, each Prolog-discharged (python-checked: SWI-Prolog unavailable, labelled truthfully; 40 queries discharged, program comp/3,conv/2,rel/3,solve_/4 emitted + cross-checked).

  HONEST CAVEATS (downstream paper): natural prose averages ~1020 chars (no 3000-char doc; not padded); absent pairs are STRUCTURAL (different components) so absent abstention is structural-by-construction (conceded); docred absent gold downgraded; primitive-level scoring (surface secondary); extraction MEASURED not improved. Total OpenRouter spend ~$1.5 (final run replays primary at $0 from the sha256 cache; cross-family tail $0.19), far under the $9 cap. IMPLICATION: the diagnostic (confident absent hallucination invisible to confidence) is corpus-robust and reader-diverse, but the certificate's safety advantage is extraction-recall-limited on real prose -- CLUTRR stays the templated power demo; the natural contribution is the honest, quantified boundary plus the gold-read ceiling isolating extraction as the binding constraint.
type: experiment

id: art_RfjDpsGkBXDG
title: Natural-Text Located-In Absent-Relation Corpus from Re-DocRED + DocRED
summary: |-
  A document-level GEOGRAPHIC / ADMINISTRATIVE CONTAINMENT ('located-in') corpus over genuinely-natural Wikipedia introductory prose (Re-DocRED, the completeness-corrected re-annotation of DocRED; vanilla DocRED kept as a downgraded secondary slice). It is the STRUCTURAL TWIN of the iter-6 natural-kinship corpus and a SECOND genuinely-natural absent-relation domain, built to show the closure-certificate confidence-blindness diagnostic is NOT kinship-specific. Consumed by iter-8's domain-generality experiment. Built $0 LLM (deterministic cue check passes 100%, judge skipped).

  FORMAT: exp_sel_data_out, ONE ROW PER DOCUMENT, grouped by dataset. datasets=[{dataset:'re-docred', examples:[...]}, {dataset:'docred', examples:[...]}]. Each example: input=detokenized Wikipedia prose; output=json.dumps(gold_graph) with {doc_id, source, split, nodes, atomic_edges, query_edges, absent_relation_pairs, absent_pairs_source='structural_closure', contradiction_pairs}; plus flat metadata_* columns. Counts re-docred 2604 docs / docred 2080.

  ENGINE (drop-in): kinship.py forward least-fixpoint UNION closure is REUSED VERBATIM, parameterized by containment_composition_table.json — a DEGENERATE single-relation TRANSITIVE table (located_in∘located_in=located_in; contains∘contains=contains; ALL else UNDEFINED). NOT a relation algebra. Map each atomic edge to {a:source, b:target, type:primitive}; D[(s,t)]={located_in} EMIT, ∅ both directions ABSTAIN (absent), |D|>1 Mode-B conflict (0 here). Direction: source located_in target; P131/P17/P1376/P276 src=h tgt=t, P150/P36 INVERT.

  THREE STRATA. (1) Atomic located_in edges (LOC-LOC NER filter, deduped, true 2-cycles dropped), each flagged locally_justifiable (adjacent-sentence locality + surface cue); re-docred 20,825 edges, locally_justifiable_frac 0.588. (2) PRESENT deduction-required queries (re-docred 3,510), gold certain, TWO honest sub-types: never_annotated (118; pair never a direct edge, composed_only=true, provably non-circular — RARE because DocRED annotates geography near-transitively, a measured domain difference) and held_out (3,392; a directly-annotated located_in edge that is ALSO derivable via an alternative ≥2-hop path and is non-local — consumer MUST drop the single (source,target) atomic edge before querying, then the engine deduces it; SOUND because removing a redundant edge preserves the full transitive closure). (3) ABSENT no-derivation pairs (re-docred 24,088), two regimes: different_component (3,274; unrelated places, clean kinship-analog) and same_component_sibling (20,814; co-component, neither inside the other — the reviewer-named containment-specific regime). Per-doc caps present_cap=40, absent_cap=30 (stratified), atomic_cap=80; *_truncated flagged.

  QUALITY. Round-trip gate (verify.py) PASSES: never_annotated 367/367, held_out 4357/4357 (deduced after ablation), absent 41100/41100 empty in BOTH directions, every derivation_path a valid DIRECTED located_in chain, cue-present 19885/19885, Mode-B 0. offset_ok 0.988/0.990. Schema-validated 3/3 (full/mini/preview). Completeness correction (2079 shared titles): Re-DocRED +67.5% located-in edges and 2.8x present queries vs DocRED — so absent gold is TRUSTWORTHY only on re-docred; docred absent is DOWNGRADED. Char honesty: mean ~1025 chars, max 2969, NO doc reaches 3000 (no padding/concatenation — natural-text + absent-relation is the load-bearing property). Caveats: closed-world absent; composed_only is pair-level (not type-level as kinship); multi-parent DAG; admin_level node tag best-effort/non-load-bearing; P276 lower precision (~0 LOC-LOC on re-docred). See dataset_card.md / README.md.
type: dataset

id: art_5zL3Idms1neE
title: >-
  Zero-spend empirical-isolation reframe: non-circular FACT-A/FACT-B ledger + scaffold
summary: >-
  Pure $0 re-analysis (numpy/scipy/json only; no LLM, no network; eval.py hard-asserts cumulative spend == $0 and that no
  OpenRouter/network module is imported). It reconstructs the 282-record CLUTRR pool (180 absent + 102 present) from art_LeRQRGHJZcdQ
  IN THE ORIGINAL iter-3 order (load_stored_iter3 ordering, restored via the iter-3 key sequence so index-tie-broken matched_coverage_mask
  and the by_doc story-clustered bootstrap reproduce exactly) and re-derives every carried literal with the source's verbatim
  helper functions (seed=20260617, B=10000). STEP-0 reproduce-verify gate: 38/38 checks PASS, reproduction_ok=True — FACT
  A raw absent-hallucination 0.4722 (deepseek 0.4833), FACT B crux survival 0.4353/0.7176/0.2471/0.7176 (deepseek 0.6724/0.2241/0.1034/0.2241),
  certificate absent CW 0.0278 (reduction 0.4444), mixed-pool selective accuracy 0.8267 vs 0.4133/0.3733/0.44/0.3733 @c*=0.266,
  mixed CW reductions 0.1099/0.1206/0.1028/0.1206 with Holm p_adj 0.0004/0.0027/0.0027/0.0027 and CIs excluding 0, spatial
  boundary cert CW 0.0219 vs raw-abstain 0.0351, multi-hop present win 0.8857 vs 0.5429 @0.6863, atomic P/R/F1 0.5361/0.5324/0.5343.
  Count arithmetic hard-asserted: re-docred 360/368 + docred 116/209 = 476/577. Deliverables: eval.py (+prose.py), eval_out.json
  (exp_eval_sol_out-VALID; full/mini/preview) carrying metadata.structural_by_construction_paragraph, a 48-row non_circular_vs_structural
  ledger (every number tagged side in {NON_CIRCULAR, STRUCTURAL_BY_CONSTRUCTION, INHERITED, NON_CIRCULAR_CONDITIONAL, MEASURED,
  PENDING} + evidence_tag + source_artifact + recomputed/matches flags), count_breakdown+fix sentence, abstract_front_matter
  (OpenCyc/general-fuzzy/atomic-re-extraction/3000-char OUT OF SCOPE; NeSy venue), operational compression recommendation,
  fuzzy_reframe (LEAD with spatial 5/5 Mode-B sound-violation catch; demoted query-vs-edge unit caveat; supporting cert CW
  0.000 vs commit-argmax 0.364/0.216), a 7-row one_thesis_table with evidence-class tags as COLUMNS and a clearly-labeled
  PENDING natural-corpus slot, and headline_structure_guidance. eval_digest.md mirrors all of it paper-facing. Three schema-valid
  datasets (non_circular_facts_ledger 48, one_thesis_contribution_table 7, reproduction_gate 38). Tells GEN_PAPER_TEXT to
  LEAD with confidence-blindness isolation, concede the closure mechanism INHERITED (+0.673 inherited / +0.0025 novel) up
  front, and never re-center on the structural-by-construction 2.8%.
type: evaluation
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
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
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Short descriptive figure title",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title - concise, descriptive, captures the main contribution",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.

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
</prompt>s-CERTIFICATE, no preserved
  disjunction, no abstention/risk-coverage, no cross-path zero-FP narrowing. We read its negative result as motivation to
  PRESERVE and NARROW the disjunction.
- >-
  Hu, Huang & Feng 2024 (arXiv:2408.07353, METRE): a TRAINED multi-LABEL classifier inferring the possibility of each temporal
  relation independently, treating VAGUE as >1 possible relation, on TB-Dense/MATRES/UDS-T. Difference: METRE is trained to
  maximise F1 (not recall-oriented soundness); it carries no set through an EXACT composition table across MULTIPLE paths,
  performs no cross-path intersection, issues no certificate, does not abstain. We use it as an ALTERNATIVE EDGE-READER into
  the SAME closure pipeline (Tier-2) at MATCHED per-edge recall with reported rho, to show the cross-path-closure gain is
  reader-AGNOSTIC -- explicitly handling that its F1 training may make its soundness differ from the LLM reader.
- >-
  Temporal-relation extraction with ILP global inference (Ning, Feng & Roth 2017, EMNLP; CogCompTime) and SputLink (Verhagen
  2004/2005) / CAEVO (Chambers et al. 2014, TACL): trained/sieve extractors that enforce transitivity to output a single globally-consistent
  labeling; SputLink computes closure to DENSIFY TimeBank. Differences: all COMMIT to one relation per pair for F1, use learned/approximate
  inference, and (for SputLink) produce the very non-adjacent gold whose circularity we AVOID by using NarrativeTime's direct
  human-timeline gold and TDDMan's manual non-auto-inferable gold; we PRESERVE disjunction, NARROW by exact-table cross-path
  intersection, and ABSTAIN.
- >-
  Path-of-Thoughts (2024, arXiv:2412.17963): graph extraction -> path identification -> per-path reasoning, beating SOTA by
  up to 21.3% on StepGame/CLUTRR. PRIMARY real-text baseline. Difference (verified): it calls an external reasoner 'for each
  reasoning path' INDEPENDENTLY and does NOT intersect relations arriving at the same pair from multiple paths nor detect
  cross-path contradictions; when paths disagree it outputs multiple relations but does NOT abstain. This is EXACTLY the gap
  Mode A fills; PoT is given a matched abstention signal (path-agreement).
- >-
  DSR-LM / 'LLMs can Learn Rules' (Yang et al. 2023, arXiv:2305.03742; Zhu et al. 2023, arXiv:2310.07064): INDUCE weighted/symbolic
  composition rules to fit task accuracy. Difference: rule induction optimises data fit and gives a point answer; we enforce
  the EXACT ALGEBRAIC LAWS (converse, associativity, disjointness) necessary for soundness independent of training data, and
  use closure for zero-FP narrowing, detection, repair, and abstention. Our table-held-fixed closure ON-vs-OFF ablation isolates
  path-consistency from 'a fixed consistent table exists' (DSR-LM's contribution).
- >-
  Logic-LM (Pan et al. 2023, arXiv:2305.12295) and LINC (Olausson et al. 2023, arXiv:2310.15164): Logic-LM self-refines using
  solver crash/unsat messages; LINC majority-votes the answers of multiple formalisations. Difference: Logic-LM reacts only
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
  read off text, producing per-instance certificates, abstention, and trace-graphs.
- >-
  Generic LLM selective prediction / abstention, incl. temporal QA (SelectLLM 2025; abstention surveys 2025; 'When Silence
  Is Golden: Can LLMs Learn to Abstain in Temporal QA' arXiv:2602.04755): reduce error by abstaining via learned uncertainty,
  vote margins, or RL with abstention-aware rewards. Difference: abstention is driven by GENERIC confidence/uncertainty signals
  or learned at the QA-answer level; there is no algebraic consistency certificate, no per-edge reading-error localisation,
  no preserved relation-algebra disjunction, and no closure-based narrowing. Ours abstains precisely because deductive closure
  leaves the query a disjunction -- a structural, training-free, per-edge certificate.
- >-
  Classical qualitative reasoners and tractability theory: GQR, SparQ, Allen (1983), Mackworth (1977, path-consistency PC-1/PC-2
  ITERATED to a fixpoint -- distinguishing full closure from a single intersection pass, exploited in our naive-intersection
  ablation), Renz & Nebel (random network model A(n,d,l)), Vilain & Kautz 1986 (point algebra), Nebel & Burckert 1995 (ORD-Horn,
  JACM 42(1)). So PC is COMPLETE for the convex point algebra and ORD-Horn yet SOUND-BUT-INCOMPLETE for full Allen IA / RCC-8.
  Difference: these assume a clean human-given table on already-formal data; none read the algebra off NL via an LLM, certify
  reading errors, narrow by cross-path intersection of LLM disjunctions, model an EMPIRICALLY-audited recall-bounded redundancy
  OPTIMUM, or optimise risk-coverage.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer from Qualitative Spatial-Temporal Reasoning and Tarski's relation algebras
  -- Allen's interval algebra, RCC-8, the convex point algebra, composition tables, and the path-consistency / algebraic-closure
  constraint-propagation algorithms (GQR/SparQ; Mackworth's iterated PC), plus the tractability theory (point-algebra and
  ORD-Horn completeness vs full-Allen NP-completeness) -- imported into LLM-based relational reasoning and hallucination control,
  with Reiter's 1980s model-based diagnosis (minimal hitting sets of conflict sets) for localising which extracted atom to
  retract. The Level-1 framing is CODING THEORY: an exact composition table turns multi-path redundancy in a document into
  an error-correcting code over LLM extractions -- redundant constraining paths let closure DETECT and CORRECT mis-reads with
  no external labels, as parity checks detect bit errors. The coding-theory 'optimal rate' sharpening (net benefit is an INVERTED-U
  because narrowing stays zero-FP only while every contributing symbol is sound) is made RIGOROUS: the joint-soundness 'decoding
  margin' is MEASURED empirically as J(E) rather than assumed as the independence product r^E, since a single LLM reader produces
  positively-correlated reading errors -- so the predicted peak uses the measured channel correlation. The Level-2 framing
  is SELECTIVE PREDICTION / risk-coverage in ML: compare an abstaining method against non-abstaining baselines at MATCHED
  COVERAGE with a shared coverage object and report the ACTIONABLE (singleton-resolution-to-correct) yield AND the downstream
  hallucination-rate reduction. Two refinements drive THIS iteration. (a) CORPUS SELECTION AS EXPERIMENTAL DESIGN: a mechanism's
  claim must live on a corpus that can structurally host it -- since MATRES annotates only adjacent-sentence pairs its deduction-required
  envelope is empty by construction, so the headline is relocated to a DENSE, full-coverage, direct-human-gold corpus (NarrativeTime)
  and corroborated where gold is provably non-closure-derived (TDDMan), with MATRES retained as a control that proves the
  gate discriminates. (b) ARM SCOPING borrowed from the discipline of stating where a mechanism's advantage must and must
  not appear: iterated closure provably equals a single intersection pass on acyclic length-2 structures, so the iteration
  win is claimed only on >=3-edge/cyclic structures -- now found on BOTH synthetic networks and the dense corpus's real long-hop
  stratum, dissolving the prior internal contradiction without confining the win to synthetic data. Three cross-field insights
  anchor the design: (1) LLMs are competent LOCAL qualitative namers that do NOT propagate constraints across paths -- the
  missing piece is global ITERATED propagation, and cross-path INTERSECTION of sound sets is a zero-FP win needing no over-commitment;
  (2) because the table is mathematical ground truth, intersection-of-sound-sets can only move toward gold and collapse-of-unsound-sets
  is a calibration-free certificate -- flipping the objective from accuracy-by-committing (ILP global inference, whose own
  results show consistency-enforcement does not raise F1) to faithfulness-by-abstaining; (3) the coding-theory lens names
  BOTH the safe primary mode (erasure-style narrowing) and the Achilles heel (a recall-bounded decoding radius whose EMPIRICAL
  joint-soundness decay produces an inverted-U), elevated to a pre-registered, decomposed, estimation-precision-bounded prediction
  anchored on both synthetic and real text.
terms:
- term: Dense direct-human-gold CO-PRIMARY (NarrativeTime / TimeBankNT)
  definition: >-
    The relocated real-text headline host: a timeline-based, FULL-TLink-coverage human re-annotation of TimeBank-Dense (news),
    IAA Krippendorff alpha ~0.68. Its density supplies abundant multi-path and >=3-edge/cyclic constraint structures (hosting
    both narrowing and a real-text iteration demonstration); its start-point restriction lands in the convex point algebra
    (PC COMPLETE); and its non-local gold is HUMAN-timeline-placed, not algorithmic-closure output, so closure recovery is
    non-circular. Replaces MATRES as primary because MATRES annotates only adjacent-sentence pairs.
- term: Gate-validation control (MATRES)
  definition: >-
    MATRES is retained but repositioned: because it annotates ONLY same/adjacent-sentence event pairs, every gold edge is
    locally co-occurring (directly-readable), so its deduction-required multi-path-with-bite envelope is structurally near-EMPTY
    and T0's N* ~ 0 by construction. Reporting this N* ~ 0 alongside NarrativeTime/TDDMan N* >> 0 demonstrates the deduction-required
    gate is DISCRIMINATIVE rather than vacuous.
- term: Non-circularity anchor (TDDMan)
  definition: >-
    The manually-annotated long-distance (>1-sentence-apart) subset of TDDiscourse whose pairs 'cannot be inferred automatically
    from existing annotations' -- so its gold is provably NOT the output of the closure algorithm under test. A Mode-A narrowing
    win on TDDMan therefore cannot be a closure artifact, bounding the residual timeline-implied-circularity worry about NarrativeTime
    by empirical replication rather than assertion. Relation set {before, after, simultaneous, includes, is_included}, coarse
    interval algebra.
- term: Non-circularity audit (locally-justifiable vs purely-timeline-implied)
  definition: >-
    For NarrativeTime, a partition of held-out edges into LOCALLY-JUSTIFIABLE (a textual cue near both events that the local-only
    reader can exploit) versus PURELY-TIMELINE-IMPLIED (no local cue; gold obtainable only from the human's holistic timeline).
    The deduction-required headline subset is the latter; because its gold is human-timeline placement (not algorithmic PC),
    recovering it by closure over independently LLM-read edges uses a DIFFERENT inference process and is non-circular. The
    fraction is reported up front.
- term: End-to-end hallucination-reduction headline (H2)
  definition: >-
    Promoted from a Tier-2 echo to a co-headline because it is the umbrella pipeline's actual deliverable: on the deduction-required
    / absent-relation subset, the closure pipeline's CONFIDENT-WRONG (non-abstained gold-mismatch) rate is lower than a raw
    LLM forced to a single relation, by at least a PRE-REGISTERED minimum effect, adjusted-CI-separated. A gateway test of
    the confirmatory family.
- term: Real-text iteration stratum (H3 on real text)
  definition: >-
    The dense corpus's >=3-edge/cyclic constraint structures, whose prevalence T0 computes a-priori (zero LLM spend). Length-2
    real queries still tie naive intersection (as predicted), but on this stratum full ITERATED closure can beat naive single-pass
    intersection -- bringing part of the iteration win onto real text instead of confining it to synthetic networks. If the
    stratum is empty/tiny, the iteration claim honestly stays synthetic-only.
- term: Applicability-envelope threshold (concrete number)
  definition: >-
    The pre-registered NUMBER distinguishing a 'general mechanism' from a 'niche safety-net': the deduction-required multi-path-with-bite
    fraction of evaluable held-out edges is scored >=10% = general mechanism, 5-10% = useful module, <5% = niche safety-net.
    Fixed before any LLM spend and reported from T0, so the contribution's reach is declared, not argued post-hoc.
- term: Multiplicity policy (confirmatory vs exploratory)
  definition: >-
    A pre-registered stance against the garden-of-forking-paths objection: the CONFIRMATORY family is H1 (narrowing), H2 (hallucination
    reduction), H3 (iteration gap grows), H4 (redundancy inverted-U disconfirmer), tested with Holm-Bonferroni / hierarchical
    gatekeeping (H1/H2 gateways) and ADJUSTED CIs; all strata, per-bin curves, reader-agnosticity, Mode-B, and secondary corpora
    are EXPLORATORY with nominal CIs.
- term: Recall-and-rho-matched reader-agnosticity
  definition: >-
    The protocol for the alternative-edge-reader test: each reader (METRE-style trained multi-label head; a second LLM/prompt
    family) is tuned to a MATCHED per-edge recall AND its measured cross-edge error correlation rho is reported, with the
    agnosticity verdict interpreted conditional on BOTH (conditioning on rho if it differs materially). Prevents 'the win
    is in the algebra' from being confounded by a reader whose F1-oriented training gives the same recall but different error
    correlation.
- term: Empirical joint soundness J(E)
  definition: >-
    The realized fraction of E-edge constraining subnetworks in which ALL edges are sound, MEASURED directly from data, replacing
    the independence product prod_e r_e. The zero-FP audit's reliability curve is pre-registered against J(E); the inverted-U
    cost term is 1 - J(E); positive cross-edge correlation rho makes J(E) decay slower than r^E so the predicted peak sits
    further out than an independence model says.
- term: Sound narrowing (Mode A, primary)
  definition: >-
    The zero-false-positive value mode: when every contributing LLM edge set is SOUND (contains its gold relation) but sub-universal,
    intersecting the compositions arriving at a query pair from MULTIPLE non-universal paths yields a set that still contains
    gold yet is strictly tighter than any single path. Requires breadth + multi-path bite, NOT over-commitment; its zero-FP
    guarantee SURVIVES PC incompleteness; inert only in the degenerate all-universal limit.
- term: Singleton-resolution-to-correct yield (headline metric)
  definition: >-
    The load-bearing Mode-A metric: the fraction of multi-path SOUND-input query pairs whose cross-path intersection collapses
    the query to the single CORRECT relation. Distinguished from STRICT-TIGHTENING yield (any reduction), which does NOT move
    matched-coverage selective accuracy nor the hallucination-rate metric. Both reported; singleton-resolution is load-bearing.
- term: Inverted-U redundancy optimum
  definition: >-
    Net Mode-A selective-accuracy gain RISES then FALLS as path redundancy/hop-count increases at fixed per-edge recall: more
    paths add narrowing benefit, but each added contributing edge lowers empirical joint soundness J(E), so silent-narrowing
    cost (1 - J(E)) eventually dominates. Peak location increases with recall; the recall-floor gate shifts it outward. Established
    only at a pre-registered estimation precision; otherwise reported as 'directionally consistent.'
- term: Naive-intersection baseline
  definition: >-
    Intersect the compositions arriving at the query pair in a SINGLE pass, without iterating to a fixpoint and without algebra-seeded
    converse propagation -- i.e. 'Path-of-Thoughts plus one obvious intersection step.' It COINCIDES with full closure on
    length-2 multi-path queries (so Mode A is predicted to TIE it on the real-text length-2 stratum) but diverges on longer/cyclic
    networks, where the full-minus-naive gap GROWS -- the iteration claim, tested on synthetic AND the real >=3-edge/cyclic
    stratum.
- term: Detection/repair (Mode B, secondary)
  definition: >-
    The collapse-based value mode: an empty closure certifies that some LLM edge is UNSOUND -- a gold-free zero-FP DETECTION
    flag (conditional on recall). Requires at least one over-committed/recall-failed edge to fire, supports Reiter-style minimal-hitting-set
    localisation/repair (which can mislocalise), and carries the silent-wrong-narrowing dual. Reported distinctly from Mode
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
    and draw the primary subset preferentially from deduction-required triangles. The T0 gate uses a structural proxy (no
    shared local span) computable without the LLM.
- term: Convex point algebra (NarrativeTime start-point arm)
  definition: >-
    The relation algebra over a single time point per event with convex base relations <=, =, >= (and disjunctions). NarrativeTime's
    timeline yields start-points whose ordering instantiates this algebra, for which path-consistency is provably COMPLETE
    and the table exact. We widen non-convex {<,>} (genuine !=) to VAGUE to preserve completeness and MEASURE the bite lost;
    if non-trivial we add a full-interval Allen arm scored as a lower-bound detector.
- term: Silent wrong narrowing (pre-registered failure mode)
  definition: >-
    When a contributing set OMITS gold (unsound), closure can narrow the query to a confident WRONG singleton with NO empty
    collapse -- a certified-LOOKING hallucination the mechanism actively endorses. Its rate is bounded per-edge by (1-recall)
    and per-network by (1 - J(E)); reported in the decomposition of gold-wrong non-abstained predictions; the recall-floor
    gate is tested as a mitigation and as the lever that shifts the inverted-U redundancy peak.
- term: Matched-coverage selective comparison
  definition: >-
    The protocol for comparing an abstaining method against baselines: each baseline is given its own abstention/confidence
    signal (vote margin, verbalised confidence, vote agreement, path-agreement), thresholds are swept so every method reports
    at the SAME coverage using the SAME coverage object (single-relation resolution), and selective accuracy is compared with
    paired-bootstrap CIs -- preventing the headline from conflating 'closure' with 'closure has a better-calibrated abstain.'
- term: Trace-graph
  definition: >-
    A human-auditable record: the QCN, which composition entries fired on which paths during closure, any minimal repairs,
    and optionally an equivalent SWI-Prolog/ASP proof discharged from the closed table for replay -- the connective tissue
    to the umbrella text-to-logic pipeline's auditability and quantified-hallucination-reduction requirements.
summary: >-
  We import exact relation-algebra path consistency (Allen interval, convex point algebra, RCC-8) into the deduction module
  of a text-to-logic pipeline and -- fixing the prior version's fatal corpus choice -- relocate the real-text headline from
  MATRES (adjacent-sentence-only, deduction-required envelope empty by construction) to a DENSE direct-human-gold corpus (NarrativeTime,
  full TLink coverage, human-timeline gold), corroborated on TDDMan whose gold is provably non-closure-derived: cross-path
  SOUND NARROWING of the LLM's high-recall disjunctive sets beats path-isolated reasoning and voting at matched coverage AND
  cuts the hallucination rate versus a raw LLM, while iterated closure beats naive single-pass intersection on long-hop/cyclic
  structures both synthetic AND real, and the recall-bounded inverted-U redundancy optimum is audited via empirical joint
  soundness J(E). An a-priori, zero-LLM-spend envelope gate (with a concrete applicability threshold), a confirmatory-vs-exploratory
  multiplicity policy, and recall-and-rho-matched reader-agnosticity make every headline falsifiable before any model is called.
_relation_rationale: >-
  Same certificate frame; novelty reframed to confidence-blindness isolation; absent-win conceded by-construction.
_confidence_delta: unchanged
_key_changes:
- >-
  REFRAMED the headline novelty (reviewer novelty MAJOR) from 'the certificate mechanism' to an EMPIRICAL/DIAGNOSTIC contribution:
  the entire confidence/uncertainty family is structurally blind to confident absent-relation hallucination while a gold-free
  structural signal is not. Conceded up-front (as framing, not footnote) that compose-through-table + abstain-on-collapse
  is the inherited NeSy premise (+0.673 inherited / +0.0025 novel).
- >-
  ACCEPTED the structural-by-construction critique (reviewer rigor MAJOR): CLUTRR absent pairs are disconnected components,
  so the certificate's 2.8% confident-wrong on them is near-tautological; re-centered the load-bearing claim on the two NON-CIRCULAR
  facts — FACT A (raw LLM confidently hallucinates on 47.2% of absent pairs) and FACT B (the 4-signal battery cannot filter
  them, crux-survival 0.435/0.718/0.247/0.718).
- >-
  Made RUNNING STEP B the single decisive iter-7 experiment (reviewer evidence MAJOR): the four-signal fair-baseline on the
  already-built natural Re-DocRED present/absent pools at matched coverage (crux-survival + mixed-pool showdown + Holm-adjusted
  CW reductions), on a stronger reader, with a publishable honest fork. Tied this to the rigor critique: on natural prose
  the extracted graph is not trivially correct (imperfect extraction can over-abstain on present pairs), which makes the experiment
  DECISIVE not confirmatory.
- >-
  Added a SECOND-DOMAIN/READER generality requirement (reviewer novelty MAJOR-ii): confirm FACT A + FACT B on >=1 additional
  relation domain (spatial/temporal absent) or reader so confidence-blindness is shown not kinship-specific (cross-family
  deepseek already supplies reader diversity).
- >-
  Distinguished the corpus-robust DIAGNOSTIC contribution (FACT A + FACT B, properties of the raw LLM and signals) from the
  certificate's NET UTILITY (extraction-limited on natural text), so the contribution survives even if the natural-corpus
  mixed-pool win is gated by extraction recall.
- >-
  Fuzzy section (reviewer evidence MINOR): flagged the query-level vs edge-read unit-of-analysis mismatch in the 0.000-vs-0.415
  contrast; directed iter-7 to build a true query-level confidence abstainer OR downweight the section and lead with the 5/5
  Mode-B sound-violation catch.
- >-
  Scope (reviewer scope MINOR): moved the deduction-sub-module scoping (OpenCyc/general-fuzzy/atomic-re-extraction/3000-char-natural
  OUT, named as future work not claimed) to the FIRST paragraph of the abstract; directed compression of the bracket-selected/concatenation-constructed
  operational case study to buy space for the natural-corpus result.
- >-
  Clarity (reviewer clarity MINOR): added the per-dataset Re-DocRED breakdown — 360 present / 368 absent on the re-docred
  primary slice; 476/577 round-trip is the combined re-docred + docred verification — to remove the 360!=476 / 368!=577 apparent
  inconsistency.
- >-
  Confidence held unchanged: STEP A CONFIRM strengthens the diagnostic core, but the sharpened structural-by-construction
  rigor concern and the still-unrun natural-corpus experiment (the binding magnitude/locus gap) offset it; the path to clearing
  the bar is now cheap and well-specified.
relation_type: evolution
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 32 research artifacts across all iterations.

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

--- Item 22 ---
id: art_i53dBKgGY3Ig
type: experiment
title: >-
  Spatial RCC-8 cross-path test: structural scope-boundary + closure hallucination audit
summary: |-
  Decisive iter-5 experiment on SpaRTUN/SpaRP-PS1 (the strongest real spatial venue, 27.4% structurally-flagged 'tight multipath'), resolving two pre-registered questions. CPU-only; total LLM spend $0.225 (< $9 cap, gemini-3.1-flash-lite primary + deepseek-v3.2 cross-family); cached reruns $0. All four method_out variants validate against exp_gen_sol_out.

  ENGINE (new, self-tested, reusable): RCC-8 (8-relation, 64-cell GQR table) AND a Cardinal Direction Calculus (CDC, 9-relation) built as the product of two convex point algebras (reproduces GQR cd.comp per dossier art_2Xp7DiYUxoNo) -- 81 cells. Both pass a blocking self-test; closure unit tests verify naive==full@len-2, naive!=full@>=3-hop chain, Mode-B inconsistency collapse, non-symmetric orientation (TPP<->TPPi), and a multi-path intersection narrowing.

  Q1 (cross-path-intersection FORK) = SCOPE-BOUNDARY, gold-structural, $0. A zero-LLM a-priori gate over VERIFIED gold composition shows the error-correcting-code mechanism cannot realize on the real gold graphs of EITHER single algebra: the RCC-8 subgraph is a containment TREE (all 228 RCC-8 deduction queries have exactly 1 edge-disjoint path), and the cardinal subgraph's 57 >=2-short-path queries already compose to a SINGLETON on the best single path (best_single_len_hist={1:54,2:2,3:1}), leaving no room for intersection bite. The corpus's 27.4% flag is purely STRUCTURAL (undirected, mixed-algebra, no composition); the genuine redundancy is CROSS-ALGEBRA (topology vs direction), not intersectable in one calculus. This empirically vindicates the dataset card's own 'verify, don't trust noise labels' caveat at a deeper level, and is a SHARPER negative than the iter-4 temporal one: it needs no LLM reads. The mechanism IS real when same-algebra redundancy + sound reads exist -- the synthetic RCC-8 positive control (1-D interval model) at recall 0.95 gives intersection selective-acc 0.89 > best-single 0.80 (+0.093, mean bite 1.23), degrading correctly as recall drops.

  Q2 (real-venue closure-certified deduction vs neural baselines) = ABSTENTION-DRIVEN HALLUCINATION REDUCTION. On the 228 single-path RCC-8 deduction queries SpaRP-PS1 hosts (gold-singleton, gold-sound, hops 2-3), the neuro-symbolic method (read local stated RCC-8 constituents -> exact GQR-table compose -> abstain on collapse/non-singleton) cuts confident-wrong (hallucination) from raw-LLM 0.193 / chain-of-thought 0.123 to 0.022 (reduction 0.171, 95% CI [0.118,0.228], Holm-significant), with auditable Prolog trace-graphs. HONEST framing surfaced prominently: this is a COVERAGE tradeoff, not an accuracy gain -- the method answers only 15% of queries; at MATCHED coverage the raw LLM is NOT less accurate (method 0.853 vs raw 0.941, gap CI [-0.22,0.04]); and a neural baseline given the same abstention signal (raw-abstain: hallucination 0.035 @ coverage 0.285) is competitive/dominant. The gold-read ORACLE resolves 0.89 at 0 hallucination -> the symbolic engine is SOUND and not the bottleneck; the binding constraint is constituent-read recall (0.55) under a coverage-vs-soundness tradeoff. Spatial RCC-8 reads are FAR more informative than temporal-Allen reads (breadth 2.1/8 vs 11.5/13; underdetermined 0.04 vs 0.87), so the spatial negative is STRUCTURAL, not a read-quality failure -- a distinct second binding mode from the temporal venue. SpaRP object descriptions were recovered 100% from the raw symbolic_entity_map (resolving the #1 mention-recovery risk). Cross-family (deepseek-v3.2) corroborates (constituent recall 0.585, method hallucination 0.0). Prolog audit (python-checked, swipl unavailable) emits a synthetic 2-path narrowing (5-set ∩ 3-set -> {DC}), two real single-path closure traces, and a Mode-B collapse ({NTPP} ∩ {DC} = empty); python==engine on all.

  For downstream paper-writing: lead Q1 as a clean $0 gold-structural scope-boundary (mechanism synthetic-only, proven real by the control); present Q2 as an honest interpretability result (certified abstain-on-collapse converts confident-wrong outputs into auditable abstentions but does not beat a confidence-thresholded neural baseline). The transferable contribution is the training-free, gold-free abstain-on-collapse certificate + sound exact-table composition; the cross-path error-correcting-code thesis remains synthetic-only.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_5/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 23 ---
id: art_I22c-J7-OcXl
type: experiment
title: Genuine LLM Fuzzy-Unification with a Certificate-Bounded Hallucination Guarantee
summary: |-
  Converts reviewer MAJOR #2 (the iter-4 Mode-P 'fuzzy unification' was circular memorized-table recall at confidence exactly 1.0) into a real, measured contribution. method.py builds GENUINELY-fuzzy LLM reads from existing gold in two labeled settings and shows a training-free abstain-on-collapse CERTIFICATE bounds the hallucination cost of feeding them into a sound closure engine.

  SETTING 1 (vague spatial RCC-8, SpaRP-PS1, art_f-ofxduZjwSM): a KNOWN RCC-8 relation is rendered with a vague preposition (near/touching/around/inside/overlapping) that has no single RCC-8 answer; gemini-3.1-flash-lite (temp 0) emits a calibrated sub-1.0 disjunction over the 8 base relations. SETTING 2 (ambiguous kinship, CLUTRR, art_HS7-lxhZnU9m): an atomic fact is replaced by an informal term (guardian/descendant/family elder/sibling-figure/relative by marriage/younger relative) mapping to a type-disjunction.

  MEASURED (cap 1500/setting; total real spend $0.0029 over 22 sha256-cached calls; warm reruns $0): (i) CALIBRATION - frac_conf_1p0=0.00 in BOTH settings vs the memorized Mode-P's 1.00 (the headline honesty contrast, loaded from the iter-4 method_out.json); per-candidate ECE 0.142 (spatial)/0.111 (kinship), top-1 ECE 0.286/0.051; spatial read soundness 0.93 (genuine unsound reads), kinship 1.00. (ii) CERTIFICATE-BOUNDED CLOSURE - fuzzy disjunction + exact-table reads fed into qcn.algebras RCC-8 path composition+intersection and a new disjunctive-seed kinship forward-union closure; output contract COMMIT(|D|=1)/COLLAPSE(|D|=0,Mode-B)/ABSTAIN(|D|>1). Risk-coverage vs commit-argmax (point estimate, always answers) and abstain-always: certificate confident-wrong=0.000 at coverage 0.54 (spatial, n=228 all deduction-required RCC-8 queries, 38 multipath) and 0.31 (kinship, n=1013 clean multi-hop) vs commit-argmax 0.364/0.216 (doc-clustered paired-bootstrap Delta-CI [0.30,0.43] and [0.17,0.26], both exclude 0). The read-soundness-conditional ZERO-FP invariant (sound read => no confident-wrong) is proved by construction and ASSERTED (0 violations); spatial unsound reads caught 1.0 (0 silent-wrong missed). (iii) AUDITABLE TRACE-GRAPHS tag every step exact_table vs llm_fuzzy with the emitted set + per-relation p + gold-retained flag + final certificate decision, including the honest unsound-read-caught case (around -> {NTPPi,TPPi} drops gold EC => certificate ABSTAINs instead of committing wrong DC).

  Also: cross-family sensitivity (deepseek-v3.2 hedges broader, breadth 4.6/6.1, still calibrated frac_conf_1p0=0.00); symbolic self-tests T1/T2 (200/200 spatial exact-path soundness, 200/200 kinship gold-clean recovery, disjunctive-seed zero-FP unit test); VERDICT YES for both settings.

  BASELINES: commit-argmax and abstain-always on the identical query pool, plus the memorized Mode-P calibration contrast. Reuses iter-4 engines (llm.py sha256 cache + $9 hard guard, kinship.py, stats.py, dataio.py, qcn/). HONEST CAVEATS recorded: reads are term-conditioned (the vague term is the unit of fuzziness; ~6 distinct reads drive hundreds of per-edge calibration records, empirical per-term gold mix is the target); SpaRP uses symbolic ids + templated text; CLUTRR <=871 chars; kinship had 0 unsound reads so its certificate-catch is untested (zero confident-wrong holds trivially there). Files: method.py, figures.py (4 PNGs: calibration contrast, reliability diagrams, risk-coverage frontier, breadth-vs-confidence), method_out.json (aii exp_gen_sol_out validated) + mini/preview/full. method_out.json datasets: spatial_fuzzy_rcc8 (1728 ex) and kinship_fuzzy_paraphrase (2513 ex) with predict_certificate/predict_commit_argmax/predict_abstain_always.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_5/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 24 ---
id: art_WQoePKrpsTPo
type: experiment
title: Operational ~3000-char end-to-end closure-certified deduction case study
summary: |-
  FIRST end-to-end run of the closure-certified text->logic pipeline on real ~3000-char professional documents (retires reviewer MINOR #4), framed as an OPERATIONAL CASE STUDY (per-document operating points, NOT a powered test). TWO arms, each: span-local LLM atomic read -> QCN closure (emit singleton / abstain non-singleton / Mode-B empty) -> runnable SWI-Prolog discharge EXECUTED in swipl 9.0.4 -> quantified confident-wrong (hallucination) reduction vs raw LLM as a risk-coverage tradeoff with coverage beside every number.

  TEMPORAL primary = 5 NarrativeTime news articles in the PC-complete convex POINT start-point algebra. NarrativeTime has NO single doc in [2500,3500] chars (cluster <2500 or >4200), so docs are BRACKET-selected around 3000 (mean 3050.6, range 2197-4293; exact lengths reported). Atomic disjunctive-set recall 0.77-0.92 (broad reads, breadth ~2.45/3), most-likely precision 0.36-0.56; 150 queries -> 22 emit / 126 abstain / 2 Mode-B collapse; hallucination reduction vs whole-document raw 0.27-0.60 (mean 0.45) with coverage_modeA 0-0.33 and coverage_raw 1.0 (faithfulness-by-abstention; Mode-A confident-wrong 0-0.17).

  KINSHIP contrast = 3 ~3000-char documents (3246-3602 chars) each concatenated from disjoint-entity CLUTRR sub-stories (calculus memorized -> pipeline works FULLY). Atomic recall 0.39-0.56 (mean 0.49 = the EXTRACTION bottleneck, not closure), within-story multi-hop selective accuracy 0.75 (8 emit, 6 correct; misses are extraction-limited), and 56/56 cross-story ABSENT pairs abstained = 0 confident-wrong BY CONSTRUCTION. A new forward-closure least-fixpoint Prolog emitter (prolog_kinship.py) reproduces the certified engine EXACTLY (engine-match 35/35; the iter-3 simple-path solve_/4 is incomplete on long chains). 95 Prolog programs discharged AND executed in swipl (60 temporal + 35 kinship); 4 coherent human-auditable trace-graphs (temporal narrowing + faithful-abstain, kinship multi-hop derivation + absent-abstain) ship with runnable .pl paths + swipl stdout.

  Blocking gates passed before any spend: closure tests (Allen-vs-GQR + point PC), point-algebra self-verify, kinship gold-atomic go/no-go (17/17 recovered, 100% sound), swipl probe, cache round-trip. Output method_out.json (datasets narrativetime_3kchar=150 rows, clutrr_3kchar_concat=73 rows; per-document blocks, case_study_summary, prolog_execution_aggregate, trace_graphs, honesty_commitments) validates against exp_gen_sol_out; 0.6MB. Total LLM cost $0.31 (warm-cache rerun $0.02), << $10 cap. ~99% of code reused: temporal_core.py = iter-2 method.py verbatim (build_read_prompt/parse_read/make_read_items/parse_read_results/per_edge_recall/run_query/emit_prolog/point<->coarse maps); iter-3 kinship.py/prolog.py/readers.py/dataio.py/baselines.py/stats.py; iter-3 llm.py (per-item max_tokens/temperature/tag, SHA-256 cache, hard cost guard). NEW: document-selection-by-length (bracket), CLUTRR concat builder, most_likely_precision, run_pot/run_sc/run_full_doc_raw_temporal, prolog_kinship.py, per-document reporting, whole-document raw baseline, trace-graph/output assembler. Honest scope: closure CERTIFICATE + abstain-on-collapse contract is the contribution; atomic extraction is MEASURED not improved; OpenCyc/fuzzy-unification out of scope.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_5/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 25 ---
id: art_N8G6ZlQTONfk
type: evaluation
title: >-
  Iter-5 $0 re-analysis: synthetic-Allen small-bite + one-thesis tags-in-columns table
summary: >-
  Pure $0 re-analysis (numpy+scipy only, deterministic seed=20260617, B=10000 paired bootstrap, ~1s CPU) EXTENDING the validated
  iter-4 re-analysis; 0 reproduction mismatches against iter-4 headline numbers. Deliverables: (1) MINOR #5 small-bite caveat.
  Reproduced the synthetic Allen positive-control recall_95 cell EXACTLY (intersection cov 0.250/selacc 0.976; best_single
  0.226/0.717; naive 0.316/0.842) and added paired-bootstrap CIs: cross-path COVERAGE gain +0.024, 95% CI [-0.022,0.070],
  boot_p=0.17 -> CI INCLUDES 0 (small, not sig); SELECTIVE-ACCURACY gain +0.259, 95% CI [0.177,0.349], boot_p=0.0 -> EXCLUDES
  0 (large, real). Auditable precision decomposition: of best_single's 113 answers, 50 both-resolve (perfect agreement, aligned
  gain 0.000), 75 intersection-only @0.96 acc, and 32 wrong best_single commitments AVOIDED by collapse. Inverted-U recovered
  on the realized-coverage axis (realized_cov = benefit + cost_silent_wrong = 1-abstain-collapse, identity verified <1e-9)
  per (recall,K) bin with Wilson + Newcombe CIs; peak K*=[2,4,7,10,16], silent-wrong 0.006->0.146; honest recall-dependence
  + K1-vs-best-single caveat (large K-gains only at unreachable high recall). Net reframe: PRECISION of committed answers,
  not expanded coverage. (2) MAJOR #3: one_thesis_contribution_table with evidence tags as COLUMNS (claim|evidence_tag|where_it_holds|status|key_numbers):
  two-row SPINE (gold-free abstain-on-collapse CERTIFICATE @CLUTRR; read-informativeness precision/recall IMPOSSIBILITY),
  scaling-law + inverted-U DEMOTED to supporting, marginal-temporal + scope as footnotes, spatial-RCC-8 SpaRTUN left as a
  labeled PENDING slot. Plus carried corrected_temporal (neither Holm gateway clears, CIs include 0, 42.5% confident-wrong)
  and deduction-submodule ceiling (0.53 atomic recall->19% coverage). Outputs: eval.py, make_digest.py, eval_out.json (+full/mini/preview,
  all aii-json exp_eval_sol_out VALIDATED) with 38 flat numeric metrics_agg scalars and datasets[] = 8 synthetic-Allen worked
  examples + carried 282 CLUTRR + 600 temporal per-record examples, and eval_digest.md (paper-facing: small-bite table, inverted-U
  realized-coverage table, the contribution table, headline-structure guidance). $0 LLM spend, no OpenRouter client instantiated.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_5/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 26 ---
id: art_NUWTxBVWENIJ
type: dataset
title: Natural-Text Absent-Relation Kinship Corpus from Re-DocRED + DocRED
summary: |-
  Document-level KINSHIP corpus built from genuinely-natural Wikipedia introductory prose (no templating, no concatenation), for iter-7's STEP-B experiment: does a closure CERTIFICATE beat a confidence-thresholded abstainer on a real-text ABSENT-relation regime? It replaces templated CLUTRR / symbolic-id spatial corpora with real prose.

  SCHEMA: exp_sel_data_out, ONE ROW PER DOCUMENT, grouped by dataset. input = detokenized Wikipedia prose (per-token char offsets recorded; mention spans verified, offset_ok ~0.98). output = json.dumps(gold_graph) with: nodes [{entity_id, surface, type, gender(best-effort), mention_spans=[[char_start,char_end)], wikidata_qid:null}]; atomic_edges (the KB / proof chain; each flagged locally_justifiable = a span-local reader can extract it: adjacent-sentence co-occurrence + surface kinship cue); query_edges (held-out PRESENT, deduction-required: no direct annotated edge, no local co-occurrence, derivable >=2-hop composition; composed_only types grand/uncle/in-law/... are OUTSIDE DocRED's inventory => provably non-circular; fields incl primitive=robust gold, hop_count, derivation_path, fully_readable); absent_relation_pairs (both entities family-participating but in DIFFERENT connected components => no kinship path; closed-world). Flat metadata_* columns per row (fold by SHA-256%5, source, split, char_len, present/absent counts, hop_histogram, locally_justifiable_frac, offset_ok_frac, ...).

  DIRECTION CONVENTION (fixed): edge source->target with type=primitive means 'target is source's primitive'. DocRED {h,t,r} => source=h,target=t: P22->inv-child(parent,male), P25->inv-child(female), P40->child, P26->SO, P3373->sibling. P1038 is NOT in DocRED's inventory (0 edges) -> unused.

  DROP-IN ENGINE: top-level metadata.composition_table holds the CLUTRR finite kinship table verbatim (rules_store primitive compositions + relations_store surface<->primitive<->gender map; tagged NOT a relation algebra). iter-7 runs kinship.py forward least-fixpoint UNION closure UNCHANGED by mapping each atomic_edge to {a:source,b:target,type:primitive}. VERIFIED: the engine reproduces 476/476 emitted PRESENT golds and derives EMPTY for 577/577 ABSENT pairs.

  TWO DATASETS (target_num_datasets=2): 're-docred' (PRIMARY, 575 family-bearing docs from tonytan48/Re-DocRED, sha e0ab3489) gives 360 PRESENT multi-hop queries (222 composed-only/non-circular; hops 2:318/3:38/4:4) and 368 ABSENT pairs -- both EXCEED the >=150 / >=300 targets. 'docred' (SECONDARY, 400 docs from thunlp/docred, sha 7985b4e0) corroborates and demonstrates the completeness-correction: on 400 shared titles Re-DocRED carries 3087 family edges vs DocRED's 1716 (+1371, +80%), so vanilla false-negatives would corrupt absent gold -- the load-bearing reason absent labels are only trustworthy on the re-docred slice; docred absent gold is DOWNGRADED.

  HONESTY (report actuals, no padding): DocRED intro prose averages ~1020 chars; NO family-bearing doc reaches 3000 chars and only ~2.6% reach 2000 (15 docs in [2000,4000], flagged) -- we do NOT concatenate/pad; the natural-text + absent-relation regime is load-bearing, not the 3000-char target. locally_justifiable_frac ~0.62 (readability/non-circularity audit). Gender is best-effort (primitive is the robust gold when unknown). $0 LLM spend (deterministic cue check passes 100%; optional LLM judge skipped). All 3 variants validate against exp_sel_data_out; full=4.5MB (<100MB, no split). Files: data.py (uv entry), assemble.py/build.py/detok.py/kinship.py (pipeline + verbatim closure engine), verify.py, clutrr_composition_table.json, README.md.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 27 ---
id: art_LeRQRGHJZcdQ
type: experiment
title: Closure certificate vs a strong 4-signal confidence-thresholded neural abstainer
summary: >-
  STEP A executed (VERDICT=CONFIRM; one-time spend ~$0.30, far under the $9 cap; cached re-runs $0). We re-use the EXACT cached
  iter-3 CLUTRR pool (180 absent + 102 present) and iter-5 spatial RCC-8 pool (228 single-path queries). A reproduction gate
  rebuilds the 282 records from CLUTRR and verifies certificate/raw/sc/pot predictions are IDENTICAL to the published iter-3
  pool (art_0a7i481ZRwS1; 0 mismatches, $0). We add a 4-signal confidence/uncertainty BATTERY to the raw LLM answerer: (a)
  verbalized confidence, (b) self-consistency vote-margin@k=10, (c) Kadavath P(True), (d) semantic-entropy negentropy; each
  defines a confidence-thresholded RAW-ABSTAIN baseline at matched coverage. KEY RESULTS (REAL-LLM-READ, gemini-3.1-flash-lite;
  story-clustered paired bootstrap B=10000, Holm/4): the raw LLM hallucinates a kinship on 47.2% of absent pairs vs the certificate's
  2.8% (reduction 0.444, CI[0.317,0.583]); at the LLM's natural coverage NO signal removes any hallucination. CRUX survival
  table: verbalized confidence is >=0.5 on 100% of hallucinations; fractions surviving a certificate-matched rule are 0.435/0.718/0.247/0.718
  for verbalized/sc_margin/ptrue/negent — only P(True) partially separates them (median 0.0) yet 24.7% still survive. DECISIVE
  mixed-pool matched-coverage showdown (coverage 0.266): certificate selective accuracy 0.827 vs every signal 0.37-0.44 (~2x);
  confident-wrong reductions 0.10-0.12 with Holm-adjusted CIs all excluding 0. HONEST scope boundary (P_O): on the genuine
  ordinary SINGLE-PATH stratum (spatial RCC-8) the certificate ties/loses (selective-accuracy gap -0.088, CI[-0.222,0.040];
  confident-wrong 0.022 vs raw-abstain 0.035, CI includes 0); CLUTRR-present is multi-hop where the certificate also wins.
  Cross-family (deepseek-v3.2) reproduces the edge (48.3% absent hallucination; survival 0.672/0.224/0.103/0.224). Includes
  worked no-derivation and Mode-B-collapse abstentions with Prolog programs (python-checked, swipl unavailable, labelled truthfully)
  and the full leaderboard/risk-coverage/crux/Holm tables. Output method_out.json (exp_gen_sol_out) groups per-query rows
  into clutrr_no_derivation (180), clutrr_ordinary_deduction (102), spatial_rcc8_ordinary (228). Caveat: on the pure-absent
  pool confident-wrong==coverage, so per-signal discrimination lives in the mixed-pool view and the crux table (stated explicitly).
  Provides the load-bearing 'certificate beats the BEST uncertainty signal, not a strawman' evidence for the paper.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 28 ---
id: art_0MDLD-w-RXOu
type: evaluation
title: 'Zero-spend fuzzy fair-baseline re-analysis: certificate vs confidence threshold'
summary: >-
  Pure numpy+scipy, $0-LLM, deterministic (seed=20260617, doc-clustered bootstrap B=10000) re-analysis producing four GEN_PAPER_TEXT
  deliverables. STEP 0 reproduce-verify of iter-4/iter-5 carried literals passes with 0 mismatches (29+13 checks) and 0 carried-literal
  mismatches vs CLUTRR/SPATIAL source files; FUZZY ground-truth literals asserted (spatial cert cov 0.5350877 / CW 0.000 /
  commit-argmax CW 0.3640=83/228 / n_unsound 5; kinship cert cov 0.3139191 / commit-argmax CW 0.2162=219/1013 / n_unsound
  0). TASK 1 (MAJOR #2, the only new computation): a confidence-thresholded top-1 neural abstainer built at the EDGE-READ
  level (1500 calibration reads/setting; query records lack per-query confidence) via top-k selection at matched coverage.
  Result: the certificate (CW=0.000) BEATS the fair confidence baseline in BOTH settings — spatial CW 0.4147 95% CI [0.3760,0.4566]
  @cov 0.5353 (implied tau 0.7, ECE 0.286 POOR); kinship CW 0.3461 95% CI [0.2931,0.4128] @cov 0.314 (implied tau 0.4, ECE
  0.051 GOOD — beats anyway because max conf is only 0.8 and read accuracy is modest). Both bootstrap lower bounds exclude
  0 -> certificate_beats=True. Full risk-coverage frontier emitted (spatial CW floors ~0.37 even at 10% coverage); hard-tau
  overshoot reported. Mode-B distinctive edge: 5/5 query-pool unsound spatial reads caught, 0 silent-wrong missed; 100 unsound
  calibration edge-reads ALL at high conf {0.7:13,0.8:87}, 88 sitting in the committed region a threshold would commit-wrong
  — kinship Mode-B UNTESTED (0 unsound reads). A load-bearing unit-of-analysis caveat is recorded (certificate CW on closure
  QUERIES vs baseline CW on edge READS; query-level abstainer is PENDING STEP-A). TASK 2 (MAJOR #3): verbatim tempered 'two-conditions-independently-violated,
  not a predictive law' paragraph for sec:decisive + tagged supporting numbers. TASK 3 (MINOR #5): one-thesis contribution
  table (tags as columns) with ONE certificate spine row, cross-path negative as one supporting row, mechanism analysis demoted
  to appendix rows, footnote/ceiling rows, labeled PENDING slots, and a verbatim one-line thesis. TASK 4 (MINOR #4): venue
  reposition (ACL Knowledge Extraction -> NeSy/temporal-and-qualitative-reasoning), scope boundaries, and bracket-selected/concatenation-constructed
  3000-char doc labels. Outputs: eval.py, eval_out.json (exp_eval_sol_out VALIDATED; metrics_agg 46 numbers; datasets fuzzy_spatial_conf_baseline
  300 / fuzzy_kinship_conf_baseline 300 / fuzzy_spatial_unsound_reads 100; every derived number carries an evidence_tag),
  full/mini/preview variants, and a paper-facing eval_digest.md with the rebuilt per-setting Table 3, tempered paragraph,
  one-thesis table, venue/scope, and headline-structure guidance. Files 0.42 MB (<100MB, no split). Deps pinned (numpy==2.4.6,
  scipy==1.17.1, loguru==0.7.3).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 29 ---
id: art_dA_3iFe_7fn_
type: research
title: >-
  No-Derivation Abstention vs Confidence Family; NeSy Reposition; Re-DocRED Absent Gold
summary: >-
  Pure-web research bundle ($0) for iter-6/iter-7 of the closure-certificate project, across three workstreams. (A) Pins the
  confidence/uncertainty selective-prediction family our STEP-A battery competes against -- verbalized confidence [Lin2022;
  Tian2023], self-consistency [Wang2023], P(True)/P(IK) [Kadavath2022], semantic entropy [Kuhn2023; Farquhar2024], SelfCheckGPT
  [Manakul2023], the abstention survey [Wen2024], learned temporal abstention [Zhou2026], and the adversarial internal-state-probe
  neighbour [Song2026] -- with verified BibTeX, per-method abstention signals + verbatim quotes, a paper-ready signals-vs-catches
  table, and a ~250-word drop-in differentiation paragraph arguing every signal is dispersion/confidence-driven and therefore
  BLIND to a confident, self-consistent absent-relation hallucination, whereas the certificate abstains STRUCTURALLY (no derivation
  path) regardless of confidence -- with honest scope (confidence baselines tie at matched coverage on ordinary uncertain
  deduction). (B) A timing-aware (as-of 2026-06-18) NeSy / qualitative-reasoning venue shortlist -- Neurosymbolic AI journal
  (rolling, the only open NeSy-family target now), NeSy 2026/2027, *SEM, KR 2026 (qualitative reasoning in scope), STRL, EMNLP/ARR
  -- a crisp 'why not ACL Knowledge Extraction' statement, and a recommendation to SWAP primary<->fallback. (C) Verifies Re-DocRED
  (tonytan48/Re-DocRED, arXiv:2205.12696, 2022.emnlp-main.580, MIT, splits 3,053/500/500, '~64.6% of triples missing' in original
  DocRED, recall 32.07->69.40), confirms kinship coverage (P22/P25/P26/P40/P3373 PRESENT; P1038 ABSENT), documents the false-negative
  pitfall + disconnected-component absent-gold methodology, and scouts alternative natural hosts (CustFRE = natural prose
  with explicit no_relation gold; KinshipQA = generated/synthetic, fails the natural bar). Directly retires the reviewer novelty
  MAJOR + venue MINOR and de-risks iter-7 STEP-B.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 30 ---
id: art_htcr8yOZLCQy
type: experiment
title: Closure Certificate vs 4-Signal Confidence Battery on Natural Re-DocRED Kinship
summary: |-
  STEP-B (iter-7): the iter-6 CLUTRR fair-baseline experiment re-run VERBATIM on the GENUINELY-NATURAL Re-DocRED/DocRED Wikipedia kinship corpus (art_NUWTxBVWENIJ). It moves the load-bearing diagnostic off templated text onto real prose: a closure CERTIFICATE (forward least-fixpoint UNION over LLM-extracted kinship edges -> abstain when no derivation path) vs the strongest confidence/uncertainty BATTERY on the raw LLM answerer (verbalized, self-consistency vote-margin@k=10, Kadavath P(True), semantic-entropy negentropy).

  REUSE vs NEW: readers.py / kinship.py (forward-UNION engine, the correct one for the finite kinship table) / baselines.py / stats.py / llm.py / prolog.py are copied VERBATIM from iter-6. New code: dataio_redocred.py (natural-corpus loader + entity-name GROUNDING of LLM names to gold entity_ids via mention-span aliases; measured grounding recall ~0.99) and method.py orchestration (PRIMITIVE-level scoring since gender is best-effort, natural-prose atomic P/R, certificate-abstention DECOMPOSITION, gold-read ceiling, pre-registered FORK verdict).
````

### [2] SKILL-INPUT — aii-paper-writing · 2026-06-18 03:23:51 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [3] SKILL-INPUT — aii-semscholar-bib · 2026-06-18 03:24:04 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
