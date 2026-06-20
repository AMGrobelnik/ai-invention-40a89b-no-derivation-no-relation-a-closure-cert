# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 17:40:35 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation

<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: >-
  Closure-Certified Composition for the LOCAL-Reader Deduction Module of a Text-to-Logic Pipeline: Iterated Path-Consistency
  Error-Corrects Span-Local LLM Reads (Synthetic-Validated and Discharged End-to-End in Prolog), the Zero-FP Certificate is
  Read-Soundness-Bounded, and Real-Text Read-Soundness is the Measured Bottleneck
hypothesis: |-
  LEAD -- FOUR ARM-SCOPED CLAIMS, EACH WITH A GENUINE DISCONFIRMER, NOW CENTERED ON THE LOCAL-READER PIPELINE REGIME WHERE iter-1 EVIDENCE SHOWS CLOSURE ACTUALLY HAS WORK TO DO (read first; everything below elaborates).

  (LOCAL-READER VALUE CLAIM -- THE NEW HEADLINE.) In a MODULAR pipeline that reads each event/entity pair from ONLY its local span (the architecture a text->FOL/Prolog pipeline must use to build a reusable knowledge base, not to answer one query from the whole document), composing those span-local LLM reads by ITERATED path-consistency closure recovers deduction-required relations the local reads alone cannot, achieving strictly higher SELECTIVE ACCURACY AT MATCHED COVERAGE than (a) the local raw LLM forced to a single relation, (b) Path-of-Thoughts, and (c) self-consistency voting, AND cutting the CONFIDENT-WRONG (hallucination) rate versus the local raw LLM on absent-relation pairs -- both CI-separated under paired bootstrap. SCOPE CORRECTION FORCED BY iter-1: closure provides essentially NO net gain over a FULL-CONTEXT reader (measured delta<=0; best closure singleton-to-correct 0.172 vs direct full-context read 0.184), because a reader given the whole document already reconstructs the global evidence closure would; the iter-1 local-only probe pins gold only 26.7% of the time, so closure's value is DEFINED ONLY against a local reader, and that is the comparison we run. DISCONFIRMED if closure-over-local-reads beats NEITHER the local raw LLM NOR PoT/voting at matched coverage -- in which case the contribution becomes the negative localization plus the synthetic mechanism, honestly targeted at NeSy / a findings/short track.

  (END-TO-END DELIVERABLE CLAIM -- THE PROJECT-GOAL ANCHOR, no longer 'can be discharged'.) The closed QCN is emitted as executable Prolog/ASP, the held-out query is DISCHARGED in SWI-Prolog, and we report an ACTUAL quantified hallucination-rate reduction versus raw LLM generation on real documents in the local-reader regime -- the project's literal deliverable, which iter-1 only described as hypothetical. CLUTRR kinship (an explicitly named target benchmark, naturally span-local, composition-required, with a finite kinship composition table) is the clean end-to-end venue that delivers all four required numbers at once: atomic-extraction precision/recall, multi-hop deduction accuracy, human-auditable trace-graphs, and the hallucination-rate reduction; the temporal corpora supply the harder, naturalistic arm. DISCONFIRMED if no end-to-end hallucination reduction materializes at the pre-registered minimum effect on any real venue.

  (ITERATION CLAIM -- RELOCATED OFF THE DENSE TIMELINE.) FULL ITERATED closure beats NAIVE single-pass intersection with a gap that GROWS in hop-count and cyclomatic number, demonstrated on synthetic long-hop/cyclic networks AND on SPARSE long-hop real gold (TDDMan, where iter-1 found the genuine signal: full_only=12, 408 vs 396 resolved) -- NOT on dense timelines (NarrativeTime full_only=0, near-transitively-closed, where iteration provably ties single-pass and 'recovery' is guaranteed, not earned). DISCONFIRMED if full==naive even on sparse multi-hop/cyclic queries (then the contribution is 'any intersection,' not ITERATION).

  (REDUNDANCY CLAIM -- UNCHANGED IN FORM, RE-TAGGED AS CHANNEL-SIMULATION EVIDENCE.) At fixed per-edge recall, net Mode-A gain is an INVERTED-U in path redundancy whose peak moves outward with recall (iter-1 synthetic: K*=2,4,5,5,8 for recall 0.5->0.95) and shifts under a recall-floor gate; the genuine disconfirmer is the ABSENCE of any redundancy region beating BOTH best-single-path and naive-intersection -- a flat/turned-over curve ALONE is the predicted recall x redundancy interaction, not a disconfirmation. HONEST CAVEAT (reviewer): recall and rho are INPUTS to the iter-1 simulated channel, not measured outcomes, so this is currently a property of a controlled channel -- to be reproduced with a channel whose breadth knob genuinely trades recall for bite and whose per-edge error-type distribution matches real reads (TV<=0.10) before any transfer to real text is implied.

  WHAT iter-1 ESTABLISHED, TAGGED BY EVIDENCE CLASS (so no result is over-weighted). (THEOREM / SANITY-CHECK, not empirical discoveries): the zero-FP certificate (all contributing reads sound => gold in output with probability 1.0) is the soundness invariant of path-consistency, verified on consistent-by-construction data; the N*=25,450 'exact recovery' on NarrativeTime is GUARANTEED because a dense human timeline IS a globally-consistent point network that closure trivially recovers; the gate's discriminativeness (MATRES N*=0 vs NarrativeTime 25,450) merely restates the corpora's annotation-distance distributions. These are design validations, NOT the contribution. (GENUINE SYNTHETIC EMPIRICAL FINDINGS): the iteration gap growing with hop/cyclomatic (Page p~=1.2e-4 -- CORRECTED from the paper's mis-stated 1e-13; the gap is recall-dependent, e.g. L=6 gap 0.99 at recall~=1.0 but 0.63 at recall 0.90, so it MUST be reported per-recall-slice); the recall-dependent inverted-U; and the silent-wrong rate (5.8% pooled) as a function of per-edge recall. (GOLD-ONLY GATE): the a-priori envelope per corpus. (REAL LLM READS -- the one real negative result): the recall-bite frontier NO-GO (no real arm cleared the soundness gate at the tested cheap reader). The contribution's empirical weight must rest on the GENUINE FINDINGS plus the NEW local-reader and end-to-end tests, never on the theorems.

  THE SIX FIXES THIS ITERATION (each tied to an iter-1 finding or a reviewer critique).
  FIX 1 -- RELOCATE VALUE TO THE LOCAL-READER REGIME. iter-1 showed closure ~= full-context read (delta<=0) yet local reads miss ~73% of deduction-required gold; so the head-to-head is closure-over-LOCAL-reads vs {local raw LLM, PoT, voting}, NEVER vs a full-context oracle. This is also the only setting consistent with the project's modular text->FOL pipeline (atomic facts must be extracted span-by-span to populate a reusable knowledge base).
  FIX 2 -- DELIVER THE END-TO-END SLICE FOR REAL. Emit Prolog/ASP from the closed QCN, discharge in SWI-Prolog, and report an ACTUAL hallucination-rate number. Promote CLUTRR to a Tier-1 end-to-end venue (atomic P/R + multi-hop accuracy + trace-graph + hallucination reduction in one). Stop describing discharge as hypothetical.
  FIX 3 -- ACTUALLY RUN THE BASELINES. The seven enumerated baselines (raw LLM, CoT, self-consistency, LINC-style voting, Path-of-Thoughts, ILP-commit, naive single-pass) were NEVER executed in iter-1, so the central comparative claim ('Mode A beats PoT and voting') was unsupported. Run them at matched coverage AT LEAST on the synthetic backbone (mechanism works at recall 0.96) AND on the local-reader real slice. Any baseline not run is REMOVED from the protocol, not left as a promise.
  FIX 4 -- QUALIFY THE CERTIFICATE AS READ-SOUNDNESS-BOUNDED. Everywhere, state 'zero-FP CONDITIONAL ON READ-SOUNDNESS.' Report the silent-wrong rate as an explicit function of per-edge recall; state the per-edge bound (1-recall) and per-network bound (1-J(E)); make explicit that the certificate is STRONGEST where reads are already good and WEAKEST in the real low-recall regime where it is most needed -- the honest tension, surfaced, not hidden in the abstract.
  FIX 5 -- UN-CONFLATE NarrativeTime FROM TimeBank-Dense AND POWER THE BOTTLENECK CLAIM. iter-1 read TimeBank-Dense as a 'NarrativeTime stand-in' (deduction-required fraction 0.039) while transferring NarrativeTime's gate applicability (0.882) -- a ~22x mismatch. Run LLM reads on the ACTUAL NarrativeTime gold graphs (delivered in the dataset artifact) so the 0.882 applicability is exercised with real reads. Scale the closure-vs-direct deduction-triangle sample by >=10x (iter-1 used n=7 for TimeBank-Dense, with closure scoring WORSE 0.172 vs 0.184), report CIs on the closure-minus-direct delta, and test >=2 readers INCLUDING one substantially stronger model -- the recall ceiling 0.58-0.86 may be a weak-model property, and a reader crossing the 0.85/0.90 gate would directly confirm or falsify the read-soundness-bottleneck headline.
  FIX 6 -- REPAIR THE SYNTHETIC CHANNEL'S REALISM. iter-1 breached its own pre-registered TV<=0.10 (measured TV=0.25, 2.5x over) and its breadth knob produced identical recall (0.958) across all five settings S1-S5, so the recall-bite trade-off was never exercised on synthetic data. Either tune the noisy channel to TV<=0.10 with a breadth knob that GENUINELY trades recall for bite, or explicitly downgrade ALL synthetic results to 'mechanism characterization under an idealized channel' with no implied transfer to real-text behavior.

  MODE A (SOUND NARROWING, PRIMARY, READ-SOUNDNESS-CONDITIONAL zero-FP). The local reader emits per span a high-recall sub-universal disjunction (with an explicit universal/underdetermined option); intersecting the compositions arriving at the query pair from multiple constraining paths yields a still-sound, strictly-tighter set. The load-bearing metric is SINGLETON-RESOLUTION-TO-CORRECT (intersection collapses the query to the single correct relation), the only yield that moves matched-coverage selective accuracy and the hallucination rate; strict-tightening is reported separately and stated non-load-bearing. Mode A needs only sub-universal breadth + multi-path bite, not over-commitment; it is inert only in the all-universal limit; its zero-FP property survives PC incompleteness (intersection of sound sets is sound) but is CONDITIONAL on every contributing read being sound.
  MODE B (DETECTION/REPAIR, SECONDARY). An empty closure certifies that some read is UNSOUND -- a gold-free, zero-FP DETECTION flag (conditional on recall) -- carrying the pre-registered dual of SILENT WRONG NARROWING (an unsound set OMITTING gold drives a confident WRONG singleton with no collapse); magnitude tracks the measured over-commitment rate; Reiter-style minimal-hitting-set repair (which can mislocalize) is reported distinctly from Mode A.
  ITERATION ISOLATION. Naive = single-pass query-node intersection (no fixpoint, no algebra-seeded converse propagation) = 'PoT plus one obvious intersection step'; it COINCIDES with full closure on length-2 multi-path queries (verified) and diverges on >=3-edge/cyclic structure, so the full-minus-naive gap isolates ITERATED path-consistency -- built on TDDMan + synthetic long-hop, NOT on the dense timeline.
  LOCAL-READER REGIME (load-bearing definition). A local-only reader sees ONLY the minimal span(s) where two events co-occur (or flags 'no shared span'); edges it confidently and correctly names are DIRECTLY-READABLE, the rest are DEDUCTION-REQUIRED (obtainable only by composing >=2 edges). The honest pipeline reads atomically/locally to populate the FOL knowledge base, THEN composes -- so closure's value is measured exactly here, never against a full-context oracle that bypasses the modular architecture.

  REDUNDANCY AS A CODING RATE, AUDITED ON EMPIRICAL JOINT SOUNDNESS. Mode A's zero-FP narrowing holds only when EVERY contributing edge is sound; a single LLM reading one document produces positively-correlated errors, so instead of the independence product prod_e r_e we MEASURE the empirical joint soundness J(E) and report the within-document cross-edge error correlation rho. The inverted-U cost term is 1-J(E); positive rho makes J(E) decay slower than r^E, pushing the peak outward. iter-1 confirmed J(E)>r^E (e.g. J(2)=0.55>0.48, J(3)=0.34>0.33 with rho=0.10) -- but, per FIX 6, this must be re-shown on a realism-matched channel before transfer.

  GENERALITY, TEMPERED (reviewer). EXACT only on the convex point algebra (PC complete; a timeline is a partial order); Allen IA and RCC-8 numbers are SOUND LOWER BOUNDS (PC incomplete); RCC-8 is untested on real text and CLUTRR kinship is a finite composition table, not a full relation algebra. Generality is scoped to 'demonstrated on convex point (exact) + Allen (lower bound) + kinship composition (end-to-end)', with an RCC-8 real-text spatial arm as an OPTIONAL stretch, not asserted; spatial/legal framing is removed from the abstract unless backed by an executed arm.

  NOVELTY, STATED PRECISELY (reviewer). New is NOT the algebra or closure (Allen/point/RCC-8, SputLink, CAEVO, Ning 2017, Kougia 2024, Eirew 2025 are established) but (1) the disjunction-PRESERVING, abstain-on-collapse OUTPUT CONTRACT that inverts the F1-maximizing commit objective, (2) the gold-free closure CERTIFICATE, and (3) the redundancy-as-coding-rate inverted-U -- with the explicit caveat that (3) is so far a simulated-channel property (recall and rho are inputs, not measured outcomes). Situate the read-soundness finding against recent LLM temporal-consistency work (temporal referential consistency, counterfactual-consistency prompting, DNF-consistency for fact-checking), to be cited.

  SUCCESS. CONFIRM if: (LOCAL-READER) closure-over-local-reads beats the local raw LLM AND PoT AND voting at matched coverage with adjusted-CI separation, on >=1 real venue and/or CLUTRR; (END-TO-END) a Prolog-discharged pipeline shows a hallucination-rate reduction >= the pre-registered minimum vs raw LLM, with atomic-extraction P/R and multi-hop accuracy reported and a human-auditable trace-graph; (ITERATION) the full-minus-naive gap grows with hop/cyclomatic on synthetic AND TDDMan, reported per-recall-slice; (REDUNDANCY) the inverted-U with outward-moving peak at the pre-registered precision, ON A REALISM-MATCHED CHANNEL. DISCONFIRM / SCOPE-BOUNDARY if: closure adds nothing over local reads (contribution = negative localization + synthetic mechanism, retargeted to NeSy/findings); no end-to-end hallucination reduction at the minimum effect; full==naive on multi-hop/cyclic; or no realism-matched channel reproduces the inverted-U.

  HONESTY COMMITMENTS. (1) TAG every reported number as THEOREM / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / REAL-LLM-READ, so its evidence class is legible; (2) zero-FP is READ-SOUNDNESS-CONDITIONAL and silent-wrong is reported as a function of recall; (3) baselines are RUN or REMOVED, never promised; (4) the real-text NO-GO stands as a measured frontier unless a stronger reader OR the local-reader regime changes it; (5) include one concrete 3-event WORKED EXAMPLE (one Mode-A narrowing path, one Mode-B collapse path) and a compact notation/metric table so a reader can immediately weight the evidence.
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
  Same closure frame; value relocated to local-reader regime + committed end-to-end Prolog slice after real-text NO-GO
_confidence_delta: decreased
_key_changes:
- >-
  Relocated the real-text value claim from dense-timeline narrowing to the LOCAL-reader regime, since iter-1 showed closure~=full-context
  reader (delta<=0) and local reads pin gold only 26.7%; the head-to-head is now closure-over-local-reads vs {local raw LLM,
  PoT, voting}, never vs a full-context oracle.
- >-
  Promoted the END-TO-END deliverable (emit Prolog/ASP, discharge in SWI-Prolog, report an ACTUAL hallucination-rate reduction)
  to a headline and added CLUTRR as the clean end-to-end venue delivering atomic P/R + multi-hop accuracy + trace-graph +
  hallucination number at once -- addressing the project-goal disconnect.
- >-
  Required actually RUNNING the seven enumerated baselines at matched coverage (synthetic backbone + local-reader real slice);
  unrun baselines are removed, not promised, fixing the unsupported central comparative claim.
- >-
  Qualified the certificate everywhere as 'zero-FP CONDITIONAL ON READ-SOUNDNESS', required reporting silent-wrong rate vs
  per-edge recall, and explicitly tagged theorems/sanity-checks (zero-FP invariant, N*=25,450 recovery, gate discriminativeness)
  vs genuine empirical findings.
- >-
  Un-conflated NarrativeTime (gate applicability 0.882) from the TimeBank-Dense stand-in actually read (0.039); require reads
  on the actual NarrativeTime gold, >=10x deduction-triangle samples with CIs, and >=2 readers including a substantially stronger
  model.
- >-
  Relocated the iteration claim off the dense timeline (full_only=0, recovery guaranteed) onto TDDMan (full_only=12, the genuine
  signal) + synthetic long-hop.
- >-
  Flagged the synthetic realism breach (TV=0.25 vs pre-registered <=0.10) and the identical-recall breadth knob (0.958 across
  S1-S5); require a realism-matched channel with a knob that genuinely trades recall for bite, or an explicit downgrade to
  'idealized channel'.
- >-
  Corrected the Page p-value (1.2e-4, not 1e-13) and required per-recall-slice reporting of the iteration gap (0.99 at recall~1.0
  vs 0.63 at recall 0.90).
- >-
  Tempered generality to convex-point (exact) + Allen (lower bound) + kinship composition (end-to-end); RCC-8 real-text and
  spatial/legal framing made optional/removed unless an arm is executed.
- >-
  Sharpened the novelty statement (the new piece is the output contract + certificate + coding-rate framing, NOT the algebra)
  and required citing recent LLM temporal-consistency work; added a worked-example + notation-table requirement for clarity.
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

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
in_dependencies:
- id: art_aQ2Rf8rwqteI
  label: extends
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
in_dependencies:
- id: art_ghVQmxVlmOJJ
  label: dataset
- id: art_aQ2Rf8rwqteI
  label: baseline-specs
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
in_dependencies:
- id: art_ghVQmxVlmOJJ
  label: dataset
- id: art_aQ2Rf8rwqteI
  label: specs
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
in_dependencies:
- id: art_PNrS9T8JeATf
  label: dataset
- id: art_aQ2Rf8rwqteI
  label: baseline-specs
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
</all_artifacts>

<new_artifacts_this_iteration>
These 5 artifacts were created THIS iteration.

id: art_Dm5vYXmD1R8h
type: research
in_dependencies:
- id: art_aQ2Rf8rwqteI
  label: extends
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

id: art_N0e4pH_C_Cxw
type: experiment
in_dependencies:
- id: art_ghVQmxVlmOJJ
  label: dataset
- id: art_aQ2Rf8rwqteI
  label: baseline-specs
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

id: art_FtN4LBzazO_l
type: experiment
in_dependencies:
- id: art_ghVQmxVlmOJJ
  label: dataset
- id: art_aQ2Rf8rwqteI
  label: specs
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

id: art_fil2iJ6xSrYx
type: experiment
in_dependencies:
- id: art_PNrS9T8JeATf
  label: dataset
- id: art_aQ2Rf8rwqteI
  label: baseline-specs
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
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.


# Introduction

A growing class of systems reads a short, professionally written document---a news report, a contract clause, a children's story---into a formal representation (first-order logic predicates, Prolog facts) that a symbolic reasoner can execute, with a large language model (LLM) resolving the terminology, concepts, and relations the surface text leaves implicit. Such a pipeline promises auditable, replayable reasoning over text, but it has a structurally identifiable weak link. Atomic extraction---naming the entities and the relations that hold between locally co-occurring mentions---is by now something LLMs do competently. The \emph{deduction} step is where faithfulness breaks: synthesizing the explicitly stated facts with implicit composition knowledge to answer a query about a pair of entities that never co-occur in any single span. This multi-hop relational reasoning is what the user ultimately cares about, and it is exactly where hallucination is most damaging and hardest to detect.

Faithful multi-hop relational reasoning over text matters wherever the cost of a confidently wrong answer is high: ordering the events in a news story, tracking kinship in a narrative, resolving containment in a description, chaining clauses in a legal document. The relations involved---temporal order, kinship, spatial containment---are precisely those for which mathematics has supplied exact \emph{composition laws} for forty years: Allen's interval algebra \citep{Allen1983}, the convex point algebra \citep{Vilain1986}, the region connection calculus RCC-8 \citep{Randell1992}, and the path-consistency constraint-propagation algorithms over them \citep{Mackworth1977}. If a document says event $A$ is before $B$ and $B$ is before $C$, the relation between $A$ and $C$ is not a matter of opinion to be guessed; it is fixed by an exact table. The opportunity is to make an LLM-driven pipeline reason with these laws rather than around them.

The deduction step is hard because the obvious ways of using an LLM fail in characteristic ways. Composing freely, the LLM is locally fluent but globally inconsistent: it can assign more than one temporal relation to the same pair and violate transitivity, producing silent errors that an answer-level vote \citep{Wang2022} or a solver-crash signal \citep{Pan2023} cannot see. Reasoning each path in isolation---the strategy of backward chaining \citep{Kazemi2022} and Path-of-Thoughts \citep{Zhang2024}---deliberately avoids the global check, so it can neither tighten a disjunctive query by intersecting evidence from multiple paths nor detect a contradiction arriving at the same pair from two routes. Hand-crafting composition rules (the kinship rules behind CLUTRR \citep{Sinha2019}) does not scale, and inducing rules to fit task accuracy \citep{Zhang2023, Zhu2023} optimizes data fit rather than the algebraic laws needed for soundness.

Why has this not been solved? Because the recent lineage attacks it under the wrong output contract. A 2024 study of zero-shot temporal extraction finds LLMs assign multiple relations to over half (up to $97\%$) of pairs and violate transitivity, then enforces consistency with integer linear programming (ILP) and reports that consistency enforcement \emph{does not improve} F1 \citep{Kougia2024}; the most recent global temporal-graph generator (EMNLP~2025) still aggregates generations and ILP-commits to a single label per pair, preserving no disjunction, issuing no certificate, and offering no abstention \citep{Eirew2025}. Classical temporal closure (SputLink densifies TimeBank \citep{Verhagen2005}; CAEVO does global inference by cascaded sieves \citep{Chambers2014}; structured learning enforces transitivity \citep{Ning2017}) likewise commits to one consistent labeling to maximize F1. The newest LLM temporal-consistency work---measuring sequence-vs-absolute consistency \citep{Bajpai2025}, counterfactual-consistency prompting \citep{Kim2025}, and propositional consistency for fact-checking \citep{Ghosh2024, Bajpai2024}---still optimizes an accuracy/commit objective and preserves no relation-algebra disjunction. We read this as evidence that consistency enforcement under the F1-maximizing \emph{commit} contract is the wrong objective. The LLM's native multi-relation output is not noise to be collapsed; it is a \emph{sound disjunction} to be preserved and narrowed, and the right objective is faithfulness-by-abstention, not extraction F1.

Our approach inverts the contract. The LLM emits, per text span, a high-recall disjunctive set of base relations the span does not exclude. Because the composition tables are exact ground truth, intersecting the disjunctive sets arriving at a query pair from multiple constraining paths---via iterated path consistency---can only move toward the gold relation (Mode~A, a zero-false-positive narrowing \emph{conditional on every contributing read being sound}, needing no over-commitment and no labels), while an empty intersection certifies that some read was unsound (Mode~B, a gold-free reading-error flag). Multi-path redundancy in a document thereby becomes an \emph{error-correcting code} over LLM extractions. The coding-theory lens predicts an optimal rate: narrowing stays zero-FP only while every contributing read is sound, and that joint probability decays as redundancy grows, so net benefit is an inverted-U whose peak tracks the measured per-edge recall and the measured cross-edge error correlation. We separate, by an explicit evidence tag on every number (\textsc{theorem} / \textsc{synthetic-channel} / \textsc{gold-only-gate} / \textsc{real-llm-read}), what is a soundness theorem from what is an empirical finding from what is a real-text measurement---a discipline the previous draft lacked.

[FIGURE:fig1]

This iteration's headline is a positive, fully-powered finding obtained by actually running the comparison the previous draft only specified: a real LLM reads $2{,}520$ networks span-by-span, and \emph{all seven} enumerated baselines are evaluated at matched coverage. Mode~A's advantage over neural per-path reasoning \emph{scales with relation-algebra richness}---negligible on the simple point algebra, decisive on the rich Allen algebra. We then characterize the mechanism on a realism-matched channel (iteration error-correction; the recall-dependent inverted-U; a read-soundness-bounded silent-wrong rate), deliver an end-to-end Prolog-discharged slice with a hallucination-rate number, and---our honest negative---localize the real-text bottleneck to LLM read-soundness, not closure, with a stronger reader still short of the gate.

## Summary of Contributions

- \textbf{A matched-coverage showdown that runs every baseline, with a new scaling law} (Section~\ref{sec:showdown}): with a real LLM making span-local reads of $2{,}520$ synthetic networks, Mode~A beats Path-of-Thoughts, self-consistency, raw, CoT, LINC-vote, and ILP-commit at matched coverage on both algebras (Holm-adjusted), and the advantage over per-path reasoning \emph{grows with algebra richness} (point gap vs.\ PoT $+0.043$; Allen $+0.676$) [ARTIFACT:art_N0e4pH_C_Cxw]. This directly resolves the prior critique that no head-to-head was executed.
- \textbf{The mechanism, on a realism-matched channel} (Section~\ref{sec:mechanism}): after repairing the channel to its pre-registered realism bound (per-edge error-type total-variation distance $\le 0.0065$, down from $0.25$), iterated closure error-corrects with a gap that grows in hop length \emph{per recall slice} (Page $p\!\approx\!10^{-4}$, correcting the prior mis-stated $10^{-13}$), and net narrowing gain is a recall-dependent inverted-U with peak $K^\ast=2,4,7,10,16$ [ARTIFACT:art_FtN4LBzazO_l].
- \textbf{A read-soundness-bounded certificate} (Section~\ref{sec:certificate}): the zero-FP property is a soundness \emph{theorem} of path consistency (tagged as such, not an empirical discovery); empirically the silent-wrong rate is a decreasing function of per-edge recall ($0.146$ at recall $0.5\!\to\!0.006$ at $0.95$), bounded per-edge by $(1-\text{recall})$ and per-network by $(1-J(E))$, so the certificate is strongest where reads are already good and weakest in the real low-recall regime [ARTIFACT:art_FtN4LBzazO_l].
- \textbf{An end-to-end, auditable slice} (Section~\ref{sec:realtext}): we read \emph{the actual} NarrativeTime and TDDMan gold graphs span-locally (no TimeBank-Dense stand-in), emit the closed network as runnable Prolog with a trace, and report a confident-wrong (hallucination) reduction; and we localize the binding constraint to read-soundness---a stronger reader reaches per-edge recall $0.897$, still below the $0.90$ gate, so the bottleneck is not a weak-model artifact [ARTIFACT:art_fil2iJ6xSrYx]. We are explicit that the real-text head-to-head ($n=20$ deduction queries) is underpowered, and that OpenCyc grounding and a CLUTRR end-to-end run are prepared but not executed.

# Related Work
\label{sec:related}

\textbf{What is new, in one sentence.} Path consistency over relation algebras and consistency enforcement over machine-extracted temporal relations are both well established; our contribution is not the algebra or the closure algorithm but (1) the disjunction-\emph{preserving}, abstain-on-collapse \emph{output contract} that inverts the F1-maximizing commit objective, (2) the gold-free closure \emph{certificate}, and (3) the redundancy-as-coding-rate inverted-U (which we are careful to label a property of a controlled channel, since recall and the error correlation are inputs to it).

\textbf{Qualitative reasoning and tractability.} Allen's interval algebra \citep{Allen1983}, the convex point algebra \citep{Vilain1986}, and RCC-8 \citep{Randell1992} supply exact composition tables; Mackworth's path consistency \citep{Mackworth1977} iterates length-2 intersections to a fixpoint. Tractability is well charted: path consistency is \emph{complete} for the convex point algebra and the ORD-Horn fragment \citep{Nebel1994} but only \emph{sound-but-incomplete} for full Allen IA and RCC-8 \citep{Renz1999}. These frameworks assume a clean, human-given table on already-formal data; none reads the algebra off natural language via an LLM, certifies reading errors, narrows by intersecting LLM disjunctions, or models a recall-bounded redundancy optimum. We import the algorithms and inherit the tractability facts: our point-algebra arm is exact; our Allen arm is a sound lower bound.

\textbf{Closure over machine-extracted temporal relations.} SputLink computes temporal closure to densify TimeBank annotations \citep{Verhagen2005}; CAEVO performs global temporal inference by cascaded sieves \citep{Chambers2014}; structured learning enforces transitivity for extraction \citep{Ning2017}. All commit to a single globally consistent labeling to maximize F1, preserve no disjunction, certify no reading error, and do not abstain. Critically, SputLink-style closure \emph{produces} the non-adjacent gold whose circularity we must avoid; we therefore evaluate against direct human-timeline gold \citep{Rogers2019} and manual long-distance gold \citep{Naik2019}.

\textbf{Consistency enforcement under the commit contract.} A zero-shot temporal study reports LLMs assign multiple relations to $50$--$97\%$ of pairs and that ILP consistency enforcement does not raise F1 \citep{Kougia2024}; the most recent global temporal-graph generator still ILP-commits to one label per pair \citep{Eirew2025}. METRE trains a multi-label head to model temporal-relation ambiguity \citep{Hu2024} but is F1-trained, carries no set through a composition table across multiple paths, and does not abstain---we position it as the alternative reader that future work plugs into the same closure pipeline at matched recall. Recent LLM temporal/logical-consistency work measures or repairs consistency under an accuracy objective---sequence-vs-absolute references \citep{Bajpai2025}, counterfactual-consistency prompting \citep{Kim2025}, propositional consistency over knowledge-graph queries \citep{Ghosh2024}, and paraphrase-level factual consistency \citep{Bajpai2024}---but none preserves a relation-algebra disjunction, composes it across paths, or issues an abstain-on-collapse certificate. LOCO-LMs fine-tune for propositional consistency at training time \citep{Calanzone2024}; we are training-free, at inference time, over a relation algebra.

\textbf{LLM reasoning, formalization, and abstention.} Chain-of-thought \citep{Wei2022} and self-consistency \citep{Wang2022} operate at the answer level and cannot see that individually popular composition steps are jointly inconsistent. Logic-LM self-refines on solver crashes \citep{Pan2023} and LINC majority-votes formalizations \citep{Olausson2023}, but neither maintains a positive global invariant over relational knowledge. Path-of-Thoughts reasons each extracted path independently \citep{Zhang2024}, beating prior methods on multi-hop spatial and kinship benchmarks \citep{Shi2022, Sinha2019}---precisely the cross-path intersection gap Mode~A fills. The discourse-level reading prompts of \citet{Wei2024} ground our span-local protocol. Selective prediction \citep{Geifman2017} abstains on generic uncertainty; our abstention is structural, triggered when deductive closure leaves a disjunction. RuleTaker \citep{Clark2020} targets propositional entailment, an out-of-scope contrast to our relational composition. Reiter's model-based diagnosis \citep{Reiter1986} supplies the minimal-hitting-set machinery for the Mode-B repair we scope as future work. Hallucination in generation is a broad concern \citep{Ji2022}; ours is a per-edge, certificate-backed reduction rather than a generic confidence filter.

# Method
\label{sec:method}

## Overview and the inverted output contract

The deduction module sits downstream of atomic extraction: it receives, for each pair of mentions co-occurring in a span, the relation the text licenses, and must answer queries about pairs that do \emph{not} co-occur. We model the relations as a Qualitative Constraint Network (QCN): nodes are events/entities, and each edge carries a \emph{set} of base relations from a relation algebra $\mathcal{A}$ (the disjunction not excluded by the evidence). The query (held-out) edge starts at the universal set. Three commitments define the contract. First, the LLM is a \emph{disjunctive, high-recall reader}: for each span it emits the maximal sound set the text does not exclude, with an explicit universal/underdetermined option, rather than committing to one relation. \emph{Soundness} of an edge means its set contains the gold relation; \emph{recall} is $r=P(\text{gold}\in\text{emitted set})$. Second, composition and converse come from the \emph{exact published table} of $\mathcal{A}$, never from the LLM. Third, the system narrows by closure and \emph{abstains} when the query edge remains a non-singleton. Table~\ref{tab:notation} fixes the notation.

\begin{table}[t]
\centering
\small
\begin{tabular}{ll}
\hline
Symbol / term & Meaning \\
\hline
$\mathcal{A}$ & relation algebra (convex point: 3 base relations; Allen: 13) \\
QCN & nodes = entities; each edge = a \emph{set} of base relations \\
$r$ & per-edge recall, $P(\text{gold}\in\text{emitted set})$ \\
sound edge & emitted set contains the gold relation \\
\textsc{full} & iterated PC-2 closure to a fixpoint (our method) \\
\textsc{naive} & single-pass query-node intersection (PoT $+$ one step) \\
\textsc{off} & no propagation (lower baseline) \\
Mode~A & cross-path intersection narrows the query (primary) \\
Mode~B & empty closure certifies an unsound read (secondary) \\
sing.-res.-to-correct & query collapses to the single \emph{correct} relation \\
matched coverage & every method scored at the same single-relation resolution rate \\
$K$ & path redundancy (number of constraining paths) \\
$J(E)$ & empirical joint soundness of $E$-edge subnetworks \\
$\rho$ & within-document cross-edge reading-error correlation \\
$N^\ast$ & a-priori count of deduction-required, multi-path, bite-retaining, \\
 & singleton-resolving held-out edges \\
\hline
\end{tabular}
\caption{Notation and metrics used throughout.}
\label{tab:notation}
\end{table}

## A worked example

Consider five event start-points read span-locally from one news document, with the query edge $A\!\to\!E$ held out (Section~\ref{sec:realtext} discharges this exact case in Prolog). \textbf{Mode~A (narrowing).} Suppose local reads give $A\!<\!B$, $B\!<\!E$ on one path and $A\!<\!C$, $C\!<\!E$ on another. Composition along each path yields $A\!<\!E$ (since $\textsf{before}\circ\textsf{before}=\textsf{before}$); the intersection of the two single-path results is $\{\textsf{before}\}$, a singleton the held-out edge could not be read directly---this is a singleton-resolution-to-correct. \textbf{Mode~B (collapse).} Now suppose one read is unsound: $A\!<\!B$, $B\!<\!E$ but a mis-read $E\!<\!A$. Closure derives $A\!<\!E$ from the first path while the direct edge asserts $E\!<\!A$; their intersection is empty, certifying---with no gold label---that some contributing read is unsound. The danger Mode~A cannot see is \emph{silent wrong narrowing}: if instead the gold $\textsf{before}$ is \emph{omitted} from a contributing set (recall failure), closure can narrow to a confident wrong singleton with no collapse---the failure mode we bound by recall below.

## Two modes of value

\textbf{Mode~A (sound narrowing, primary).} When every contributing edge set is sound but sub-universal, intersecting the compositions arriving at the query pair yields a set that still contains gold yet is strictly tighter than any single path. The load-bearing metric is the \emph{singleton-resolution-to-correct} yield (only this moves selective accuracy and the hallucination rate; strict-tightening is reported separately and is non-load-bearing). Mode~A needs only sub-universal breadth and multi-path bite, not over-commitment, and its zero-FP guarantee survives path-consistency incompleteness because \emph{the intersection of sound sets is always sound}---\emph{conditional on every contributing read being sound}.

\textbf{Mode~B (detection/repair, secondary).} An empty closure is a deductive certificate that some edge is unsound, with no gold labels. It fires only when an over-committed or recall-failed edge is present, and carries the silent-wrong-narrowing dual above, which we bound per-edge by $(1-r)$ and per-network by $(1-J(E))$.

## Iterated closure versus naive intersection

We instrument three closure variants in one engine [ARTIFACT:art_K7riobQ_Rmwz]. \textsc{full} is iterated Mackworth PC-2 to a fixpoint with algebra-seeded converse propagation (our method). \textsc{naive} intersects the compositions arriving at the query pair in a single pass, without iterating and without converse seeding---i.e.\ Path-of-Thoughts plus one obvious intersection step. \textsc{off} performs no propagation. A theorem we exploit and verify by unit test: on length-2 multi-path queries \textsc{naive} equals \textsc{full}; they diverge only on networks with $\geq 3$-edge paths or cyclomatic structure, where iterated propagation reaches tight-edge anchors a single pass cannot. The full-minus-naive gap is therefore the signature of \emph{iteration}, isolating our claim from ``any intersection helps.''

## Redundancy as a coding rate

Because Mode~A's zero-FP property holds only when all contributing edges are sound, and a single LLM reading one document produces positively correlated errors, we do not assume independent per-edge soundness. Instead of the product $\prod_e r_e$ we \emph{measure} the empirical joint soundness $J(E)$---the realized fraction of $E$-edge constraining subnetworks in which all edges are sound---and report the within-document error correlation $\rho$. The inverted-U cost term is $1-J(E)$; positive $\rho$ makes $J(E)$ decay slower than $r^E$, so the predicted peak sits further out than an independence model says. Net gain rises while marginal narrowing dominates, then falls once silent-narrowing cost dominates: an error-correcting code's optimal rate, with the decoding radius set by recall and the channel correlation measured, not assumed.

## The a-priori envelope gate and Prolog discharge

Before spending any LLM budget, we compute from each gold graph \emph{alone} a four-stage funnel over held-out edges (deduction-required; $\geq 2$ paths; non-universal after widening; intersection equal to the gold singleton, $N^\ast$) plus the $\geq 3$-edge/cyclic prevalence and a power calculation [ARTIFACT:art_K7riobQ_Rmwz]. The applicability threshold is pre-registered as a number: deduction-required-multi-path-with-bite fraction $\geq 10\%$ = general mechanism, $5$--$10\%$ = useful module, $<5\%$ = niche. For auditability the closed QCN is emitted as an executable Prolog program: the algebra composition table as \texttt{comp/3} facts, each local read as a \texttt{rel/3} fact (both directions via converse), and the query as the intersection of all path compositions; $|R|{=}1$ emits, $|R|{>}1$ abstains, $|R|{=}0$ flags an unsound read [ARTIFACT:art_fil2iJ6xSrYx].

## Datasets, baselines, and metrics

\textbf{Synthetic backbone} [ARTIFACT:art_ghVQmxVlmOJJ]. $35{,}100$ globally-consistent QCNs over the convex point and Allen algebras (primary) and RCC-8 (secondary), generated by model-based realization so every edge's gold atomic relation is exact and the network is consistent by construction. Redundancy $P$, hop length $L$, and cyclomatic number $\mu$ are swept independently; a correctness gate (composition along every path contains the gold query relation) passes on all $35{,}100$ networks. \textbf{Real corpora} [ARTIFACT:art_PNrS9T8JeATf]. The dense host is \emph{NarrativeTime}, a timeline-based, full-TLink-coverage human re-annotation of TimeBank-Dense ($36$ docs, $1{,}715$ events) \citep{Rogers2019, Cassidy2014}; its start-points instantiate the convex point algebra (PC complete), and our build reproduces the shipped TLINKs exactly ($207{,}496$ relation-multisets), so the gold is non-circular. \emph{TDDMan} supplies manual long-distance pairs that ``cannot be inferred automatically'' \citep{Naik2019}; \emph{MATRES} \citep{Ning2018} annotates only same/adjacent-sentence pairs and serves as the gate-validation control. A CLUTRR kinship slice \citep{Sinha2019} with the finite composition table and absent-relation pairs is prepared as an end-to-end venue [ARTIFACT:art_HS7-lxhZnU9m] but, in the interest of honesty, is \emph{not} executed this iteration.

\textbf{Baselines}, each given a matched abstention signal thresholded to the same coverage object: raw LLM (verbalized confidence), chain-of-thought \citep{Wei2022}, self-consistency \citep{Wang2022}, LINC-style multi-formalization voting \citep{Olausson2023}, Path-of-Thoughts with path-agreement abstention \citep{Zhang2024}, the ILP-commit contract \citep{Eirew2025}, and \textsc{naive} single-pass intersection; configurations are drawn from two implementation dossiers [ARTIFACT:art_aQ2Rf8rwqteI] [ARTIFACT:art_Dm5vYXmD1R8h]. \textbf{Metrics}: singleton-resolution-to-correct and selective accuracy at matched coverage (headline); end-to-end confident-wrong (hallucination) rate; the zero-FP audit conditioned on $J(E)$; the full-minus-naive gap versus hop/cyclomatic structure; applicability $N^\ast$; and per-edge recall.

# Experimental Setup
\label{sec:setup}

We execute a tiered plan. \textbf{T0} (zero LLM spend) is the envelope gate over the three real corpora [ARTIFACT:art_K7riobQ_Rmwz]. \textbf{The matched-coverage showdown} reads $2{,}520$ synthetic networks with a real LLM and runs all seven baselines [ARTIFACT:art_N0e4pH_C_Cxw]. \textbf{The realism-matched channel} re-establishes the mechanism claims under a reader channel calibrated to the real-text frontier [ARTIFACT:art_FtN4LBzazO_l]. \textbf{The local-reader real-text experiment} reads the actual NarrativeTime/TDDMan gold graphs with two readers and discharges Prolog [ARTIFACT:art_fil2iJ6xSrYx]. The showdown reader is \texttt{google/gemini-3.1-flash-lite} at temperature $0$; the real-text experiment adds a stronger reader (\texttt{google/gemini-3.5-flash}). All LLM calls use a SHA-256 disk cache and a hard global cost guard; the showdown's final run cost \$2.21 over $24{,}938$ billed calls ($0$ errors), the channel is \$0 (pure CPU), and the real-text re-run is \$0 (cached). The QCN engine is bitmask-encoded and gated by a unit-test suite: the Allen 169-cell table matches the published cells and the composition-converse law ($0$ failures), convex-point completeness is confirmed against brute force ($0$ mismatches over $200$ networks), and the iteration-isolation test confirms \textsc{full}$=$\textsc{naive} at length 2 and \textsc{full}$\neq$\textsc{naive} on a 3-hop chain [ARTIFACT:art_K7riobQ_Rmwz].

# Results

We tag every subsection with its evidence class so the reader can weight it immediately.

## The matched-coverage showdown: closure's advantage scales with algebra richness (\textsc{real-llm-read})
\label{sec:showdown}

The previous draft specified seven baselines and a matched-coverage protocol but ran none of them; this is the gap we close first. A real LLM makes span-local disjunctive reads of $2{,}520$ synthetic networks, those reads feed the validated PC-2 engine, and every method is scored at the same single-relation coverage on the same networks [ARTIFACT:art_N0e4pH_C_Cxw]. On the bite-bearing pool ($n=900$ per algebra) Mode~A beats all six neural/ILP baselines on both algebras, with Holm-adjusted bootstrap confidence intervals excluding zero (Table~\ref{tab:leaderboard}).

[FIGURE:fig2]

The decisive structure is how the advantage \emph{scales with the richness of the relation algebra}. On the 3-relation convex point algebra (PC-complete, exact), a strong per-path baseline already composes correctly, so Mode~A ties Path-of-Thoughts ($1.000$ vs.\ $0.957$, gap $+0.043$, adjusted CI $[0.024,0.063]$) while still beating self-consistency ($0.854$, gap $+0.146$, CI $[0.114,0.181]$). On the 13-relation Allen interval algebra (NP-hard consistency), neural per-path chaining collapses---Path-of-Thoughts $0.308$, self-consistency $0.343$, raw $0.347$, CoT $0.336$, LINC $0.333$, the best non-closure method ILP-commit only $0.559$---while symbolic closure stays robust at $0.984$ (gap vs.\ PoT $+0.676$, CI $[0.624,0.728]$; vs.\ SC $+0.641$, CI $[0.588,0.691]$). The interpretation is mechanistic: on a coarse algebra an LLM rarely has more than one plausible composition to confuse, so the symbolic step is redundant; as the algebra's branching grows, free neural composition accumulates locally-fluent but globally-inconsistent steps that exact intersection eliminates. This scaling is the paper's central empirical claim, and it holds with real reads, not a simulated channel.

\begin{table}[t]
\centering
\small
\begin{tabular}{lcc}
\hline
Method (matched coverage) & Point ($0.60$) & Allen ($0.48$) \\
\hline
\textbf{Mode~A (ours)} & \textbf{1.000} & \textbf{0.984} \\
Path-of-Thoughts \citep{Zhang2024} & 0.957 & 0.308 \\
Self-consistency \citep{Wang2022} & 0.854 & 0.343 \\
Raw LLM (forced single) & 0.930 & 0.347 \\
Chain-of-thought \citep{Wei2022} & 0.911 & 0.336 \\
LINC-vote \citep{Olausson2023} & 0.861 & 0.333 \\
ILP-commit \citep{Eirew2025} & 0.856 & 0.559 \\
\hline
\end{tabular}
\caption{Selective accuracy at matched coverage (bite-bearing pool, $n{=}900$/algebra), \textsc{real-llm-read}. Mode~A's gap over every baseline is Holm-adjusted-CI-separated from zero; the gap over per-path reasoning grows from $+0.043$ (point) to $+0.676$ (Allen).}
\label{tab:leaderboard}
\end{table}

Two controls travel with the headline. First, closure recovers genuine deduction-required bite: \textsc{off} (no propagation) has coverage $0$ because the query pair never co-occurs locally, while Mode~A resolves $48.7\%$ (point) / $38.2\%$ (Allen) of held-out queries. Second, the soundness audit is clean: per-edge recall is $1.000$ (point) / $0.966$ (Allen), and on all-sound networks the closed query set contains gold with probability $1.0$ ($1{,}260$ point / $998$ Allen all-sound networks); silent wrong arises only from the $3.4\%$ unsound Allen reads ($10/481$ covered queries, $2.1\%$).

## Iteration error-corrects, per recall slice, on a realism-matched channel (\textsc{synthetic-channel})
\label{sec:mechanism}

A reviewer rightly flagged that the previous synthetic channel breached its own pre-registered realism bound (per-edge error-type total-variation distance $0.25$ vs.\ a $0.10$ threshold) and that its breadth knob produced identical recall across settings. We repaired the channel to a single ordinal knob that \emph{samples} the per-edge error-type category from the calibrated real distribution, so recall becomes an \emph{output} [ARTIFACT:art_FtN4LBzazO_l]. The real recall ladder is now reproduced to a maximum error of $0.003$ (real $[.572,.599,.625,.783,.796]$), and the per-edge error-type TV falls to $\le 0.0065$ in the apples-to-apples projected space (and $\le 0.0072$ in the full 5-category Allen space): realism\_matched $=$ true.

[FIGURE:fig3]

On this channel, iterated closure error-corrects exactly as the theory predicts, \emph{reported per recall slice} (correcting the earlier conflation of recall levels). At every recall slice the full-minus-naive gap is a structural $0.0$ at hop length $L=2$ (the predicted tie, CI includes zero) and grows with $L$: at recall $1.0$ the gap runs $0.0\!\to\!0.95\!\to\!0.92\!\to\!0.90\!\to\!0.885$ for $L=2,3,4,5,6$ (\textsc{naive} resolves nothing beyond $L=2$); the gap also rises with cyclomatic number (Page trend $p\approx10^{-4}$, \emph{not} the $10^{-13}$ mis-stated previously). The gap is itself recall-dependent, a predicted signal: the maximum-$L$ gap rises monotonically with recall---$0.22, 0.31, 0.48, 0.65, 0.78, 0.885$ at recall $0.572, 0.625, 0.783, 0.90, 0.95, 1.0$---so any single-number summary must name its recall level. The full-scale showdown corroborates the iteration claim with \emph{real} reads: on point networks the full-minus-naive coverage gap is $0.0$ at $L{=}2$ and $+0.344$ at $L{=}3$, rising with cyclomatic number to $+0.367$; on Allen, $+0.144$ at $L{=}3$ [ARTIFACT:art_N0e4pH_C_Cxw].

## The redundancy optimum and a read-soundness-bounded certificate (\textsc{synthetic-channel}, \textsc{theorem})
\label{sec:certificate}

[FIGURE:fig4]

\textbf{The recall-dependent inverted-U.} Net Mode-A resolution is an inverted-U in path redundancy $K$, and the optimum moves outward with recall: the peak sits at $K^\ast=2,4,7,10,16$ for recall $0.5,0.625,0.78,0.90,0.95$, with resolution-at-peak rising $0.295\!\to\!0.407\!\to\!0.68\!\to\!0.905\!\to\!0.968$ [ARTIFACT:art_FtN4LBzazO_l]. A net-positive region (beating both best-single-path and \textsc{off}) exists at every recall level, and the recall-floor gate shifts the peak further outward. Under positive $\rho$ the measured $J(E)$ exceeds the $r^E$ independence model, pushing the optimum further still. We follow the reviewer in stating plainly that this inverted-U is a property of a controlled channel: recall and $\rho$ are knobs, not measured outcomes, so it characterizes the mechanism rather than predicting a specific real-text operating point.

\textbf{The certificate, separated into theorem and measurement.} The zero-FP property---on all-sound contributing edges the Mode-A output contains gold with probability exactly $1.0$, and a collapse never co-occurs with all-sound reads---is the soundness invariant of path consistency. We tag it a \textsc{theorem} (verified deterministically on $100{,}296$ all-sound networks), not an empirical discovery, exactly as the reviewer asked. The empirical content is the \emph{conditionality}: as per-edge recall falls, the silent-wrong rate rises---$0.006, 0.015, 0.044, 0.095, 0.146$ at recall $0.95, 0.90, 0.78, 0.625, 0.50$---always staying below the per-network bound $(1-J(E))$ and the per-edge bound $(1-r)$. The certificate is therefore strongest where reads are already good and weakest in the real low-recall regime where it is most needed; we no longer claim ``zero-FP'' without the ``conditional on read soundness'' qualifier. The reliability slope of contains-gold on $J(E)$ is $0.65$ ($<1$): the convex algebra absorbs most single unsound reads, so gold is retained \emph{more} robustly than $J(E)$ predicts---a certificate that over-delivers---and the intercept offset disappears when the predictor is switched from $r^E$ to empirical $J(E)$, correctly attributing it to the independence approximation rather than a soundness failure.

## Real text: read-soundness, not closure, is the bottleneck---and an end-to-end slice (\textsc{real-llm-read}, \textsc{gold-only-gate})
\label{sec:realtext}

We now read \emph{the actual} NarrativeTime and TDDMan gold graphs span-locally, removing the previous draft's conflation of NarrativeTime (whose T0 applicability is $0.882$) with the TimeBank-Dense stand-in that was actually read (deduction-required fraction $0.039$) [ARTIFACT:art_fil2iJ6xSrYx]. The character-offset event marking aligns at fraction $1.000$ on all three corpora.

[FIGURE:fig5]

\textbf{The binding constraint is the read, and it is not a weak-model artifact.} Per-edge recall of span-local reads tops out below the soundness gates: on NarrativeTime the primary reader reaches $0.743$ ($n{=}74$), and a substantially stronger reader (\texttt{gemini-3.5-flash}) reaches $0.897$ ($n{=}39$, CI $[0.667,1.0]$)---still short of the $0.90$ point gate. Because even the stronger reader does not cross the gate, the binding constraint is real-text local read-soundness, not the closure step; this is the load-bearing localization. The within-document soundness correlation is positive ($\rho=0.16$--$0.42$), as the channel model assumes. The gate-validation control behaves as designed: MATRES yields $0$ multi-path deduction queries (\textsc{gold-only-gate}), confirming the deduction-required gate is discriminative because MATRES annotates only adjacent-sentence pairs---a restatement of its annotation distribution, which we label as such rather than as a discovery.

\textbf{An end-to-end, auditable slice with a hallucination number.} We emit the closed network as runnable Prolog and discharge the held-out query: the worked Mode-A program intersects the length-2 path compositions for a real NarrativeTime query and narrows it to the single relation \textsf{before}, agreeing with the engine; a companion program reaches an empty intersection and certifies a reading error (Mode~B). On the deduction-required queries, the abstaining closure pipeline drives the confident-wrong (hallucination) rate to $0.0$ versus $0.65$ for the raw LLM forced to a single relation (reduction $0.65$, CI $[0.47,0.80]$). We are explicit about the cost of honesty here: this real-text head-to-head rests on only $n=20$ deduction queries across three documents per corpus and is \emph{underpowered}; the H2 reduction is driven partly by the closure pipeline's heavy abstention (it answered $2$ of $20$), and the selective-accuracy advantage over Path-of-Thoughts and self-consistency is \emph{not} statistically established at this sample ($p>0.05$). The matched-coverage evidence for the mechanism therefore rests on the fully-powered showdown (Section~\ref{sec:showdown}); a \$0 synthetic backstop within the same experiment confirms that when reads are sound (recall $0.96$) Mode~A beats raw by $+0.22$ to $+0.26$, self-consistency by $+0.04$, and Path-of-Thoughts where the latter can reach Mode-A's coverage at all [ARTIFACT:art_fil2iJ6xSrYx].

## The a-priori gate, stated as what it is (\textsc{gold-only-gate})

Run over the three corpora at zero LLM cost, the T0 gate is discriminative \emph{by construction}: MATRES yields $N^\ast=0$ (adjacent-sentence gold), NarrativeTime yields $N^\ast=25{,}450$ at applicability $0.882$, and TDDMan lands in the module band ($0.085$, $N^\ast=408$) [ARTIFACT:art_K7riobQ_Rmwz]. We now state plainly what these numbers are and are not. The NarrativeTime ``exact recovery'' is \emph{guaranteed}, not earned: a dense human timeline assigns numeric coordinates to every event, which is a globally consistent point network, so closure trivially recovers every pairwise relation---and indeed iteration adds nothing there (\texttt{full\_only}$=0$, near-transitively-closed). The genuine iteration signal lives on \emph{sparse} long-hop gold: TDDMan exhibits $12$ held-out edges \textsc{full} resolves but \textsc{naive} cannot (\texttt{full\_only}$=12$; $408$ vs.\ $396$). The gate thus scopes the iteration claim to sparse/synthetic long-hop structure, where Sections~\ref{sec:showdown}--\ref{sec:mechanism} demonstrate it, and away from the dense timeline.

# Discussion

\textbf{What the evidence supports.} With real LLM reads and every baseline run, Mode~A beats neural per-path reasoning, voting, and ILP-commit at matched coverage, and the advantage scales with relation-algebra richness---the central, fully-powered finding. On a realism-matched channel, iterated closure error-corrects with a gap that grows in hop length per recall slice; net narrowing is a recall-dependent inverted-U; and the silent-wrong rate is a bounded, decreasing function of recall. The certificate's zero-FP property is a theorem, tagged as such. We deliver an end-to-end Prolog-discharged slice with a hallucination-rate number.

\textbf{What it does not support, stated without spin.} The real-text head-to-head is underpowered ($n=20$), so Mode~A's selective-accuracy advantage over Path-of-Thoughts and self-consistency is not established on real news this iteration; the hallucination reduction is directional. The mechanism's transfer to real text is gated on read-soundness, which a stronger reader still does not reach ($0.897<0.90$). We therefore frame the contribution precisely: a closure-certified \emph{deduction module}---not a full pipeline---validated where reads are sound, with an honestly measured real-text scope boundary, targeted at the ACL Knowledge Extraction track with neuro-symbolic (NeSy) and findings tracks as natural homes for the measured boundary.

\textbf{Why the algebra-richness scaling matters.} A recurring puzzle is that consistency enforcement does not improve F1 \citep{Kougia2024, Eirew2025}. Our scaling result reframes it: on a coarse algebra (where most temporal benchmarks effectively live after coarsening) there is little for a symbolic step to fix, so enforcement looks inert; the symbolic advantage materializes precisely on rich algebras, where free neural composition is most error-prone. The actionable implication is to deploy closure where the relation algebra is rich and to invest in per-edge read-soundness (the binding real-text constraint) rather than in more consistency post-processing.

\textbf{Connection to the text-to-logic pipeline, and its limits.} The module is training-free, runs in milliseconds on commodity hardware, preserves disjunction, abstains, and emits a trace-graph dischargeable in SWI-Prolog/ASP---meeting the pipeline's auditability and quantified-hallucination-reduction requirements for the deduction step. It does \emph{not} address the full project goal: atomic extraction is held fixed (we report per-edge recall as the read-quality measure rather than re-extracting), OpenCyc/upper-ontology grounding \citep{Lenat1995} is not used, and the CLUTRR kinship end-to-end venue is prepared (composition table and absent-relation pairs delivered) but not run. We list these as scope, not as achievements.

\textbf{Limitations.} (1) The real-text Mode-A and end-to-end hallucination claims are underpowered and gated on reader improvement. (2) Path consistency is complete only for the convex point algebra; Allen collapse and recovery numbers are sound lower bounds, and RCC-8 is untested on real text. (3) The inverted-U is established on a controlled channel whose recall and $\rho$ are inputs, not measured real-text outcomes; the channel matches real per-edge error types (TV $\le 0.0065$) and short-range topology (TV $\le 0.14$) but its long-hop tail is descriptive only. (4) Mode-B repair quality, the RCC-8 arm, the CLUTRR end-to-end demo, and the METRE-style alternative-reader test are scoped as future work. (5) The kinship/legal/spatial framing is intentionally removed from the headline; only convex-point (exact) and Allen (lower bound) arms are backed by executed experiments.

# Conclusion

We treated the deduction step of a text-to-logic pipeline as a coding problem: keep the LLM as a high-recall disjunctive reader, and let exact relation-algebra path consistency error-correct over the redundant constraining paths a document supplies. Running, for the first time in this line of work, the full matched-coverage comparison with a real LLM and every baseline, we find that symbolic closure's advantage over neural per-path reasoning \emph{scales with relation-algebra richness}---a tie on the 3-relation point algebra ($+0.043$) becoming a decisive $+0.68$ on the 13-relation Allen algebra, Holm-adjusted. On a realism-matched channel the mechanism behaves as the coding-theory lens predicts: iterated closure (not a single pass) error-corrects with a hop-growing gap per recall slice, net narrowing is a recall-dependent inverted-U ($K^\ast=2,4,7,10,16$), and the zero-FP certificate is a theorem whose practical value is bounded by read-soundness (silent-wrong $0.146\!\to\!0.006$ as recall rises). We deliver an auditable Prolog-discharged slice with a confident-wrong reduction, and we localize the real-text obstacle to read-soundness: a stronger reader still falls short of the gate. Three concrete next steps: (1) raise per-edge read recall into the $0.90$ regime, where the validated mechanism predicts a real-text payoff; (2) run the prepared CLUTRR end-to-end venue and a stronger-reader real-text study at adequate power; and (3) execute the Mode-B repair and RCC-8 arms now that the mechanism and its operating envelope are characterized.

\bibliographystyle{plainnat}
\bibliography{references}

</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (scope) The decisive positive evidence is entirely on synthetic, templated text, and does not transfer to the project's target domain. The 'matched-coverage showdown' and the 'advantage scales with algebra richness' finding are tagged REAL-LLM-READ-ON-SYNTHETIC: each edge is one professional-prose sentence, recall is ~1.0, and (per the artifact/README) the 2,520 networks collapse to only ~35 unique entity-normalized read prompts — so the LLM's actual linguistic exposure is a few dozen templated sentences, with all the variety living in graph topology. On the actual target (real ~3000-char documents), the head-to-head is n=20 with p>0.05 (modeA_vs_pot CI [0.0,1.0], boot p=0.25; modeA_vs_sc p=0.18), i.e. the comparative advantage is NOT statistically established on real text. The paper is honest about this, but the central comparative contribution remains a synthetic-only result.
  Action: Demonstrate the comparative advantage on the target domain at power: (a) scale the real-text deduction-query sample by 5–10x (the gold graphs contain far more multi-path edges than the 20 scored) and report risk-coverage curves with doc-clustered CIs; and/or (b) run the already-prepared CLUTRR end-to-end slice, which gives a clean, non-synthetic, non-temporal head-to-head with a real absent-relation hallucination test. If neither is feasible this round, retitle the headline to make explicit that the scaling law is a synthetic-text mechanism result and that real-text transfer is an open negative.
- [MAJOR] (rigor) The most decision-relevant real-text claim — 'the binding constraint is real-text local read-soundness, not the closure step, and it is not a weak-model artifact' — is statistically unsupported and presented as 'the load-bearing localization.' The stronger reader reaches per-edge recall 0.897 at n=39 with CI [0.667, 1.0], which comfortably contains the 0.90 gate; 0.897 vs 0.90 differ by 0.003, far inside the noise at n=39. Moreover the TDDMan primary reader already achieves 0.902 (crosses the gate), undercutting a universal read-soundness-ceiling narrative. Concluding that a stronger reader categorically does not cross the gate, from n=39 and a 0.003 point-estimate margin, is not warranted.
  Action: Enlarge the stronger-reader recall sample (n=39→≥150 scorable edges) and report whether the gate-crossing is statistically distinguishable; until then, downgrade the claim to 'the stronger reader's point estimate sits at the gate; whether reads can clear it is not resolved at this sample.' Reconcile the TDDMan 0.902 vs NarrativeTime 0.74/0.90 discrepancy — the bottleneck may be corpus/genre-specific, which itself is a publishable, more defensible framing than a universal ceiling.
- [MAJOR] (methodology) The paper's 'central empirical claim' — closure's advantage scales with relation-algebra richness (+0.043 point → +0.676 Allen vs PoT) — conflates two distinct effects and thereby overstates the novel contribution. The +0.676 Allen gap is dominated by exact-table composition vs LLM composition: PoT has the LLM compose 13-relation Allen relations along paths, which it does at 0.308. That LLMs compose rich algebras poorly is close to definitional and is the standard neuro-symbolic premise, not a discovery. The paper's genuinely novel mechanism (iteration / cross-path intersection / the certificate) is isolated by the full-vs-naive contrast, where the Allen effect is much smaller (naive resolves 0.405 → Mode-A 0.477; full-minus-naive ~+0.144 at L=3). The headline elevates the near-definitional component to the paper's signature finding.
  Action: Make the full-vs-naive (iteration-specific) gap the headline contribution alongside the system-level vs-PoT gap, and explicitly decompose +0.676 into a table-vs-LLM-composition component and an iteration/intersection component. Frame 'use exact tables instead of LLM composition' as the inherited neuro-symbolic premise and the disjunction-preserving certificate + iteration as the novel delta, with their separately-measured effect sizes.
- [MAJOR] (scope) Against the stated project goal, several core deliverables remain absent or token. (1) No OpenCyc/upper-ontology grounding. (2) CLUTRR/RuleTaker prepared but not run. (3) Atomic-extraction precision/recall is required by the goal but held fixed and not measured (only per-edge recall of the deduction reads). (4) The end-to-end real-text hallucination reduction (0.65→0.0) rests on Mode-A answering only 2 of 20 queries — near-total abstention makes a near-zero confident-wrong rate trivial. (5) The Prolog 'discharge' was 'python-checked (swipl-unavailable)' per the artifact, so SWI-Prolog symbolic execution — an explicit goal requirement — was not actually performed; the paper's 'runnable Prolog ... discharge the held-out query' phrasing implies execution that did not occur.
  Action: Install and run SWI-Prolog (apt-installable) on the two worked programs and report actual execution output, since symbolic execution is a goal requirement; if it cannot be run, say plainly 'validated by a Python re-implementation, not executed in SWI-Prolog.' Report the real-text hallucination number as a risk-coverage tradeoff with the 90% abstention rate stated alongside. Run a minimal CLUTRR end-to-end slice to satisfy goal items (i)/(ii) on non-synthetic data. If OpenCyc and atomic-extraction P/R remain out of scope, foreground in the intro/abstract that the contribution is the deduction sub-module only, not the operational pipeline the goal describes.
- [MINOR] (evidence) The end-to-end hallucination reduction is mechanically driven by abstention, not by better answers. Mode-A answers 2/20 deduction queries and is confident-wrong on 0; raw is forced to answer all 20 and is wrong on 0.65. Any method that abstains on ~90% of queries will show a near-zero confident-wrong rate, so 'reduction 0.65' is a coverage-vs-risk comparison rather than an apples-to-apples hallucination measurement.
  Action: Always pair the confident-wrong number with the coverage/abstention rate, and present the full risk-coverage (selective-accuracy) curve instead of a single confident-wrong delta. State explicitly that the reduction is achieved via abstention on real text, and that selective accuracy at matched coverage — the fair metric — is not significant at n=20.
- [MINOR] (novelty) The closest recent neuro-symbolic temporal-reasoning and temporal-abstention works are not cited, which weakens the differentiation of the central contribution. Missing neighbors include NeSTR (neuro-symbolic abductive temporal reasoning, arXiv:2512.07218), 'Towards Neuro-Symbolic Temporal Reasoning for LLMs' (Findings-ACL 2025), 'Consistent Discourse-level Temporal Relation Extraction' (Findings-EMNLP 2025), and abstention-in-temporal-QA work ('When Silence Is Golden'). These operate on commit/abductive-correction objectives, so they sharpen rather than threaten the novelty, but their absence makes the related-work positioning look incomplete to an area expert.
  Action: Add 2–4 of these and extend the one-sentence differentiation: the contribution preserves a relation-algebra disjunction and abstains on closure-collapse (a gold-free certificate), versus their single-label commit (Eirew, Kougia) or generate-then-abductively-repair (NeSTR) objectives.
- [MINOR] (scope) The multi-algebra generality remains broader in framing than in execution. Only the convex point algebra arm is exact; Allen is a sound lower bound; RCC-8 is never run at all (neither synthetic nor real), yet spatial containment and legal-clause chaining appear in the motivating framing. The convex point arm over a timeline is essentially a partial order, so the 'relation algebra' generality demonstrated is narrow.
  Action: Either run a small RCC-8 synthetic arm to substantiate the spatial claim (cheap given the existing engine and generator), or drop spatial/legal/kinship from the abstract/intro framing and state that executed evidence covers convex point (exact) and Allen (lower bound) only.
</reviewer_feedback>



<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
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
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title (may be unchanged if still accurate)",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-17 17:40:35 UTC

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
