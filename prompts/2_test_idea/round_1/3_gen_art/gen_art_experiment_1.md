# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 13:39:23 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx4
type: experiment
title: >-
  T0 A-Priori Envelope Gate + Reusable QCN Path-Consistency Engine (zero-LLM-spend)
summary: >-
  Implement and unit-validate a reusable QCN path-consistency engine (Allen-13, convex point algebra, RCC-8; FULL iterated
  PC-2, NAIVE single-pass intersection, closure-OFF), then run the decisive zero-LLM-spend T0 envelope gate over three real
  temporal corpora (NarrativeTime/TimeBankNT, TDDMan, MATRES) from GOLD GRAPHS ALONE. Compute the deduction-required x multi-path
  x bite-after-widening x singleton-resolving funnel (N*), the >=3-edge/cyclic iteration envelope, widening bite-loss, a paired-bootstrap
  power/MDE calc per corpus, and (NarrativeTime) the locally-justifiable vs purely-timeline-implied non-circularity split.
  Score each corpus against the pre-registered applicability NUMBER (>=10% general / 5-10% module / <5% niche), output the
  hosting decision + explicit GO/NO-GO verdict, and report the expected MATRES N*~0 vs NarrativeTime/TDDMan N*>>0 as gate
  validation. cpu-only, $0 LLM. Engine and parsed graphs are checkpointed for reuse by iter-2 Tier-1.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # =====================================================================
  # ARTIFACT experiment_iter1_dir4 -- T0 ENVELOPE GATE + CLOSURE ENGINE
  # ZERO LLM SPEND. CPU-only. All computation from GOLD GRAPHS alone.
  # Runtime target: minutes (graph ops are ms/network). uv venv, no GPU.
  # Deliverable: method_out.json (aii-json validated) + reusable engine module.
  # =====================================================================

  # ---------------------------------------------------------------------
  # SETUP (uv, no LLM, no GPU)
  # ---------------------------------------------------------------------
  # uv venv; uv pip install numpy scipy pandas networkx requests bitsets lxml
  # git clone https://github.com/alreich/qualreas  -> use its Algebras/*.json as
  #   the AUTHORITATIVE composition/converse tables (Allen, Linear Point, RCC8).
  #   Do NOT depend on qualreas runtime; only parse its JSON tables, then run our
  #   own instrumented PC engine (we need FULL/NAIVE/OFF variants it does not expose).
  # Log to logs/run.log. Cache all parsed corpora + gold graphs to ./cache/ (pickle/json)
  #   so reruns and iter-2 Tier-1 can reload without re-parsing.

  # =====================================================================
  # MODULE 1 -- ALGEBRA + QCN PATH-CONSISTENCY ENGINE (reusable, ms/network)
  # =====================================================================

  class Algebra:                       # one per: ALLEN13, POINT (convex), RCC8
      base_relations: list[str]        # e.g. POINT=['<','=','>']; ALLEN=13 rels
      identity: frozenset              # POINT={'='}; ALLEN={'eq'}; RCC8={'EQ'}
      universe: frozenset              # all base relations (= 'no information')
      converse: dict[str,str]          # per-base-relation converse, FROM ALGEBRA ONLY
      compose_tbl: dict[(str,str), frozenset]   # base x base -> set, FROM ALGEBRA ONLY
      # Load from qualreas Algebras/*.json (preferred). If parse fails, hand-code:
      #   POINT: trivial (<o<=<, <o== <, <o> = universe, =o anything = that, etc.)
      #   ALLEN: 13x13 table from Allen 1983 / Wikipedia 'Allen's interval algebra'
      #   RCC8: standard 8x8 table.  VALIDATE hand-coded vs qualreas on all cells.

      def compose_sets(R, S):  return union over r in R, s in S of compose_tbl[(r,s)]
      def converse_set(R):     return { converse[r] for r in R }
      def intersect(R, S):     return R & S

  class QCN:                           # qualitative constraint network
      nodes: list                      # events (ids)
      edge: dict[(i,j)] -> frozenset   # relation set; missing edge => universe
      # invariants: edge[(j,i)] == converse_set(edge[(i,j)]); edge[(i,i)] == identity
      def get(i,j):  return edge.get((i,j), universe)   # symmetric via converse

  # --- THREE INSTRUMENTED CLOSURE VARIANTS ---

  def pc2_full(qcn) -> (qcn_closed, consistent: bool, fired_log):
      # Mackworth PC-2 to FIXPOINT. Seed converses+identity FROM ALGEBRA.
      queue = all ordered triples / all edges (worklist)
      while queue:
          (i,k,j) = pop
          new = intersect( qcn.get(i,j), compose_sets(qcn.get(i,k), qcn.get(k,j)) )
          if new != qcn.get(i,j):
              if new == empty: return (qcn, consistent=False, log)   # MODE B certificate
              qcn.set(i,j,new); qcn.set(j,i, converse_set(new))      # propagate + converse
              push all triples touching (i,j) back onto queue
              record (i,j,k,fired_composition) in fired_log          # trace-graph seed
      return (qcn, consistent=True, fired_log)

  def naive_single_pass(qcn, query=(q1,q2)) -> frozenset:
      # 'Path-of-Thoughts + ONE intersection step': intersect compositions arriving
      # at the query node over LENGTH-2 paths only, in a SINGLE pass.
      # NO fixpoint, NO converse seeding beyond gold edges, NO propagation to other edges.
      R = universe
      for k in nodes if k not in {q1,q2}:
          if has_gold(q1,k) and has_gold(k,q2):
              R = intersect(R, compose_sets(qcn.get(q1,k), qcn.get(k,q2)))
      return R

  def closure_off(qcn, query) -> frozenset:
      return universe    # table held fixed but closure NOT run (baseline for later tiers)

  # --- UNIT TESTS (must pass before any T0 run) ---
  # T-A  hand-checked Allen compositions vs qualreas/Wikipedia (e.g. o o o = {b,o,m};
  #      b o b = {b}; d o di = universe; etc.) -- ALL 169 cells equal qualreas.
  # T-P  point: '<' o '<' = {'<'}; '<' o '=' = {'<'}; '<' o '>' = universe; converses.
  # T-C  consistency: triangle A<B, B<C, C<A  => pc2_full returns consistent=False.
  # T-CMP convex-point COMPLETENESS: for random small convex point nets (n<=6),
  #      pc2_full minimal labels == labels from brute-force enumeration of all
  #      consistent point scenarios (ground-truth minimal). Confirms PC complete on POINT.
  # T-IT iteration isolation: build ONE acyclic length-2 query (naive==full) AND ONE
  #      3-hop / cyclic query where full resolves a singleton but naive leaves it loose.
  #      Assert naive==full on length-2, naive!=full on the 3-hop/cyclic case.
  # Record all test outcomes in method_out.engine_validation.

  # =====================================================================
  # MODULE 2 -- CORPUS PARSERS -> per-document GOLD GRAPHS (zero LLM)
  # =====================================================================

  # ---- MATRES (github.com/CogComp/MATRES: timebank.txt, aquaint.txt, platinum.txt)
  #   cols: docid, verb1, verb2, eiid1, eiid2, rel in {BEFORE,AFTER,EQUAL,VAGUE}
  #   ALGEBRA = POINT (convex) on event START-POINTS:
  #     BEFORE->{'<'}, AFTER->{'>'}, EQUAL->{'='}, VAGUE->universe (NOT evaluable).
  #   LOCALITY: annotation window is same/adjacent-sentence => deduction-proxy(i)
  #     FAILS for ~all edges by construction => expected N*~0 (gate validation).
  #     Optionally confirm by mapping eiid->sentence via TBAQ-cleaned .tml
  #     (github.com/jspotter/TempEval-3 data/TBAQ-cleaned), else assert structurally.
  #
  # ---- TDDMan (github.com/aakanksha19/TDDiscourse: TDDMan/TDDMan{Train,Dev,Test}.tsv)
  #   cols (tab): docid, e1, e2, rel in {a=After,b=Before,i=Includes,ii=Is_Included,s=Simultaneous}
  #   ALGEBRA = coarse interval via ALLEN-subset image (primary STRICT singleton map):
  #     b->{'b'} a->{'bi'} i->{'di'} ii->{'d'} s->{'eq'}  (compose in ALLEN-13).
  #     SENSITIVITY (report alongside): broad map i->{di,si,fi}, ii->{d,s,f}, s->{eq,s,si,f,fi}.
  #   LOCALITY: TDDMan pairs are ALL >1-sentence-apart, manual, 'cannot be inferred
  #     automatically' => deduction-proxy(i) holds for EVERY edge BY CONSTRUCTION
  #     (no source text needed) + this is the NON-CIRCULARITY anchor.
  #   GOLD GRAPH per docid = all TDDMan pairs in that doc (sparse manual set).
  #
  # ---- NarrativeTime/TimeBankNT (arXiv:1908.11443, LREC-COLING 2024) -- CO-PRIMARY
  #   LOCATE DATA FIRST (search budget ~10 min): try github text-machine-lab,
  #     project page text-machine.cs.uml.edu/projects/temporal/, and grep the LREC
  #     paper PDF (aclanthology.org/2024.lrec-main.1054) for 'github'/'available at'.
  #   Annotation = each event gets a timeline interval [start,end] (with vagueness combs).
  #   Build FULL gold graph from timeline coords (full TLink coverage):
  #     POINT arm (PRIMARY): start(u) vs start(v) -> {'<','=','>'}; widen genuine != (non-convex)
  #       to VAGUE/universe to keep PC COMPLETE; MEASURE bite lost by this widening.
  #     ALLEN full-interval arm (lower-bound detector): derive 13-rel from [start,end] order.
  #   LOCALITY: need event sentence index (from NarrativeTime files or aligned TimeBank
  #     .tml). proxy(i) = |sent(u)-sent(v)| > 1.
  #
  # All parsers emit: {docid -> {events:set, gold_edges:{(u,v):rel_set}, sent_idx:{e->int}}}
  # Cache to ./cache/<corpus>_graphs.json.

  # =====================================================================
  # MODULE 3 -- T0 ENVELOPE FUNNEL per corpus (the gate)
  # =====================================================================

  for corpus in [NARRATIVETIME, TDDMAN, MATRES]:
    alg = algebra_for(corpus)
    EVALUABLE = []          # primary denominator
    funnel = Counter()      # i, i_ii, i_ii_iii, N_star
    iter_envelope = Counter()   # full_resolves, naive_resolves, full_only(>=3-edge/cyclic)
    bite_loss = 0; widening_destroyed = 0
    for doc, G in corpus_graphs.items():
      for (u,v), gold in G.gold_edges.items():
          if gold is universe/VAGUE or not singleton(gold): continue   # need determinate gold
          # primary evaluable def: gold singleton AND both u,v appear in >=1 OTHER gold edge
          if degree(u)<2 and degree(v)<2: continue
          EVALUABLE.append((doc,u,v))
          Gm = G minus direct edge (u,v)        # HOLD OUT the query edge; (u,v)=universe

          # (i) deduction-required proxy (no local/adjacent-sentence co-occurrence)
          if corpus==TDDMAN: i_ok = True                       # by construction
          elif corpus==MATRES: i_ok = (sent dist>1 if positions else False)
          else: i_ok = abs(sent_idx[u]-sent_idx[v]) > 1        # NarrativeTime
          if not i_ok: continue
          funnel['i'] += 1

          # (ii) >=2 constraining paths through DISTINCT intermediates
          inter2 = { w for w in Gm.nodes if has_gold(u,w) and has_gold(w,v) }   # length-2
          longer = exists_path(Gm, u, v, min_len>=3) or in_cycle(Gm,u,v)
          if len(inter2) < 2 and not (len(inter2)>=1 and longer): continue
          funnel['i_ii'] += 1

          # (iv pre-widen) does FULL closure on held-out gold graph recover gold singleton?
          closed,_ ,_ = pc2_full(Gm_with_query_universe)
          derived_full = closed.get(u,v)
          derived_naive = naive_single_pass(Gm_with_query_universe, (u,v))
          resolves_full  = (derived_full  == gold)            # singleton-to-correct (FULL)
          resolves_naive = (derived_naive == gold)            # singleton-to-correct (NAIVE/length-2)
          if resolves_full: iter_envelope['full_resolves'] += 1
          if resolves_naive: iter_envelope['naive_resolves'] += 1
          if resolves_full and not resolves_naive:            # ITERATION-DEPENDENT (H3 real envelope)
              iter_envelope['full_only_>=3edge_or_cyclic'] += 1

          # (iii) BITE after non-convex->VAGUE widening: re-run with widened inputs
          Gw = widen_nonconvex_to_vague(Gm)                   # POINT: drop genuine !=; ALLEN: convex/coarse relax
          derived_w = pc2_full(Gw_with_query_universe).get(u,v)
          bite_after_widen = (derived_w != alg.universe)       # still sub-universal => has bite
          if (not bite_after_widen) and resolves_full: widening_destroyed += 1
          if not bite_after_widen: continue
          funnel['i_ii_iii'] += 1            # == 'deduction-required multi-path-with-bite' set

          # (iv) cross-path intersection == gold singleton (use widened-input FULL result)
          if derived_w == gold:
              funnel['N_star'] += 1          # N* = all four conditions

    n_eval = len(EVALUABLE)
    applic_frac = funnel['i_ii_iii'] / n_eval           # SCORED against the NUMBER
    band = 'general' if applic_frac>=0.10 else ('module' if applic_frac>=0.05 else 'niche')
    ge3_frac = iter_envelope['full_only_>=3edge_or_cyclic'] / n_eval   # real iteration envelope (H3)
    # report ALSO with alternate denominator = all gold-singleton edges (anti-gaming)

    # --- NarrativeTime ONLY: non-circularity split (structural proxy) ---
    if corpus==NARRATIVETIME:
       locally_justifiable = edges with |sent(u)-sent(v)|<=1   (local cue exists)
       purely_timeline_implied = edges with |sent(u)-sent(v)|>1 (== proxy(i) set)
       report both fractions; headline subset = purely_timeline_implied.

    # --- PAIRED-BOOTSTRAP POWER / MDE per corpus (a-priori; no LLM yields yet) ---
    # Simulate the iter-2 paired comparison on the deduction-required-multi-path-with-bite set.
    def power_mde(N, base_acc=0.5, rho_pair=0.3, B=1000, sims=500):
       for effect in [0.05,0.10,0.15,0.20,0.25]:
          wins=0
          for s in sims:
             draw N paired binary outcomes: baseline~Bern(base_acc),
                modeA~Bern(base_acc+effect), positively correlated (rho_pair)
             bootstrap B resamples of the N paired diffs -> 95% CI on mean(diff)
             if CI excludes 0: wins+=1
          power[effect] = wins/sims
       MDE_80 = smallest effect with power>=0.80
       return power, MDE_80
    power = power_mde(N = funnel['i_ii_iii'])   # use the powering count (report N* too)

  # =====================================================================
  # MODULE 4 -- HOSTING DECISION + GO/NO-GO + OUTPUT
  # =====================================================================
  # gate_discriminative := (matres applic_frac ~0 / N*~0) AND (NarrativeTime or TDDMan N*>>0)
  # real_text_co_primary := NarrativeTime if its applic_frac>=NUMBER AND MDE_80 <= pre-reg min effect
  #                          (else TDDMan if it clears; else null)
  # corroboration_arm := TDDMan (non-circularity-clean) if usable
  # IF no real corpus clears the NUMBER with adequate power:
  #     verdict = 'NO-GO for real-text headline -> synthetic becomes headline, real = niche safety-net'
  # ELSE verdict = 'GO: host real-text headline on <corpus>; iter-2 may spend LLM budget'
  # STATE the verdict explicitly in method_out.hosting_decision.verdict_text.

  # method_out.json (validate with aii-json):
  # {
  #  pre_registered: {applicability_number:'>=10% general;5-10% module;<5% niche',
  #                   min_effect_size: <pre-reg, e.g. 0.10>, power_target:0.80,
  #                   evaluable_definition:'gold singleton edge, both endpoints in >=1 other gold edge'},
  #  engine_validation: {allen_169cells_match_qualreas:bool, point_tests:bool,
  #                      consistency_detection:bool, convex_point_completeness:bool,
  #                      iteration_isolation_len2_eq_and_3hop_neq:bool},
  #  per_corpus: { <name>: {algebra, n_docs, n_gold_edges, n_evaluable,
  #                 funnel:{i,i_ii,i_ii_iii,N_star},
  #                 applicability_fraction, applicability_band,
  #                 applicability_fraction_alt_denominator,
  #                 N_star_fraction, ge3_edge_cyclic:{full_resolves,naive_resolves,full_only,fraction},
  #                 bite_loss:{widening_destroyed}, mapping_sensitivity (TDDMan),
  #                 power:{N, MDE_80, power@0.10, power@0.20},
  #                 narrativetime_noncircularity:{locally_justifiable_frac,purely_timeline_implied_frac}}},
  #  gate_validation:{matres_N_star, narrativetime_N_star, tddman_N_star, gate_discriminative:bool},
  #  hosting_decision:{real_text_co_primary, corroboration_arm, go_no_go:'GO'|'NO-GO', verdict_text},
  #  honesty_notes:{point_arm_exact_allen_arm_lower_bound:true, narrativetime_data_status}
  # }
  # Check method_out.json size with aii-file-size-limit (expected small).
fallback_plan: >-
  DATA-ACQUISITION FALLBACKS (most likely failure points). (1) NarrativeTime/TimeBankNT not downloadable: TDDMan is FULLY
  usable from its tsv ALONE (all edges non-local by construction, no source text needed), so make TDDMan the operative real-text
  T0 host + non-circularity anchor and MATRES the control; emit a complete gate with NarrativeTime marked status='deferred_to_iter2_acquisition'.
  The gate still produces a valid GO/NO-GO. (2) Source TimeML positions (TBAQ-cleaned / TimeBank-Dense) unobtainable for the
  locality proxy: rely on each corpus's structural guarantee -- TDDMan all-non-local, MATRES all-local -- and for NarrativeTime
  approximate locality by document event-order distance (a coarse proxy) or restrict NarrativeTime to the subset where positions
  ARE derivable; flag the approximation in honesty_notes. (3) qualreas JSON hard to parse: hand-code the Allen 13x13 table
  (Allen 1983 / Wikipedia), the trivial convex point table, and the standard RCC-8 table, and VALIDATE every cell against
  qualreas or published examples before use. (4) TDDMan coarse->Allen mapping ambiguity: use the STRICT singleton map as primary,
  report the broad-map sensitivity alongside; if results flip between maps, report both and treat as a robustness caveat.
  METHOD/RESULT FALLBACKS. (5) Allen-arm PC is sound-but-incomplete, so its (iv) recovery counts are a LOWER BOUND -- report
  explicitly; the convex point arm (MATRES, NarrativeTime start-points) is EXACT and is the primary recoverability number.
  (6) If N* / applicability fraction is small on EVERY real corpus and power is inadequate (MDE_80 > pre-registered min effect):
  this is a LEGITIMATE, publishable gate outcome -- emit verdict 'NO-GO for real-text headline; synthetic arm becomes headline,
  real text scoped to niche safety-net'. Surfacing this BEFORE any LLM spend is the artifact's core value, not a failure.
  (7) If even the engine completeness test on convex point fails for some net: debug the table/seeding; do NOT proceed to
  T0 scoring until T-CMP and T-IT pass. (8) If runtime balloons (unexpected; ops are ms): cap per-document node count and
  the longer-path search depth (e.g. path length <=4) and report the cap. Throughout, NEVER fabricate -- if a corpus cannot
  be obtained, say so in method_out.json rather than inventing numbers.
testing_plan: >-
  STAGE 0 (engine correctness, gate before anything else): run the unit-test battery in MODULE 1 -- (T-A) all 169 Allen composition
  cells equal qualreas; (T-P) point compositions+converses; (T-C) the A<B<C<A triangle returns consistent=False; (T-CMP) PC
  minimal labels == brute-force enumeration on random small convex point nets (confirms PC completeness on the point algebra);
  (T-IT) FULL==NAIVE on a hand-built length-2 acyclic query AND FULL!=NAIVE on a hand-built 3-hop/cyclic query (confirms the
  iteration-isolation logic underpinning H3). ALL must pass before T0; record outcomes in engine_validation. STAGE 1 (parser
  smoke): parse ONE document from each corpus; print the gold graph (nodes, gold edges, relation sets), confirm relation-code
  mappings (TDDMan a/b/i/ii/s; MATRES BEFORE/AFTER/EQUAL/VAGUE; NarrativeTime timeline->point), and confirm symmetric/converse
  consistency of each gold graph. STAGE 2 (single-doc T0 smoke): run the full funnel on that one document per corpus; eyeball
  that the funnel monotonically shrinks (i >= i_ii >= i_ii_iii >= N_star) and that a hand-traceable held-out edge is classified
  correctly. CONFIRMATION SIGNAL to look for: on MATRES the deduction-required proxy (i) should already eliminate ~all edges
  (N*~0) -- if MATRES shows large N* at full scale, the locality proxy is mis-wired; on TDDMan every edge should pass (i).
  STAGE 3 (scale to full corpora): run all documents; verify the headline sanity check -- MATRES N*~0 vs NarrativeTime/TDDMan
  N*>>0 (gate_discriminative=True). Sanity-check the power calc by confirming MDE_80 decreases as N grows (monotone) and that
  power@effect increases with effect. STAGE 4 (output validation): validate method_out.json against its schema with the aii-json
  skill; confirm hosting_decision.verdict_text states GO/NO-GO explicitly and that every reported fraction has its denominator
  stated. Cross-check: the >=3-edge/cyclic 'full_only' count must be <= 'full_resolves' and naive_resolves <= full_resolves
  by construction -- assert these invariants and fail loudly if violated.
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

### [2] HUMAN-USER prompt · 2026-06-17 13:39:23 UTC

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

### [3] SKILL-INPUT — aii-json · 2026-06-17 13:40:27 UTC

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

### [4] SKILL-INPUT — aii-python · 2026-06-17 13:40:27 UTC

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

### [5] SYSTEM-USER prompt · 2026-06-17 14:21:16 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx4
type: experiment
title: >-
  T0 A-Priori Envelope Gate + Reusable QCN Path-Consistency Engine (zero-LLM-spend)
summary: >-
  Implement and unit-validate a reusable QCN path-consistency engine (Allen-13, convex point algebra, RCC-8; FULL iterated
  PC-2, NAIVE single-pass intersection, closure-OFF), then run the decisive zero-LLM-spend T0 envelope gate over three real
  temporal corpora (NarrativeTime/TimeBankNT, TDDMan, MATRES) from GOLD GRAPHS ALONE. Compute the deduction-required x multi-path
  x bite-after-widening x singleton-resolving funnel (N*), the >=3-edge/cyclic iteration envelope, widening bite-loss, a paired-bootstrap
  power/MDE calc per corpus, and (NarrativeTime) the locally-justifiable vs purely-timeline-implied non-circularity split.
  Score each corpus against the pre-registered applicability NUMBER (>=10% general / 5-10% module / <5% niche), output the
  hosting decision + explicit GO/NO-GO verdict, and report the expected MATRES N*~0 vs NarrativeTime/TDDMan N*>>0 as gate
  validation. cpu-only, $0 LLM. Engine and parsed graphs are checkpointed for reuse by iter-2 Tier-1.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # =====================================================================
  # ARTIFACT experiment_iter1_dir4 -- T0 ENVELOPE GATE + CLOSURE ENGINE
  # ZERO LLM SPEND. CPU-only. All computation from GOLD GRAPHS alone.
  # Runtime target: minutes (graph ops are ms/network). uv venv, no GPU.
  # Deliverable: method_out.json (aii-json validated) + reusable engine module.
  # =====================================================================

  # ---------------------------------------------------------------------
  # SETUP (uv, no LLM, no GPU)
  # ---------------------------------------------------------------------
  # uv venv; uv pip install numpy scipy pandas networkx requests bitsets lxml
  # git clone https://github.com/alreich/qualreas  -> use its Algebras/*.json as
  #   the AUTHORITATIVE composition/converse tables (Allen, Linear Point, RCC8).
  #   Do NOT depend on qualreas runtime; only parse its JSON tables, then run our
  #   own instrumented PC engine (we need FULL/NAIVE/OFF variants it does not expose).
  # Log to logs/run.log. Cache all parsed corpora + gold graphs to ./cache/ (pickle/json)
  #   so reruns and iter-2 Tier-1 can reload without re-parsing.

  # =====================================================================
  # MODULE 1 -- ALGEBRA + QCN PATH-CONSISTENCY ENGINE (reusable, ms/network)
  # =====================================================================

  class Algebra:                       # one per: ALLEN13, POINT (convex), RCC8
      base_relations: list[str]        # e.g. POINT=['<','=','>']; ALLEN=13 rels
      identity: frozenset              # POINT={'='}; ALLEN={'eq'}; RCC8={'EQ'}
      universe: frozenset              # all base relations (= 'no information')
      converse: dict[str,str]          # per-base-relation converse, FROM ALGEBRA ONLY
      compose_tbl: dict[(str,str), frozenset]   # base x base -> set, FROM ALGEBRA ONLY
      # Load from qualreas Algebras/*.json (preferred). If parse fails, hand-code:
      #   POINT: trivial (<o<=<, <o== <, <o> = universe, =o anything = that, etc.)
      #   ALLEN: 13x13 table from Allen 1983 / Wikipedia 'Allen's interval algebra'
      #   RCC8: standard 8x8 table.  VALIDATE hand-coded vs qualreas on all cells.

      def compose_sets(R, S):  return union over r in R, s in S of compose_tbl[(r,s)]
      def converse_set(R):     return { converse[r] for r in R }
      def intersect(R, S):     return R & S

  class QCN:                           # qualitative constraint network
      nodes: list                      # events (ids)
      edge: dict[(i,j)] -> frozenset   # relation set; missing edge => universe
      # invariants: edge[(j,i)] == converse_set(edge[(i,j)]); edge[(i,i)] == identity
      def get(i,j):  return edge.get((i,j), universe)   # symmetric via converse

  # --- THREE INSTRUMENTED CLOSURE VARIANTS ---

  def pc2_full(qcn) -> (qcn_closed, consistent: bool, fired_log):
      # Mackworth PC-2 to FIXPOINT. Seed converses+identity FROM ALGEBRA.
      queue = all ordered triples / all edges (worklist)
      while queue:
          (i,k,j) = pop
          new = intersect( qcn.get(i,j), compose_sets(qcn.get(i,k), qcn.get(k,j)) )
          if new != qcn.get(i,j):
              if new == empty: return (qcn, consistent=False, log)   # MODE B certificate
              qcn.set(i,j,new); qcn.set(j,i, converse_set(new))      # propagate + converse
              push all triples touching (i,j) back onto queue
              record (i,j,k,fired_composition) in fired_log          # trace-graph seed
      return (qcn, consistent=True, fired_log)

  def naive_single_pass(qcn, query=(q1,q2)) -> frozenset:
      # 'Path-of-Thoughts + ONE intersection step': intersect compositions arriving
      # at the query node over LENGTH-2 paths only, in a SINGLE pass.
      # NO fixpoint, NO converse seeding beyond gold edges, NO propagation to other edges.
      R = universe
      for k in nodes if k not in {q1,q2}:
          if has_gold(q1,k) and has_gold(k,q2):
              R = intersect(R, compose_sets(qcn.get(q1,k), qcn.get(k,q2)))
      return R

  def closure_off(qcn, query) -> frozenset:
      return universe    # table held fixed but closure NOT run (baseline for later tiers)

  # --- UNIT TESTS (must pass before any T0 run) ---
  # T-A  hand-checked Allen compositions vs qualreas/Wikipedia (e.g. o o o = {b,o,m};
  #      b o b = {b}; d o di = universe; etc.) -- ALL 169 cells equal qualreas.
  # T-P  point: '<' o '<' = {'<'}; '<' o '=' = {'<'}; '<' o '>' = universe; converses.
  # T-C  consistency: triangle A<B, B<C, C<A  => pc2_full returns consistent=False.
  # T-CMP convex-point COMPLETENESS: for random small convex point nets (n<=6),
  #      pc2_full minimal labels == labels from brute-force enumeration of all
  #      consistent point scenarios (ground-truth minimal). Confirms PC complete on POINT.
  # T-IT iteration isolation: build ONE acyclic length-2 query (naive==full) AND ONE
  #      3-hop / cyclic query where full resolves a singleton but naive leaves it loose.
  #      Assert naive==full on length-2, naive!=full on the 3-hop/cyclic case.
  # Record all test outcomes in method_out.engine_validation.

  # =====================================================================
  # MODULE 2 -- CORPUS PARSERS -> per-document GOLD GRAPHS (zero LLM)
  # =====================================================================

  # ---- MATRES (github.com/CogComp/MATRES: timebank.txt, aquaint.txt, platinum.txt)
  #   cols: docid, verb1, verb2, eiid1, eiid2, rel in {BEFORE,AFTER,EQUAL,VAGUE}
  #   ALGEBRA = POINT (convex) on event START-POINTS:
  #     BEFORE->{'<'}, AFTER->{'>'}, EQUAL->{'='}, VAGUE->universe (NOT evaluable).
  #   LOCALITY: annotation window is same/adjacent-sentence => deduction-proxy(i)
  #     FAILS for ~all edges by construction => expected N*~0 (gate validation).
  #     Optionally confirm by mapping eiid->sentence via TBAQ-cleaned .tml
  #     (github.com/jspotter/TempEval-3 data/TBAQ-cleaned), else assert structurally.
  #
  # ---- TDDMan (github.com/aakanksha19/TDDiscourse: TDDMan/TDDMan{Train,Dev,Test}.tsv)
  #   cols (tab): docid, e1, e2, rel in {a=After,b=Before,i=Includes,ii=Is_Included,s=Simultaneous}
  #   ALGEBRA = coarse interval via ALLEN-subset image (primary STRICT singleton map):
  #     b->{'b'} a->{'bi'} i->{'di'} ii->{'d'} s->{'eq'}  (compose in ALLEN-13).
  #     SENSITIVITY (report alongside): broad map i->{di,si,fi}, ii->{d,s,f}, s->{eq,s,si,f,fi}.
  #   LOCALITY: TDDMan pairs are ALL >1-sentence-apart, manual, 'cannot be inferred
  #     automatically' => deduction-proxy(i) holds for EVERY edge BY CONSTRUCTION
  #     (no source text needed) + this is the NON-CIRCULARITY anchor.
  #   GOLD GRAPH per docid = all TDDMan pairs in that doc (sparse manual set).
  #
  # ---- NarrativeTime/TimeBankNT (arXiv:1908.11443, LREC-COLING 2024) -- CO-PRIMARY
  #   LOCATE DATA FIRST (search budget ~10 min): try github text-machine-lab,
  #     project page text-machine.cs.uml.edu/projects/temporal/, and grep the LREC
  #     paper PDF (aclanthology.org/2024.lrec-main.1054) for 'github'/'available at'.
  #   Annotation = each event gets a timeline interval [start,end] (with vagueness combs).
  #   Build FULL gold graph from timeline coords (full TLink coverage):
  #     POINT arm (PRIMARY): start(u) vs start(v) -> {'<','=','>'}; widen genuine != (non-convex)
  #       to VAGUE/universe to keep PC COMPLETE; MEASURE bite lost by this widening.
  #     ALLEN full-interval arm (lower-bound detector): derive 13-rel from [start,end] order.
  #   LOCALITY: need event sentence index (from NarrativeTime files or aligned TimeBank
  #     .tml). proxy(i) = |sent(u)-sent(v)| > 1.
  #
  # All parsers emit: {docid -> {events:set, gold_edges:{(u,v):rel_set}, sent_idx:{e->int}}}
  # Cache to ./cache/<corpus>_graphs.json.

  # =====================================================================
  # MODULE 3 -- T0 ENVELOPE FUNNEL per corpus (the gate)
  # =====================================================================

  for corpus in [NARRATIVETIME, TDDMAN, MATRES]:
    alg = algebra_for(corpus)
    EVALUABLE = []          # primary denominator
    funnel = Counter()      # i, i_ii, i_ii_iii, N_star
    iter_envelope = Counter()   # full_resolves, naive_resolves, full_only(>=3-edge/cyclic)
    bite_loss = 0; widening_destroyed = 0
    for doc, G in corpus_graphs.items():
      for (u,v), gold in G.gold_edges.items():
          if gold is universe/VAGUE or not singleton(gold): continue   # need determinate gold
          # primary evaluable def: gold singleton AND both u,v appear in >=1 OTHER gold edge
          if degree(u)<2 and degree(v)<2: continue
          EVALUABLE.append((doc,u,v))
          Gm = G minus direct edge (u,v)        # HOLD OUT the query edge; (u,v)=universe

          # (i) deduction-required proxy (no local/adjacent-sentence co-occurrence)
          if corpus==TDDMAN: i_ok = True                       # by construction
          elif corpus==MATRES: i_ok = (sent dist>1 if positions else False)
          else: i_ok = abs(sent_idx[u]-sent_idx[v]) > 1        # NarrativeTime
          if not i_ok: continue
          funnel['i'] += 1

          # (ii) >=2 constraining paths through DISTINCT intermediates
          inter2 = { w for w in Gm.nodes if has_gold(u,w) and has_gold(w,v) }   # length-2
          longer = exists_path(Gm, u, v, min_len>=3) or in_cycle(Gm,u,v)
          if len(inter2) < 2 and not (len(inter2)>=1 and longer): continue
          funnel['i_ii'] += 1

          # (iv pre-widen) does FULL closure on held-out gold graph recover gold singleton?
          closed,_ ,_ = pc2_full(Gm_with_query_universe)
          derived_full = closed.get(u,v)
          derived_naive = naive_single_pass(Gm_with_query_universe, (u,v))
          resolves_full  = (derived_full  == gold)            # singleton-to-correct (FULL)
          resolves_naive = (derived_naive == gold)            # singleton-to-correct (NAIVE/length-2)
          if resolves_full: iter_envelope['full_resolves'] += 1
          if resolves_naive: iter_envelope['naive_resolves'] += 1
          if resolves_full and not resolves_naive:            # ITERATION-DEPENDENT (H3 real envelope)
              iter_envelope['full_only_>=3edge_or_cyclic'] += 1

          # (iii) BITE after non-convex->VAGUE widening: re-run with widened inputs
          Gw = widen_nonconvex_to_vague(Gm)                   # POINT: drop genuine !=; ALLEN: convex/coarse relax
          derived_w = pc2_full(Gw_with_query_universe).get(u,v)
          bite_after_widen = (derived_w != alg.universe)       # still sub-universal => has bite
          if (not bite_after_widen) and resolves_full: widening_destroyed += 1
          if not bite_after_widen: continue
          funnel['i_ii_iii'] += 1            # == 'deduction-required multi-path-with-bite' set

          # (iv) cross-path intersection == gold singleton (use widened-input FULL result)
          if derived_w == gold:
              funnel['N_star'] += 1          # N* = all four conditions

    n_eval = len(EVALUABLE)
    applic_frac = funnel['i_ii_iii'] / n_eval           # SCORED against the NUMBER
    band = 'general' if applic_frac>=0.10 else ('module' if applic_frac>=0.05 else 'niche')
    ge3_frac = iter_envelope['full_only_>=3edge_or_cyclic'] / n_eval   # real iteration envelope (H3)
    # report ALSO with alternate denominator = all gold-singleton edges (anti-gaming)

    # --- NarrativeTime ONLY: non-circularity split (structural proxy) ---
    if corpus==NARRATIVETIME:
       locally_justifiable = edges with |sent(u)-sent(v)|<=1   (local cue exists)
       purely_timeline_implied = edges with |sent(u)-sent(v)|>1 (== proxy(i) set)
       report both fractions; headline subset = purely_timeline_implied.

    # --- PAIRED-BOOTSTRAP POWER / MDE per corpus (a-priori; no LLM yields yet) ---
    # Simulate the iter-2 paired comparison on the deduction-required-multi-path-with-bite set.
    def power_mde(N, base_acc=0.5, rho_pair=0.3, B=1000, sims=500):
       for effect in [0.05,0.10,0.15,0.20,0.25]:
          wins=0
          for s in sims:
             draw N paired binary outcomes: baseline~Bern(base_acc),
                modeA~Bern(base_acc+effect), positively correlated (rho_pair)
             bootstrap B resamples of the N paired diffs -> 95% CI on mean(diff)
             if CI excludes 0: wins+=1
          power[effect] = wins/sims
       MDE_80 = smallest effect with power>=0.80
       return power, MDE_80
    power = power_mde(N = funnel['i_ii_iii'])   # use the powering count (report N* too)

  # =====================================================================
  # MODULE 4 -- HOSTING DECISION + GO/NO-GO + OUTPUT
  # =====================================================================
  # gate_discriminative := (matres applic_frac ~0 / N*~0) AND (NarrativeTime or TDDMan N*>>0)
  # real_text_co_primary := NarrativeTime if its applic_frac>=NUMBER AND MDE_80 <= pre-reg min effect
  #                          (else TDDMan if it clears; else null)
  # corroboration_arm := TDDMan (non-circularity-clean) if usable
  # IF no real corpus clears the NUMBER with adequate power:
  #     verdict = 'NO-GO for real-text headline -> synthetic becomes headline, real = niche safety-net'
  # ELSE verdict = 'GO: host real-text headline on <corpus>; iter-2 may spend LLM budget'
  # STATE the verdict explicitly in method_out.hosting_decision.verdict_text.

  # method_out.json (validate with aii-json):
  # {
  #  pre_registered: {applicability_number:'>=10% general;5-10% module;<5% niche',
  #                   min_effect_size: <pre-reg, e.g. 0.10>, power_target:0.80,
  #                   evaluable_definition:'gold singleton edge, both endpoints in >=1 other gold edge'},
  #  engine_validation: {allen_169cells_match_qualreas:bool, point_tests:bool,
  #                      consistency_detection:bool, convex_point_completeness:bool,
  #                      iteration_isolation_len2_eq_and_3hop_neq:bool},
  #  per_corpus: { <name>: {algebra, n_docs, n_gold_edges, n_evaluable,
  #                 funnel:{i,i_ii,i_ii_iii,N_star},
  #                 applicability_fraction, applicability_band,
  #                 applicability_fraction_alt_denominator,
  #                 N_star_fraction, ge3_edge_cyclic:{full_resolves,naive_resolves,full_only,fraction},
  #                 bite_loss:{widening_destroyed}, mapping_sensitivity (TDDMan),
  #                 power:{N, MDE_80, power@0.10, power@0.20},
  #                 narrativetime_noncircularity:{locally_justifiable_frac,purely_timeline_implied_frac}}},
  #  gate_validation:{matres_N_star, narrativetime_N_star, tddman_N_star, gate_discriminative:bool},
  #  hosting_decision:{real_text_co_primary, corroboration_arm, go_no_go:'GO'|'NO-GO', verdict_text},
  #  honesty_notes:{point_arm_exact_allen_arm_lower_bound:true, narrativetime_data_status}
  # }
  # Check method_out.json size with aii-file-size-limit (expected small).
fallback_plan: >-
  DATA-ACQUISITION FALLBACKS (most likely failure points). (1) NarrativeTime/TimeBankNT not downloadable: TDDMan is FULLY
  usable from its tsv ALONE (all edges non-local by construction, no source text needed), so make TDDMan the operative real-text
  T0 host + non-circularity anchor and MATRES the control; emit a complete gate with NarrativeTime marked status='deferred_to_iter2_acquisition'.
  The gate still produces a valid GO/NO-GO. (2) Source TimeML positions (TBAQ-cleaned / TimeBank-Dense) unobtainable for the
  locality proxy: rely on each corpus's structural guarantee -- TDDMan all-non-local, MATRES all-local -- and for NarrativeTime
  approximate locality by document event-order distance (a coarse proxy) or restrict NarrativeTime to the subset where positions
  ARE derivable; flag the approximation in honesty_notes. (3) qualreas JSON hard to parse: hand-code the Allen 13x13 table
  (Allen 1983 / Wikipedia), the trivial convex point table, and the standard RCC-8 table, and VALIDATE every cell against
  qualreas or published examples before use. (4) TDDMan coarse->Allen mapping ambiguity: use the STRICT singleton map as primary,
  report the broad-map sensitivity alongside; if results flip between maps, report both and treat as a robustness caveat.
  METHOD/RESULT FALLBACKS. (5) Allen-arm PC is sound-but-incomplete, so its (iv) recovery counts are a LOWER BOUND -- report
  explicitly; the convex point arm (MATRES, NarrativeTime start-points) is EXACT and is the primary recoverability number.
  (6) If N* / applicability fraction is small on EVERY real corpus and power is inadequate (MDE_80 > pre-registered min effect):
  this is a LEGITIMATE, publishable gate outcome -- emit verdict 'NO-GO for real-text headline; synthetic arm becomes headline,
  real text scoped to niche safety-net'. Surfacing this BEFORE any LLM spend is the artifact's core value, not a failure.
  (7) If even the engine completeness test on convex point fails for some net: debug the table/seeding; do NOT proceed to
  T0 scoring until T-CMP and T-IT pass. (8) If runtime balloons (unexpected; ops are ms): cap per-document node count and
  the longer-path search depth (e.g. path length <=4) and report the cap. Throughout, NEVER fabricate -- if a corpus cannot
  be obtained, say so in method_out.json rather than inventing numbers.
testing_plan: >-
  STAGE 0 (engine correctness, gate before anything else): run the unit-test battery in MODULE 1 -- (T-A) all 169 Allen composition
  cells equal qualreas; (T-P) point compositions+converses; (T-C) the A<B<C<A triangle returns consistent=False; (T-CMP) PC
  minimal labels == brute-force enumeration on random small convex point nets (confirms PC completeness on the point algebra);
  (T-IT) FULL==NAIVE on a hand-built length-2 acyclic query AND FULL!=NAIVE on a hand-built 3-hop/cyclic query (confirms the
  iteration-isolation logic underpinning H3). ALL must pass before T0; record outcomes in engine_validation. STAGE 1 (parser
  smoke): parse ONE document from each corpus; print the gold graph (nodes, gold edges, relation sets), confirm relation-code
  mappings (TDDMan a/b/i/ii/s; MATRES BEFORE/AFTER/EQUAL/VAGUE; NarrativeTime timeline->point), and confirm symmetric/converse
  consistency of each gold graph. STAGE 2 (single-doc T0 smoke): run the full funnel on that one document per corpus; eyeball
  that the funnel monotonically shrinks (i >= i_ii >= i_ii_iii >= N_star) and that a hand-traceable held-out edge is classified
  correctly. CONFIRMATION SIGNAL to look for: on MATRES the deduction-required proxy (i) should already eliminate ~all edges
  (N*~0) -- if MATRES shows large N* at full scale, the locality proxy is mis-wired; on TDDMan every edge should pass (i).
  STAGE 3 (scale to full corpora): run all documents; verify the headline sanity check -- MATRES N*~0 vs NarrativeTime/TDDMan
  N*>>0 (gate_discriminative=True). Sanity-check the power calc by confirming MDE_80 decreases as N grows (monotone) and that
  power@effect increases with effect. STAGE 4 (output validation): validate method_out.json against its schema with the aii-json
  skill; confirm hosting_decision.verdict_text states GO/NO-GO explicitly and that every reported fraction has its denominator
  stated. Cross-check: the >=3-edge/cyclic 'full_only' count must be <= 'full_resolves' and naive_resolves <= full_resolves
  by construction -- assert these invariants and fail loudly if violated.
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
