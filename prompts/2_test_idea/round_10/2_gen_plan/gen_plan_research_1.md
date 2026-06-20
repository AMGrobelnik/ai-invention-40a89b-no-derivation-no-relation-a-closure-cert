# gen_plan_research_1 — test_idea

> Phase: `invention_loop` · round 10 · `gen_plan`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_research_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-18 08:33:35 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: RESEARCH

RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings
</artifact_type_info>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>
</available_resources>

<time_budget>

The research executor has 3h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

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

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

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

<hypothesis>
kind: hypothesis
title: >-
  Confident Absent-Relation Hallucination Is a Compositional False-Premise Failure That No Single Confidence Threshold — and
  No Same-Model or Stronger Cross-Family Query-Side Verifier — Can Both Cover-and-Abstain Against; a Gold-Free No-Derivation
  Certificate Catches It, but Its Net Deployable Utility on Natural Prose Is Extraction-Gated and That Boundary Is FUNDAMENTAL
  for Prompt-Only Extraction — An Empirical Isolation in the Deduction Sub-Module of Text-to-Logic Pipelines (decisive open
  test now = a PRECISION-PRESERVING / lightly fine-tuned extractor on ONE domain, OR a naturally-high-recall semi-structured
  input, since iter-9's recall–precision frontier REFUTED the prompt-only extraction fix; the non-by-construction same-component-sibling
  caught-objective win 0.785 is established as TARGETING QUALITY, not deployable net-utility; cross-path algebra coding stays
  synthetic-only)
hypothesis: |-
  ONE THESIS, RE-SCOPED THIS ROUND AROUND A FAILED CHEAP-FIX AND A SHARPENED OPEN TEST (reviewer significance MAJOR still binding + rigor MAJOR on the stronger-verifier denominator + evidence MINOR on the one-sided caught objective). The core is unchanged: in the DEDUCTION SUB-MODULE of a text-to-logic pipeline, keep the LLM a high-recall disjunctive reader, compose ONLY through an exact relation-algebra / finite composition table, and ABSTAIN when iterated closure leaves a disjunction or finds no derivation path. We continue to concede UP FRONT, as the paper's FRAMING not a footnote, that this compose-through-table + abstain-on-collapse machinery is the INHERITED neuro-symbolic premise (+0.673 inherited vs only +0.0025 novel on selective accuracy, art_D0cHQUJ8kY75) — the novelty is NOT the certificate mechanism. iter-9 executed the prior hypothesis's PATH 2 (raise natural-prose extraction recall via better prompting) and it FAILED decisively (art_fXvxt4JO9hWy, VERDICT=EXTRACTION-LIMITED-BOUNDARY-CONFIRMED both domains): the prompt-only extraction fix cannot lift the certificate's net-utility win onto natural prose. The novel CONTRIBUTION is therefore now stated as (i) a corpus-, domain-, and reader-robust DIAGNOSTIC (FACT A + the signal-agnostic capability gap), (ii) a one-sided CATCHING-OBJECTIVE win on a non-structural-by-construction natural regime that beats the confidence family AND the query-side false-premise verifier (same-model AND a stronger cross-family one), and (iii) a now-QUANTIFIED recall–precision frontier proving the natural-prose net-utility boundary is FUNDAMENTAL for prompt-only extraction. The decisive iter-10 test is redefined as a PRECISION-PRESERVING (lightly fine-tuned) extractor — the ONLY surviving route to a deployable net win, per both the experiment's own conclusion and the reviewer.

    RESOLVED THIS ROUND — NOVELTY MAJOR (was CORRECTION 1). The ACL-Knowledge-Extraction reviewer's novelty objection is retired (art_mxFG0bGhTe2-, $0 web). The paper now engages TWO literature clusters with web-verified BibTeX: CLUSTER 1, RE NO_RELATION / hallucination-resistant relation extraction — DEPTH (Yang2025DEPTH, arXiv:2508.14391; Qwen2.5-14B over-predicts a relation on 96.9% of NO-RELATION SciERC pairs, 45/1,475 correct), LLM+Relation-Classifier (Li2024RelClassifier, 2408.13889; 'attention dispersion due to entity pairs without relations'), RelPrior (Pi2025RelPrior, 2511.08143; fine-tuned binary prior); CLUSTER 2, training-free structural / premise verification — Premise Verification (Qin2026PremiseVerification, 2504.06438, TMLR 2026; logicalize + EXTERNAL-KB RAG, no logits / no fine-tuning), GraphEval (Sansford2024GraphEval, 2407.10793, KiL@KDD 2024 — first author SANSFORD, NLI-vs-PROVIDED-CONTEXT triple check) — alongside the inherited FalseQA / AbstentionBench / Wen2024 line. We DROP the untenable 'absent-relation hallucination is not derivable a priori' assertion (DEPTH already quantifies single-hop over-prediction) and carve a defensible TWO-PART delta: SETTING (compositional, MULTI-HOP, document-internal absent-relation premise vs single-hop schema-bound NO_RELATION classification and sentence-level false premise) and METHOD (gold-free, training-free, NO-EXTERNAL-KB deductive-closure certificate vs trained RE refiners/classifiers, external-KB/RAG premise checks, and NLI-vs-context triple checks). VENUE updated: ACL Knowledge Extraction PRIMARY, NeSy / temporal-and-qualitative-reasoning FALLBACK (matches the user's stated publication target; reverses the prior NeSy-primary call). ONE remaining add for iter-10 (reviewer novelty MINOR): a single sentence distinguishing the no-derivation certificate (per-query, gold-free abstention from deductive closure over the document-internal graph) from ontology-grounded POST-EXTRACTION structural CORRECTION (e.g. arXiv:2605.29168), which repairs/commits a labeling against EXTERNAL structure — preserving the gold-free / training-free / no-external-KB delta.

    CORRECTION A — THE PROMPT-ONLY EXTRACTION FIX IS REFUTED; THE NATURAL-PROSE NET-UTILITY BOUNDARY IS FUNDAMENTAL; THE DECISIVE iter-10 TEST IS A PRECISION-PRESERVING EXTRACTOR (reviewer significance MAJOR, still binding). iter-9's booster experiment (art_fXvxt4JO9hWy) swept >=6 prompt-only extraction strategies above the iter-8 floor (few-shot enumeration + no-omission inventory; sentence-by-sentence + coreference; self-consistency UNION over k=4; multi-model UNION gemini ∪ mistral-small; plus high-precision agreement>=2 / cue-supported variants) on BOTH natural domains. The dose-response is real: recall rose (located-in 0.148->0.227; kinship 0.376->0.396) and lifted certificate present coverage ~3x (0.051->0.165; corr(recall, present-coverage)=0.96). BUT the recall is PRECISION-BOUGHT: corr(recall, sibling-confident-wrong)=0.91 — injected false edges make the certificate fabricate sibling containment paths — so the worst-case (min-over-6-competitors) mixed-pool confident-wrong REDUCTION moves AWAY from a flip as recall rises (CI-lower-vs-recall slope -0.30 located-in / -0.67 kinship). The reduction-optimal operating point is the HIGHEST-precision / LOWEST-recall strategy; the S0 default reproduces iter-8 EXACTLY (recall 0.1478, present cov 0.0505, sibling confident-wrong 0.0733); the gold-read ceiling stays 1.0/1.0/1.0 throughout. CONCLUSION: the deployment headroom is real (gold-read ceiling shows ALL of it is in extraction, none in closure) but NOT PROMPTABLE — closing it requires a precision-PRESERVING (lightly fine-tuned) extractor, not a better prompt. The natural-prose net-utility boundary is therefore FUNDAMENTAL for prompt-only extraction, and this recall–precision frontier is itself a publishable, quantified result (it converts iter-8's bare 'extraction-limited boundary' into a mechanism with a measured slope). The decisive iter-10 test (PATH 3) is to lightly FINE-TUNE / otherwise build a precision-preserving extractor on ONE domain (located-in OR kinship) until the mixed-pool confident-wrong REDUCTION CI EXCLUDES 0 on natural prose; a cheaper alternative (PATH 4) is a naturally-HIGH-RECALL semi-structured input (infoboxes / explicit relational statements / list-structured prose) where extraction recall is high WITHOUT the precision tax. If neither is feasible this cycle, the paper holds at its current ceiling with the explicit abstract caveat, framing the natural-prose contribution as catching-objective + a PROVABLE / fundamental boundary so reviewers calibrate impact correctly.

    CORRECTION B — REPORT THE STRONGER CROSS-FAMILY VERIFIER ON ITS OWN n=60 SUBSAMPLE (reviewer rigor MAJOR). The stronger cross-family verifier's 0.10 caught fraction is computed on a DIFFERENT subsample (deepseek-v3.2, k=5; n_sibling=250 with 60 raw fabrications) than the main caught-fraction pool (n_sibling=450 with 135 fabrications). On THAT n=60 subsample the comparable numbers are: certificate 0.667 / weak same-model verifier 0.20 / stronger cross-family verifier 0.10 / self-verify-strong 0.533 (art_fXvxt4JO9hWy stronger_verifier_block). iter-10 MUST report these in their OWN small table or a clearly-labeled footnote and NEVER place 0.10 in the same column/denominator as the main pool's certificate 0.785 and same-model verifier 0.274 (that juxtaposition is apples-to-oranges). The qualitative conclusion is unchanged and now reader-robust: a stronger verifier is NO BETTER (in fact worse, because a better geographer OVER-infers co-regional containment), and both verifiers sit far below the certificate — certificate-necessity is intrinsic to running the premise check on a generative LLM, NOT an artifact of a weak same-model verifier (this retires methodology MINOR #5).

    CORRECTION C — THE 0.785 CAUGHT-OBJECTIVE WIN IS TARGETING QUALITY, NOT DEPLOYABLE NET-UTILITY; PAIR IT WITH THE EXTRACTION-GATED CAVEAT EVERYWHERE (reviewer evidence MINOR). The matched-coverage-FAIR caught fraction is the correct headline metric on the non-by-construction same-component-sibling regime (art_4xy3D05YxvRr re-analysis: certificate 0.785 vs verbalized 0.400 / P(True) 0.304 / self-verify 0.459 / query-side verifier 0.274 / sc_margin 0.067 / semantic-entropy 0.067, with all SIX certificate-minus-competitor caught-gaps excluding 0, doc-clustered paired bootstrap B=10000, seed 20260617; natural confident-wrong certificate 0.073 vs raw/all-dispersion 0.30 vs verifier 0.218, ~3x). It REPLACES the earlier '0.2267 reduction at matched coverage' sentence, which the re-analysis exposed as MECHANICALLY (0.30 - 0.0733) — a pure-absent identity (named-rate == confident-wrong == coverage on the 450-pair absent pool), NOT a risk-coverage gain. BUT the caught objective is ONE-SIDED: on a pure-absent pool it measures only how well a method's abstentions TARGET the fabrications, and it structurally REWARDS methods that abstain more on absent pairs. The deployment-relevant DUAL — net utility on a MIXED present/absent pool — is exactly where the same structural abstention OVER-abstains on present pairs and LOSES on all natural prose (extraction-gated). The two results are two scorings of one mechanism. So whenever the 0.785 'decisive' number is stated (abstract, intro, contribution list, conclusion), it MUST be paired in the same sentence with the net-utility caveat (extraction-gated, NOT a deployment win) and a note that the catching objective inherently favors high-abstention methods on the absent subset, so the win establishes TARGETING QUALITY, not deployable net utility.

    CORRECTION D — DE-DENSIFY THE PAPER (reviewer presentation + scope MINORs). Move evidence-class tags (REAL-LLM-READ, GOLD-ONLY-GATE, etc.) into the spine table and section headers ONLY; delete inline \textsc{...} markers in results prose; rewrite defensive meta-narration ('a skeptical reviewer rightly observed...', 'stated without spin', 'we never let that number carry the contribution') as declarative claims-with-caveats; collapse the 7 bold-headed intro paragraphs so the contributions and headline numbers appear sooner. FOLD the operational ~3000-char note and the fuzzy-unification feasibility note into a SINGLE short 'feasibility' appendix; keep the explicit out-of-scope statement (OpenCyc grounding, atomic re-extraction, general fuzzy unification, genuine ~3000-char documents) in the intro.

    ----- CLAIM 1 (THE SPINE, EMPIRICAL DIAGNOSTIC). TAG: REAL-LLM-READ. -----
    FACT A (ROBUST, the load-bearing non-circular fact): the raw LLM emits a confident absent-relation fabrication at HIGH confidence — CLUTRR 47.2% (gemini) / 48.3% (deepseek), Re-DocRED kinship 32.6% / 31.8%, Re-DocRED located-in SIBLING 30.0% (gemini, mean conf 0.94, 94.8% at conf>=0.9) / 43.8% (mistral) — corpus-, domain-, AND reader-transferable, and the compositional/document-internal lift of the single-hop RE over-prediction DEPTH documents (96.9% on SciERC NO-RELATION). THE MIXED-POOL CAPABILITY GAP (signal-agnostic, the spine): no single confidence threshold can both cover present pairs and abstain on absent ones at matched coverage (powered on CLUTRR: certificate selective accuracy 0.827 vs every signal 0.37-0.44; Holm-adjusted confident-wrong reductions 0.103-0.121, CIs exclude 0), because one scalar knob cannot separate confident-and-right (present) from confident-and-wrong (absent). FACT B is reported HONESTLY per-signal x reader x corpus via the 16-cell SURVIVAL/CAUGHT table (caught swings ~15% Re-DocRED/gemini to ~90% CLUTRR/deepseek; verbalized confidence is the most ROBUSTLY blind; dispersion signals catch the MAJORITY for the stronger deepseek reader), NOT as family-level / reader-diverse blindness, and the 'no signal removes a single one' phrasing is scoped to the LLM's NATURAL (no-abstention) coverage only — at the certificate's coverage P(True) already catches 75.3% on CLUTRR / 51.7% on natural Re-DocRED. We are explicit the capability gap is POWERED ONLY on clean templated CLUTRR; CLAIMs 2-3 test it on natural prose. The multi-hop PRESENT selective-accuracy win (CLUTRR 0.886 vs 0.543 at matched coverage 0.686) is the INHERITED NeSy premise, labeled as such. The CLUTRR-absent 2.8% confident-wrong is STRUCTURAL-BY-CONSTRUCTION (disconnected components) and never carries the section.

    ----- CLAIM 2 (THE NON-BY-CONSTRUCTION CATCHING WIN, ESTABLISHED but ONE-SIDED). TAG: REAL-LLM-READ. -----
    On the Re-DocRED located-in SAME-COMPONENT-SIBLING regime (art_RfjDpsGkBXDG, 20,814 such pairs; two places in one component sharing a parent but neither containing the other, so closure derives EMPTY because located_in∘contains is UNDEFINED — a GENUINE deductive abstention, NOT 'disconnected => trivially empty'), the certificate CATCHES 0.785 of the raw LLM's high-confidence fabrications vs <=0.40 for every dispersion signal, 0.274 for the same-model query-side verifier, and (on its own n=60 subsample) 0.10 for the stronger cross-family verifier; all six certificate-minus-competitor caught-gaps exclude 0. This regime is decisive for the CATCHING objective because (i) the raw reader fabricates a containment on 30% of sibling pairs vs only 6% of different-component pairs, and (ii) a relatedness verifier is ACTIVELY FOOLED by the shared parent (returns RELATED at conf 1.0). HONESTY: this is a TARGETING-QUALITY win, NOT a deployment net-utility win (CORRECTION C) — it is one-sided on a pure-absent pool. The query-side verifier baseline (same-model AND stronger cross-family) is the established detect-then-respond method for this failure mode, so the certificate's edge over it is the load-bearing comparison (art_963U_7mCLAMJ: certificate catches 0.941/0.850 vs verifier 0.588/0.100 on CLUTRR/Re-DocRED kinship; CIs exclude 0).

    ----- CLAIM 3 (THE DECISIVE OPEN EXPERIMENT for iter-10, REDEFINED). TAG: REAL-LLM-READ. -----
    PATH 2 (prompt-only extraction-recall fix) is RETIRED as EXECUTED -> FAILED (CORRECTION A). The new decisive test is a NET certificate win on natural prose via a PRECISION-PRESERVING extractor: (PATH 3, preferred) lightly FINE-TUNE (or distill a span-tagger / constrained decoder) an extractor on ONE domain so recall rises WITHOUT the precision tax that defeated prompting, then re-run the certificate vs the four-signal battery AND the query-side verifier on a MIXED present / same-component-sibling-absent pool at matched coverage with Holm-adjusted doc-clustered CIs; (PATH 4, cheaper alternative) run the SAME mixed-pool showdown on a naturally-HIGH-RECALL semi-structured input (infoboxes / list-structured / explicit relational prose) where extraction recall is high a priori. FORK (both publishable): IF the certificate's Holm-adjusted mixed-pool confident-wrong reduction EXCLUDES 0 on natural prose (and it matches/beats the query-side verifier) -> the headline converts from 'diagnostic + targeting-quality win + fundamental boundary' to 'diagnostic + DEMONSTRATED FIX', lifting significance; IF even a precision-preserving extractor cannot reach the regime -> the net-utility boundary is structural to natural-prose extraction (deeper than 'prompt-only'), reported HONESTLY, while the DIAGNOSTIC (FACT A + capability gap) and the CATCHING win still stand. The gold-read ceiling (1.0/1.0/1.0) guarantees the entire headroom is in extraction, so PATH 3/4 is the highest-leverage move.

    ----- CLAIM 4 (GENUINE FUZZY UNIFICATION, FEASIBILITY NOTE, FOLDED). TAG: REAL-LLM-READ. -----
    The fuzzy-unification experiment (art_I22c-J7-OcXl) retired the iter-4 circular Mode-P: vague prepositions / informal kinship terms yield CALIBRATED sub-1.0 disjunctions (fraction-at-1.0 = 0.00 vs Mode-P's 1.00; per-candidate ECE 0.142 spatial / 0.111 kinship); the distinctive Mode-B catch (around -> {NTPPi,TPPi} drops gold EC => collapse => abstain; 5/5 sound-violating spatial reads caught, 0 silent-wrong missed; kinship UNTESTED, 0 unsound reads). Per reviewer scope MINOR, FOLD this into a single short FEASIBILITY appendix together with the operational ~3000-char case study (CLAIM 6). Keep the supporting query-level cert CW 0.000 vs commit-argmax 0.364/0.216 (CIs exclude 0, art_0MDLD-w-RXOu) but flag the query-vs-edge unit-of-analysis caveat. Establishes feasibility on commodity hardware, NOT a substantive contribution.

    ----- CLAIM 5 (SUPPORTING NEGATIVE): CROSS-PATH CODING IS SYNTHETIC-CHANNEL-ONLY. TAG: GOLD-ONLY-GATE + SYNTHETIC-CONTROL. -----
    The cross-path-intersection coding mechanism is established at power ONLY on synthetic channels and FAILED on BOTH a-priori-gated real venues for opposite reasons (temporal Allen reads near-universe 0.87, intersection/best-single/naive all resolve 0/125, deepseek MORE conservative 0.99, art_0AIWMhwc1pJM; spatial RCC-8 reads informatively but gold is a containment TREE with one edge-disjoint path per query, art_i53dBKgGY3Ig). Synthetic positive controls confirm the mechanism when both conditions hold (Allen +0.259 selective accuracy CI [0.177,0.349]; RCC-8 0.890 vs 0.797). Present as an explanatory account of two gated-venue negatives, NOT a law; do NOT re-run RCC-8 (the negative is clean, needs no LLM).

    ----- CLAIM 6 (NATURAL TEMPORAL TEXT: certificate only WEAKLY protective; OPERATIONAL CASE STUDY FOLDED). TAG: REAL-LLM-READ. -----
    On natural temporal text the raw LLM out-accuracies Mode-A at matched coverage (0.699 vs 0.575); the corrected fixed-operating-point H1 CIs INCLUDE 0 (vs PoT +0.027 [-0.088,0.140]; vs SC +0.035 [-0.061,0.135]; the earlier CONFIRM was a bootstrap artifact, art_Vc1UBGIVSi0T). Among ~19% Mode-A commits, 42.5% confident-wrong, all silent-wrong-narrowing. A $0 synthetic backstop (recall 0.96) gives Mode-A +0.225 over raw, isolating read-soundness as the binding constraint. FOLD the operational ~3000-char bracket-selected arm (95 Prolog programs discharged & executed in swipl 9.0.4; hallucination reduction 0.27-0.60 / mean 0.45 at Mode-A coverage 0-0.33; atomic recall ~0.49 the binding ceiling, art_WQoePKrpsTPo) into the single FEASIBILITY appendix; CUT the concatenated-kinship arm entirely (56/56 cross-story abstentions trivial by construction). Label documents bracket-selected; state the pipeline RUNS at length, not that it is USEFUL at length. Supporting, not a headline.

    ----- CLAIM 7 (MECHANISM ANALYSIS / APPENDIX, DEMOTED). TAG: REAL-LLM-READ-ON-SYNTHETIC + SYNTHETIC-CHANNEL + THEOREM. -----
    Compact appendix, labeled inherited/synthetic/textbook: (7a) ALGEBRA-RICHNESS SCALING (point +0.043 -> RCC-8 +0.448 -> Allen +0.676; INHERITED table-vs-LLM-composition at recall ~1.0; the +0.676 decomposes +0.673 inherited / +0.0025 novel); (7b) REDUNDANCY INVERTED-U on a realism-matched channel (Page p ~ 5e-4, peak K* = 2,4,7,10,16 for recall 0.5->0.95, silent-wrong 0.006->0.146 bounded by (1-r)); (7c) the ZERO-FP soundness THEOREM (all-sound contributing edges => gold in Mode-A output w.p. 1.0; verified on 100,296 networks; recall and rho are INPUTS, so it characterizes rather than predicts a real-text operating point). None competes with the diagnostic headline.

    ----- CLARITY FIX: RE-DOCRED + LOCATED-IN COUNTS PER-DATASET. -----
    Kinship: re-docred PRIMARY slice = 360 present multi-hop (222 composed-only / non-circular) + 368 absent; the 476/476 present and 577/577 absent engine round-trip is the COMBINED re-docred (360/368) + docred (116/209) verification (docred absent gold DOWNGRADED ~64.6% false-negatives). Located-in: 515 present (400 held-out + 115 never-annotated) / 450 sibling-absent / 250 different-component-absent over 283 docs / 1,215 queries (count_reconciliation in art_4xy3D05YxvRr). Removes the apparent count inconsistencies.

    ----- METHOD CORE (unchanged in substance; re-scoped). -----
    MODE A (SOUND NARROWING / no-derivation abstention, PRIMARY, READ-SOUNDNESS-CONDITIONAL zero-FP): high-recall sub-universal disjunction per span; compose+intersect through the EXACT table -> EMIT singleton / ABSTAIN disjunction / ABSTAIN 'no relation' on no-derivation. The cross-path-INTERSECTION variant is SYNTHETIC-ONLY-at-power (CLAIM 5); CLUTRR, kinship, and located-in use a union-fixpoint, not intersection. MODE B (DETECTION/REPAIR, SECONDARY): empty closure certifies an UNSOUND read (gold-free, recall-conditional). BASELINES: every certificate comparison includes (i) the CONFIDENCE-THRESHOLDED RAW-ABSTAIN battery (verbalized + sc_margin + P(True) + semantic-entropy negentropy) at MATCHED coverage, AND (ii) a QUERY-SIDE FALSE-PREMISE VERIFIER — same-model relatedness + self-verification AND a stronger cross-family (deepseek-v3.2 k=5) instantiation, the latter reported on its OWN subsample — alongside always-answer commit-the-argmax, PoT, and self-consistency. EXTRACTION (the now-binding lever): default prompt extraction recall is the ceiling on natural prose (located-in 0.148, kinship 0.376); prompt-only boosting raises recall ONLY by buying precision (art_fXvxt4JO9hWy); a PRECISION-PRESERVING (fine-tuned / constrained-decoding) extractor is the iter-10 intervention. GENERALITY, TEMPERED: EXACT only on the convex point algebra (PC complete); Allen IA and RCC-8 are SOUND LOWER BOUNDS; kinship and located-in are finite composition tables, NOT relation algebras, NOT cross-path-intersection venues.

    ----- HONESTY COMMITMENTS. -----
    (1) Evidence-class tags (THEOREM / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / REAL-LLM-READ / REAL-LLM-READ-ON-SYNTHETIC) live in the SPINE TABLE and section headers, NOT inline in prose (de-densify per reviewer presentation MINOR). (2) Do NOT call CLUTRR natural — it is TEMPLATED (<=871 chars, hand-supplied table). (3) The certificate MECHANISM is the INHERITED NeSy premise (+0.673 inherited / +0.0025 novel); the candidate NOVELTY is the DIAGNOSTIC (FACT A + capability gap) + the CATCHING win + the recall-precision frontier; the certificate-as-FIX is PENDING a precision-preserving natural net win. (4) Position the diagnostic as a COMPOSITIONAL false-premise instance; cite the RE NO_RELATION cluster (DEPTH/Li2024/Pi2025), the premise-verification cluster (Qin2026/Sansford2024), and FalseQA/AbstentionBench/Wen2024; DROP 'not derivable a priori'; add the one ontology-grounded-post-extraction-correction distinguishing sentence; VENUE = ACL Knowledge Extraction PRIMARY, NeSy FALLBACK. (5) FACT A transfers (corpus/domain/reader); FACT B is reader- and signal-dependent (16-cell survival/caught table); do NOT claim family-level / reader-diverse blindness. (6) The CLUTRR-absent abstention is STRUCTURAL-BY-CONSTRUCTION; the sibling caught-objective win is non-by-construction but ONE-SIDED (targeting quality, not net-utility) and must be paired with the extraction-gated caveat. (7) The natural-prose net-utility boundary is EXTRACTION-LIMITED and FUNDAMENTAL for prompt-only extraction (recall is precision-bought; slope -0.30 / -0.67; gold-read ceiling 1.0/1.0/1.0). (8) Report the stronger cross-family verifier on its OWN n=60 subsample (cert 0.667 / weak 0.20 / stronger 0.10 / self-verify-strong 0.533), never beside the n=450/135 numbers. (9) Cross-path coding is SYNTHETIC-CHANNEL-ONLY. (10) zero-FP is READ-SOUNDNESS-CONDITIONAL. (11) Report every hallucination number WITH coverage/abstention. (12) SWI-Prolog execution reported truthfully. (13) DEDUCTION SUB-MODULE only — OpenCyc grounding, atomic re-extraction, general fuzzy unification, and genuine ~3000-char documents are FUTURE WORK NOT CLAIMED; fold the operational + fuzzy notes into one feasibility appendix.

    SUCCESS / DISCONFIRM (re-centered on the diagnostic + the precision-preserving-extractor net win). CONFIRM if: (i) FACT A and the MIXED-POOL CAPABILITY GAP reproduce, reported honestly per-signal/reader/corpus, engaging the RE-NO_RELATION + premise-verification + false-premise literature with a query-side verifier baseline (same-model AND stronger cross-family on its own subsample) — the corpus-robust DIAGNOSTIC; AND (ii) the certificate's Holm-adjusted MIXED-POOL confident-wrong reduction EXCLUDES 0 on natural prose under a PRECISION-PRESERVING extractor (PATH 3) or a naturally-high-recall domain (PATH 4) AND it matches/beats the query-side verifier — the DEMONSTRATED FIX; AND a SWI-Prolog-executed pipeline reports atomic P/R, multi-hop accuracy, trace-graphs, and abstention beside every hallucination number. DISCONFIRM / SCOPE-BOUNDARY (each publishable): some confidence signal robustly filters confident absent hallucinations at matched coverage for the deployed reader (=> FACT B reader-defeated, diagnostic narrows to verbalized confidence / weaker readers); OR even a precision-preserving extractor cannot lift the mixed-pool reduction CI above 0 because the recall-precision tradeoff is structural to natural-prose extraction (=> certificate net utility is FUNDAMENTALLY extraction-bound on natural text — a deeper boundary than 'prompt-only' — while FACT A + the capability gap + the catching win survive); OR the query-side false-premise verifier (same-model or stronger) already catches the fabrications as well as the certificate (NOT observed: stronger verifier is WORSE, 0.10 vs cert 0.667 on its subsample); OR cross-path intersection never beats single-path on any real multi-path stratum (already observed => coding mechanism honestly synthetic-only).
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
  it enforces consistency under the F1-maximizing COMMIT contract (which it shows fails); no closure-as-CERTIFICATE, no preserved
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
  Same certificate-diagnostic frame; PATH-2 prompt-fix refuted, decisive test now a precision-preserving extractor.
_confidence_delta: unchanged
_key_changes:
- >-
  RETIRED PATH 2 (raise natural-prose extraction recall via better prompting) as EXECUTED -> FAILED: art_fXvxt4JO9hWy swept
  >=6 prompt-only strategies; recall is PRECISION-BOUGHT (corr(recall, sibling-confident-wrong)=0.91), so the worst-case mixed-pool
  reduction moves AWAY from a flip as recall rises (CI-lower slope -0.30 located-in / -0.67 kinship). No prompt strategy flips
  the fork on either domain.
- >-
  REDEFINED the decisive iter-10 test as a PRECISION-PRESERVING (lightly fine-tuned / constrained-decoding) extractor on ONE
  domain (PATH 3), with a naturally-high-recall semi-structured input as a cheaper alternative (PATH 4) — the only surviving
  routes to a deployable net-utility win, per the experiment's own conclusion and the reviewer.
- >-
  FRAMED the natural-prose net-utility boundary as FUNDAMENTAL for prompt-only extraction (a quantified recall-precision frontier
  with measured slope + gold-read ceiling 1.0/1.0/1.0), upgrading iter-8's bare 'extraction-limited boundary' into a publishable
  mechanism.
- >-
  FIXED the stronger-verifier rigor MAJOR: report deepseek-v3.2 k=5 on its OWN n=60 subsample (cert 0.667 / weak same-model
  0.20 / stronger 0.10 / self-verify-strong 0.533), never beside the main n=450/135 numbers (cert 0.785 / verifier 0.274).
- >-
  RE-SCOPED the 0.785 caught-objective win as TARGETING QUALITY not deployable net-utility (one-sided pure-absent objective
  favors high-abstention methods); mandated pairing it with the extraction-gated caveat in abstract/intro/contributions/conclusion.
- >-
  MARKED the NOVELTY MAJOR RESOLVED via art_mxFG0bGhTe2- (RE NO_RELATION lit: DEPTH/Li2024/Pi2025; premise-verification: Qin2026/Sansford2024);
  DROPPED 'not derivable a priori'; re-carved the two-part SETTING+METHOD delta.
- >-
  UPDATED venue to ACL Knowledge Extraction PRIMARY / NeSy FALLBACK (reversing prior NeSy-primary call, matching the user's
  stated publication target).
- >-
  ADDED one required distinguishing sentence (reviewer novelty MINOR) separating the no-derivation certificate from ontology-grounded
  POST-EXTRACTION structural correction (arXiv:2605.29168).
- >-
  CONFIRMED certificate-necessity is intrinsic (a stronger cross-family verifier is WORSE, over-infers co-regional containment)
  — retires methodology MINOR #5.
- >-
  DE-DENSIFICATION + scope: move evidence tags into the spine table/headers, delete inline markers and reviewer-response meta-narration,
  collapse the 7-paragraph intro, and FOLD the operational ~3000-char note + fuzzy-unification note into a single feasibility
  appendix.
- >-
  Confidence UNCHANGED: PATH 2 closed (one of two upgrade routes) but the descriptive core firmed up (recall-precision frontier,
  stronger-verifier robustness, strengthened novelty positioning); the binding significance ceiling and the path to lifting
  it (fine-tuned extractor) are now sharply defined.
relation_type: evolution
</hypothesis>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: research_iter10_dir3
type: research
objective: >-
  Retire the remaining novelty MINOR and preempt the obvious KE reaction to a supervised extractor. (a) Pin arXiv:2605.29168
  (ontology-grounded post-extraction structural correction for KG construction) and its closest 1-2 neighbors with verified
  BibTeX and the ONE drop-in distinguishing sentence separating the no-derivation certificate (per-query, gold-free abstention
  from deductive closure over the DOCUMENT-INTERNAL graph) from ontology-grounded post-extraction correction (repairs/commits
  a labeling against EXTERNAL structure), preserving the gold-free / training-free / no-external-KB delta. (b) Pin the framing
  that iter-10's precision-preserving SUPERVISED extractor is an INTERCHANGEABLE COMPONENT (any precision-preserving extractor
  works; the headroom is purely extraction per the gold-read ceiling) and is NOT the contribution — so a KE reviewer does
  not conflate it with the DEPTH/Li2024/Pi2025 NO_RELATION-refiner novelty; the contribution remains the compositional false-premise
  DIAGNOSTIC + the gold-free structural CERTIFICATE. (c) Final ACL-Knowledge-Extraction-primary venue framing note (NeSy fallback).
approach: >-
  Pure web research ($0, no code). aii-web-tools (search -> fetch -> fetch_grep) + aii-semscholar-bib for BibTeX. WORKSTREAM
  1 (novelty MINOR): pin arXiv:2605.29168 with verified BibTeX (project key, venue/year/authors), method TYPE, and 1-2 verbatim
  quotes establishing that it repairs/commits a labeling against EXTERNAL ontological structure; identify the 1-2 closest
  ontology-grounded / KG-construction post-extraction-correction neighbors; write the single drop-in distinguishing sentence
  for the 'Closure over machine-extracted relations' / premise-verification paragraph (no-derivation certificate = per-query
  gold-free abstention from deductive closure over the document-internal graph vs ontology-grounded post-extraction correction
  = repairs/commits labels against external structure; gold-free / training-free / no-external-KB delta preserved). WORKSTREAM
  2 (preempt the supervised-extractor KE reaction, building on [ARTIFACT:art_mxFG0bGhTe2-]): pin the crisp 1-2-sentence framing
  that the precision-preserving supervised extractor is standard RE plumbing / an interchangeable component (supervised, distilled,
  or constrained-decoding — all precision-preserving — interchange freely; the gold-read ceiling 1.0/1.0/1.0 shows the headroom
  is purely extraction), and the CONTRIBUTION remains the diagnostic + the gold-free, training-free, no-external-KB structural
  certificate that catches multi-hop document-internal absent-relation premises where the confidence family AND a query-side
  verifier fail — explicitly NOT the extractor — so introducing it does not muddy the novelty against DEPTH/Li2024/Pi2025.
  WORKSTREAM 3 (final venue polish): a short ACL-Knowledge-Extraction-primary framing note (atomic + multi-hop extraction
  P/R foregrounded; RE NA-problem lead) with NeSy fallback, consistent with the brief. OUTPUT research_out.json {answer, sources,
  follow_up_questions} + research_report.md with the verified BibTeX block (new key for arXiv:2605.29168 + reused keys), the
  distinguishing sentence, the extractor-as-component framing sentences, and the venue note.
depends_on:
- id: art_mxFG0bGhTe2-
  label: extends
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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
out_dependency_files:
  file_list:
  - research_out.json
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for research artifacts:
  - cpu_light: 4 vCPUs, 16GB RAM — proofs, research, lightweight tasks (fallback: memory-optimized CPUs first (cpu3m → cpu5m), then GPU hosts last-ditch)

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
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
  "description": "Plan for a RESEARCH artifact.",
  "properties": {
    "title": {
      "description": "Short title for the plan",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "question": {
      "default": "",
      "description": "The specific research question to investigate",
      "title": "Question",
      "type": "string"
    },
    "research_plan": {
      "description": "Step-by-step plan for web research to gather this research",
      "title": "Research Plan",
      "type": "string"
    },
    "explanation": {
      "description": "Why this research matters and what question it answers",
      "title": "Explanation",
      "type": "string"
    }
  },
  "required": [
    "title",
    "research_plan",
    "explanation"
  ],
  "title": "ResearchPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-18 08:33:35 UTC

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
