# review_paper — test_idea

> Phase: `invention_loop` · round 9 · Substep: `review_paper`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave the agent(s) in this substep — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-18 08:08:31 UTC

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
\label{sec:intro}

This paper studies the \emph{deduction sub-module} of a text-to-logic pipeline: a sound symbolic forward-closure over LLM-extracted relations that abstains rather than guess. We fix the scope in the first sentence so no reader mistakes the contribution. This is \emph{not} a full operational text-to-first-order-logic system: atomic and multi-hop relation \emph{extraction} we measure but do not improve; upper-ontology / OpenCyc grounding \citep{Lenat1995}, general open-vocabulary fuzzy unification, and reasoning over genuine $\sim$3000-character professional documents are out of scope and named as future work this paper does not claim.

\textbf{What is the problem?} A growing class of systems reads a short professional document---a news report, a contract clause, a biography---into formal predicates a symbolic reasoner can execute, with a large language model (LLM) resolving the terminology the surface text leaves implicit \citep{Pan2023, Olausson2023}. Atomic extraction (naming locally co-occurring relations) is by now something LLMs do competently if imperfectly. The \emph{deduction} step is where faithfulness breaks: synthesizing explicit facts with implicit composition knowledge to answer a query about two entities that never co-occur in one span.

\textbf{Why it matters.} The single most damaging deduction error is the \emph{absent-relation} hallucination: the truthful answer is ``these two entities are not related,'' but the LLM, asked for the relation, names a locally plausible one anyway---at \emph{high} confidence, with samples agreeing. This is a recognized knowledge-extraction failure. In relation extraction (RE), \citet{Yang2025DEPTH} measure that Qwen2.5-14B incorrectly predicts a relation on $96.9\%$ of \textsc{no-relation} pairs in SciERC (correct on only $45$ of $1{,}475$); \citet{Li2024RelClassifier} trace the document-level LLM gap to ``the dispersion of attention by LLMs due to entity pairs without relations''; and \citet{Pi2025RelPrior} filter ``unrelated entity pairs [that] introduce noise.'' We therefore do \emph{not} claim that confident absent-relation fabrication is a new or a-priori-undiscoverable phenomenon---its single-hop \emph{rate} is already documented. What is unaddressed is the \emph{compositional} case.

\textbf{Why it is hard, framed as a compositional false premise.} We argue the multi-hop version is best understood as a \emph{compositional false-premise} failure: the question ``what is $X$ to $Y$?'' presupposes that a \emph{derivation path} exists between $X$ and $Y$, and that presupposition is a \emph{structural} claim about the document's relational graph that can be false even when both entities are richly related to others. False-premise and unanswerable-question abstention is an open problem---FalseQA shows LLMs answer questions with false presuppositions \citep{Hu2023}; AbstentionBench finds false-premise abstention unsolved at frontier scale and that reasoning fine-tuning \emph{degrades} it by $24\%$ \citep{Kirichenko2025}; the abstention survey of \citet{Wen2024} separates \emph{query answerability} $a(x)$ from model confidence $c(x,y)$. Existing detectors operate at the \emph{sentence level} and are trained or prompt-elicited; the single-hop RE refiners above are schema-bound and require fine-tuning. Our setting lifts the premise to a \emph{compositional, multi-hop, document-internal} structural claim, and our detector is a property of the extracted graph's closure rather than a learned or retrieval judgment.

\textbf{Why the default defenses fail on exactly these errors.} The dominant defense against LLM error is selective prediction: abstain when an uncertainty signal is low. Every member of the confidence/uncertainty family is a monotone function of prediction \emph{dispersion} or self-assessed confidence---verbalized confidence \citep{Lin2022, Tian2023}, self-consistency vote-margin \citep{Wang2022}, Kadavath's P(True) \citep{Kadavath2022}, semantic entropy \citep{Kuhn2023, Farquhar2024}, SelfCheckGPT \citep{Manakul2023}. A high-confidence, self-consistent fabrication reads as ``certain'' to every one of them. The second recognized defense is a \emph{query-side false-premise verifier}---a detect-then-respond check that asks whether the question's presupposition holds. We benchmark both families and report, decisively, that neither suffices where the structural certificate does, because the verifier inherits the very error it is meant to catch.

[FIGURE:fig1]

\textbf{What we contribute, and the one honest concession.} We do \emph{not} claim the repair mechanism as novel. Keeping the LLM a high-recall disjunctive reader, composing only through an exact finite composition table, and abstaining when iterated closure leaves a disjunction or collapses to the empty set is the \emph{inherited neuro-symbolic premise}; by our own decomposition it is worth $+0.673$ inherited versus $+0.0025$ novel on selective accuracy [ARTIFACT:art_D0cHQUJ8kY75]. The genuinely new content is (1) a \emph{compositional false-premise diagnostic}: confident absent-relation fabrication, documented single-hop, becomes at the compositional/document level a false-premise failure that transfers across corpora, domains, and readers, against which no single confidence threshold can both cover present pairs and abstain on absent ones (the \emph{capability gap}); and (2) a demonstration that a \emph{gold-free, training-free, no-external-KB} structural detector---the no-derivation certificate---catches these fabrications where the confidence family \emph{and} a query-side false-premise verifier do not.

\textbf{The decisive test, and the honest boundary.} A skeptical reviewer rightly observed that the certificate's near-zero confident-wrong on CLUTRR absent pairs is structural-by-construction: CLUTRR absent pairs are \emph{defined} as entities in different connected components, so a sound closure abstains almost by definition. We accept this and never let that number carry the contribution. To answer it, we run the certificate on a natural regime where abstention is a \emph{non-trivial} deductive result: the \emph{same-component sibling} containment regime of a Re-DocRED \emph{located-in} corpus, where two places lie in one connected component and share a containing parent but neither contains the other, so closure derives the empty set because the composition cell $\textsf{located\_in}\circ\textsf{contains}$ is undefined. This regime is decisive because (i) the raw reader fabricates a containment on $30\%$ of sibling pairs versus only $6\%$ of different-component pairs, and (ii) a relatedness verifier is \emph{actively fooled} by the shared parent. There, at matched coverage, the certificate turns $78.5\%$ of the raw LLM's high-confidence fabrications into abstentions, versus $\leq 40\%$ for every dispersion signal, $27.4\%$ for a same-model query-side verifier, and $10\%$ for a \emph{stronger cross-family} verifier [ARTIFACT:art_l3mUIdHiAufv][ARTIFACT:art_4xy3D05YxvRr]. We report the boundary without spin: the certificate's \emph{full mixed-pool net utility}---abstaining on absent pairs without over-abstaining on present ones---is demonstrated only on clean/templated CLUTRR; on natural prose it is gated by extraction recall ($0.148$ located-in, $0.376$ kinship). A controlled extraction-recall sweep shows this boundary is \emph{fundamental for prompt-only extraction}: every prompt strategy that raises recall does so by buying precision, injecting false edges that make the certificate fabricate sibling paths, so net utility moves \emph{further} from a win as recall rises [ARTIFACT:art_fXvxt4JO9hWy]. A gold-read ceiling of $1.0/1.0/1.0$ locates the entire deployment headroom in extraction, not closure.

\begin{table}[t]
\centering
\small
\begin{tabular}{p{2.05cm}p{1.5cm}p{1.5cm}p{1.45cm}}
\hline
Claim & Evidence & Where & Status \\
\hline
\textbf{Compositional false-premise diagnostic (FACT~A + signal-agnostic capability gap)} & \textsc{real-read} (2 corpora, 2 domains, 3 readers) & \S\ref{sec:diagnostic} & \textbf{Robust; gap powered on clean graph} \\
Structural certificate $>$ confidence battery \emph{and} query-side verifier (catching objective) & \textsc{real-read} & \S\ref{sec:verifier}, \S\ref{sec:locatedin} & \textbf{Confirmed, incl.\ stronger cross-family verifier} \\
Net mixed-pool utility & \textsc{real-read} & \S\ref{sec:boundary} & Clean graph: yes; natural prose: extraction-gated \\
Boundary is fundamental for prompt-only extraction (recall--precision frontier) & \textsc{real-read} & \S\ref{sec:boundary} & \textbf{New: confirmed, both domains} \\
Closure/abstain mechanism is inherited & \textsc{decomp} & \S\ref{sec:diagnostic}, App.~\ref{sec:mechanism} & Conceded ($+0.673/{+}0.0025$) \\
Cross-path coding synthetic-only & \textsc{gold-gate}+\textsc{synth} & \S\ref{sec:crosspath} & Resolved negative \\
\hline
\end{tabular}
\caption{The paper's spine. Evidence-class tags are columns, not inline hedging. \textsc{real-read}: a real LLM reads natural(istic) text. \textsc{gold-gate}: zero-LLM structural gate over verified gold. \textsc{synth}: synthetic channel. \textsc{decomp}: zero-spend re-analysis.}
\label{tab:spine}
\end{table}

## Summary of Contributions

\begin{itemize}
\item \textbf{A compositional false-premise diagnostic with a signal-agnostic capability gap} (Section~\ref{sec:diagnostic}). The raw LLM fabricates absent relations at high confidence in a tight $30$--$48\%$ band across CLUTRR and Re-DocRED, kinship and containment, and three readers (FACT~A)---consistent with, and lifting to the compositional level, the single-hop RE over-prediction documented by \citet{Yang2025DEPTH}. A $16$-cell per-signal $\times$ reader $\times$ corpus \emph{caught} table shows the fraction a confidence threshold catches swings from $\sim$$15\%$ to $\sim$$90\%$ by reader, so blindness is \emph{not} family-level; the reader-invariant spine is the mixed-pool capability gap, powered on CLUTRR (certificate selective accuracy $0.827$ vs.\ $0.37$--$0.44$; Holm-adjusted confident-wrong reductions $0.103$--$0.121$, all CIs exclude $0$) [ARTIFACT:art_Kq_ROSdyIqPU].
\item \textbf{A query-side false-premise verifier baseline---same-model and stronger cross-family---which the certificate beats} (Section~\ref{sec:verifier}). Against the recognized detect-then-respond method for this failure mode, the certificate catches strictly more confident fabrications on both kinship venues ($0.941/0.850$ vs.\ verifier $0.588/0.100$; caught-gap CIs exclude $0$), because the verifier inherits the generating model's confident error [ARTIFACT:art_963U_7mCLAMJ]. A larger, different-family verifier (deepseek-v3.2, $k{=}5$) does \emph{worse} ($0.10$ caught on located-in siblings), so the result is not an artifact of a weak same-model verifier [ARTIFACT:art_fXvxt4JO9hWy].
\item \textbf{The decisive non-by-construction test, scored by the matched-coverage-fair caught fraction} (Section~\ref{sec:locatedin}). On Re-DocRED located-in \emph{same-component sibling} pairs, the certificate catches $\mathbf{0.785}$ of high-confidence fabrications vs.\ verbalized $0.400$, P(True) $0.304$, query-side verifier $0.274$, self-verify $0.459$, sc-margin / semantic-entropy $0.067$; all six certificate-minus-competitor caught-gaps exclude $0$ (doc-clustered paired bootstrap $B{=}10000$) [ARTIFACT:art_4xy3D05YxvRr].
\item \textbf{An honest extraction-limited boundary, sharpened into a recall--precision frontier} (Section~\ref{sec:boundary}). The mixed-pool win does not transfer to natural prose (extraction recall $0.376$ kinship / $0.148$ containment); a gold-read ceiling ($1.0/1.0/1.0$) isolates extraction. A controlled sweep of $\geq 6$ prompt-only extractors shows recall is precision-bought: the worst-case mixed-pool confident-wrong \emph{reduction} is a monotone-decreasing function of recall (CI-lower-vs-recall slope $-0.30$ located-in / $-0.67$ kinship), so no prompt strategy flips the boundary---it requires precision-preserving (fine-tuned) extraction [ARTIFACT:art_fXvxt4JO9hWy].
\item \textbf{An end-to-end SWI-Prolog-executed CLUTRR pipeline} delivering atomic P/R, multi-hop accuracy, trace-graphs, and absent-relation safety (Section~\ref{sec:clutrr}), plus honest boundaries: fuzzy unification is a feasibility note (Section~\ref{sec:fuzzy}); cross-path coding is synthetic-only (Section~\ref{sec:crosspath}); natural temporal text is only weakly protective (Section~\ref{sec:temporal}).
\end{itemize}

# Related Work
\label{sec:related}

\textbf{Confident absent-relation fabrication in relation extraction.} Confident \emph{absent}-relation fabrication is a documented RE phenomenon: LLM extractors over-predict relations on entity pairs that bear none. \citet{Yang2025DEPTH} measure a $96.9\%$ relation rate on \textsc{no-relation} pairs in SciERC and counter it with dependency-aware sentence simplification, hierarchical refinement, and a causality-driven RLHF reward model; \citet{Li2024RelClassifier} trace the document-level LLM gap to ``the dispersion of attention by LLMs due to entity pairs without relations'' and pre-filter candidate pairs with a trained classifier on DocRED/Re-DocRED; \citet{Pi2025RelPrior} likewise filter ``unrelated entity pairs [that] introduce noise'' with a binary relation prior. All three target a \emph{single-hop, schema-bound} ``no label for this pair'' decision solved by better extraction, refinement, or filtering, not a verdict over \emph{composed} edges. The closest structural detectors verify premises against \emph{external} knowledge: \citet{Qin2026PremiseVerification} validate each premise of a logicalized query by retrieval-augmented generation over factual sources (training-free and logits-free, but KB-dependent), and \citet{Sansford2024GraphEval} check response triples against the \emph{provided context} with a trained NLI model. The unanswerable / false-premise line \citep{Hu2023, Kirichenko2025, Wen2024, Kim2022, Yu2022} addresses sentence-level presuppositions with trained or prompt-based detectors. None of these targets a \emph{compositional, multi-hop, document-internal} absent-relation premise detected \emph{gold-free, training-free, and without any external KB} by deductive closure---the gap this paper fills. \textbf{Our two-part delta.} \emph{Setting}: we lift absent-relation detection from a single-hop, schema-bound \textsc{no\_relation} classification \citep{Yang2025DEPTH, Li2024RelClassifier, Pi2025RelPrior} and a sentence-level false premise \citep{Hu2023, Kim2022, Yu2022} to the structural claim that ``a derivation path exists between $X$ and $Y$.'' \emph{Method}: we detect it with a gold-free, training-free, no-external-KB deductive-closure certificate (no path $\Rightarrow$ abstain), versus trained RE refiners/classifiers, external-KB/RAG premise verification \citep{Qin2026PremiseVerification}, and NLI-vs-context triple checks \citep{Sansford2024GraphEval} [ARTIFACT:art_mxFG0bGhTe2-].

\textbf{Abstention by confidence vs.\ abstention by structure.} The selective-prediction family \citep{Geifman2017, Lin2022, Tian2023, Wang2022, Kadavath2022, Kuhn2023, Farquhar2024, Manakul2023} thresholds a dispersion or self-confidence scalar. We make the contrast empirical (Sections~\ref{sec:diagnostic}--\ref{sec:locatedin}) rather than asserted, and keep scope honest: on ordinary single-path deduction, where dispersion \emph{is} informative, the confidence baselines tie or beat the certificate (Section~\ref{sec:boundary}). We additionally instantiate the recognized query-side method---self-ask decomposition \citep{Press2022}, self-verification \citep{Weng2022}, and P(True) self-evaluation \citep{Kadavath2022}---as an explicit baseline (Section~\ref{sec:verifier}) and show the certificate beats it.

\textbf{Consistency enforcement under the commit contract.} A zero-shot study reports that ILP consistency enforcement does not raise F1 \citep{Kougia2024}; the most recent global temporal-graph generator still ILP-commits to one label per pair \citep{Eirew2025}. Our closest neuro-symbolic neighbors all retain a commit objective: NeSTR repairs inconsistencies toward a single conclusion \citep{Liang2025}; TReMu generates and commits code over dialogue memory \citep{Ge2025}; Fan and Strube's discourse extractor pairs Allen-algebra prompts with reflection to commit one F1-maximizing label \citep{Fan2025}; GDLLM classifies one relation per pair \citep{Zhao2025}. METRE trains a multi-label head to model ambiguity \citep{Hu2024} but is F1-trained, carries no set through a composition table across paths, and does not abstain. ``When Silence Is Golden'' targets temporal abstention but \emph{trains} it via chain-of-thought supervision \citep{Zhou2026}; ours is structural and training-free. BeDiscovER is a discourse \emph{evaluation} suite \citep{Li2025}. None preserves a disjunction \emph{and} abstains on closure-collapse with a gold-free per-edge certificate.

\textbf{Closure over machine-extracted relations.} SputLink computes temporal closure to densify TimeBank \citep{Verhagen2005}; CAEVO does global inference by cascaded sieves \citep{Chambers2014}; structured learning enforces transitivity \citep{Ning2017}. All commit to one consistent labeling, preserve no disjunction, certify no reading error, and do not abstain. SputLink-style closure \emph{produces} the non-adjacent gold whose circularity we avoid by using direct human-timeline gold \citep{Rogers2019, Cassidy2014} and manual long-distance gold \citep{Naik2019}.

\textbf{Qualitative reasoning and LLM reasoning.} Allen's interval algebra \citep{Allen1983}, the convex point algebra \citep{Vilain1986}, RCC-8 \citep{Randell1992}, and the cardinal-direction calculus \citep{Frank1996, Ligozat1998} supply exact tables; Mackworth's path consistency \citep{Mackworth1977} iterates length-2 intersections to a fixpoint. Path consistency is \emph{complete} for the convex point algebra and ORD-Horn \citep{Nebel1994} but only \emph{sound-but-incomplete} for full Allen IA and RCC-8 \citep{Renz1999}; we import these facts (our point arm is exact; Allen and RCC-8 arms are sound lower bounds). Chain-of-thought \citep{Wei2022} and self-consistency \citep{Wang2022} operate at the answer level; Logic-LM self-refines on solver crashes \citep{Pan2023} and LINC majority-votes formalizations \citep{Olausson2023}, but none maintains a positive global invariant over relational knowledge. Path-of-Thoughts \citep{Zhang2024} and backward chaining \citep{Kazemi2022} reason each path independently. Inducing composition rules to fit task accuracy \citep{Zhang2023, Zhu2023} optimizes data fit rather than the algebraic laws needed for soundness. The discourse-level reading prompts of \citet{Wei2024} ground our span-local protocol; RuleTaker \citep{Clark2020} targets propositional entailment; Reiter's diagnosis \citep{Reiter1986} supplies the hitting-set machinery for the Mode-B repair we scope as future work; hallucination in generation is a broad concern \citep{Ji2022}. For the spatial venue we use SpaRTUN-style RCC-8 scenes \citep{Mirzaee2022}, with SpartQA \citep{Mirzaee2021} and StepGame \citep{Shi2022} as structural contrasts; the natural absent-relation corpora are built from Re-DocRED \citep{Tan2022}, the completeness-corrected re-annotation of DocRED \citep{Yao2019}.

# Method
\label{sec:method}

## The inverted output contract

The deduction module sits downstream of atomic extraction: it receives, for each pair of mentions co-occurring in a span, the relation the text licenses, and must answer queries about pairs that do \emph{not} co-occur. We model the relations as a Qualitative Constraint Network (QCN): nodes are events/entities, each edge carries a \emph{set} of base relations from a finite composition system $\mathcal{A}$ (the disjunction the evidence does not exclude), and the held-out query edge starts at the universal set. Three commitments define the contract. First, the LLM is a \emph{disjunctive, high-recall reader}: for each span it emits the maximal sound set the text does not exclude, with an explicit universal/underdetermined option, rather than committing to one relation. Second, composition and converse come from the \emph{exact published table} of $\mathcal{A}$, never from the LLM. Third, the system narrows by closure and \emph{abstains} when the query edge remains a non-singleton, and \emph{flags an unsound read} when it collapses to the empty set. Table~\ref{tab:notation} fixes notation.

\begin{table}[t]
\centering
\small
\begin{tabular}{ll}
\hline
Symbol / term & Meaning \\
\hline
$\mathcal{A}$ & composition system (point:3; RCC-8:8; Allen:13; kinship/located-in: finite tables) \\
$r$ & per-edge recall, $P(\text{gold}\in\text{emitted set})$ \\
no-derivation & query unreachable by any composition path \\
FACT~A & raw-LLM confident absent-relation fabrication rate \\
caught & fraction of fabrications a method turns into abstention ($1-$survival) \\
capability gap & no scalar threshold both covers present and abstains on absent \\
sibling-absent & same component, share a parent, no valid derivation path \\
diffcomp-absent & different components (structural-by-construction absence) \\
confident-wrong (CW) & a committed (non-abstained) answer $\neq$ gold \\
matched cov. & every method scored at the same single-relation resolution rate \\
\hline
\end{tabular}
\caption{Notation and metrics used throughout.}
\label{tab:notation}
\end{table}

## Two value modes

\textbf{Mode~A (sound narrowing and no-derivation abstention).} Composing the LLM's per-edge sets through the exact table and intersecting at the query pair, the system emits iff the result is a singleton, abstains iff a disjunction remains, and---the load-bearing case---abstains with ``no relation'' iff \emph{no} composition path reaches the query. The intersection of sound sets is always sound, so under all-sound inputs Mode~A's output contains gold with probability exactly $1.0$; this survives path-consistency incompleteness. \textbf{Mode~B (detection).} An empty closure is a deductive certificate that some contributing read is unsound, with no gold labels. Both modes carry the \emph{silent-wrong-narrowing} dual: if gold is \emph{omitted} from a contributing set (recall failure), closure can narrow to a confident wrong singleton with no collapse---bounded per-edge by $(1-r)$.

## The definitional half, stated once; the empirical half, led with

A high-confidence, self-consistent fabrication survives \emph{any} dispersion threshold \emph{by construction}: if the model commits an absent relation with maximal confidence and zero answer-dispersion, no threshold tuned on that dispersion can single it out. This is definitional and needs no experiment. The \emph{empirical}, non-obvious questions---which we lead with---are: \emph{how often} the LLM emits absent-relation fabrications at high confidence, and \emph{how strongly that fraction varies by reader}. The reader-invariant claim that survives is geometric: a single scalar knob cannot separate confident-and-right (present) from confident-and-wrong (absent) when the LLM emits both at the same confidence, whereas a structural certificate separates them by whether a derivation path exists.

## Baselines: confidence battery and query-side false-premise verifiers

Every certificate comparison includes two baseline families thresholded to the \emph{same} single-relation coverage object. (1) A \emph{confidence-thresholded raw-abstain} battery: (a) verbalized confidence; (b) self-consistency vote-margin over $k{=}10$ samples; (c) Kadavath's P(True); (d) semantic-entropy negentropy over $k{=}10$ relation-clustered samples [ARTIFACT:art_LeRQRGHJZcdQ]. (2) The recognized method for this failure mode: a \emph{query-side false-premise verifier}. We run two prompt-based, zero-training variants on the \emph{same} reader---a \textsc{relatedness} verifier (``are $X$ and $Y$ related by $\langle$kinship$|$containment$\rangle$ at all?'' $\rightarrow$ abstain on \textsc{unrelated}) and a \textsc{self-verify} pass on the committed answer [ARTIFACT:art_oUhZgMSjf7lm]---and, to forestall the objection that this is merely a weak same-model proxy, a \emph{stronger cross-family} verifier (deepseek-v3.2 with $k{=}5$ self-consistency) [ARTIFACT:art_fXvxt4JO9hWy]. The certificate's claim is credible only if it matches or beats these verifiers at matched coverage; otherwise we report an honest negative.

## Two absent regimes (the decisive design choice)

A natural absent-relation pair can be absent for two structurally different reasons. \emph{Different-component} absence: the two entities lie in disjoint connected components, so a sound closure derives the empty set \emph{almost by definition}---abstention is structural-by-construction and carries no evidential weight. \emph{Same-component sibling} absence: the two entities lie in one connected component and share a containing parent, but no valid derivation path links them (e.g.\ two places in one region where neither contains the other, so the only relevant composition cell, $\textsf{located\_in}\circ\textsf{contains}$, is undefined). The certificate's abstention here is \emph{still} a structural no-path determination, but a \emph{non-trivial} one: it requires the composition table, not mere disconnection. The sibling regime is decisive not because the abstention stops being structural but because (i) the raw reader fabricates a containment on $30\%$ of sibling pairs versus only $6\%$ of different-component pairs, and (ii) a relatedness verifier is \emph{fooled} by the shared parent into asserting a relation [ARTIFACT:art_RfjDpsGkBXDG].

## Genuine fuzzy unification, bounded by the certificate (feasibility note)

We substantiate the ``fuzzy unification'' framing only as a feasibility note: a known relation is rendered with a \emph{vague} preposition (\textsf{near}, \textsf{around}) or an \emph{informal} kinship term (\textsf{guardian}, \textsf{family elder}), and the LLM emits a calibrated disjunction over a \emph{known} base vocabulary, into which the abstain-on-collapse certificate runs unchanged. This is explicitly not upper-ontology grounding and not open-vocabulary predicate invention.

## Datasets and metrics

\textbf{Templated end-to-end venue.} CLUTRR kinship \citep{Sinha2019}, standardized to gold graphs with typed atomic edges, held-out multi-hop queries (hops $2$--$10$), and within-document absent pairs [ARTIFACT:art_HS7-lxhZnU9m]; template-generated, short ($\leq 871$ chars). \textbf{Natural absent-relation corpora.} Re-DocRED \citep{Tan2022} kinship [ARTIFACT:art_NUWTxBVWENIJ] and geographic/administrative \emph{located-in} containment [ARTIFACT:art_RfjDpsGkBXDG], the latter carrying the same-component-sibling regime. \textbf{Natural temporal corpora.} NarrativeTime \citep{Rogers2019, Cassidy2014}, TDDMan \citep{Naik2019}, MATRES \citep{Ning2018} [ARTIFACT:art_PNrS9T8JeATf]. \textbf{Spatial venue.} SpaRP-PS1 RCC-8 scenes \citep{Mirzaee2022} [ARTIFACT:art_f-ofxduZjwSM]. \textbf{Synthetic backbone.} Globally-consistent QCNs over point, Allen, RCC-8 [ARTIFACT:art_ghVQmxVlmOJJ]. \textbf{Metrics}: FACT~A; per-signal\,$\times$\,reader\,$\times$\,corpus \emph{caught} fraction (matched-coverage-fair, same denominator); mixed-pool selective accuracy at matched coverage; confident-wrong rate \emph{always reported with coverage}; atomic P/R (held-fixed control); and, for fuzzy reads, expected calibration error (ECE).

# Experimental Setup
\label{sec:setup}

Readers are \texttt{google/gemini-3.1-flash-lite} (primary, temperature $0$) and, for cross-family checks, \texttt{deepseek/deepseek-v3.2} and \texttt{mistralai/mistral-small-2603}; all LLM calls use a SHA-256 disk cache and a hard cost guard. Two zero-spend reproduction gates underpin the carried literals: an $80/80$-check re-analysis of the CLUTRR and natural-kinship batteries ($62$ genuinely recomputed) [ARTIFACT:art_Kq_ROSdyIqPU], and a $68/68$-check re-analysis that recomputes every located-in / verifier literal from the per-query rows and hard-asserts equality with the carried aggregates [ARTIFACT:art_4xy3D05YxvRr]. A separate $32/32$ gate confirms the rebuilt CLUTRR/Re-DocRED pools are byte-identical to the published pools before any new spend [ARTIFACT:art_963U_7mCLAMJ]. Story-/document-clustered paired bootstraps use $B{=}10000$, Holm-adjusted. The QCN engine is unit-test gated: the Allen $169$-cell and RCC-8 $64$-cell tables match published cells with $0$ failures, convex-point completeness is confirmed against brute force, and an iteration-isolation test confirms \textsc{full}$=$\textsc{naive} at length $2$ and \textsc{full}$\neq$\textsc{naive} on $3$-hop chains. The located-in run reads $1{,}215$ queries over $283$ documents ($515$ present $=$ $400$ held-out $+$ $115$ never-annotated; $450$ sibling-absent; $250$ different-component-absent) at $\sim$\$$2.66$; the extraction-recall sweep adds $\geq 6$ extraction strategies and the stronger cross-family verifier for a one-time $\$1.21$; the kinship verifier run adds verifier/self-verify calls at \$$0.14$; the CLUTRR battery \$$0.30$; the natural-kinship run $\sim$\$$1.5$; cached re-runs \$$0$.

# Results

## The compositional false-premise diagnostic (\textsc{real-llm-read})
\label{sec:diagnostic}

\textbf{FACT~A is robust across corpora, domains, and readers.} The raw LLM commits a confident absent-relation answer on a tight band of absent pairs: CLUTRR $47.2\%$ (gemini) / $48.3\%$ (deepseek); Re-DocRED kinship $32.6\%$ / $31.8\%$; Re-DocRED located-in sibling pairs $30.0\%$ (gemini, mean confidence $0.94$, $94.8\%$ at confidence $\geq 0.9$) / $43.8\%$ (mistral) [ARTIFACT:art_Kq_ROSdyIqPU][ARTIFACT:art_l3mUIdHiAufv]. This is the same over-prediction \citet{Yang2025DEPTH} document single-hop ($96.9\%$ on SciERC \textsc{no-relation} pairs), measured here at the \emph{compositional, document-internal} level and shown to transfer across corpora and reader families; the contribution is the reframing and its transfer, not the existence of the rate.

[FIGURE:fig2]

\textbf{Whether a confidence signal can filter them is reader- and signal-dependent.} Table~\ref{tab:caught} reports, for each of four signals $\times$ two readers $\times$ two corpora, the fraction of fabrications a certificate-matched rule \emph{catches}. The fraction swings from $\sim$$15\%$ (Re-DocRED/gemini, sc\_margin and negentropy) to $\sim$$90\%$ (CLUTRR/deepseek, P(True)): a practitioner using deepseek with self-consistency vote-margin already filters $\sim$$78\%$. We therefore do \emph{not} claim family-level, reader-invariant blindness. The ``no signal removes a single fabrication'' statement holds \emph{only} at the LLM's natural (no-abstention) coverage; at the certificate's coverage P(True) already catches $75.3\%$ on CLUTRR and $51.7\%$ on natural Re-DocRED (gemini). Verbalized confidence is the most robustly blind.

\begin{table}[t]
\centering
\small
\begin{tabular}{llccccc}
\hline
Corpus & Reader & FACT~A & verb. & sc\_marg. & P(True) & negent. \\
\hline
CLUTRR & gemini & 0.472 & 0.565 & 0.282 & \textbf{0.753} & 0.282 \\
CLUTRR & deepseek & 0.483 & 0.328 & 0.776 & \textbf{0.897} & 0.776 \\
Re-DocRED & gemini & 0.326 & 0.492 & 0.150 & 0.517 & 0.150 \\
Re-DocRED & deepseek & 0.318 & 0.588 & 0.706 & 0.676 & 0.706 \\
\hline
\end{tabular}
\caption{The $16$-cell per-signal $\times$ reader $\times$ corpus table of fraction \emph{caught} ($=1-$survival) (\textsc{real-llm-read}). FACT~A (fabrication rate) is reader-robust in a $0.32$--$0.48$ band; the \emph{caught} fraction swings $\sim$$15\%$ to $\sim$$90\%$ by reader, so confidence-blindness is \emph{not} family-level. The spine is therefore the signal-agnostic capability gap, not per-signal blindness.}
\label{tab:caught}
\end{table}

\textbf{The signal-agnostic capability gap (the spine), powered on CLUTRR.} On a mixed present/absent pool ($n{=}282$) so abstaining-on-everything cannot win, at matched coverage $0.266$ the certificate's selective accuracy is $0.827$ versus verbalized $0.413$, sc\_margin $0.373$, P(True) $0.440$, negentropy $0.373$---roughly double every signal. Certificate-versus-signal confident-wrong reductions are $0.110$ (verbalized, Holm $p_{\text{adj}}{=}0.0004$), $0.121$ (sc\_margin, $0.0027$), $0.103$ (P(True), $0.0027$), $0.121$ (negentropy, $0.0027$), all Holm-adjusted CIs excluding $0$ [ARTIFACT:art_Kq_ROSdyIqPU]. A single neural threshold cannot simultaneously abstain on absent pairs and cover present ones; the certificate does both because its signal is structural. We are explicit that this capability gap is currently \emph{powered only on clean templated CLUTRR}; Sections~\ref{sec:locatedin}--\ref{sec:boundary} test it on natural prose.

## A query-side false-premise verifier is not enough (\textsc{real-llm-read})
\label{sec:verifier}

The recognized method for false-premise abstention is a query-side verifier, not a dispersion threshold on a forced answer. We therefore ask the disconfirming question directly: does a ``are $X$ and $Y$ related at all?'' verifier (or a self-verification pass) recover the certificate's safety without the closure engine? On the absent-relation \emph{fabrication} set (the pairs the raw LLM confidently committed), the fraction \emph{caught} is, certificate vs.\ verifier vs.\ self-verify vs.\ best dispersion signal: CLUTRR $0.941$ / $0.588$ / $0.824$ / $0.753$; Re-DocRED $0.850$ / $0.100$ / $0.542$ / $0.517$ [ARTIFACT:art_963U_7mCLAMJ]. The certificate catches \emph{strictly more} than the verifier on both venues (doc-clustered paired bootstrap $B{=}10000$; caught-gap $0.353$, CI $[0.187,0.510]$, and $0.750$, CI $[0.620,0.848]$, both excluding $0$, $p\leq 0.002$). The mechanism is the point: the verifier runs on the \emph{same} LLM that hallucinated, so when the reader confidently invents ``$Y$ is $X$'s sister'' on an unrelated pair, asking ``are $X$ and $Y$ related?'' returns \textsc{related} at confidence $1.0$---it inherits the generation error---whereas the certificate's abstention is independent of the LLM's confidence.

[FIGURE:fig5]

\textbf{A stronger verifier does not close the gap (methodology).} We scope the necessity claim precisely to \emph{a same-model prompt-based} query-side verifier, then test whether a stronger one helps. On located-in siblings, a \emph{larger, different-family} verifier (deepseek-v3.2 with $k{=}5$ self-consistency) catches only $0.10$ of the raw LLM's confident containment fabrications---\emph{worse} than the same-model weak verifier ($0.274$) and far below the certificate ($0.785$)---because a better geographer \emph{over-infers} containment between co-regional places [ARTIFACT:art_fXvxt4JO9hWy]. Certificate-necessity is therefore not an artifact of using a weak same-model verifier; the failure is intrinsic to running the premise check on a generative LLM.

## The decisive non-by-construction test: located-in same-component siblings (\textsc{real-llm-read})
\label{sec:locatedin}

We run the four-signal battery, the query-side verifiers, and the certificate on a \emph{second} natural domain---Re-DocRED geographic containment---and, decisively, on the \emph{same-component sibling} regime. A worked example: a Re-DocRED biography states that the A~Sầu Valley is located in Thừa~Thiên-Huế Province (located in Vietnam) and is bisected by Route~548; asked ``what is the geographic relationship of the valley to Route~548?'', the gold is \textsf{no-relation} ($\textsf{located\_in}\circ\textsf{bisected-by}$ is undefined). The raw reader names a containment at high confidence; the certificate composes the extracted edges, finds no derivation reaching the pair, and abstains.

\textbf{The caught fraction is the matched-coverage-fair headline.} On the $450$ sibling-absent pairs, FACT~A is $30\%$, so $135$ pairs carry a high-confidence fabrication. Of those, the fraction each method turns into an abstention---computed on the \emph{same denominator}, the certificate's matched-coverage comparison---is: certificate $\mathbf{0.785}$, self-verification $0.459$, verbalized $0.400$, P(True) $0.304$, query-side verifier $0.274$, sc\_margin $0.067$, semantic-entropy $0.067$ (Table~\ref{tab:locatedin}). A new doc-clustered paired bootstrap ($B{=}10000$) confirms all six certificate-minus-competitor caught-gaps exclude $0$ [ARTIFACT:art_4xy3D05YxvRr]. Under \texttt{mistral} the result is reader-general: FACT~A on siblings is $0.438$ and the certificate still catches $\sim$$78\%$.

[FIGURE:fig3]

\textbf{Why we do not headline a confident-wrong ``reduction.''} On a \emph{pure-absent} pool every committed (named) answer is wrong, so each method's confident-wrong rate equals its coverage. The certificate's natural confident-wrong is $0.073$ (it abstains on $92.7\%$) versus $0.30$ for the raw reader and every dispersion signal at its natural operating point, $0.218$ for the verifier, and $0.162$ for self-verify. The apparent ``$0.227$ reduction at matched coverage'' is therefore \emph{mechanically} $0.30-0.073$---a difference of abstention rates, not a risk-coverage selective-accuracy gain---and we deliberately do \emph{not} present it as the headline; on a pure-absent pool a confident-wrong reduction is uninformative without matched coverage. The genuinely fair, matched-denominator comparison is the caught fraction above [ARTIFACT:art_4xy3D05YxvRr].

\begin{table}[t]
\centering
\small
\begin{tabular}{lcc}
\hline
Method & caught$^\dagger$ & nat.\ CW$^\ddagger$ \\
\hline
\textbf{Certificate (structural)} & \textbf{0.785} & \textbf{0.073} \\
self-verification & 0.459 & 0.162 \\
verbalized confidence & 0.400 & 0.300 \\
P(True) & 0.304 & 0.300 \\
query-side verifier (same model) & 0.274 & 0.218 \\
sc\_margin & 0.067 & 0.300 \\
semantic-entropy & 0.067 & 0.300 \\
query-side verifier (stronger, x-family) & 0.100 & 0.220 \\
raw (commit) & 0.000 & 0.300 \\
\hline
\end{tabular}
\caption{The decisive non-by-construction test: Re-DocRED located-in \emph{same-component sibling} pairs ($n{=}450$, FACT~A $0.30$) (\textsc{real-llm-read}). $^\dagger$Caught $=$ fraction of the raw LLM's high-confidence fabrications turned into an abstention; this is the matched-coverage-fair (same-denominator) comparison and all six certificate-minus-competitor gaps exclude $0$. $^\ddagger$Natural confident-wrong $=$ coverage on this pure-absent pool; reported as the certificate's abstaining operating point ($0.073$) vs.\ each baseline at its natural operating point, \emph{not} as a matched-coverage gain.}
\label{tab:locatedin}
\end{table}

## The honest boundary: net utility is extraction-limited, and the boundary is fundamental (\textsc{real-llm-read})
\label{sec:boundary}

The catching-objective win above asks: among queries the raw LLM would answer with a fabrication, what fraction does the method abstain on? A second, stricter objective is \emph{net utility}: on a mixed pool of present and absent queries, improve selective accuracy at matched coverage---abstain on absent \emph{without} over-abstaining on present. Net utility additionally requires high present coverage, which depends on extraction recall, and here the certificate is gated. On Re-DocRED kinship, the certificate-versus-signal mixed-pool confident-wrong reductions are $-0.055$, $-0.034$, $-0.047$, $-0.034$ (vs.\ verbalized, sc\_margin, P(True), negentropy), doc-clustered CIs all including $0$, Holm rejecting none; mixed selective accuracy is certificate $0.475$ vs.\ signals $0.60$--$0.675$ [ARTIFACT:art_htcr8yOZLCQy]. On located-in, present coverage collapses to $0.05$ because containment extraction recall is only $0.148$ (precision $0.665$; $0.243$ against the locally-justifiable span-extractable subset), so the certificate over-abstains on $94.9\%$ of present pairs [ARTIFACT:art_l3mUIdHiAufv]. A gold-read ceiling settles attribution: closure over \emph{gold} atomic edges (queried edge ablated) reproduces $100\%$ of present golds and abstains on $100\%$ of absent pairs (present selective accuracy $1.0$), so the gap to the LLM-read certificate \emph{is} the extraction ceiling, not the closure logic.

\textbf{The boundary is fundamental for prompt-only extraction (new).} A natural question is whether a better extractor flips this boundary. We swept $\geq 6$ prompt-only extraction strategies above the default floor---few-shot enumeration with an explicit no-omission inventory, sentence-by-sentence reading with coreference, self-consistency union over $k{=}4$ samples, and multi-model union (gemini $\cup$ mistral)---plus high-precision variants requiring source agreement \emph{and} a cue phrase [ARTIFACT:art_fXvxt4JO9hWy]. The strongest strategy \emph{measurably} raises recall (located-in $0.148\rightarrow0.227$; kinship $0.376\rightarrow0.396$) and lifts the certificate's present coverage $\sim$$3\times$ ($0.051\rightarrow0.165$; corr$(\text{recall},\text{present cov})=0.96$). But the recall is \emph{precision-bought}: corr$(\text{recall},\text{sibling confident-wrong})=0.91$, because every extra edge that lifts coverage also injects false edges that make the certificate fabricate sibling paths. Consequently the worst-case (min-over-six-competitors) mixed-pool confident-wrong \emph{reduction} is a \emph{monotone-decreasing} function of recall (CI-lower-vs-recall slope $-0.30$ located-in / $-0.67$ kinship); the reduction-optimal operating point is the highest-precision, \emph{lowest}-recall strategy, and no prompt-only strategy flips the fork on either domain, as the recall--precision frontier below shows. The default strategy reproduces the headline operating point exactly (recall $0.148$, present coverage $0.051$, sibling confident-wrong $0.073$); the gold-read ceiling stays $1.0/1.0/1.0$ throughout. The deployment headroom is therefore real but \emph{not promptable}: closing it requires a precision-preserving (fine-tuned) extractor, not a better prompt. We separate, deliberately, the contribution---a corpus-, domain-, and reader-robust diagnostic plus a structural detector that wins the catching objective off the by-construction stratum---from the deployment caveat, whose cause we now localize quantitatively to extraction recall.

[FIGURE:fig4]

\begin{table}[t]
\centering
\small
\begin{tabular}{lccc}
\hline
Quantity & CLUTRR & Re-DocRED & located-in \\
 & (templ.) & kinship & sibling \\
\hline
FACT~A (gemini) & 0.472 & 0.326 & 0.300 \\
caught: certificate & struct. & 0.850 & \textbf{0.785} \\
caught: best dispersion & 0.753 & 0.517 & 0.400 \\
caught: query verifier & 0.588 & 0.100 & 0.274 \\
nat.\ CW certificate & 0.028$^\S$ & 0.071 & 0.073 \\
\hline
mixed sel.\ acc.\ cert. & \textbf{0.827} & 0.475 & 0.441 \\
mixed cert.\ CW redux & $+.10/+.12$ & $-.03/-.06$ & degen.$^\P$ \\
\quad Holm rejects? & yes & no & no \\
atomic recall & 0.532 & 0.376 & 0.148 \\
present cov.\ (LLM) & high & 0.483 & 0.050 \\
gold-read present cov. & --- & 1.000 & 1.000 \\
\hline
\end{tabular}
\caption{Catching objective vs.\ net-utility objective across venues (\textsc{real-llm-read}). The certificate wins the catching objective everywhere, including the non-by-construction located-in sibling regime, and beats the query-side verifier. The mixed-pool \emph{net-utility} win is powered only on clean CLUTRR; on natural prose extraction recall ($0.376$/$0.148$) binds and the gold-read ceiling ($1.0$ present coverage) isolates extraction. $^\S$structural-by-construction (different-component); $^\P$present coverage $0.05$ makes the matched-coverage reduction degenerate.}
\label{tab:venues}
\end{table}

## End-to-end on CLUTRR (\textsc{real-llm-read})
\label{sec:clutrr}

The certificate runs end-to-end on real (templated) CLUTRR text: a real LLM reads atomic kinship triples span-by-span, a forward-union least-fixpoint engine recovers the held-out query, and a certificate is emitted [ARTIFACT:art_0a7i481ZRwS1]. As a $0$-LLM go/no-go, the gold-atomic engine on all $16{,}131$ clean stories is $100\%$ accurate on every emitted answer at a $98.5\%$ singleton rate; the $1.5\%$ abstentions are genuine table ambiguities. Four deliverables: (i) the span-local reader extracts typed kinship triples at P/R/F1 $=0.536/0.532/0.534$ (held-fixed control); (ii) Mode~A's selective accuracy stays $0.75$--$1.00$ from hop-2 through hop-10 while the raw LLM collapses (hop-3 $0.444\rightarrow$ hop-10 $0.0$), and at matched coverage $0.686$ Mode~A reaches $0.886$ versus Path-of-Thoughts $0.457$ (gap $+0.429$, CI $[0.299,0.563]$, Holm $p_{\text{adj}}{=}0.0015$)---this present-pair win is the \emph{inherited} premise; (iii) the closed network is discharged as runnable SWI-Prolog $9.0.4$ and \emph{executed}: $40/40$ sampled programs run to exit $0$, $40/40$ match the Python engine, $39/40$ match gold; (iv) the absent-relation safety of Sections~\ref{sec:diagnostic}--\ref{sec:locatedin}. A gold-read oracle ($1.00$ at coverage $0.951$) localizes the bottleneck to the neural read, not the closure. We restate the concession: CLUTRR's $2.8\%$ confident-wrong on absent pairs is structural-by-construction (disconnected components) and never carries the contribution.

## Genuine fuzzy unification: a feasibility note (\textsc{real-llm-read})
\label{sec:fuzzy}

Per the reviewer's scope request we demote fuzzy unification to a feasibility note. In two labeled settings (vague spatial RCC-8; ambiguous kinship) a real LLM emits a calibrated disjunction over a known base vocabulary (fraction at confidence $1.0$ is $0.00$ in both, versus $1.00$ for the memorized-table recall a prior version mislabeled fuzzy unification; per-candidate ECE $0.142$ spatial / $0.111$ kinship), and the abstain-on-collapse certificate runs unchanged: all $5$ genuinely sound-violating spatial reads were caught (e.g.\ \textsf{around}$\rightarrow\{\textsf{NTPPi},\textsf{TPPi}\}$ drops gold \textsf{EC}, so closure collapses and the certificate abstains), with $0$ silent-wrong missed; the kinship arm had $0$ unsound reads, so its catch is untested [ARTIFACT:art_I22c-J7-OcXl][ARTIFACT:art_0MDLD-w-RXOu]. The note establishes feasibility on commodity hardware, not a substantive contribution.

## Cross-path coding is synthetic-channel-only: a bounded negative (\textsc{gold-gate}/\textsc{synth})
\label{sec:crosspath}

The most \emph{novel} mechanism we explored---cross-path intersection of disjunctive reads as an error-correcting code over LLM extractions---does not transfer to real text. It needs two conditions jointly: per-edge reads must be informative (sub-universal), and the document must offer same-algebra structural redundancy. Each was independently violated on the two real venues we could a-priori-gate before any LLM spend. \textbf{Temporal Allen violates informativeness}: the gate is GO ($N{=}125$ gold-singleton multi-path-with-bite queries on TDDMan) but LLM Allen reads are near-universe (underdetermined-rate $0.87$; the stronger deepseek is \emph{more} conservative at $0.99$), so intersection, best-single, and naive all resolve $0/125$ [ARTIFACT:art_0AIWMhwc1pJM]. \textbf{Spatial RCC-8 violates same-algebra redundancy}: reads are informative (breadth $2.1$ of $8$) but a zero-LLM gate shows the RCC-8 subgraph is a containment tree (all $228$ queries have one edge-disjoint path) [ARTIFACT:art_i53dBKgGY3Ig]. Synthetic controls satisfying both conditions confirm the mechanism is real (Allen intersection selective accuracy $0.976$ vs.\ best-single $0.717$, $+0.259$, CI $[0.177,0.349]$; RCC-8 $0.890$ vs.\ $0.797$). We present this as an explanatory account of two gated-venue negatives, not a law, and do not re-run it.

## Natural temporal text: the certificate is only weakly protective (\textsc{real-llm-read})
\label{sec:temporal}

On dense natural temporal prose we report the certificate's limits without spin. Scaling to $600$ deduction-required queries in the PC-complete convex point algebra and re-analyzing with a corrected fixed-operating-point bootstrap [ARTIFACT:art_OETjJkketEVS][ARTIFACT:art_Vc1UBGIVSi0T]: the Mode-A advantage is marginal and not robustly significant (vs.\ Path-of-Thoughts $+0.027$, CI $[-0.088,0.140]$, $p{=}0.33$; vs.\ self-consistency $+0.035$, CI $[-0.061,0.135]$, $p{=}0.26$; neither clears Holm; the raw LLM is in fact \emph{more} accurate than Mode~A at this coverage, $0.699$ vs.\ $0.575$). Among the $18.8\%$ of queries Mode~A commits, $42.5\%$ are confident-wrong, all silent-wrong-narrowing (gold omitted from a contributing read, undetectable by Mode~B). A \$$0$ synthetic backstop closes the loop: when reads are sound (recall $0.96$), Mode~A beats raw by $+0.225$ at matched coverage [ARTIFACT:art_FtN4LBzazO_l]---isolating read-soundness, not closure, as the gate. The operational $\sim$3000-character case study is compressed to a single feasibility note: the full pipeline runs end-to-end on $5$ bracket-selected NarrativeTime articles (mean $3050$ chars), discharging $60$ Prolog programs in SWI-Prolog $9.0.4$ with hallucination reduction $0.27$--$0.60$ at Mode-A coverage $0$--$0.33$ and atomic recall $\sim 0.49$ the binding ceiling [ARTIFACT:art_WQoePKrpsTPo]; the concatenated-kinship arm is cut because its $56/56$ cross-story abstentions are trivial by construction. The note establishes only that the pipeline \emph{runs} at length, not that it is useful at length.

# Discussion
\label{sec:discussion}

\textbf{What the evidence supports.} The compositional false-premise diagnostic holds as a robust empirical fact: the raw LLM fabricates absent relations at high confidence in a $30$--$48\%$ band across two corpora, two relational domains, and three readers---the compositional, document-internal lift of a single-hop RE phenomenon \citep{Yang2025DEPTH}---and no single confidence threshold can both cover present pairs and abstain on absent ones. We do \emph{not} claim family-level, reader-invariant per-signal blindness; the $16$-cell table shows the dispersion signals catch a majority of fabrications for the stronger reader. Onto this diagnostic the structural certificate converts the geometry into a measurable safety advantage: it beats the confidence battery, the same-model query-side verifier, \emph{and} a stronger cross-family verifier, and---decisively---catches $78.5\%$ of high-confidence fabrications on a non-structural-by-construction natural containment regime where every dispersion signal catches $\leq 40\%$ and the verifier $27\%$.

\textbf{What it does not support, stated without spin.} The certificate's \emph{full mixed-pool net utility} is bounded on natural prose: extraction recall is low ($0.376$ kinship, $0.148$ containment), so the certificate over-abstains on present pairs and ties or loses the matched-coverage mixed-pool showdown there; a gold-read ceiling ($1.0/1.0/1.0$) isolates extraction. The extraction-recall sweep shows this boundary is \emph{fundamental for prompt-only extraction}: recall is precision-bought, so net utility moves further from a win as recall rises, and the headroom requires a precision-preserving extractor. The certificate mechanism itself is the inherited neuro-symbolic premise ($+0.673$ inherited / $+0.0025$ novel), not our discovery. The cross-path-intersection coding mechanism is synthetic-channel-only, and the natural-temporal advantage is marginal because recall-driven silent narrowing is undetectable.

\textbf{Where to deploy, and why.} Deploy the certificate wherever confident absent-relation (false-premise) queries carry real cost and the relational graph can be extracted at high recall---clean or semi-structured inputs, or after extraction is improved with a precision-preserving extractor---because that is exactly where a confidence threshold and a query-side verifier both fail and the structural signal succeeds. Where extraction recall is low, the diagnostic still tells operators that neither the confidence family nor a same-model (or stronger) verifier will catch confident absent-relation fabrications, so the engineering lever is per-edge read-soundness, not more consistency post-processing or a better-calibrated threshold.

\textbf{Limitations.} (1) The certificate's mixed-pool \emph{net-utility} win is powered only on templated CLUTRR; on natural Re-DocRED kinship and located-in it is extraction-limited (the catching-objective win and the diagnostic still transfer), and the recall--precision frontier shows prompting alone cannot lift it. (2) The cross-path coding mechanism is synthetic-only. (3) Path consistency is complete only for the convex point algebra; Allen and RCC-8 numbers are sound lower bounds. (4) No benchmark document reaches $\sim$3000 characters (natural prose averages $\sim$$1025$); the operational note's documents are bracket-selected. (5) Upper-ontology grounding, atomic re-extraction, and general open-vocabulary fuzzy unification are out of scope. (6) The Mode-B fuzzy edge rests on $5$ caught spatial reads ($0$ testable on kinship). (7) A third-party \emph{trained} false-premise detector (FalseQA-style; DEPTH-style RE refiner) is not run head-to-head and is future work; our verifier baselines are prompt-based (same-model and a stronger cross-family judge).

# Conclusion
\label{sec:conclusion}

We treated the deduction sub-module of a text-to-logic pipeline as a faithfulness problem and reframed its most damaging error---confident fabrication of a relation that does not exist---as a \emph{compositional false-premise} failure, lifting a documented single-hop relation-extraction phenomenon to the compositional, document-internal level. The new knowledge is a diagnostic and a contrast: the raw LLM fabricates absent relations at high confidence robustly across corpora, domains, and readers; no single confidence threshold can both cover present and abstain on absent; and a gold-free, training-free, no-external-KB structural no-derivation certificate catches these fabrications where the confidence family \emph{and} a query-side false-premise verifier (same-model \emph{and} a stronger cross-family judge) do not, catching $78.5\%$ versus $\leq 40\%$ and $27\%$ on a non-by-construction natural containment regime. We concede the certificate's machinery as the inherited neuro-symbolic premise, and we are explicit about the boundary: the certificate's full mixed-pool net utility on natural prose is gated by extraction recall, and a controlled sweep shows the boundary is fundamental for prompt-only extraction because recall is precision-bought. Three concrete next steps follow: (1) build a precision-preserving (lightly fine-tuned) extractor to move into the regime where the certificate's mixed-pool advantage transfers, since the gold-read ceiling shows the entire headroom is in extraction; (2) evaluate against a third-party \emph{trained} false-premise / RE-NA detector head-to-head; and (3) integrate the validated certificate into a full pipeline with upper-ontology grounding.

\appendix
# Appendix: Mechanism analysis (\textsc{real-on-synth} / \textsc{synth} / \textsc{theorem})
\label{sec:mechanism}

We collect the inherited and synthetic mechanism results that explain---but do not compete with---the diagnostic headline. \textbf{Algebra-richness scaling (inherited).} With real LLM reads on synthetic NL, the matched-coverage advantage over Path-of-Thoughts grows monotonically with base-relation count: point ($3$) $+0.043 \rightarrow$ RCC-8 ($8$) $+0.448 \rightarrow$ Allen ($13$) $+0.676$ (all Holm-significant) [ARTIFACT:art_N0e4pH_C_Cxw][ARTIFACT:art_QToTkRe6Umb8]; the $+0.676$ Allen system gap decomposes into an inherited $+0.673$ and a novel-on-selective-accuracy $+0.0025$ [ARTIFACT:art_D0cHQUJ8kY75]. \textbf{Redundancy inverted-U (synthetic).} On a channel calibrated to the real-text frontier, the full-minus-naive gap is a structural $0.0$ at hop length $2$ and grows with hop length and cyclomatic number (Page trend $p\approx 5\times 10^{-4}$); net Mode-A resolution is an inverted-U in path redundancy $K$ with the optimum moving outward with recall (peak $K^\ast = 2,4,7,10,16$ for recall $0.5,0.625,0.78,0.90,0.95$) and silent-wrong rising $0.006\rightarrow0.146$, always below the bound $(1-r)$ [ARTIFACT:art_FtN4LBzazO_l][ARTIFACT:art_N8G6ZlQTONfk]. \textbf{Zero-false-positive theorem.} On all-sound contributing edges the Mode-A output contains gold with probability exactly $1.0$, and a collapse never co-occurs with all-sound reads---the soundness invariant of path consistency, verified on $100{,}296$ all-sound networks. Recall is an \emph{input} here, so this characterizes the mechanism rather than predicting a real-text operating point; its empirical content is the conditionality (silent-wrong rises as recall falls), and Sections~\ref{sec:boundary} and~\ref{sec:temporal} show the operating point is extraction-gated on real venues.

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

--- Item 33 ---
id: art_oUhZgMSjf7lm
type: research
title: >-
  Reframing absent-relation hallucination as compositional false-premise abstention
summary: >-
  Pure-web ($0) research that retires the LITERATURE half of the reviewer NOVELTY MAJOR and de-risks the new mandatory query-side
  baseline for the closure-certificate paper (iter-8). (1) Pins the closest-neighbor false-premise / unanswerable abstention
  literature with verified BibTeX, exact detection-method TYPES, and verbatim quotes: FalseQA [Hu2023, ACL 2023, 2023.acl-long.309]
  = 2365 FPQs + a SENTENCE-LEVEL, TRAINED discriminator (256 examples); AbstentionBench [Kirichenko2025, NeurIPS 2025 D&B,
  arXiv:2506.09038] = false-premise abstention UNSOLVED at frontier scale and reasoning fine-tuning DEGRADES it 24%, models
  commit definitive answers while internally uncertain; and a CORRECTION of the dossier's Wen2024 framing -- the survey [Wen2024]
  is built on three perspectives (query answerability a(x) | model confidence c(x,y) | human values), with a(x) INDEPENDENT
  of confidence, so answerability is a distinct axis, not confidence thresholding. Venue reconciled: Wen2024 is authoritatively
  TACL Volume 13, 2025 (pp. 529-556, DOI 10.1162/tacl_a_00754); the iter-8 'TACL 2025' is correct (dossier's '2024' = preprint
  year); key Wen2024 retained for downstream cites. Optional adjacency ((QA)^2 [Kim2023], CREPE [Yu2023] 25%/8,400 Reddit
  Qs, Self-Align [Deng2024]) confirms prior false-premise QA is sentence-level and/or trained. (2) Carves the two-part delta
  into a drop-in Related-Work paragraph (real \cite keys), a SETTING delta (compositional/multi-hop relational premise vs
  sentence-level) + METHOD delta (gold-free, training-free STRUCTURAL detector vs trained/prompt detectors), and one honest
  novelty sentence scoped to the corpus-robust diagnostic + capability gap (certificate mechanism = inherited NeSy premise).
  (3) Specifies the mandatory query-side verifier baseline grounded in self-ask [Press2023], self-verification [Weng2023],
  P(True) [Kadavath2022], self-consistency [Wang2023], and detect-then-respond [Hu2023, Deng2024]: two cheap prompt-based
  verifiers (RELATEDNESS check + SELF-VERIFICATION pass, each with a k=5 self-consistency variant), exact prompt templates
  for kinship and containment, parse/abstain rules, and a matched-coverage thresholding recipe (same single-relation coverage
  object on the mixed present/same-component-sibling-absent pool; Holm-adjusted doc-clustered B=10000 CIs). Credibility bar:
  the certificate must match-or-beat the query-side verifier at matched coverage, else honest negative. Reuses dossier BibTeX
  (Kadavath2022, Wang2023) verbatim. Feeds the iter-8 Related-Work and the experiment that decides the diagnostic-vs-demonstrated-fix
  fork.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 34 ---
id: art_l3mUIdHiAufv
type: experiment
title: >-
  Closure certificate vs confidence battery vs query-side verifier on natural located-in
summary: |-
  iter-8 decisive domain-generality experiment: a drop-in adaptation of the iter-7 STEP-B natural-kinship run to a SECOND genuinely-natural absent-relation domain -- Re-DocRED geographic/administrative containment (located_in/contains). The kinship.py forward least-fixpoint UNION engine is reused VERBATIM, parameterized by the DEGENERATE located_in/contains transitive table (located_in o located_in = located_in; located_in o contains = UNDEFINED). baselines.py/stats.py/llm.py/prolog.py are reused verbatim; new code = dataio_locatedin.py (held_out direct-edge ABLATION + absent-regime split), readers_locatedin.py (containment prompts + best-effort arm), queryside.py (the NEW query-side false-premise VERIFIER + SELF-VERIFICATION baselines), method.py (orchestration + the 4-way FORK).

  Run: 1,215 queries / 283 docs stratified doc-clustered subsample (400 held_out + 115 never_annotated + 450 same_component_sibling + 250 different_component). Two readers: PRIMARY google/gemini-3.1-flash-lite + CROSS-FAMILY mistralai/mistral-small-2603 (swapped in for deepseek-v3.2, which was too slow). All reads REAL OpenRouter, SHA-256 cached; total spend ~$2.66 (well under the $9 cap); $0 cache-replay verified, verdict byte-stable.

  VERDICT = EXTRACTION-LIMITED-BOUNDARY. Key numbers (all REAL-LLM-READ, NATURAL-PROSE): (i) FACT A -- the raw LLM confidently fabricates a containment on 30% of natural SIBLING-absent pairs (mean conf 0.94; 95% at conf>=0.9), vs only 6% on different-component pairs, so the same_component_sibling regime (non-structural-by-construction: closure derives EMPTY because located_in o contains is UNDEFINED -- a GENUINE DEDUCTIVE abstention) is the hard, decisive one. (ii) The certificate CATCHES 78.5% of those high-confidence sibling hallucinations structurally, vs <=40% for every dispersion signal (verbalized/SC-margin/P(True)/semantic-entropy), 27% for the NEW query-side verifier, 46% for self-verify; natural confident-wrong on the sibling pool: certificate 0.073 vs raw/all-signals 0.30 vs verifier 0.218 -- the certificate beats the established false-premise detector by ~3x. (iii) Reader-general: under mistral, FACT A sibling = 0.44 and certificate catches 78%. (iv) The gold-read ceiling is 1.0 present coverage / 1.0 absent abstention / 1.0 present selective accuracy (engine sound), but LLM extraction recall ~0.148 (best-effort 0.186) caps the LLM-read certificate's present coverage at ~0.05 -- so the certificate over-abstains on PRESENT and the mixed-pool matched-coverage REDUCTION is degenerate (load-bearing comparison is the crux fraction-caught + natural confident-wrong, not the matched reduction).

  Output method_out.json (exp_gen_sol_out, validated full/mini/preview, 2.9MB) has one row per query in three groups (locatedin_present, locatedin_absent_sibling, locatedin_absent_diffcomponent) with predict_certificate, predict_certificate_goldread, predict_conf_thresh_{verbalized,sc_margin,ptrue,negent}, predict_queryside_verifier, predict_queryside_selfverify, predict_commit_argmax, predict_pot, predict_sc, gold output, and metadata_regime/reader/conf_*. metadata carries the FACT-A-per-regime table, the fraction-caught crux table (all 6 competitors), both mixed leaderboards (sibling DECISIVE + diffcomponent CONTRAST) with Holm-adjusted doc-clustered confident-wrong reductions (B=10000), the abstention decomposition, the gold-read ceiling, natural-prose atomic P/R (converse-invariant + strict + vs-locally-justifiable + best-effort arm), the cross-family block, the cost ledger, three worked traces (a sibling no-derivation abstention where raw AND the verifier both commit but the certificate abstains; an over-abstain-present extraction-limited case; a present located_in composition trace -- Prolog comp/3/conv/2/rel/3/solve_/4 discharged python-checked, swipl unavailable, labelled truthfully), and the pre-registered 4-way FORK verdict. GATE-0 (no-LLM) engine wiring passed (held_out deduces located_in after ablation; sibling+diffcomp abstain EMPTY both directions; gold-read ceiling 1.0/1.0).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 35 ---
id: art_963U_7mCLAMJ
type: experiment
title: >-
  Query-side verifier vs no-derivation certificate on CLUTRR + Re-DocRED kinship pools
summary: |-
  iter-8 experiment_2 EXECUTED: the reviewer-mandated DISCONFIRM test for the closure-certificate paper. It asks whether a cheap QUERY-SIDE false-premise VERIFIER ('are X and Y related by kinship at all?') or a SELF-VERIFICATION pass ('is Y really X's <raw answer>?') recovers the structural certificate's absent-relation hallucination-safety without the closure engine. REUSE-HEAVY: loads the two fully-cached prediction pools by filesystem read (CLUTRR battery iter_6/gen_art_experiment_1, 102 present + 180 absent; Re-DocRED battery iter_7/gen_art_experiment_1, 360 present + 368 absent + 116 docred-present), reuses llm.py/stats.py/baselines.py/kinship.py VERBATIM, and adds ONLY the verifier + self-verify calls (reader-matched gemini-3.1-flash-lite, sha256-cached, total billed $0.14, hard cap $9).

  A $0 REPRODUCTION GATE (32/32 checks PASS) re-derives every published literal from the carried row fields and asserts it matches each pool's own aggregates AND the published constants: FACT-A absent-hallucination rate (CLUTRR 0.472 gemini / 0.483 deepseek; Re-DocRED 0.326 / 0.318), certificate confident-wrong-on-absent (0.0278 / 0.0707), the mixed-pool matched-coverage CERTIFICATE selective accuracy (0.8267 / 0.475), EVERY confidence-signal mixed selacc (CLUTRR 0.4133/0.3733/0.44/0.3733; Re-DocRED 0.675/0.6/0.645/0.6), and the crux survival fractions (CLUTRR 0.4353/0.7176/0.2471/0.7176; Re-DocRED 0.5083/0.85/0.4833/0.85) -- ALL EXACT. The tie-break-sensitive signal selaccs reproduce byte-exactly only after the source record ORDER is reconstructed (CLUTRR <- iter-3 row order; Re-DocRED <- dataset doc order, present-then-absent per doc); certificate/FACT-A/crux numbers are order-independent. A structural mismatch is a hard stop (no spend).

  HEADLINE VERDICT = CERTIFICATE_NECESSARY_BOTH_VENUES. On the absent-relation FABRICATION set (raw LLM confidently committed a kinship on a different-component pair), fraction CAUGHT (method abstains / answers no-relation): certificate 0.941 (CLUTRR) / 0.850 (Re-DocRED) vs query-side verifier 0.588 / 0.100 vs self-verify 0.824 / 0.542 vs best dispersion signal P(True) 0.753 / 0.517. The certificate catches STRICTLY MORE than the query-side verifier on BOTH venues (doc-clustered paired bootstrap B=10000; cert-minus-verifier caught-gap 0.353 CI[0.187,0.510] and 0.750 CI[0.620,0.848]; CIs exclude 0, p<=0.002). WHY THE VERIFIER FAILS: it runs on the SAME LLM that hallucinated, so when the reader confidently invents 'Y is X's sister' on an unrelated pair, 'are X and Y related?' returns RELATED (p=1.0) -- the verifier inherits the generation error; the certificate's abstention is independent of LLM confidence. Self-verify is intermediate but still significantly below the certificate.

  HONEST BOUNDARY (emitted alongside, not hidden): on Re-DocRED MIXED-pool selective accuracy the certificate ties/loses (0.475 vs verifier 0.595 / signals 0.60-0.675) because natural-prose extraction recall makes it OVER-ABSTAIN on PRESENT pairs (the iter-7 extraction-limited finding); the necessity verdict is therefore scoped to the hallucination-CATCHING objective (the paper's safety claim), where the certificate dominates. READER SCOPE: both pools carry per-row predictions from the GEMINI reader only (deepseek aggregate-only), so the verifier is reader-matched to gemini and deepseek FACT-A is reproduced from the carried aggregate; a deepseek-verifier robustness arm exists behind a flag (disabled in the final artifact for focus).

  OUTPUT method_out.json (exp_gen_sol_out, validated 0 errors; full/mini/preview, all <3MB) groups 1126 per-query rows into clutrr_present/clutrr_absent/redocred_present/redocred_absent/docred_present, each carrying predict_certificate, predict_conf_thresh_{4}, predict_commit_argmax, predict_queryside_verifier, predict_queryside_selfverify, predict_verifier_as_signal (ALL STRINGS) + gold + rich metadata; metadata holds the reproduction_gate, per-venue matched-coverage leaderboards (Holm-adjusted doc-clustered B=10000 CIs), fraction_caught_crux_tables, and the certificate_necessity_verdict. This is the load-bearing evidence that the certificate's structural abstention is NOT reproducible by a query-side LLM verifier -- the reviewer's DISCONFIRM does not disconfirm.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 36 ---
id: art_Kq_ROSdyIqPU
type: evaluation
title: >-
  eval_iter8_dir4 — capability-gap pivot + 16-cell survival/caught reframe scaffold
summary: >-
  PURE $0 re-analysis (numpy/json only; no LLM, no network; hard-asserted spend==0 and no network/LLM module imported) of
  two executed experiments: art_LeRQRGHJZcdQ (CLUTRR 4-signal battery) and art_htcr8yOZLCQy (Re-DocRED natural kinship battery).
  It reproduce-verifies every carried literal from the per-query rows: a STEP-0 gate of 80 checks PASSES 80/80 (62 GENUINELY
  RECOMPUTED), reproduction_ok=True. CLUTRR is rebuilt in original iter-3 order (282 records) and Re-DocRED is rebuilt row-faithfully
  in original build order (728 primary records); FACT A, crux survival, mixed selective accuracy (cert+4 signals), confident-wrong
  reduction POINTS, Holm p_adj, and ci_excludes_0 all recompute byte-faithfully — only the Re-DocRED cw CI95 numeric bounds
  are CARRIED (doc-list bootstrap MC noise <2.1e-3; flagged, fraction-caught still exact). DELIVERABLES for GEN_PAPER_TEXT:
  (1) the centerpiece 16-cell per-signal x reader x corpus SURVIVAL/CAUGHT table (caught=1-survival, all 16 cells match the
  plan exactly) splitting the ROBUST FACT A (fabrication rate in a tight 0.3178-0.4833 band across both corpora and both readers)
  from the READER/SIGNAL-DEPENDENT FACT B (caught swings ~15% Re-DocRED/gemini to ~90% CLUTRR/deepseek); (2) the NEW spine
  = signal-agnostic MIXED-POOL CAPABILITY GAP (no scalar threshold both covers present and abstains on absent) POWERED on
  CLUTRR (cert selacc 0.8267 vs 0.3733-0.44, Holm p_adj 0.0004/0.0027/0.0027/0.0027, all CIs exclude 0) but NOT yet won on
  natural Re-DocRED (cert 0.475 vs 0.675, CIs include 0, Holm rejects none; extraction recall 0.3762 binds, gold-read ceiling
  1.0/1.0/1.0 isolates extraction); (3) dropped_claims = ['family-level structural blindness','reader-diverse blindness'];
  (4) definitional-vs-empirical split + softened overclaims (P(True) caught 0.7529 CLUTRR / 0.5167 Re-DocRED); (5) abstract
  first-sentence scope front-matter + concatenated-kinship operational-arm CUT (56/56 trivial-by-construction); (6) one-thesis
  contribution table with SPINE row first (compositional-false-premise diagnostic + gold-free structural detector; mechanism
  conceded INHERITED +0.673/+0.0025) and two clearly-labeled PENDING rows (P1 located-in same-component-sibling net-win art_RfjDpsGkBXDG;
  P2 query-side false-premise verifier) for iter-9; plus false_premise_positioning (FalseQA/AbstentionBench/Know-Your-Limits).
  Outputs: eval.py, prose.py, eval_out.json + full/mini/preview (all schema-VALID exp_eval_sol_out), eval_digest.md, logs/run.log.
  datasets[]: crux_caught_table(16), non_circular_facts_ledger(84), one_thesis_contribution_table(8), reproduction_gate(80).
  metrics_agg has 46 numeric scalars incl. the 16 caught_{corpus}_{reader}_{signal}. Both eval_out.json and full_eval_out.json
  are 0.153MB (well under 100MB). Deterministic (seed 20260617, B=10000) so re-runs reproduce byte-identical CIs.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 37 ---
id: art_fXvxt4JO9hWy
type: experiment
title: Extraction-Recall Booster for the Closure-Certificate Net-Utility Fork
summary: |-
  iter-9 experiment that tries to FLIP the iter-8 EXTRACTION-LIMITED-BOUNDARY fork by RAISING natural-prose atomic extraction recall, on two genuinely-natural Re-DocRED absent-relation domains (located-in administrative containment + kinship). It reuses the entire iter-8 located-in harness VERBATIM (the iter-8 method.py is imported as core.py; kinship.py forward-union closure engine, dataio_locatedin/readers_locatedin/queryside, baselines/stats/llm/prolog) and the iter-7 kinship harness (dataio_redocred + readers_kinship), and adds ONE new module booster.py plus a new orchestrator method.py + queryside_kinship.py + kinship_pipeline.py.

  METHOD. booster.py sweeps >=4 extraction strategies above the iter-8 floor: S0 default + S1 best-effort (iter-8 arms, cached), S2 fewshot_enum (few-shot + place/person inventory + explicit NO-OMISSION, max_tokens 1200), S3 sentencewise (sentence-by-sentence + coref->inventory, max_tokens 1500), S4 sc_union (self-consistency UNION over k=4 temp-0.7 samples), S5 multimodel_union (gemini ∪ mistral-small-2603), plus high-precision variants (agreement>=2 AND cue-supported). A PRECISION GUARD canonicalises edges converse-invariantly, counts per-edge source agreement, drops directed 2-cycles, and keeps an edge iff agreement>=2 OR a domain cue phrase co-occurs with both endpoint mentions; ungroundable names become isolated NAME:: nodes. Per strategy, ONLY the certificate (modeA) is recomputed; the 6 confident-wrong competitors (verbalized / SC-margin / P(True) / semantic-entropy + query-side verifier + self-verify) stay FIXED and are snapshot-asserted byte-identical (replayed from the iter-8/iter-7 sha256 caches at $0). Downstream views (matched-coverage mixed-pool confident-wrong reduction with doc-clustered Holm B=10000 CIs, abstention decomposition, atomic P/R, FACT A, fraction-caught) are the iter-8 functions reused verbatim.

  RESULT (verdict EXTRACTION-LIMITED-BOUNDARY-CONFIRMED, both domains). The booster MEASURABLY raises recall (located-in 0.148->0.227, kinship 0.376->0.396) and lifts the certificate's present coverage ~3x (0.051->0.165), with corr(recall, present_coverage)=0.96 -- the dose-response is real. BUT the recall is PRECISION-BOUGHT: corr(recall, sibling-confident-wrong)=0.91, so injected false edges make the certificate fabricate sibling paths, and the worst-case (min-over-6) mixed-pool confident-wrong REDUCTION moves AWAY from a flip as recall rises (CI-lower-vs-recall slope -0.30 located-in / -0.67 kinship). The reduction-optimal operating point is the HIGHEST-precision / LOWEST-recall strategy; no prompt-only strategy flips the fork. S0 default reproduces iter-8 EXACTLY (recall 0.1478, present cov 0.0505, sibling conf-wrong 0.0733); kinship default recall 0.3762 reproduces iter-7. The gold-read ceiling stays 1.0/1.0/1.0 (engine sound) -- so the headroom is real but NOT promptable without precision loss: the fix requires precision-preserving (fine-tuned) extraction, not better prompts.

  SECONDARY (retires methodology MINOR #5). A STRONGER, larger, different-family query-side verifier (deepseek-v3.2, k=5 self-consistency) catches only 0.10 of the raw LLM's confident sibling hallucinations -- WORSE than the same-model weak verifier (0.20) and far below the certificate (0.67-0.79), because a better geographer over-infers containment. Certificate-necessity is therefore not an artifact of a same-model verifier.

  FOR THE PAPER. This converts iter-8's 'diagnostic + boundary' into a quantified recall-PRECISION frontier proving the boundary is FUNDAMENTAL for prompt-only extraction, plus a stronger-verifier robustness result. Output method_out.json (schema exp_gen_sol_out, 4.95MB) has 5 corpora (locatedin_present/absent_sibling/absent_diffcomponent + kinship_present/absent), per-strategy rows, the recall-vs-reduction frontier + extrapolation, FACT A, the stronger-verifier block, the cost ledger (one-time $1.21, re-runs $0), and worked traces (a present-RECOVERY newly enabled by the booster, a residual over-abstain, a composition trace, a sibling no-derivation abstention; Prolog python-checked, swipl unavailable, labelled truthfully). All four variants validate against exp_gen_sol_out.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_9/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 38 ---
id: art_mxFG0bGhTe2-
type: research
title: >-
  Retire NOVELTY MAJOR: RE NO_RELATION lit + structural premise-verification + ACL-KE venue
summary: >-
  Pure-web ($0, no code) research that retires the ACL-Knowledge-Extraction reviewer's NOVELTY MAJOR for the closure-certificate
  paper (iter-9). It pins, with web-verified BibTeX, exact verbatim quotes, method-types, datasets and venues, the two literature
  clusters a KE reviewer demands. CLUSTER 1 (RE NO_RELATION/NA + hallucination-resistant RE): DEPTH [Yang2025DEPTH, arXiv:2508.14391]
  reports Qwen2.5-14B over-predicts a relation on 96.9% of NO-RELATION SciERC pairs (45/1,475 correct) and fixes it with dependency-aware
  grounding + RLHF (v2 numbers 7.9%/9.3% over eight sentence-RE benchmarks -- a CORRECTION of the planner's v1 7.0%/17.2%/six
  pin); LLM+Relation-Classifier [Li2024RelClassifier, 2408.13889] blames 'attention dispersion due to entity pairs without
  relations' and pre-filters with a trained classifier on DocRED/Re-DocRED; RelPrior [Pi2025RelPrior, 2511.08143] filters
  'unrelated entity pairs [that] introduce noise' with a fine-tuned binary prior. CLUSTER 2 (training-free structural/logical
  premise verification + KG-triple detection): Premise Verification [Qin2026PremiseVerification, 2504.06438, TMLR 2026 CONFIRMED]
  logicalizes a query then RAG-validates each premise against EXTERNAL factual sources ('no logits / no large-scale fine-tuning');
  GraphEval [Sansford2024GraphEval, 2407.10793, KiL@KDD 2024 -- first author Sansford, NOT the planner's tentative 'Wang2024GraphEval']
  checks single response triples against the PROVIDED CONTEXT with a trained NLI model, explicitly out-of-scope for world
  knowledge/deduction. It DROPS the untenable 'absent-relation hallucination is not derivable a priori' assertion (DEPTH already
  quantifies single-hop over-prediction) and re-carves a defensible two-part delta -- SETTING (compositional, multi-hop, document-internal
  absent-relation premise vs single-hop/schema-bound NO_RELATION classification and sentence-level false premise) and METHOD
  (gold-free, training-free, no-external-KB deductive-closure certificate vs trained RE refiners/classifiers, external-KB/RAG
  premise checks, and NLI-vs-context triple checks) -- plus the empirical contrast that the confidence family AND a same-model
  query-side verifier both fail where the structural certificate succeeds. A breadth probe confirms the deductive-multi-hop-NA
  (abstain-on-no-path) niche is unclaimed. Deliverables: a drop-in Related-Work paragraph (~200 words, real \cite keys folding
  both new clusters + inherited FalseQA/AbstentionBench/Wen2024), a sharpened one-sentence novelty statement, the re-carved
  DELTA-1/DELTA-2, a method-delta table on five axes, a verified BibTeX block for the five new keys (dossier keys reused verbatim),
  and a concrete ACL-KE-primary / NeSy-fallback venue recommendation. Feeds the iter-9 Related-Work, Introduction, and venue
  decision.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_9/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 39 ---
id: art_4xy3D05YxvRr
type: evaluation
title: >-
  Zero-spend re-analysis: caught-fraction replaces located-in 0.227 coverage artifact
summary: >-
  Pure $0 re-analysis (numpy/scipy only; cost counter asserted ==0 and forbidden network/LLM modules asserted absent from
  sys.modules) of three frozen iter-7/iter-8 outputs (located-in, query-side verifier, Re-DocRED kinship). A REPRODUCTION
  GATE recomputes every paper-facing literal from the per-query rows and HARD-asserts it equals the carried metadata: 68/68
  hard checks PASS (FACT-A rates, caught-fractions, natural confident-wrong, abstention decompositions, CLUTRR present leaderboard,
  counts, verdict strings) plus 5/5 doc-clustered-bootstrap soft cross-checks within Monte-Carlo tol; a mismatch is a hard-stop.
  RIGOR FIX: exposes the pure-absent identity (named-rate==confident-wrong==coverage on the 450-pair absent pool) showing
  the located-in '0.2267 reduction at matched coverage / meets-0.20-bar' sentence is mechanically (0.30-0.0733), not a risk-coverage
  gain, and ELEVATES the matched-coverage-FAIR CAUGHT-FRACTION as the headline: certificate 0.785 vs verbalized 0.400 / sc_margin
  0.067 / P(True) 0.304 / semantic-entropy 0.067 / query-side verifier 0.274 / self-verify 0.459, with a NEW doc-clustered
  paired bootstrap (EVAL seed 20260617, B=10000) where ALL SIX cert-minus-competitor caught-gaps exclude 0. Natural confident-wrong:
  certificate 0.073 vs raw/all-dispersion 0.30 vs verifier 0.218 (~3x). The degenerate mixed-pool reduction (-0.0342, negative
  from extraction recall 0.148) is carried and reconciled with the artifact's own pure_absent_degeneracy / matched_coverage_degeneracy
  caveats. Provides a 16-cell capability-gap table (survival+caught per signal x reader x corpus: Re-DocRED/gemini REPRODUCED-FROM-ROWS;
  Re-DocRED/deepseek CARRIED-NOT-REPRODUCED since deepseek per-row predictions are absent; CLUTRR/gemini+deepseek CARRIED-LITERAL)
  splitting the ROBUST FACT A (fabrication rate transfers across corpora+readers) from the reader/signal-dependent FACT B.
  Delivers seven paper-facing scaffold blocks for GEN_PAPER_TEXT (corrected located-in table with delete-vs-relabel option
  for the 0.227 sentence; clean regenerated sec:boundary + a draft-wide proofread checklist; sibling decisiveness via prevalence
  30% vs 6% + verifier-fooled-by-shared-parent; one-line fuzzy demotion; verifier scoped to a same-model prompt-based instantiation
  + a STRONGER-CROSS-MODEL PENDING slot; one-thesis contribution table with a DEMONSTRATED-FIX-PENDING row; and an abstract
  first-results FORK-A/FORK-B with an explicit selection rule keyed to the parallel extraction experiment) plus a count_reconciliation
  (kinship 360/368 primary vs 476/577 combined-round-trip; located-in 515/450/250/115/400/283). Every derived number sits
  under metadata with an evidence_tag. Outputs: eval.py (deterministic, byte-stable across reruns), eval_out.json + full/mini/preview
  (exp_eval_sol_out validated, <100MB no split), eval_digest.md. budget {cumulative_usd:0.0, n_llm_calls:0}.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_9/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</supplementary_materials>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (clarity) Section 'The honest boundary' (sec:boundary) is corrupted: a multi-paragraph block of raw artifact-summary text is spliced into the middle of the opening paragraph, beginning at '...Net utility additionally requires high present coverage, which depends on extraction recall, and here the certificate is gat[ed] rt-point gold is structurally DISJUNCTIVE -- explaining iter-3's full==naive; MATRES 0, confirming the gate is discriminative). Gold bite hist {2:62, 4:63}...' and continuing through a synthetic-Allen positive-control description, 'Item 18', 'workspace_path', and 'out_expected_files' before the real boundary text resumes ('...invisibed. On Re-DocRED kinship, mixed-pool confident-wrong reductions are slightly negative...'). The word 'invisibed' is itself a truncation artifact. As handed to a reviewer this is disqualifying.
  Action: Regenerate sec:boundary from the intended content only (net-utility is extraction-limited; Re-DocRED kinship reductions -0.034 to -0.055 with CIs including 0 and Holm rejecting none; located-in present coverage collapses to 0.05 at extraction recall 0.148; gold-read ceiling 1.0/1.0/1.0 isolates extraction). Then proofread the whole draft end-to-end for any other spliced or truncated text introduced during assembly.
- [MAJOR] (novelty) The novelty positioning improved (false-premise framing) but engages the wrong closest literature for the target venue. FACT A -- LLMs confidently fabricate relations on unrelated pairs -- is a documented finding in relation extraction: recent work reports LLMs 'overpredict relations and frequently hallucinate links between unrelated entities' and 'exhibit a higher tendency to generate new relations when the gold is NO/OTHER RELATION' (e.g., DEPTH / hallucination-resistant RE, arXiv:2508.14391; LLM-RE NA-problem and relation-classifier work, arXiv:2408.13889, 2511.08143). Separately, the no-derivation certificate is close to training-free structural/logical premise verification (e.g., 'Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning', arXiv:2504.06438) and KG/triple-based structural hallucination detection (GraphEval-style). An RE/Knowledge-Extraction reviewer will read FACT A as a known phenomenon and the certificate as an instance of structural premise verification.
  Action: Add a related-work paragraph engaging (a) the RE NO_RELATION / NA-problem and hallucination-resistant-RE literature, and (b) training-free structural/logical premise-verification and KG-triple hallucination-detection methods. Re-carve the delta crisply as: (i) a COMPOSITIONAL multi-hop absent-relation premise resolved by document-internal closure (vs single-hop NO_RELATION classification and vs external-RAG premise verification), and (ii) the empirical contrast that the confidence/uncertainty family AND a same-model query-side verifier both fail where the structural certificate succeeds. Avoid asserting FACT A is 'not derivable a priori' without acknowledging the RE precedent.
- [MAJOR] (significance) The certificate's deployable (net-utility) advantage is still confined to by-construction templated CLUTRR: the mixed-pool selective-accuracy win (0.827 vs 0.37-0.44) is on a stratum the paper concedes is near-tautological (disconnected components), and the capability-gap 'spine' is powered only there. On natural prose, net utility is extraction-gated (Re-DocRED reductions CIs include 0; located-in present coverage 0.05), and the 'decisive' located-in result wins only the one-sided catching objective. With the mechanism conceded inherited (+0.673/+0.0025), the net novel contribution is a diagnostic plus an abstention-targeting demonstration -- valuable but modest, which caps significance.
  Action: To lift significance, demonstrate a net-utility win where it is NOT structural-by-construction: raise extraction recall on one domain (better-prompted/lightly-tuned extractor) until the mixed-pool reduction excludes 0 with CIs, converting 'diagnostic + boundary' into 'diagnostic + demonstrated fix'. If that is out of reach this cycle, state in the abstract's first results sentence that the certificate's net utility is demonstrated only on clean/templated graphs and that the natural-prose contribution is a catching-objective win plus a quantified extraction boundary, so reviewers calibrate impact correctly.
- [MAJOR] (rigor) The located-in headline 'the certificate's confident-wrong reduction is 0.227 vs every dispersion signal (CI [0.176,0.280], meets the pre-registered 0.20 bar)' is a coverage artifact, not an abstention-quality result. On a pure-absent pool every committed answer is wrong, so confident-wrong rate equals coverage for any method; matched coverage therefore forces equal CW. The artifact's own primary_reader_results_sibling_DECISIVE.view1_absent confirms this: each signal's matched_operating_points CW equals its natural CW (0.30) -- the 'matching' is vacuous -- while modeA sits at coverage/CW 0.073. So the 0.227 reduction merely reflects that the certificate abstains more (0.073 coverage) than the signal at its 0.30 operating point; it is the exact 'abstain-on-everything wins' confound the paper warns against elsewhere. The genuinely fair, matched-coverage result is the caught-fraction (certificate 0.785 vs verbalized 0.400, verifier 0.274).
  Action: Make the caught-fraction the headline located-in number and present it as the matched-coverage win. Either delete the '0.227 CW reduction at matched coverage / meets the pre-registered 0.20 bar' sentence or relabel it explicitly as certificate-at-its-abstaining-operating-point vs signal-at-natural-operating-point, and note that on a pure-absent pool CW reduction is uninformative without matched coverage. Reconcile this with the artifact's own note that the mixed-pool matched reduction is 'degenerate'.
- [MINOR] (methodology) The query-side verifier baseline is a same-model, prompt-based proxy run on the very reader that hallucinated; the paper itself explains it inherits the generation error. But the actually-established methods for false-premise detection (FalseQA-style trained discriminators; Deng2024 detect-then-respond) are not run -- they are deferred to future work. So 'the certificate beats the established query-side false-premise verifier' and the 'certificate-necessary' verdict are scoped to same-model prompt verifiers, where the failure is near-tautological, rather than to the established trained detectors the related work cites.
  Action: Either run a stronger verifier (a different/stronger model as judge, a retrieval-grounded check, or a trained relation-existence/false-premise detector such as a DEPTH-style classifier) on at least one venue, or scope the claim precisely to 'a same-model prompt-based verifier cannot recover the certificate's safety' and soften 'the established method' to 'a recognized prompt-based instantiation'.
- [MINOR] (clarity) The framing that the same-component-sibling regime makes abstention 'non-structural-by-construction' / 'a genuine deductive result' is imprecise: the certificate still abstains on a purely structural property (no directed composition path; located_in o contains undefined). What is genuinely harder and decisive about this regime is that fabrication is prevalent (30% vs 6% on different-component) and a relatedness verifier is actively fooled because the entities share a parent -- not that the abstention itself is non-structural.
  Action: Restate the decisiveness of the sibling regime in terms of (i) high fabrication prevalence and confidence and (ii) the verifier being fooled by shared structure, while acknowledging the abstention is still a structural (no-path) determination -- just a non-trivial one that requires the composition table rather than mere disconnection.
- [MINOR] (scope) Relative to the original brief (operational ~3000-char text-to-FOL, OpenCyc grounding, general probabilistic fuzzy unification, hallucination reduction on real long documents), the delivered fuzzy-unification result rests on a 5/5 sound-violation catch on spatial reads with 0 testable on kinship -- too thin to support the 'genuine fuzzy unification' framing -- and no benchmark document reaches ~3000 chars (natural prose averages ~1025). This is honestly disclosed, but the goal-vs-delivery gap remains for any reviewer holding the brief.
  Action: Either expand the fuzzy evaluation (more genuinely sound-violating reads across both domains, with calibration and catch rates powered) or demote it to a one-line feasibility note. Keep the explicit out-of-scope statement for grounding/extraction/long-document operation, and ensure the abstract's first sentence sets the deduction-sub-module scope before results.
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

### [2] HUMAN-USER prompt · 2026-06-18 08:08:31 UTC

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

### [3] SKILL-INPUT — aii-web-tools · 2026-06-18 08:12:27 UTC

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
