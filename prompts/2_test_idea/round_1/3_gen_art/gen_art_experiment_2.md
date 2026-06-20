# gen_art_experiment_2 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_2` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 13:39:00 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

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

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_2/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_2/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_2_idx5
type: experiment
title: >-
  Synthetic De-Risking of H3 (Iterated Closure > Naive Intersection) and H4 (Recall-Dependent Redundancy Inverted-U) via Controlled
  QCN + Simulated-Reader Channel
summary: >-
  A zero-LLM-spend, self-contained CPU experiment that establishes H3 and H4 on clean synthetic ground truth, decoupling the
  closure mechanism from corpus/LLM-elicitation risk. We generate random CONSISTENT qualitative constraint networks (QCNs)
  by realization (every network is consistent by construction because it is read off a sampled point/interval assignment),
  then simulate the LLM reader as an EXACTLY-controlled noisy channel with three knobs: per-edge recall r = P(gold in emitted
  set), a sub-universal breadth distribution, and a within-network cross-edge soundness correlation rho (latent equicorrelation
  Gaussian). PRIMARY algebra = the CONVEX POINT ALGEBRA (base {<,=,>}; PC provably COMPLETE; trivially-correct 3x3 composition
  table; matches the NarrativeTime start-point arm). We implement three closure variants (FULL iterated path-consistency /
  NAIVE single-pass query-node intersection / OFF) and measure: (H3) FULL-minus-NAIVE selective-accuracy gap stratified by
  hop-count L and cyclomatic number, predicted ~0 at length-2 and GROWING with L/cycles, with an ordered-alternative trend
  test; (H4) the net Mode-A gain decomposed into a narrowing BENEFIT curve and a silent-narrowing COST curve = 1 - J(E) over
  redundancy at >=4 fixed recall levels, with the inverted-U peak located, shown to move OUTWARD with recall and under a recall-floor
  gate, with J(E) MEASURED empirically (not assumed as r^E) so positive rho makes the peak sit further out than the independence
  model; plus (C3) a zero-FP audit (realized P(gold in output) vs empirical J(E), slope ~1, attribution rule). Emits an aii-json-validated
  method_out.json with curves, located peaks, audit slopes, and explicit PASS/FAIL on H3 and H4 at the pre-registered estimation
  precision. Optional secondary generality arm: Allen Interval Algebra via the validated qualreas composition table.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  ########################################################################
  # NOTE ON DEPENDENCIES: this artifact lists depends_on=[] because it is a
  # SELF-CONTAINED synthetic study. The 'dataset' is the QCN generator coded
  # INLINE (same Renz-Nebel-style realization family the synthetic DATASET
  # artifact uses). NO external dataset, NO NL text, NO LLM calls (zero spend).
  # Everything below runs on CPU in minutes; parallelize with multiprocessing
  # (see aii-parallel-computing). Seed EVERYTHING (numpy.random.default_rng with
  # a per-cell seed) for byte-reproducibility.
  ########################################################################

  === CONFIG (pre-registered; freeze BEFORE the full run) ===
  ALGEBRA_PRIMARY      = 'point'        # convex point algebra (PC COMPLETE)
  ALGEBRA_SECONDARY    = 'allen'        # optional generality arm (gate behind point PASS)
  RECALL_LEVELS        = [0.60, 0.75, 0.90, 0.95]   # >=4 FIXED levels (H4 axis)
  RHO_LEVELS           = [0.0, 0.5]     # independent vs positively-correlated reader errors
  GATE_MODES           = ['off', 'on'] # recall-floor gate
  REDUNDANCY_K         = [1,2,3,4,5,6,7,8,10,12]    # # parallel constraining paths (H4 axis)
  HOP_LENGTHS          = [2,3,4,5,6]    # chain length L between query endpoints (H3 axis)
  CYCLO_CHORDS         = [0,1,2,3]      # extra cross-edges -> cyclomatic number (H3 axis)
  N_PER_CELL           = 600            # >=500 networks per cell (pre-registered)
  BREADTH = {p_singleton:0.45, p_two:0.40, p_univ:0.15}  # sub-universal w/ bite; avg|set|~1.7
  B_BOOT               = 2000           # bootstrap resamples
  ALPHA                = 0.05
  GATE_DROP_FRACTION   = 0.20           # gate removes bottom-confidence edges
  SEED_BASE            = 20260617

  ########################################################################
  # 1. RELATION ALGEBRA  (PRIMARY = convex point algebra)
  ########################################################################
  # Encode relations as 3-bit masks: LT=1, EQ=2, GT=4, U=7, EMPTY=0.
  # Convex (allowed reader outputs): {LT(1),EQ(2),GT(4),LT|EQ(3),EQ|GT(6),U(7)}.
  # FORBIDDEN as a read: EMPTY(0)=inconsistent, LT|GT(5)=NOT-EQUAL is the ONLY
  #   non-convex relation -> if any widening would produce 5, widen to U(7)
  #   ('widen non-convex {<,>} to VAGUE') and COUNT the bite lost.

  BASE_COMP = {  # composition of single base relations (Vilain-Kautz point algebra)
    (LT,LT):LT, (LT,EQ):LT, (LT,GT):U,
    (EQ,LT):LT, (EQ,EQ):EQ, (EQ,GT):GT,
    (GT,LT):U,  (GT,EQ):GT, (GT,GT):GT }
  CONV_BASE = {LT:GT, EQ:EQ, GT:LT}

  precompute COMP[R][S] for R,S in 0..7:
      COMP[R][S] = OR over base bit a in R, base bit b in S of BASE_COMP[(a,b)]
  precompute CONV[R] = OR over base bit a in R of CONV_BASE[a]
  def INTERSECT(R,S): return R & S          # algebra intersection
  def compose(R,S):   return COMP[R][S]

  SELF-VERIFY (assert before any run):
    COMP[LT][LT]==LT; COMP[LT][GT]==U; COMP[EQ][GT]==GT; COMP[GT][LT]==U
    CONV[LT]==GT; CONV[LT|EQ]==EQ|GT; INTERSECT(LT|EQ, EQ|GT)==EQ
    composition associative on a random sample of triples (spot check)

  ########################################################################
  # 2. QCN GENERATORS  (consistent BY CONSTRUCTION via realization)
  ########################################################################
  # FAMILY R (REDUNDANCY, for H4): K parallel length-2 paths i -> m_k -> j.
  def gen_family_R(K, rng):
      # sample distinct timestamps so gold(i,j) is a definite base relation
      t_i = 0.0; t_j = 10.0                     # ensures gold(i,j) = LT
      M   = [rng.uniform(1,9) for _ in range(K)] # each intermediate between i,j
      nodes = [i, j] + m_k...
      gold[a][b] = sign-relation(t_a, t_b) in {LT,EQ,GT}   # from realization
      observed_edges = {(i,m_k),(m_k,j) for all k}          # the reader sees these
      query = (i,j)  ;  gold_query = LT
      return network(nodes, gold, observed_edges, query)

  # FAMILY H (HOP/CYCLOMATIC, for H3): chain of length L plus C chords.
  def gen_family_H(L, C, rng):
      chain = [i, x1, ..., x_{L-1}, j]  with strictly increasing timestamps
      observed_edges = consecutive pairs along the chain   # (i,x1),(x1,x2),...,(x_{L-1},j)
      # IMPORTANT: NO direct (i,j) edge and NO shortcut edges read -> a pure chain.
      add C chords: pick C non-consecutive node pairs, ADD their gold relation as
          observed edges (raises cyclomatic number = |E| - |V| + 1, gives NAIVE
          some length-2 shortcuts while FULL still benefits more from iteration)
      gold[a][b] from timestamp realization; query=(i,j); gold_query = LT
      return network(...)
  # Both families are CONSISTENT by construction (read off a real point assignment).

  ########################################################################
  # 3. SIMULATED READER CHANNEL  (exact recall / breadth / rho knobs)
  ########################################################################
  def read_network(net, recall r, rho, breadth, rng):
      qn = qnorm(r)                          # Phi^{-1}(r)
      Ulatent = rng.normal()                 # ONE per-network latent (document factor)
      for each observed edge e with gold base g = net.gold[e]:
          V = rng.normal()
          z_e = sqrt(rho)*Ulatent + sqrt(1-rho)*V    # equicorrelated latent
          sound_e = (z_e <= qn)              # marginal P(sound)=r ; corr(sound)~rho
          conf_e  = Phi(-z_e) + tiny_noise   # NOISY soundness proxy for the gate
          if sound_e:
              S_e = emit_sound_superset(g, breadth, rng)   # convex set CONTAINING g
          else:
              S_e = emit_unsound_set(g, rng)               # convex set NOT containing g
          if S_e == LT|GT(5): S_e = U(7)     # convexity guard; record bite_lost++
          read[e] = S_e ; read.conf[e]=conf_e ; read.sound[e]=sound_e
      # seed converse edges from the ALGEBRA (never from the reader):
      for each read edge (a,b): read[(b,a)] = CONV[read[(a,b)]]
      return read

  emit_sound_superset(g, breadth):   # stay convex, contain g, mostly sub-universal
    if g==LT: sample from {LT, LT|EQ, U} with weights (p_singleton, p_two, p_univ)
    if g==EQ: sample from {EQ, LT|EQ, EQ|GT, U}
    if g==GT: sample from {GT, EQ|GT, U}
  emit_unsound_set(g):               # convex, sub-universal, EXCLUDES g (over-commit)
    if g==LT: sample from {EQ, GT, EQ|GT}
    if g==EQ: sample from {LT, GT}          # (LT|GT is non-convex -> excluded)
    if g==GT: sample from {LT, EQ, LT|EQ}

  ########################################################################
  # 4. CLOSURE VARIANTS
  ########################################################################
  def closure_FULL(read, nodes):     # iterated path-consistency (PC-2 / Mackworth)
      R = dense matrix: R[a][b]=read[(a,b)] if present else U(7); R[a][a]=EQ
      changed=True
      while changed:
          changed=False
          for k in nodes: for i in nodes: for j in nodes:
              if i,j,k not distinct: continue
              new = INTERSECT(R[i][j], compose(R[i][k], R[k][j]))
              if new != R[i][j]:
                  R[i][j]=new ; R[j][i]=CONV[new]          # algebra-seeded converse
                  if new==EMPTY: return ('COLLAPSE', R)     # Mode-B certificate
                  changed=True
      return ('OK', R)

  def closure_NAIVE(read, nodes, query=(i,j)):  # single pass, NO fixpoint, NO
      # converse-derived propagation: 'PoT + one obvious intersection step'
      res = read.get((i,j), U)                    # direct reading (U if held out)
      for k in nodes, k!=i,j:
          if (i,k) in read and (k,j) in read:     # ONLY directly-read length-2 paths
              res = INTERSECT(res, compose(read[(i,k)], read[(k,j)]))
      return res

  def closure_OFF(read, query): return read.get(query, U)   # direct read only

  ########################################################################
  # 5. MODE-A ANSWER EXTRACTION + CLASSIFICATION
  ########################################################################
  def classify(result_set, gold_query):
      if result_set==EMPTY:                 return 'COLLAPSE'   # Mode-B detection
      if popcount(result_set)==1:
          return 'CORRECT' if result_set==gold_query else 'WRONG'  # WRONG=silent narrowing
      return 'ABSTAIN'                       # non-singleton -> abstain (coverage axis)
  # Coverage object = single-relation resolution, applied IDENTICALLY to every variant.

  ########################################################################
  # 6. RECALL-FLOOR GATE
  ########################################################################
  # gate ON: before narrowing, drop the bottom GATE_DROP_FRACTION of edges by conf_e
  #   (a NOISY proxy, NOT ground-truth soundness -> realistic, non-oracle). A path
  #   is admitted only if ALL its edges survive the gate; if no path resolves, ABSTAIN.
  # Compare peak location gate-ON vs gate-OFF (predict: ON shifts peak OUTWARD).

  ########################################################################
  # 7. EXPERIMENT DRIVER
  ########################################################################
  --- H4 cells: for (r in RECALL_LEVELS, rho in RHO_LEVELS, gate in GATE_MODES, K in REDUNDANCY_K):
        rng = default_rng(hash(SEED_BASE, r, rho, gate, K))
        for n in range(N_PER_CELL):
          net  = gen_family_R(K, rng)
          read = read_network(net, r, rho, BREADTH, rng)
          read_g = apply_gate(read) if gate=='on' else read
          full = closure_FULL(read_g, net.nodes); cls_full = classify(full.R[query], gold)
          # contributing edges E for this query = edges on the K admitted paths (=2*K_adm)
          record per-network: cls_full, all_edges_sound = AND(read.sound over contributing edges),
                              E = #contributing edges, contains_gold = (gold in full.R[query])
        aggregate cell:
          benefit = mean(cls=='CORRECT');  cost = mean(cls=='WRONG')
          net_gain = benefit - cost
          J_E      = mean(all_edges_sound)            # EMPIRICAL joint soundness (NOT r^E)
          r_pow_E  = r ** mean(E)                      # independence prediction (for contrast)
          contains_gold_rate = mean(contains_gold)
          store with paired-bootstrap CIs (resample the N_PER_CELL networks)

  --- H3 cells: for (L in HOP_LENGTHS, C in CYCLO_CHORDS, r in [0.90, 1.00]):  # high recall isolates ITERATION
        for n in range(N_PER_CELL):
          net  = gen_family_H(L, C, rng)
          read = read_network(net, r, rho=0, BREADTH, rng)
          full  = closure_FULL(read, net.nodes);  res_full  = full.R[query]
          naive = closure_NAIVE(read, net.nodes, query)
          acc_full  = (classify(res_full, gold)=='CORRECT')
          acc_naive = (classify(naive,   gold)=='CORRECT')
        cell gap = mean(acc_full) - mean(acc_naive)  with paired-bootstrap CI
        cyclomatic = |E| - |V| + 1

  ########################################################################
  # 8. STATISTICS / PASS-FAIL  (pre-registered precision)
  ########################################################################
  H3 PASS iff ALL:
    (a) length-2 stratum gap CI INCLUDES 0           (predicted TIE -> confirmation)
    (b) gap INCREASES with L: scipy.stats.page_trend_test (ordered) p<ALPHA AND
        Spearman(gap, L)>0 with bootstrap CI excluding 0 AND a hand-rolled
        Jonckheere-Terpstra (pairwise mannwhitneyu U-sum) p<ALPHA  (triangulate)
    (c) gap at max L CI-EXCLUDES 0 (positive)
    (d) gap also increases with cyclomatic number (Spearman>0, CI excl 0) at fixed L
  H4 PASS iff ALL (evaluated per (rho,gate) and reported):
    (a) net_gain(K) is INVERTED-U: a peak bin K* whose net_gain CI lies ABOVE BOTH
        neighbor bins' net_gain CIs (paired bootstrap on the two differences)
    (b) NET-POSITIVE REDUNDANCY REGION: exists K* with net_gain CI-lower >
        max(K=1 net_gain CI-upper, OFF-baseline net_gain CI-upper)
        [the SINGLE genuine disconfirmer is the ABSENCE of such a region]
    (c) peak location INCREASES by >=1 bin from lowest to highest recall
        (bootstrap argmax distribution; difference-in-peak CI excludes 0)
    (d) peak shifts OUTWARD by >=1 bin under gate ON vs OFF
    (e) measured J(E) > r^E whenever rho>0, AND the peak located using empirical
        J(E) sits FURTHER OUT than the peak located using the r^E independence model
  C3 ZERO-FP AUDIT PASS iff:
    (a) among networks where ALL contributing edges sound, P(gold in Mode-A output)==1.0
    (b) regress realized contains_gold_rate on empirical J(E) across cells -> slope~1
        (CI contains 1 or close); ATTRIBUTION RULE: refit predictor as r^E; a slope
        offset present under r^E that DISAPPEARS under J(E) = independence-approx
        failure (NOT a soundness failure) -> report which.
  ModeB (secondary): COLLAPSE only ever fires when >=1 contributing edge unsound
    (zero-FP DETECTION); report collapse_rate vs measured over-commitment rate.

  ########################################################################
  # 9. OUTPUT + FIGURES
  ########################################################################
  write method_out.json (validate with aii-json) with sections:
    metadata{config, seeds, algebra, n_per_cell, precision_params, breadth, bite_lost_to_convexity}
    H3{gap_by_hop:[{L,cyclo,acc_full,acc_naive,gap,gap_ci,n}], length2_tie{gap,ci,includes_zero},
       trend{page_p,spearman_rho,spearman_ci,jonckheere_p}, cyclo_trend{...}, PASS}
    H4{curves:[{recall,rho,gate,K,benefit,cost,net,net_ci,J_E,r_pow_E,mean_E,n}],
       peaks:[{recall,rho,gate,peak_K,peak_ci,above_neighbors}],
       peak_shift_recall{locations,shift_bins,MDE_met}, peak_shift_gate{...},
       JE_vs_independence{peak_JE,peak_indep,further_out}, net_positive_region{exists,K_star,beats_single,beats_naive}, PASS}
    C3{all_sound_contains_gold, slope_JE, slope_JE_ci, slope_rE, offset_disappears, PASS}
    modeB{collapse_rate_by_overcommit, zero_FP_detection}
    overall_verdict{H3:PASS/FAIL, H4:PASS/FAIL, C3:PASS/FAIL, notes}
  save PNGs: (i) gap vs L (with length-2 tie), (ii) benefit/cost/net vs K with peak
    markers per recall, (iii) J(E) vs r^E vs K, (iv) zero-FP audit scatter+fit.

  ########################################################################
  # 10. OPTIONAL SECONDARY: Allen Interval Algebra generality arm
  ########################################################################
  # Gate behind point-algebra PASS + time remaining. Build the validated Allen
  # 13x13 composition table from github.com/alreich/qualreas (JSON algebra defs)
  # OR generate it from the 4-endpoint point relations and SELF-VERIFY a few
  # canonical entries (before.before=before; before.after=universal). Generate
  # networks by sampling intervals [s,e]; gold Allen relation from endpoint order.
  # Re-run H4 redundancy curve only (richer 13-relation gradient -> smoother
  # inverted-U). Mark EXPLORATORY. PC is sound-but-incomplete for full Allen, so
  # report the closure-detectable rate as a LOWER BOUND (point arm stays exact).
fallback_plan: >-
  POINT-ALGEBRA SATURATION (compositions collapse to U too often -> no bite, Mode A inert): this is the degenerate all-universal
  limit, the ONLY under-specification outcome that genuinely disconfirms Mode A. Mitigate first: (1) bias generators toward
  MONOTONE-ALIGNED paths (all intermediates strictly between i and j in time, so every length-2 composition is < -aligned
  and contains the gold LT with bite) — already in gen_family_R; (2) lower BREADTH p_univ so reads are tighter; (3) if still
  flat, switch the redundancy curve to the Allen secondary arm (13 relations -> far richer narrowing gradient and a smoother
  inverted-U). Report the saturation rate either way.\n\nH3 GAP DOES NOT APPEAR (full ~= naive even on long chains): first
  DEBUG the implementations — assert NAIVE is truly single-pass and uses ONLY directly-read length-2 paths (no fixpoint, no
  converse-derived edges); assert pure chains carry NO shortcut (i,j) or skip edges; verify on a hand-checked 4-node chain
  that FULL resolves the query and NAIVE returns U. If correct and gap is genuinely ~0, that is the H3 DISCONFIRMER ('the
  win is any intersection, not iteration') — report it honestly; increase max L and cyclomatic chords to give iteration more
  room before concluding.\n\nNO INTERIOR INVERTED-U PEAK (cost never dominates within tested K at high recall -> net rises
  monotonically): this is EXPECTED at high recall and is itself the predicted recall-dependence (peak moved beyond the tested
  range). Guarantee an interior peak at the LOW-recall arm (r=0.60, rho=0.5) by (1) extending REDUNDANCY_K to 16-20, (2) adding
  r=0.50, (3) raising rho to 0.7 so J(E) decays faster. Pre-register that H4(a)/(b) are evaluated where an interior peak is
  structurally possible (low recall); peak MOVEMENT outward with recall (H4c) is confirmed even if the highest-recall peak
  sits at the range edge — report 'peak at/after K_max' rather than forcing one.\n\nNOISY PEAK LOCATION: raise N_PER_CELL
  to 1000, B_BOOT to 5000, and locate the peak on a lightly smoothed (3-bin moving-average) net-gain curve; bootstrap the
  argmax for a peak-location CI.\n\nALLEN COMPOSITION-TABLE RISK (transcription/lib errors): if the qualreas JSON cannot be
  fetched or the programmatic 4-endpoint table fails self-verification against canonical entries, DROP the Allen arm entirely
  — the convex point algebra alone fully de-risks H3 and H4 (it is the exact algebra of the NarrativeTime headline) and is
  the deliverable; note Allen generality as future work.\n\nMISSING STAT TOOLS: scipy lacks native Jonckheere-Terpstra — implement
  it by hand (sum of pairwise Mann-Whitney U across ordered groups, normal approximation for the p-value) and corroborate
  with scipy.stats.page_trend_test (native, ordered) plus a bootstrap CI on the Spearman slope; require >=2 of the 3 to agree
  before declaring an H3 trend.\n\nRUNTIME OVERRUN: closure on <=30-node networks is sub-millisecond, so the full grid (~100k
  tiny networks) completes in minutes; if anything is slow, parallelize cells with multiprocessing.Pool over the (recall,rho,gate,K)
  grid and cache per-network outcomes before bootstrapping. If still tight, shrink to the pre-registered minimum (RECALL_LEVELS
  kept at 4, N_PER_CELL=500, REDUNDANCY_K trimmed to [1,2,3,4,5,6,8,10]) — never drop below the pre-registered precision bars.
testing_plan: >-
  STAGE 0 — UNIT/SELF-VERIFY (seconds, must pass before anything else): assert the precomputed point-algebra COMP and CONV
  tables against hand-known identities (COMP[LT][LT]=LT, COMP[LT][GT]=U, COMP[EQ][GT]=GT, COMP[GT][LT]=U, CONV[LT|EQ]=EQ|GT,
  INTERSECT(LT|EQ,EQ|GT)=EQ); confirm composition is associative on a random sample of relation triples; confirm the convexity
  guard never emits relation 5 (NOT-EQUAL).\n\nSTAGE 1 — HAND-CHECKED TOY NETWORKS (seconds): (a) length-2 single path i-k-j
  with reads {LT|EQ} and {LT}: FULL and NAIVE must BOTH return {LT} (gap=0) — verifies the predicted length-2 tie. (b) pure
  length-3 chain i-a-b-j with all reads {LT|EQ}: FULL must resolve toward {LT} while NAIVE returns U(7) (no directly-read
  length-2 path at the query) — verifies the iteration gap appears. (c) inject ONE unsound edge that excludes gold and confirm
  it produces either a COLLAPSE (Mode-B detection) or a WRONG singleton (silent narrowing), never a false 'CORRECT'. (d) all-sound
  network: assert P(gold in FULL output)==1.0 (the zero-FP invariant).\n\nSTAGE 2 — MINI GRID (1-2 min): run N_PER_CELL=30,
  B_BOOT=200, REDUNDANCY_K=[1,2,3,4,6], RECALL_LEVELS=[0.6,0.9], HOP_LENGTHS=[2,3,4]. CONFIRMATION SIGNALS to look for before
  scaling: (i) H3 gap CI includes 0 at L=2 and is positive and growing by L=4; (ii) H4 net-gain curve is non-monotone with
  a visible interior peak at r=0.6 that is further right at r=0.9; (iii) measured J(E) exceeds r^E in the rho=0.5 cells; (iv)
  the zero-FP audit scatter hugs the identity line. If any signal is absent, debug at Stage 1 scale (do NOT scale up a broken
  pipeline).\n\nSTAGE 3 — DETERMINISM CHECK: re-run one mini cell with the same seed and assert byte-identical aggregate metrics
  (guards against unseeded RNG).\n\nSTAGE 4 — FULL RUN at pre-registered precision (N_PER_CELL=600, B_BOOT=2000, full grid),
  parallelized across cores. Then validate method_out.json with the aii-json skill against a written schema; verify every
  PASS/FAIL field is populated and that the overall_verdict matches the per-criterion booleans. Finally eyeball the four PNG
  figures for the predicted shapes (length-2 tie + rising gap; benefit/cost/net with peak markers; J(E) vs r^E divergence;
  zero-FP identity line).
</artifact_plan>



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

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-17 13:39:00 UTC

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

### [3] SKILL-INPUT — aii-python · 2026-06-17 13:39:08 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-parallel-computing · 2026-06-17 13:39:08 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [5] SKILL-INPUT — aii-long-running-tasks · 2026-06-17 13:39:14 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [6] SKILL-INPUT — aii-json · 2026-06-17 13:39:14 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [7] SKILL-INPUT — aii-file-size-limit · 2026-06-17 13:39:14 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [8] SKILL-INPUT — aii-use-hardware · 2026-06-17 13:39:14 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [9] SYSTEM-USER prompt · 2026-06-17 13:49:28 UTC

```
continue where you left off — reuse any partial work already written to disk. Do NOT start over.
```

### [10] SYSTEM-USER prompt · 2026-06-17 14:30:21 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_2/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_2/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_2_idx5
type: experiment
title: >-
  Synthetic De-Risking of H3 (Iterated Closure > Naive Intersection) and H4 (Recall-Dependent Redundancy Inverted-U) via Controlled
  QCN + Simulated-Reader Channel
summary: >-
  A zero-LLM-spend, self-contained CPU experiment that establishes H3 and H4 on clean synthetic ground truth, decoupling the
  closure mechanism from corpus/LLM-elicitation risk. We generate random CONSISTENT qualitative constraint networks (QCNs)
  by realization (every network is consistent by construction because it is read off a sampled point/interval assignment),
  then simulate the LLM reader as an EXACTLY-controlled noisy channel with three knobs: per-edge recall r = P(gold in emitted
  set), a sub-universal breadth distribution, and a within-network cross-edge soundness correlation rho (latent equicorrelation
  Gaussian). PRIMARY algebra = the CONVEX POINT ALGEBRA (base {<,=,>}; PC provably COMPLETE; trivially-correct 3x3 composition
  table; matches the NarrativeTime start-point arm). We implement three closure variants (FULL iterated path-consistency /
  NAIVE single-pass query-node intersection / OFF) and measure: (H3) FULL-minus-NAIVE selective-accuracy gap stratified by
  hop-count L and cyclomatic number, predicted ~0 at length-2 and GROWING with L/cycles, with an ordered-alternative trend
  test; (H4) the net Mode-A gain decomposed into a narrowing BENEFIT curve and a silent-narrowing COST curve = 1 - J(E) over
  redundancy at >=4 fixed recall levels, with the inverted-U peak located, shown to move OUTWARD with recall and under a recall-floor
  gate, with J(E) MEASURED empirically (not assumed as r^E) so positive rho makes the peak sit further out than the independence
  model; plus (C3) a zero-FP audit (realized P(gold in output) vs empirical J(E), slope ~1, attribution rule). Emits an aii-json-validated
  method_out.json with curves, located peaks, audit slopes, and explicit PASS/FAIL on H3 and H4 at the pre-registered estimation
  precision. Optional secondary generality arm: Allen Interval Algebra via the validated qualreas composition table.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  ########################################################################
  # NOTE ON DEPENDENCIES: this artifact lists depends_on=[] because it is a
  # SELF-CONTAINED synthetic study. The 'dataset' is the QCN generator coded
  # INLINE (same Renz-Nebel-style realization family the synthetic DATASET
  # artifact uses). NO external dataset, NO NL text, NO LLM calls (zero spend).
  # Everything below runs on CPU in minutes; parallelize with multiprocessing
  # (see aii-parallel-computing). Seed EVERYTHING (numpy.random.default_rng with
  # a per-cell seed) for byte-reproducibility.
  ########################################################################

  === CONFIG (pre-registered; freeze BEFORE the full run) ===
  ALGEBRA_PRIMARY      = 'point'        # convex point algebra (PC COMPLETE)
  ALGEBRA_SECONDARY    = 'allen'        # optional generality arm (gate behind point PASS)
  RECALL_LEVELS        = [0.60, 0.75, 0.90, 0.95]   # >=4 FIXED levels (H4 axis)
  RHO_LEVELS           = [0.0, 0.5]     # independent vs positively-correlated reader errors
  GATE_MODES           = ['off', 'on'] # recall-floor gate
  REDUNDANCY_K         = [1,2,3,4,5,6,7,8,10,12]    # # parallel constraining paths (H4 axis)
  HOP_LENGTHS          = [2,3,4,5,6]    # chain length L between query endpoints (H3 axis)
  CYCLO_CHORDS         = [0,1,2,3]      # extra cross-edges -> cyclomatic number (H3 axis)
  N_PER_CELL           = 600            # >=500 networks per cell (pre-registered)
  BREADTH = {p_singleton:0.45, p_two:0.40, p_univ:0.15}  # sub-universal w/ bite; avg|set|~1.7
  B_BOOT               = 2000           # bootstrap resamples
  ALPHA                = 0.05
  GATE_DROP_FRACTION   = 0.20           # gate removes bottom-confidence edges
  SEED_BASE            = 20260617

  ########################################################################
  # 1. RELATION ALGEBRA  (PRIMARY = convex point algebra)
  ########################################################################
  # Encode relations as 3-bit masks: LT=1, EQ=2, GT=4, U=7, EMPTY=0.
  # Convex (allowed reader outputs): {LT(1),EQ(2),GT(4),LT|EQ(3),EQ|GT(6),U(7)}.
  # FORBIDDEN as a read: EMPTY(0)=inconsistent, LT|GT(5)=NOT-EQUAL is the ONLY
  #   non-convex relation -> if any widening would produce 5, widen to U(7)
  #   ('widen non-convex {<,>} to VAGUE') and COUNT the bite lost.

  BASE_COMP = {  # composition of single base relations (Vilain-Kautz point algebra)
    (LT,LT):LT, (LT,EQ):LT, (LT,GT):U,
    (EQ,LT):LT, (EQ,EQ):EQ, (EQ,GT):GT,
    (GT,LT):U,  (GT,EQ):GT, (GT,GT):GT }
  CONV_BASE = {LT:GT, EQ:EQ, GT:LT}

  precompute COMP[R][S] for R,S in 0..7:
      COMP[R][S] = OR over base bit a in R, base bit b in S of BASE_COMP[(a,b)]
  precompute CONV[R] = OR over base bit a in R of CONV_BASE[a]
  def INTERSECT(R,S): return R & S          # algebra intersection
  def compose(R,S):   return COMP[R][S]

  SELF-VERIFY (assert before any run):
    COMP[LT][LT]==LT; COMP[LT][GT]==U; COMP[EQ][GT]==GT; COMP[GT][LT]==U
    CONV[LT]==GT; CONV[LT|EQ]==EQ|GT; INTERSECT(LT|EQ, EQ|GT)==EQ
    composition associative on a random sample of triples (spot check)

  ########################################################################
  # 2. QCN GENERATORS  (consistent BY CONSTRUCTION via realization)
  ########################################################################
  # FAMILY R (REDUNDANCY, for H4): K parallel length-2 paths i -> m_k -> j.
  def gen_family_R(K, rng):
      # sample distinct timestamps so gold(i,j) is a definite base relation
      t_i = 0.0; t_j = 10.0                     # ensures gold(i,j) = LT
      M   = [rng.uniform(1,9) for _ in range(K)] # each intermediate between i,j
      nodes = [i, j] + m_k...
      gold[a][b] = sign-relation(t_a, t_b) in {LT,EQ,GT}   # from realization
      observed_edges = {(i,m_k),(m_k,j) for all k}          # the reader sees these
      query = (i,j)  ;  gold_query = LT
      return network(nodes, gold, observed_edges, query)

  # FAMILY H (HOP/CYCLOMATIC, for H3): chain of length L plus C chords.
  def gen_family_H(L, C, rng):
      chain = [i, x1, ..., x_{L-1}, j]  with strictly increasing timestamps
      observed_edges = consecutive pairs along the chain   # (i,x1),(x1,x2),...,(x_{L-1},j)
      # IMPORTANT: NO direct (i,j) edge and NO shortcut edges read -> a pure chain.
      add C chords: pick C non-consecutive node pairs, ADD their gold relation as
          observed edges (raises cyclomatic number = |E| - |V| + 1, gives NAIVE
          some length-2 shortcuts while FULL still benefits more from iteration)
      gold[a][b] from timestamp realization; query=(i,j); gold_query = LT
      return network(...)
  # Both families are CONSISTENT by construction (read off a real point assignment).

  ########################################################################
  # 3. SIMULATED READER CHANNEL  (exact recall / breadth / rho knobs)
  ########################################################################
  def read_network(net, recall r, rho, breadth, rng):
      qn = qnorm(r)                          # Phi^{-1}(r)
      Ulatent = rng.normal()                 # ONE per-network latent (document factor)
      for each observed edge e with gold base g = net.gold[e]:
          V = rng.normal()
          z_e = sqrt(rho)*Ulatent + sqrt(1-rho)*V    # equicorrelated latent
          sound_e = (z_e <= qn)              # marginal P(sound)=r ; corr(sound)~rho
          conf_e  = Phi(-z_e) + tiny_noise   # NOISY soundness proxy for the gate
          if sound_e:
              S_e = emit_sound_superset(g, breadth, rng)   # convex set CONTAINING g
          else:
              S_e = emit_unsound_set(g, rng)               # convex set NOT containing g
          if S_e == LT|GT(5): S_e = U(7)     # convexity guard; record bite_lost++
          read[e] = S_e ; read.conf[e]=conf_e ; read.sound[e]=sound_e
      # seed converse edges from the ALGEBRA (never from the reader):
      for each read edge (a,b): read[(b,a)] = CONV[read[(a,b)]]
      return read

  emit_sound_superset(g, breadth):   # stay convex, contain g, mostly sub-universal
    if g==LT: sample from {LT, LT|EQ, U} with weights (p_singleton, p_two, p_univ)
    if g==EQ: sample from {EQ, LT|EQ, EQ|GT, U}
    if g==GT: sample from {GT, EQ|GT, U}
  emit_unsound_set(g):               # convex, sub-universal, EXCLUDES g (over-commit)
    if g==LT: sample from {EQ, GT, EQ|GT}
    if g==EQ: sample from {LT, GT}          # (LT|GT is non-convex -> excluded)
    if g==GT: sample from {LT, EQ, LT|EQ}

  ########################################################################
  # 4. CLOSURE VARIANTS
  ########################################################################
  def closure_FULL(read, nodes):     # iterated path-consistency (PC-2 / Mackworth)
      R = dense matrix: R[a][b]=read[(a,b)] if present else U(7); R[a][a]=EQ
      changed=True
      while changed:
          changed=False
          for k in nodes: for i in nodes: for j in nodes:
              if i,j,k not distinct: continue
              new = INTERSECT(R[i][j], compose(R[i][k], R[k][j]))
              if new != R[i][j]:
                  R[i][j]=new ; R[j][i]=CONV[new]          # algebra-seeded converse
                  if new==EMPTY: return ('COLLAPSE', R)     # Mode-B certificate
                  changed=True
      return ('OK', R)

  def closure_NAIVE(read, nodes, query=(i,j)):  # single pass, NO fixpoint, NO
      # converse-derived propagation: 'PoT + one obvious intersection step'
      res = read.get((i,j), U)                    # direct reading (U if held out)
      for k in nodes, k!=i,j:
          if (i,k) in read and (k,j) in read:     # ONLY directly-read length-2 paths
              res = INTERSECT(res, compose(read[(i,k)], read[(k,j)]))
      return res

  def closure_OFF(read, query): return read.get(query, U)   # direct read only

  ########################################################################
  # 5. MODE-A ANSWER EXTRACTION + CLASSIFICATION
  ########################################################################
  def classify(result_set, gold_query):
      if result_set==EMPTY:                 return 'COLLAPSE'   # Mode-B detection
      if popcount(result_set)==1:
          return 'CORRECT' if result_set==gold_query else 'WRONG'  # WRONG=silent narrowing
      return 'ABSTAIN'                       # non-singleton -> abstain (coverage axis)
  # Coverage object = single-relation resolution, applied IDENTICALLY to every variant.

  ########################################################################
  # 6. RECALL-FLOOR GATE
  ########################################################################
  # gate ON: before narrowing, drop the bottom GATE_DROP_FRACTION of edges by conf_e
  #   (a NOISY proxy, NOT ground-truth soundness -> realistic, non-oracle). A path
  #   is admitted only if ALL its edges survive the gate; if no path resolves, ABSTAIN.
  # Compare peak location gate-ON vs gate-OFF (predict: ON shifts peak OUTWARD).

  ########################################################################
  # 7. EXPERIMENT DRIVER
  ########################################################################
  --- H4 cells: for (r in RECALL_LEVELS, rho in RHO_LEVELS, gate in GATE_MODES, K in REDUNDANCY_K):
        rng = default_rng(hash(SEED_BASE, r, rho, gate, K))
        for n in range(N_PER_CELL):
          net  = gen_family_R(K, rng)
          read = read_network(net, r, rho, BREADTH, rng)
          read_g = apply_gate(read) if gate=='on' else read
          full = closure_FULL(read_g, net.nodes); cls_full = classify(full.R[query], gold)
          # contributing edges E for this query = edges on the K admitted paths (=2*K_adm)
          record per-network: cls_full, all_edges_sound = AND(read.sound over contributing edges),
                              E = #contributing edges, contains_gold = (gold in full.R[query])
        aggregate cell:
          benefit = mean(cls=='CORRECT');  cost = mean(cls=='WRONG')
          net_gain = benefit - cost
          J_E      = mean(all_edges_sound)            # EMPIRICAL joint soundness (NOT r^E)
          r_pow_E  = r ** mean(E)                      # independence prediction (for contrast)
          contains_gold_rate = mean(contains_gold)
          store with paired-bootstrap CIs (resample the N_PER_CELL networks)

  --- H3 cells: for (L in HOP_LENGTHS, C in CYCLO_CHORDS, r in [0.90, 1.00]):  # high recall isolates ITERATION
        for n in range(N_PER_CELL):
          net  = gen_family_H(L, C, rng)
          read = read_network(net, r, rho=0, BREADTH, rng)
          full  = closure_FULL(read, net.nodes);  res_full  = full.R[query]
          naive = closure_NAIVE(read, net.nodes, query)
          acc_full  = (classify(res_full, gold)=='CORRECT')
          acc_naive = (classify(naive,   gold)=='CORRECT')
        cell gap = mean(acc_full) - mean(acc_naive)  with paired-bootstrap CI
        cyclomatic = |E| - |V| + 1

  ########################################################################
  # 8. STATISTICS / PASS-FAIL  (pre-registered precision)
  ########################################################################
  H3 PASS iff ALL:
    (a) length-2 stratum gap CI INCLUDES 0           (predicted TIE -> confirmation)
    (b) gap INCREASES with L: scipy.stats.page_trend_test (ordered) p<ALPHA AND
        Spearman(gap, L)>0 with bootstrap CI excluding 0 AND a hand-rolled
        Jonckheere-Terpstra (pairwise mannwhitneyu U-sum) p<ALPHA  (triangulate)
    (c) gap at max L CI-EXCLUDES 0 (positive)
    (d) gap also increases with cyclomatic number (Spearman>0, CI excl 0) at fixed L
  H4 PASS iff ALL (evaluated per (rho,gate) and reported):
    (a) net_gain(K) is INVERTED-U: a peak bin K* whose net_gain CI lies ABOVE BOTH
        neighbor bins' net_gain CIs (paired bootstrap on the two differences)
    (b) NET-POSITIVE REDUNDANCY REGION: exists K* with net_gain CI-lower >
        max(K=1 net_gain CI-upper, OFF-baseline net_gain CI-upper)
        [the SINGLE genuine disconfirmer is the ABSENCE of such a region]
    (c) peak location INCREASES by >=1 bin from lowest to highest recall
        (bootstrap argmax distribution; difference-in-peak CI excludes 0)
    (d) peak shifts OUTWARD by >=1 bin under gate ON vs OFF
    (e) measured J(E) > r^E whenever rho>0, AND the peak located using empirical
        J(E) sits FURTHER OUT than the peak located using the r^E independence model
  C3 ZERO-FP AUDIT PASS iff:
    (a) among networks where ALL contributing edges sound, P(gold in Mode-A output)==1.0
    (b) regress realized contains_gold_rate on empirical J(E) across cells -> slope~1
        (CI contains 1 or close); ATTRIBUTION RULE: refit predictor as r^E; a slope
        offset present under r^E that DISAPPEARS under J(E) = independence-approx
        failure (NOT a soundness failure) -> report which.
  ModeB (secondary): COLLAPSE only ever fires when >=1 contributing edge unsound
    (zero-FP DETECTION); report collapse_rate vs measured over-commitment rate.

  ########################################################################
  # 9. OUTPUT + FIGURES
  ########################################################################
  write method_out.json (validate with aii-json) with sections:
    metadata{config, seeds, algebra, n_per_cell, precision_params, breadth, bite_lost_to_convexity}
    H3{gap_by_hop:[{L,cyclo,acc_full,acc_naive,gap,gap_ci,n}], length2_tie{gap,ci,includes_zero},
       trend{page_p,spearman_rho,spearman_ci,jonckheere_p}, cyclo_trend{...}, PASS}
    H4{curves:[{recall,rho,gate,K,benefit,cost,net,net_ci,J_E,r_pow_E,mean_E,n}],
       peaks:[{recall,rho,gate,peak_K,peak_ci,above_neighbors}],
       peak_shift_recall{locations,shift_bins,MDE_met}, peak_shift_gate{...},
       JE_vs_independence{peak_JE,peak_indep,further_out}, net_positive_region{exists,K_star,beats_single,beats_naive}, PASS}
    C3{all_sound_contains_gold, slope_JE, slope_JE_ci, slope_rE, offset_disappears, PASS}
    modeB{collapse_rate_by_overcommit, zero_FP_detection}
    overall_verdict{H3:PASS/FAIL, H4:PASS/FAIL, C3:PASS/FAIL, notes}
  save PNGs: (i) gap vs L (with length-2 tie), (ii) benefit/cost/net vs K with peak
    markers per recall, (iii) J(E) vs r^E vs K, (iv) zero-FP audit scatter+fit.

  ########################################################################
  # 10. OPTIONAL SECONDARY: Allen Interval Algebra generality arm
  ########################################################################
  # Gate behind point-algebra PASS + time remaining. Build the validated Allen
  # 13x13 composition table from github.com/alreich/qualreas (JSON algebra defs)
  # OR generate it from the 4-endpoint point relations and SELF-VERIFY a few
  # canonical entries (before.before=before; before.after=universal). Generate
  # networks by sampling intervals [s,e]; gold Allen relation from endpoint order.
  # Re-run H4 redundancy curve only (richer 13-relation gradient -> smoother
  # inverted-U). Mark EXPLORATORY. PC is sound-but-incomplete for full Allen, so
  # report the closure-detectable rate as a LOWER BOUND (point arm stays exact).
fallback_plan: >-
  POINT-ALGEBRA SATURATION (compositions collapse to U too often -> no bite, Mode A inert): this is the degenerate all-universal
  limit, the ONLY under-specification outcome that genuinely disconfirms Mode A. Mitigate first: (1) bias generators toward
  MONOTONE-ALIGNED paths (all intermediates strictly between i and j in time, so every length-2 composition is < -aligned
  and contains the gold LT with bite) — already in gen_family_R; (2) lower BREADTH p_univ so reads are tighter; (3) if still
  flat, switch the redundancy curve to the Allen secondary arm (13 relations -> far richer narrowing gradient and a smoother
  inverted-U). Report the saturation rate either way.\n\nH3 GAP DOES NOT APPEAR (full ~= naive even on long chains): first
  DEBUG the implementations — assert NAIVE is truly single-pass and uses ONLY directly-read length-2 paths (no fixpoint, no
  converse-derived edges); assert pure chains carry NO shortcut (i,j) or skip edges; verify on a hand-checked 4-node chain
  that FULL resolves the query and NAIVE returns U. If correct and gap is genuinely ~0, that is the H3 DISCONFIRMER ('the
  win is any intersection, not iteration') — report it honestly; increase max L and cyclomatic chords to give iteration more
  room before concluding.\n\nNO INTERIOR INVERTED-U PEAK (cost never dominates within tested K at high recall -> net rises
  monotonically): this is EXPECTED at high recall and is itself the predicted recall-dependence (peak moved beyond the tested
  range). Guarantee an interior peak at the LOW-recall arm (r=0.60, rho=0.5) by (1) extending REDUNDANCY_K to 16-20, (2) adding
  r=0.50, (3) raising rho to 0.7 so J(E) decays faster. Pre-register that H4(a)/(b) are evaluated where an interior peak is
  structurally possible (low recall); peak MOVEMENT outward with recall (H4c) is confirmed even if the highest-recall peak
  sits at the range edge — report 'peak at/after K_max' rather than forcing one.\n\nNOISY PEAK LOCATION: raise N_PER_CELL
  to 1000, B_BOOT to 5000, and locate the peak on a lightly smoothed (3-bin moving-average) net-gain curve; bootstrap the
  argmax for a peak-location CI.\n\nALLEN COMPOSITION-TABLE RISK (transcription/lib errors): if the qualreas JSON cannot be
  fetched or the programmatic 4-endpoint table fails self-verification against canonical entries, DROP the Allen arm entirely
  — the convex point algebra alone fully de-risks H3 and H4 (it is the exact algebra of the NarrativeTime headline) and is
  the deliverable; note Allen generality as future work.\n\nMISSING STAT TOOLS: scipy lacks native Jonckheere-Terpstra — implement
  it by hand (sum of pairwise Mann-Whitney U across ordered groups, normal approximation for the p-value) and corroborate
  with scipy.stats.page_trend_test (native, ordered) plus a bootstrap CI on the Spearman slope; require >=2 of the 3 to agree
  before declaring an H3 trend.\n\nRUNTIME OVERRUN: closure on <=30-node networks is sub-millisecond, so the full grid (~100k
  tiny networks) completes in minutes; if anything is slow, parallelize cells with multiprocessing.Pool over the (recall,rho,gate,K)
  grid and cache per-network outcomes before bootstrapping. If still tight, shrink to the pre-registered minimum (RECALL_LEVELS
  kept at 4, N_PER_CELL=500, REDUNDANCY_K trimmed to [1,2,3,4,5,6,8,10]) — never drop below the pre-registered precision bars.
testing_plan: >-
  STAGE 0 — UNIT/SELF-VERIFY (seconds, must pass before anything else): assert the precomputed point-algebra COMP and CONV
  tables against hand-known identities (COMP[LT][LT]=LT, COMP[LT][GT]=U, COMP[EQ][GT]=GT, COMP[GT][LT]=U, CONV[LT|EQ]=EQ|GT,
  INTERSECT(LT|EQ,EQ|GT)=EQ); confirm composition is associative on a random sample of relation triples; confirm the convexity
  guard never emits relation 5 (NOT-EQUAL).\n\nSTAGE 1 — HAND-CHECKED TOY NETWORKS (seconds): (a) length-2 single path i-k-j
  with reads {LT|EQ} and {LT}: FULL and NAIVE must BOTH return {LT} (gap=0) — verifies the predicted length-2 tie. (b) pure
  length-3 chain i-a-b-j with all reads {LT|EQ}: FULL must resolve toward {LT} while NAIVE returns U(7) (no directly-read
  length-2 path at the query) — verifies the iteration gap appears. (c) inject ONE unsound edge that excludes gold and confirm
  it produces either a COLLAPSE (Mode-B detection) or a WRONG singleton (silent narrowing), never a false 'CORRECT'. (d) all-sound
  network: assert P(gold in FULL output)==1.0 (the zero-FP invariant).\n\nSTAGE 2 — MINI GRID (1-2 min): run N_PER_CELL=30,
  B_BOOT=200, REDUNDANCY_K=[1,2,3,4,6], RECALL_LEVELS=[0.6,0.9], HOP_LENGTHS=[2,3,4]. CONFIRMATION SIGNALS to look for before
  scaling: (i) H3 gap CI includes 0 at L=2 and is positive and growing by L=4; (ii) H4 net-gain curve is non-monotone with
  a visible interior peak at r=0.6 that is further right at r=0.9; (iii) measured J(E) exceeds r^E in the rho=0.5 cells; (iv)
  the zero-FP audit scatter hugs the identity line. If any signal is absent, debug at Stage 1 scale (do NOT scale up a broken
  pipeline).\n\nSTAGE 3 — DETERMINISM CHECK: re-run one mini cell with the same seed and assert byte-identical aggregate metrics
  (guards against unseeded RNG).\n\nSTAGE 4 — FULL RUN at pre-registered precision (N_PER_CELL=600, B_BOOT=2000, full grid),
  parallelized across cores. Then validate method_out.json with the aii-json skill against a written schema; verify every
  PASS/FAIL field is populated and that the overall_verdict matches the per-criterion booleans. Finally eyeball the four PNG
  figures for the predicted shapes (length-2 tie + rising gap; benefit/cost/net with peak markers; J(E) vs r^E divergence;
  zero-FP identity line).
</artifact_plan>



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

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Descriptive title (roughly 30-90 characters). Must describe content, NOT a status message.",
      "maxLength": 90,
      "minLength": 30,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````
