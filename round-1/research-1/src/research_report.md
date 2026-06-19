# Implementation/Resource Dossier for the Closure-Certified Text-to-Logic Deduction Module

## Summary

Verified, executor-ready specifications for the closure-certified temporal-deduction pipeline: (1) corpus access+parse formats for NarrativeTime (repo github.com/text-machine-lab/nt, MIT, nt_format JSONL with per-event numeric `time` coordinate + bracket-type interval model + same-branch get_event_relation), TDDMan (4-col TSV, codes a/b/i/ii/s, join text from TimeBank-Dense; long-distance non-auto-inferable gold), and MATRES (start-point convex point algebra, 2-sentence window = N*~=0 gate control); (2) machine-readable GQR composition/converse tables for Allen (13 tokens with < / > for before/after), convex point algebra (with the only-non-convex != -> universal widening rule), and RCC-8, each with verified unit-test cells; (3) Mackworth PC-2 iterated a-closure pseudocode + the precise naive single-pass-intersection contrast (naive==full on length-2, diverges at hop>=3 / cyclomatic>=1) + soundness/completeness tractability facts (point-algebra arm EXACT, full Allen/RCC-8 a LOWER BOUND); (4) the Renz-Nebel A(n,d,l) model plus the scenario-then-abstract recipe for guaranteed-consistent synthetic QCNs with independent density/hop/cyclomatic/recall knobs; (5) baseline configs each with a matched abstention signal (Path-of-Thoughts, self-consistency, LINC, DSR-LM/HtT, ILP-commit Eirew et al. M=5, METRE) and a corrected citation (the >=50-97% multiple-relation + ILP-no-F1-gain facts are Kougia et al. arXiv:2406.11486, not 'Knez & Sun'); (6) OpenRouter model choice (primary google/gemini-2.5-flash-lite $0.10/$0.40, second-family DeepSeek-V3.2/Qwen2.5-72B/Llama-3.3-70B) with arithmetic showing <$10 and a disk-cache + hard cost-guard strategy; and (7) the operationalized three-part realism-matching statistic (per-edge error-type TV<=0.10, cross-edge soundness-correlation |dro|<=0.10 via ICC, topology histogram TV<=0.15) with J(E) vs r^E. Includes a full decision table, a 12-item gotchas list, and 3 unresolved follow-ups.

## Research Findings

# Implementation/Resource Dossier — Closure-Certified Text-to-Logic Deduction Module

**Scope.** This dossier resolves every implementation/resource decision the downstream
dataset, experiment, and evaluation executors need to build the closure-certified
deduction module: exact corpus access + parse formats, machine-readable composition
tables (Allen IA, convex point algebra, RCC-8) with the non-convex→VAGUE widening
rule, the iterated path-consistency (PC-2) spec and the naive single-pass-intersection
contrast, the Renz–Nebel random-consistent QCN generator, baseline configs each with a
matched abstention signal, the cheapest capable OpenRouter model + caching strategy,
and the realism-matching statistic. Every claim carries an exact URL / repo path /
arXiv ID. Unverified items are flagged explicitly with fallbacks.

Citations `[n]` index the **Sources** list at the bottom.

---

## SECTION 1 — CORPORA ACCESS + PARSE FORMAT  *(highest priority; gates T0 + all real-text arms)*

### 1A. NarrativeTime / TimeBankNT  — DENSE CO-PRIMARY ✅ REPO FOUND

**The repository URL the search engine never surfaced is stated twice in the arXiv PDF
footnotes:** `https://github.com/text-machine-lab/nt` (footnote 1 and footnote 6 of
arXiv:1908.11443) [1]. License: **MIT** [3]. This was the single most mission-critical
unknown and it is now resolved — NarrativeTime is publicly available and reusable.

- **Canonical refs:** ACL Anthology LREC-COLING 2024 `https://aclanthology.org/2024.lrec-main.1054/` [2]; arXiv:1908.11443 (PDF `https://arxiv.org/pdf/1908.11443`) [1]. Authors: Rogers, Karpinska, Gupta, Lialin, Smelkov, Rumshisky (UMass Lowell *text-machine-lab*). Full re-annotation of **TimeBank-Dense** on a timeline; **102,313 TLINKs excluding inverses** (vastly denser than TB-Dense) [1]; ships TimeML conversion tools.
- **Repo layout (branch `master`, verified by raw fetch)** [3]:
  - `annotationTool/` — HTML annotation interface.
  - `corpus/timebank/nt_format/` — native NarrativeTime output as **JSONL**. Files: `tbd_a1.jsonl`, `tbd_a1_tml.jsonl`, `tbd_a2.jsonl`, `tbd_a2_tml.jsonl`, `tbd_clear.jsonl`, `tbd_tml_metadata.jsonl`. `tbd` = TimeBank-Dense; `a1`/`a2` = the two independent expert annotators; `tbd_clear.jsonl` is the cleaned/adjudicated variant (recommended gold source). [3]
  - `corpus/timebank/nt_converted_to_tml/` — TimeML XML conversions (for pyTLEX / TimeML-graph tooling).
  - `narrative_time/` — Python package (`event_relations.py`, `conversion_utils.py`).
  - `utils/nt2tml.py` — JSONL→TimeML XML converter.
  - `notebooks/` — analysis/modeling.

- **TIMELINE → START-POINT extraction path (the completeness-critical detail) ✅ FULLY DECODED.**
  From `narrative_time/event_relations.py` [4], each event/timex record carries a numeric
  timeline coordinate field **`time`** (a float, e.g. `'time': '-0.1'`), an interval `type`,
  a `branch`, and `relto`. The internal model is an `Interval = namedtuple("Interval", ["start","end"])`.
  - **Bracket-type alphabet** `ALLOWED_TYPES = {"[B]", "{U}", "{U]", "[U}"}`. The brackets encode endpoint boundedness: `[`/`]` = **bounded** start/end; `{`/`}` = **unbounded** start/end. So `[B]` = bounded both ends; `{U}` = unbounded both ends; `[U}` = bounded start / unbounded end; `{U]` = unbounded start / bounded end. [4]
  - **Relation inventory** `REL_TO_ID = {BEFORE:0, AFTER:1, INCLUDES:2, IS_INCLUDED:3, SIMULTANEOUS:4, OVERLAP:5, VAGUE:6}` — **7 relations** [4]. (Corroborated independently by Eirew et al. who call NarrativeTime "NT-6": six relations *before, after, includes, is-included, equal/simultaneous, overlap* + vague [26].)
  - **Gold relation derivation** `event_relations.get_event_relation(e1, e2)`: relations are computed only when the two events are on the **same `branch`**; **cross-branch pairs → VAGUE**. A `CONVERSION_TABLE` keyed by `(type1, type2)` maps interval comparisons to a TLINK: e.g. `("[B]","[B]")` admits the full set `{BEFORE, AFTER, INCLUDES, IS_INCLUDED, OVERLAP, SIMULTANEOUS}`; any pair involving `{U}` (fully unbounded) defaults to `VAGUE`; `("[B]","{U}")` → mostly `VAGUE` except `IS_INCLUDED`/`SIMULTANEOUS`→`IS_INCLUDED`, etc. [4]
  - **For the convex point-algebra (start-point) arm:** compare the two events' `time` coordinates on the same branch — `time1 < time2` ⇒ start-point `<` (BEFORE), `==` ⇒ `=`, `>` ⇒ `>` (AFTER); cross-branch ⇒ universal/VAGUE. This is **exact** (point algebra is PC-complete; see §3C).
  - **For the full-interval Allen (lower-bound) arm:** use both endpoints — derive a `start` and `end` per event from `time` + bracket type and read off the Allen relation, or simply call the shipped `get_event_relation` and map its 7-way output to Allen sets (see §1 mapping table).
  - **Recommended path:** the executor does NOT need to reverse-engineer geometry — it can call the repo's own `get_event_relation` to obtain gold TLINKs directly, and separately compare `time` floats for the point-algebra arm.
- **TLEX / pyTLEX cross-check (worked example of TimeML-graph→timeline).** TLEX (arXiv:2406.05265 [5]) partitions a TimeML temporal graph into temporally connected subgraphs, transforms each into a **point-algebra TCSP**, extracts exact timelines, and flags inconsistencies + indeterminacies. A maintained Python implementation exists: **`https://github.com/pyTLEX-Team/pyTLEX`** (EACL 2024 demo, `https://aclanthology.org/2024.eacl-demo.4/`; FIU COGNAC lab) [6]. Reusable two ways: (a) run pyTLEX on `nt_converted_to_tml/*.tml` to get an *independent* start-point ordering as a cross-check of the `time`-coordinate method; (b) reuse its TimeML→point-CSP transform for any TimeML corpus. **Note:** since `nt_format` already stores explicit `time` coordinates, the direct method is simpler and exact; pyTLEX is a validation oracle, not a dependency.
- **GOTCHA / procurement risk → RESOLVED.** No emailing authors needed. The raw text is the TimeBank-Dense source (already embedded token-by-token in the nt_format JSONL via the `tokens`/`span` fields used by `nt2tml.py` [3]); the `nt_converted_to_tml` TimeML files carry the text too.
- **Test-set-leak gotcha (LLM-eval honesty).** The NarrativeTime authors explicitly warn that LLMs "may have seen this data coupled with temporal annotations during pre-training, especially if trained on unfiltered GitHub repositories… a test set leak" [1]. Mitigation: read relations from raw text spans (not from any annotation markup), and report this as a contamination caveat in the experiment.

### 1B. TDDMan / TDDiscourse — NON-CIRCULARITY ANCHOR ✅

- **Repo:** `https://github.com/aakanksha19/TDDiscourse` [7]; subfolder `TDDMan/` with `TDDManTrain.tsv` / `TDDManDev.tsv` / `TDDManTest.tsv`. Paper: Naik, Breitfeller, Rosé (CMU), SIGDial 2019, `https://aclanthology.org/W19-5929/` (pages 239–249) [8].
- **EXACT TSV format (verified by raw fetch of all three splits)** [7]: **tab-separated, NO header, 4 columns:** `docid  event1_id  event2_id  relation`. Example rows from `TDDManTrain.tsv`: `APW19980227.0468  e2  e8  a` ; `APW19980227.0468  e2  e79  ii` ; `APW19980213.1320  e2  e8  i`.
  - **Event ids** are TimeBank document event ids of the form `e<N>` (e.g. `e2`, `e79`, `e2000`) — they reference the **TimeBank/TimeBank-Dense source documents**, NOT EIIDs. (NarrativeTime paper confirms TDDiscourse "released data reference event IDs rather than event instance IDs" [1].) **The TSV ships only (docid, event-pair, label) triples — raw text + event offsets must be joined from the original TimeBank-Dense / TimeBank 1.2 corpus** (timeml.github.io / LDC TimeBank 1.2). This is the single biggest TDDMan gotcha.
  - **Relation codes (single letter, confirmed across all splits):** `b`=before, `a`=after, `i`=includes, `ii`=is_included, `s`=simultaneous. Mutually exclusive; **no VAGUE label**. [7]
  - **Split sizes:** TDDMan Train/Dev/Test = **4000 / 650 / 1500** pairs [7].
- **Coarse-relation → interval-algebra mapping:** `before`→Allen `<` (b), `after`→`>` (bi), `includes`→`di` (contains), `is_included`→`d` (during), `simultaneous`→`=` (equals) — i.e. restrict GQR's Allen table to the 5-symbol coarse set `{<, >, di, d, =}`. (Note `simultaneous` is best treated as the *coarse* "same-extent" class `=`; if a corpus distinguishes coextensive vs. nested-equal, widen accordingly.)
- **Non-circularity / long-distance claim — VERIFIED VERBATIM** [8]: TDDiscourse is "the **first dataset focusing specifically on temporal links between event pairs which are more than one sentence apart**… manually annotating global pairs that **cannot be inferred automatically from existing annotations**… focusing on **long-distance pairs and not being automatically inferable**." Prior work focused on same/adjacent-sentence (local) pairs where "reliance on local syntactic features suffices." **This is exactly the deduction-required, gold-not-auto-derivable property the closure hypothesis needs** — its gold edges are *not* a transitive closure of local reads, so closure-based recovery is a non-trivial test.
- **Do NOT use TDDAuto** (32607/1435/4258) for the non-circularity arm — it is auto-derived. Only **TDDMan** (manual) qualifies [7].

### 1C. MATRES — GATE-VALIDATION CONTROL ✅

- **Repo:** `https://github.com/CogComp/MATRES` [9] ("Multi-Axis Temporal Relations for Start-points"); extended version (entire TempEval-3, verbal events only) at `https://github.com/qiangning/MATRES` [1][10]. Paper: Ning, Wu & Roth, ACL 2018, arXiv:1804.07828 [11].
- **File format (verified):** files `timebank.txt`, `aquaint.txt`, `platinum.txt` (the TempEval-3 / TBAQ splits) + `rawdata/`. Columns: **`docid  verb1  verb2  eiid1  eiid2  relation`** where `eiid` = event-instance ids aligned to TempEval-3 [9]. Verb events only; main-axis only.
- **Label set:** **`{before, after, equal, vague}`** [11].
- **Locality (the structural reason its deduction envelope is ~empty) — VERIFIED.** MATRES inherits TB-Dense's annotation window: relations are annotated for comparable pairs **within a sliding two-sentence window** ("TB-Dense… annotates all event pairs within a sliding, two-sentence window") [11]; Eirew et al. independently confirm "only events within consecutive sentences are annotated" in MATRES/TB-Dense [26]. Because gold is overwhelmingly local (adjacent-sentence), there are essentially **no long-hop, deduction-required gold edges → T0 envelope N\* ≈ 0**. MATRES therefore serves as a **gate-validation control** (it should show ~zero closure bite), NOT as a headline corpus.
- **Start-point design = convex point algebra (key reuse).** MATRES deliberately compares **start-points only**: it "propose[s] TempRel annotation should focus on start-points," splitting each event into `[t_start, t_end]` and reducing the label set to "**before, after and equal**" by comparing `t1_start` vs `t2_start`, with `vague` when order is indeterminate [11]. IAA jumped from the conventional .60s to **.84 Cohen's κ** under this scheme [11]. The vague mapping uses two yes/no probes: `Q1=is it possible t1_start<t2_start?`, `Q2=t2_start<t1_start?` → `(yes,yes)=vague, (no,no)=equal, (yes,no)=before, (no,yes)=after` [11]. **MATRES is literally annotated in the convex point algebra over start-points** — making it the cleanest validation that our point-algebra closure engine matches human gold on the easy (local) regime.
- **Source text:** TempEval-3 / TBAQ (TimeBank + AQUAINT) platinum [9][11].

### Cross-corpus comparison sub-table

| Corpus | ~#docs | gold edges | label set | algebra | locality | density | gold provenance | source-text procurement | parse entrypoint |
|---|---|---|---|---|---|---|---|---|---|
| **NarrativeTime / TimeBankNT** | 36 (TB-Dense docs) | 102,313 TLINKs (excl. inverses) [1] | before/after/includes/is_included/simultaneous/overlap/vague (7) [4][26] | full-interval Allen (start+end) **and** convex point algebra (start `time`) | full coverage (timeline) | **very dense** | **human timeline** (per-event `time` coord) | text embedded in nt_format JSONL / nt_converted_to_tml | `corpus/timebank/nt_format/tbd_clear.jsonl` + `narrative_time/event_relations.py` |
| **TDDMan** | TB-Dense docs | 4000/650/1500 (train/dev/test) [7] | before/after/includes/is_included/simultaneous (5, no vague) | coarse Allen `{<,>,di,d,=}` | **long-distance (>1 sentence)** [8] | sparse (curated) | **manual, not auto-inferable** [8] | **JOIN raw text + offsets from TimeBank-Dense / TimeBank 1.2** | `TDDMan/TDDMan{Train,Dev,Test}.tsv` (4-col TSV) |
| **MATRES** | 275 (TempEval-3) | ~per TBAQ | before/after/equal/vague (4) [11] | convex point algebra (start-points) | **same/adjacent (≤2-sentence window)** [11][26] | dense-local | adjacent-pair human | TempEval-3 / TBAQ platinum | `platinum.txt` etc. (`docid,verb1,verb2,eiid1,eiid2,rel`) |

---

## SECTION 2 — EXACT COMPOSITION TABLES (Allen IA, convex point algebra, RCC-8)

**Primary source = GQR** (`https://github.com/m-westphal/gqr`) [12], a fast reasoner for
binary qualitative constraint calculi (Gantner, Westphal, Wölfl, AAAI-08 workshop). The
calculus is defined by plain-text files under `data/<calculus>/calculus/`. **No `.spec`
file exists** — a calculus is fully specified by its composition (`.comp`) and converse
(`.conv`) files (plus optional `.weights`). Base relations = the symbols appearing as
keys; identity and universal are implicit.

### 2A. File grammar (verbatim) ✅

**Allen** — `data/allen/calculus/` contains: `allen.comp`, `allen.conv`, `allen.weights`,
`contalg`, `hornalg`, `pointalg` [12].

- **Composition grammar:** `rel1 : rel2 :: ( result-base-relations… )`. Verbatim excerpt of `allen.comp` [13]:
  ```
  = : = :: ( = )   < : < :: ( < )   < : d :: ( < d s m o )   < : di :: ( < )
  > : > :: ( > )   d : di :: ( = < > d di s si f fi m mi o oi )
  o : o :: ( < m o )   o : oi :: ( = d di s si f fi o oi )
  m : m :: ( < )   m : mi :: ( = f fi )   f : fi :: ( = f fi )
  di : d :: ( = d di s si f fi o oi )
  ```
- **Converse grammar:** `rel :: converse`. Verbatim `allen.conv` (complete) [13]:
  ```
  = :: =   < :: >   > :: <   d :: di   di :: d   o :: oi   oi :: o
  m :: mi   mi :: m   s :: si   si :: s   f :: fi   fi :: f
  ```
- **⚠ GOTCHA — GQR's Allen token alphabet is `{ =, <, >, d, di, s, si, f, fi, m, mi, o, oi }` (13 base relations), using `<` for *before* and `>` for *after*** (NOT the `b`/`bi` the plan anticipated). Map your label names accordingly: `b≡<`, `bi≡>`, `eq≡=`, `m`/`mi`, `o`/`oi`, `d`/`di`, `s`/`si`, `f`/`fi`. Identity = `=`; universal = the full 13-element set.
- Composition is encoded only for **base-relation pairs**; the executor extends to **relation sets by union**: `R∘S = ⋃_{r∈R, s∈S} comp(r,s)`. Converse of a set = `⋃ conv(r)`.

### 2B. Allen 13×13 cross-check (unit-test cells) ✅

Cross-check the loaded GQR table against the canonical Allen 1983 CACM table
("Maintaining Knowledge about Temporal Intervals") [33] / Wikipedia "Allen's interval
algebra" / Alspaugh reference. **Use these GQR-verified cells as unit tests** (left =
GQR tokens, right = plan's `b/bi` notation) [13]:

| GQR cell | result set | plan notation check |
|---|---|---|
| `< ∘ <` | `{<}` | b∘b = {b} ✅ |
| `< ∘ d` | `{< d s m o}` | b∘d = {b,d,s,m,o} ✅ |
| `d ∘ di` | `{= < > d di s si f fi m mi o oi}` (full 13) | d∘di = universal ✅ |
| `o ∘ o` | `{< m o}` | o∘o = {b,m,o} ✅ |
| `m ∘ m` | `{<}` | m∘m = {b} ✅ |
| `m ∘ mi` | `{= f fi}` | m∘mi = {eq,f,fi} ✅ |
| `f ∘ fi` | `{= f fi}` | f∘fi = {eq,f,fi} ✅ |

**Rule: converses and identity must be SEEDED FROM THE ALGEBRA (`allen.conv` + `=`),
never read from an LLM.**

### 2C. Convex point algebra (NarrativeTime start-point arm) — completeness-critical ✅

- **Base point relations** `{<, =, >}`; the relation lattice has 8 subsets:
  `∅, {<}, {=}, {>}, {<,=}=≤, {=,>}=≥, {<,>}=≠, {<,=,>}=⊤` (universal).
- **GQR `data/point/calculus/point.comp` (complete, verbatim)** [14]:
  ```
  = : = :: ( = )   < : = :: ( < )   > : = :: ( > )
  = : < :: ( < )   < : < :: ( < )   > : < :: ( < = > )
  = : > :: ( > )   < : > :: ( < = > ) > : > :: ( > )
  ```
  i.e. `<∘< = <`, `>∘> = >`, `<∘> = ⊤`, `>∘< = ⊤`, `=` is identity. `point.conv`: `= :: =   < :: >   > :: <` [14]. (Cross-checked against the survey's "PC1" point algebra: base relations `<,=,>`, `{<,=}` represents `≤`, `<∘<=<`, `<∘>={<,=,>}` [17].)
- **THE WIDENING RULE (stated explicitly).** The **only non-convex** relation is `≠ = {<,>}` (its point-set is not an interval on the order). **To keep path-consistency COMPLETE for the convex point algebra, any emitted or derived `≠` is WIDENED to `⊤` (universal / VAGUE).** Convex relations = `{<, =, >, ≤, ≥, ⊤}` (all subsets except `≠`). The **bite lost by this widening must be measured** (count how many query edges would have been resolvable as `≠` but were widened to ⊤).
- **Tractability (cite):** PC is **COMPLETE** (decides consistency) for the convex point algebra / pointizable / ORD-Horn classes — Vilain & Kautz 1986 [19] (point algebra `=,<,≤,≠` decidable in PTIME by local consistency) and Nebel & Bürckert 1995 (ORD-Horn, JACM 42(1):43–66; ORD-Horn strictly contains the point algebra; maximal tractable subclass of Allen) [20].

### 2D. RCC-8 (second algebra, Tier-2) ✅

- **8 base relations** `{DC, EC, PO, EQ, TPP, NTPP, TPPI, NTPPI}` (EQ = identity).
- **GQR `data/rcc8/calculus/rcc8.comp` excerpt (verbatim)** [15]:
  ```
  DC : DC :: ( DC EC PO TPP NTPP TPPI NTPPI EQ )      # = universal
  EC : EC :: ( DC EC PO TPP TPPI EQ )
  PO : PO :: ( DC EC PO TPP NTPP TPPI NTPPI EQ )      # = universal
  TPP : TPP :: ( TPP NTPP )
  TPP : NTPP :: ( NTPP )
  NTPP : NTPP :: ( NTPP )
  ```
  **Unit-test cell:** `TPP ∘ TPP = {TPP, NTPP}` [15].
- **Tractability:** general RCC-8 consistency is **NP-complete**; PC (algebraic closure) is **complete for the three maximal tractable subclasses** `Ĥ8, C8, Q8` (Renz & Nebel) — the 76 relations not contained in any of these form the hard set `NP8` [16].

**Fallback if GQR is unreachable:** QAT / SparQ (`qsr.informatik.uni-freiburg.de`)
distributions, or the Wikipedia / Alspaugh Allen tables, or generate the point/Allen
tables programmatically from interval/point geometry and cross-check against the cells above.

---

## SECTION 3 — PATH-CONSISTENCY SPEC + NAIVE-INTERSECTION CONTRAST + TRACTABILITY

### 3A. Full iterated PC (Mackworth PC-2 / van Beek queue) ✅

Path-consistency for QCNs (a.k.a. **algebraic closure / a-closure** [17]):

```
# Inputs: nodes V; edge labels R[i][j] ⊆ Base (LLM-read disjunctive set);
#         query/held-out edges initialized to the UNIVERSAL relation ⊤.
# Seed from the ALGEBRA, never the LLM:
for i:           R[i][i] = {=}                     # identity (point: {=}; Allen: {=})
for i<j:         R[j][i] = converse(R[i][j])       # allen.conv / point.conv

queue = { (i,j) : i<j }
while queue not empty:
    (i,j) = queue.pop()
    for k in V \ {i,j}:
        # refine edge (i,k) using path i-j-k
        new_ik = R[i][k] ∩ ( R[i][j] ∘ R[j][k] )
        if new_ik == ∅:  return INCONSISTENT      # empty-collapse certificate (Mode B)
        if new_ik ⊊ R[i][k]:
            R[i][k] = new_ik; R[k][i] = converse(new_ik); queue.add((i,k))
        # refine edge (k,j) using path k-i-j
        new_kj = R[k][j] ∩ ( R[k][i] ∘ R[i][j] )
        if new_kj == ∅:  return INCONSISTENT
        if new_kj ⊊ R[k][j]:
            R[k][j] = new_kj; R[j][k] = converse(new_kj); queue.add((k,j))
return CLOSED   # fixpoint: ∀ i,k,j  R[i][k] ⊆ R[i][j] ∘ R[j][k]
```

This is Mackworth (1977) **PC-2** [18]: path-consistency ⇔ checking every length-2 path
⇔ 3-consistency. The queue-based variant with triple-weighting is van Beek & Manchak /
Renz & Nebel [16][17]. **Composition `∘` and converse come from §2 tables; the
empty-set ⇒ inconsistency is the zero-false-positive hallucination certificate (Mode B).**
Complexity: **O(n³) per pass**, n = #events in a document subnetwork (small) → runs in
**milliseconds** [16][17]. Clean references: Renz & Nebel "A Survey of Qualitative
Spatial and Temporal Calculi," arXiv:1606.00133 (defines a-closure generalizing to all
calculi) [17]; the GQR paper [12].

### 3B. Naive single-pass intersection (the iteration-isolation baseline, H3) ✅

Defined precisely: at the **query pair only**, enumerate the reasoning paths identified
between the two query nodes; for each path compute the composition of edge labels along it
(`R_path = R[q0][k1] ∘ R[k1][k2] ∘ … ∘ R[k_{m-1}][q1]`); intersect across paths
**in a SINGLE pass**: `R_query = ⋂_paths R_path`. **No iteration to fixpoint, no
algebra-seeded re-propagation of tightened upstream edges** ("Path-of-Thoughts + one
obvious intersection step"). 

- **Theorem the H3 claim rests on:** on **length-2** (single intermediate node) acyclic
  multi-path queries, naive single-pass intersection **= full PC** (because there are no
  upstream edges to re-tighten). Therefore Mode-A **ties** naive on the length-2 stratum
  (a *prediction*, not a bug). Divergence requires **path length ≥3** and/or **cycles
  (cyclomatic number ≥1)**, where re-propagation tightens intermediate edges that then
  further constrain the query.
- **Stratification knobs:** hop-count = shortest constraining path length / graph
  diameter between the query pair; **cyclomatic number `μ = m − n + c`** (m edges, n nodes,
  c connected components) on the constraint subgraph. Stratify real + synthetic queries by
  (hop, μ) and report Mode-A−naive only where the theory predicts a gap (hop≥3 or μ≥1).

### 3C. Tractability facts (for honesty/scope claims) ✅

- PC is **SOUND** for all these algebras (never removes a feasible base relation) [16][17].
- PC is **COMPLETE** (decides consistency) for: **convex point algebra** [19], **ORD-Horn**
  (point) [20], and the **maximal tractable subclasses of RCC-8 (`Ĥ8,C8,Q8`)** [16] and of
  Allen (ORD-Horn) [20].
- **FULL Allen IA consistency and FULL RCC-8 consistency are NP-complete** (Vilain–Kautz;
  Nebel–Bürckert; Renz–Nebel) [16][19][20].
- **Consequence to state in the paper:** closure-**detectable** hallucination rate is a
  **LOWER BOUND** on full Allen / full RCC-8 (PC may miss some inconsistencies), but is
  **EXACT** on the **NarrativeTime convex-point-algebra (start-point) arm** [19][20].

### 3D. Repair (Mode B, Tier-2) ✅

Reiter (1987) "A Theory of Diagnosis from First Principles," *Artificial Intelligence*
32(1):57–95 [32]: minimal-hitting-set diagnosis over the conflict (empty-collapse) set.
Formulate as MaxSAT / minimum hitting set, preferring retraction of the **lowest-confidence
edges** (LLM-verbalized confidence). Reference-only; no implementation required for Tier-1.

---

## SECTION 4 — RENZ–NEBEL RANDOM CONSISTENT QCN GENERATOR A(n,d,l)

Source: Renz & Nebel, "Efficient Methods for Qualitative Spatial Reasoning," JAIR 2001 /
arXiv:1106.0679 [16].

### 4A. The canonical A(n,d,l) model (verbatim semantics) ✅

"we randomly generated our test instances with a given number of regions **n**, an average
**label-size l**, and an average **degree d** of the constraint graph" [16]. Two models:
`A(n,d,l)` uses **all** base relations; `H(n,d,l)` uses only the hard set `NP8` [16].
Generation procedure [16]:
1. Build a constraint graph with **n** nodes and **average degree d** (⇒ ≈ `n·d/2` edges; remaining pairs are the universal relation).
2. For each edge, draw a relation of expected size `l`: "select base relations with uniform distribution and out of the remaining [base] relations each one with probability `(l−1)/(B−1)`" (for RCC-8, `B=8` ⇒ `(l−1)/7`); if the result is an allowed relation assign it, else repeat [16].
- **Phase transition** is governed most strongly by `d`, at **`d ≈ 8–10`** depending on n [16]; A(n,d,l) is not trivially flawed for small d (local-inconsistency expectation hits 1 only at `d≈11.9` for n→∞, `d≈13.98` for n=100) [16]. Use **≥500 instances per data point** (Renz–Nebel's own setting) [16].

### 4B. ⚠ CRITICAL DISTINCTION — A(n,d,l) makes *possibly-inconsistent* nets; the experiment needs *guaranteed-consistent* gold

The bare A(n,d,l) draws random labels and may be inconsistent, so "gold" is undefined.
For a **random CONSISTENT network with a KNOWN solution**, use the standard
**"random scenario then qualitative abstraction"** recipe (consistent-by-construction):

1. **Draw a concrete scenario.** Assign every node a concrete realization in the domain — for **point algebra**: a distinct real/integer coordinate per event; for **Allen**: a concrete `[start,end]` integer interval per event; for **RCC-8**: concrete regions (e.g. discs/grid cells). This realization induces a **single base relation per pair** = the **gold atomic graph** (automatically globally consistent).
2. **Abstract / weaken (the "LLM-read" inputs).** Replace each observed edge's atomic relation with a larger **sound** disjunctive set (union the true base relation with extra base relations) at a controlled **per-edge recall/breadth** level. Held-out **query** edges are set to ⊤ (universal). The **gold pairwise relation between any two nodes is read off the concrete realization** — so gold is well-defined for *every* pair, including non-adjacent query pairs.

This guarantees consistency (a realizing model exists by construction) and yields gold for
held-out edges — the property A(n,d,l) alone lacks. (This is the same idea used to avoid
"trivially flawed" instances in CSP generation [16].)

### 4C. Mapping the four control knobs to generator parameters ✅

| Knob | Generator control |
|---|---|
| **density / redundancy** | average degree `d` (⇒ #edges) **and** #independent paths between a query pair (build P parallel disjoint chains) |
| **hop-count** | shortest constraining path length / graph diameter — build layered/chain structures of length L |
| **cyclomatic number** `μ=m−n+c` | add chords/extra cycles to raise μ |
| **per-edge recall / breadth** | the abstraction step in 4B.2 — how many extra base relations are unioned onto the gold (use **≥4 fixed recall levels** per the success criteria) |

These are *designable but not perfectly orthogonal* (e.g. adding paths raises both
redundancy and density) — **design** the clean parameters (P, L) and **measure** the
emergent ones (μ, contributing-edge count) per network.

### 4D. Existing tooling

GQR ships random-instance generation and SparQ has random-network tooling [12][16]; no
turnkey pip-installable consistent-QCN generator with these exact knobs was found, so the
executor should **implement the scenario-based generator from 4B** (self-contained above).
Composition tables come from §2 (GQR files). For an independent composition cross-check
during the GATE unit-test, the `qualreas` library (alreich) ships JSON algebra tables.

---

## SECTION 5 — BASELINE SPECS, EACH WITH A MATCHED ABSTENTION SIGNAL

**Common coverage object:** a method "answers" a query pair iff it commits to a **single
relation**. Threshold each method's confidence so all report at **matched coverage**
(equal answer-rate); compare **selective accuracy** at matched coverage.

| # | Baseline | What it does | Paper / repo | Matched abstention signal |
|---|---|---|---|---|
| **5A** | **Path-of-Thoughts (PoT)** — PRIMARY real-text baseline | graph extraction → path identification → **per-path INDEPENDENT reasoning**; outputs **all possible relations** | arXiv:2412.17963 [21]; ⚠ **no public repo found** (OpenReview `jRsizFp9Mg`) → reimplement | **path-agreement**: answer only if all/most identified paths agree on one relation |
| **5B** | Self-consistency voting | k sampled single-relation answers, majority | Wang et al. arXiv:2203.11171 [22] | **vote margin** over k samples (threshold the margin) |
| **5C** | **LINC** | LLM → FOL → Prover9; **majority vote** over multiple formalizations | arXiv:2310.15164 [23]; repo `github.com/benlipkin/linc` ✅ | **agreement across formalizations** |
| **5D** | DSR-LM / HtT (rule induction) | induce weighted/symbolic rules (Scallop / rule library), reason, **no closure** | DSR-LM arXiv:2305.03742 (Scallop) [24]; HtT "LLMs can Learn Rules" arXiv:2310.07064 [25] | induced-rule answer **+ its rule-confidence/score** |
| **5E** | TempRel COMMIT via ILP | LLM generates whole graph, **M=5** samples, sum+normalize → **ILP** enforces uniqueness/symmetry/transitivity, commits one label/pair | "Beyond Pairwise" Eirew, Bar, Dagan, arXiv:2502.11114 (EMNLP 2025) [26]; repo `github.com/AlonEirew/GlobalZeroShotTRE` ✅ | ILP-committed label's score (no disjunction/abstention) |
| **5F** | METRE (alt edge-reader, Tier-2) | **trained multi-label** classifier, predicts each relation's possibility independently; treats VAGUE as >1 possible | "Only One Relation Possible?" Hu, Huang, Feng, arXiv:2408.07353 [28]; ⚠ **no public repo/checkpoint found** → approximate/reimplement | tune threshold to **matched per-edge recall**; **report cross-edge error correlation ρ** |
| **5G** | (completeness) raw LLM verbalized-confidence; CoT; neural theorem prover (NTP/CTP) | lower priority | self-consistency [22]; standard CoT | verbalized confidence / CoT vote |

**5A details (verified) [21]:** PoT "reasons over each path **independently** to alleviate
cascading errors… and infers all possible answers"; "the reasoning module infers the
answer given for each reasoning path **independently**"; "a method is allowed to output
**multiple possible relations**." It does **not** intersect relations across paths or
detect cross-path contradictions. Symbolic reasoner = **CLINGO/ASP** [21]. Tested on
StepGame + CLUTRR (kinship/spatial). This is precisely the contrast the closure module
sharpens: PoT's per-path independence is exactly what iterated PC's cross-path intersection
+ re-propagation adds.

**5E motivation anchors (verified):** Eirew et al. run the LLM **M=5 times** ("performance
saturates after five generations"), sum+normalize into a per-pair distribution, then apply
the **ILP of Ning et al. 2018a** [26]. They also test **NarrativeTime + transitive-closure
(Warshall)** and find "most inferred relations remain local and sparse" [26] — direct
corroboration that naive closure over local reads has limited reach (motivates measuring
the *deduction-required* bite). 

**5E motivation anchors — citation CORRECTION ⚠.** The figures "LLMs assign >1 relation
for **≥50% up to 97%** of pairs" and "**ILP consistency does NOT improve F1**" come from
**Kougia, Sedova, Stephan, Zaporojets & Roth, "Analysing zero-shot temporal relation
extraction on clinical notes using temporal consistency," arXiv:2406.11486 (ACL 2024,
`2024.bionlp-1.6`)** [27] — i.e. all evaluated LLMs assign >1 relation to "at least 50% of
the pairs and up to 97% (Gemma BatchQA)," and "solving the inconsistencies [via ILP] does
not improve the F1 score" [27]. **The plan's attribution to "Knez & Sun" is incorrect** —
arXiv:2406.11486 is the Kougia et al. clinical-notes paper; use this citation for those
numbers.

---

## SECTION 6 — OPENROUTER MODEL CHOICE + CACHING (well under $10)

### 6A. Cheapest capable models (OpenRouter, verified June 2026) ✅

| Model | slug | input $/Mtok | output $/Mtok | notes |
|---|---|---|---|---|
| **Gemini 2.5 Flash-Lite** ★primary | `google/gemini-2.5-flash-lite` | **$0.10** | **$0.40** | cheapest capable; reliable structured/JSON via Google [29] |
| Gemini 2.5 Flash | `google/gemini-2.5-flash` | $0.30 | $2.50 | stronger, pricier [29] |
| **DeepSeek V3.2** ★alt-primary | `deepseek/deepseek-v3.2` | $0.23 | **$0.34** | lowest output cost; structured tool-calling [30] |
| DeepSeek V3 (chat) | `deepseek/deepseek-chat` | $0.20 | $0.80 | [30] |
| DeepSeek V3.1 | `deepseek/deepseek-chat-v3.1` | $0.21 | $0.79 | 164K ctx, structured tool-calling [30] |
| **Qwen2.5-72B-Instruct** | `qwen/qwen-2.5-72b-instruct` | $0.36 | $0.40 | different family (Alibaba) [31] |
| Llama-3.3-70B-Instruct | `meta-llama/llama-3.3-70b-instruct` | ~free `:free` tier / ~$0.10–0.13 paid | — | different family (Meta); free tier has rate-limit + data-retention caveats [29] |

`:floor` suffix routes to the cheapest provider. **Free `:free` models carry rate-limit
and data-retention caveats** — not recommended for the main run.

### 6B. Recommendations

- **PRIMARY reader:** `google/gemini-2.5-flash-lite` ($0.10/$0.40) — cheapest with reliable
  structured output; or `deepseek/deepseek-v3.2` if a non-Google primary is preferred.
- **SECOND, DIFFERENT-FAMILY reader (reader-agnosticity arm, genuinely different error
  correlation ρ):** pick a *different vendor* from the primary — if primary = Gemini
  (Google), use `deepseek/deepseek-v3.2` (DeepSeek) **or** `qwen/qwen-2.5-72b-instruct`
  (Alibaba) **or** `meta-llama/llama-3.3-70b-instruct` (Meta). Different pretraining ⇒
  genuinely different per-edge error correlation.

### 6C. Cost budget (arithmetic) ✅

Per edge-read call ≈ **1.1k input** (doc ~3000 chars ≈ 750 tok + prompt/schema ~350 tok) +
**~0.2k output** (one disjunctive relation). On Flash-Lite:
`1100×$0.10/1e6 + 200×$0.40/1e6 = $0.00011 + $0.00008 ≈ $0.00019/call`.

| Scenario | #calls | cost (Flash-Lite) |
|---|---|---|
| Tier-1 real-text reads (3 corpora × ~few-k pairs) | ~10,000 | ~$1.9 |
| + baselines (PoT, self-consistency k=5, LINC, ILP M=5) | ~25,000 | ~$4.8 |
| + frontier/recall sweep (≥4 recall levels) | ~40,000 | ~$7.6 |

Stays **< $10** even at 40k calls. **T0 (the a-priori gold-graph envelope go/no-go) is
ZERO-LLM-spend** and runs first; reserve LLM budget for T1/T2 only after T0 passes.

### 6D. Caching + cost-guard ✅

1. **Deterministic disk cache** keyed by `hash(doc_span, prompt_template, model, temperature=0)` → response; reruns cost **$0**. (List the cache dir in `upload_ignore_regexes`.)
2. **Batch per-document edge reads** to reuse document context across that doc's pairs.
3. Use **OpenRouter / provider prompt-caching** for repeated document prefixes where available.
4. **All LLM calls go through OpenRouter only** (no direct OpenAI/Anthropic). Maintain a **hard cumulative-cost tracker that aborts before $10**.

---

## SECTION 7 — OPERATIONALIZE THE EXTENDED REALISM-MATCHING STATISTIC

The synthetic NL-realization must be validated to resemble real corpus reads **before** the
redundancy curve is trusted. **All thresholds are FIXED (pre-registered) before generating
the redundancy curve.**

### (i) Per-edge error-type distribution + Total-Variation distance
Define error-type categories for a read edge vs. gold base-relation set `g` (atomic) and
read set `r`:
- **exact-correct:** `r == {g}` (singleton, equals gold);
- **SOUND-tight:** `g ∈ r`, `|r|` small (contains gold, slightly loose);
- **SOUND-loose / under-specified:** `g ∈ r`, `|r|` large (e.g. ⊤);
- **OVER-COMMITTED / unsound:** `g ∉ r` (omits gold — the dangerous case).

Estimate the categorical distribution `p_real(k)` (on real corpus reads) and `p_synth(k)`
(on synthetic reads). **TV distance** `TV = 0.5·Σ_k |p_real(k) − p_synth(k)|`. Pre-register
**TV ≤ 0.10**.

### (ii) Cross-edge error-correlation ρ match
Let `s_e ∈ {0,1}` be the per-edge **soundness indicator** (`1` if `g ∈ r`). Define
`ρ` = within-document correlation of `s_e` across edges sharing a document — use the
**intraclass correlation (ICC)** of `s_e` grouped by document, or mean pairwise Pearson/φ
between co-document edge indicators. Require **|ρ_real − ρ_synth| ≤ 0.10**. (Estimators:
`scipy.stats`/`pingouin` ICC, or `numpy.corrcoef` on the co-document indicator matrix.)

### (iii) Redundancy / topology histogram match
Histograms over queries of (a) **contributing-edge count** per query and (b)
**cyclomatic number μ**. Match real vs. synthetic via **TV or χ²** histogram distance ≤ a
fixed bound (e.g. **TV ≤ 0.15**).

### J(E) and why ρ matters
`J(E)` = **empirical joint soundness** = realized fraction of E-edge subnetworks where
**all E edges are sound**. Under independence `J(E) ≈ r^E` (r = mean per-edge soundness);
**positive cross-edge correlation ρ makes `J(E)` decay SLOWER than `r^E`** (sound edges
cluster within documents). Compute both `J(E)` and `r^E` from the same `s_e` indicators and
report the gap — this is what makes the redundancy benefit/cost trade-off (the inverted-U)
realistic rather than an independence artifact.

---

## SECTION 8 — DECISION TABLE + GOTCHAS

### 8A. Decision table

| Decision | Chosen value | Source | Confidence | Fallback |
|---|---|---|---|---|
| Headline corpus | **NarrativeTime / TimeBankNT** (dense, human-timeline) | [1][2][3][4] | High | TDDMan if NT density unusable |
| Corroborating corpus | **TDDMan** (long-distance, non-auto-inferable) | [7][8] | High | — |
| Control corpus | **MATRES** (local ⇒ N\*≈0 gate) | [9][11] | High | TB-Dense |
| Primary algebra (NT) | **convex point algebra** (start `time`) + full Allen (lower-bound) | [4][14][17] | High | Allen-only |
| Primary algebra (TDDMan) | coarse Allen `{<,>,di,d,=}` | [7][13] | High | — |
| Primary algebra (MATRES) | convex point algebra (start-points) | [11] | High | — |
| Composition-table source | **GQR** `data/{allen,point,rcc8}/calculus/*.comp,*.conv` | [12][13][14][15] | High | Allen-1983 / Alspaugh / qualreas |
| PC algorithm | **Mackworth PC-2 / van Beek queue a-closure** (O(n³)) | [16][17][18] | High | — |
| Naive baseline | single-pass per-path composition ∩, no iterate, no re-propagate | [21] | High | — |
| Synthetic generator | **scenario-then-abstract consistent QCN**; knobs d/paths, L, μ, recall | [16] | High | GQR/SparQ random tooling |
| Primary OpenRouter model | `google/gemini-2.5-flash-lite` ($0.10/$0.40) | [29] | High | `deepseek/deepseek-v3.2` |
| Second-family reader | `deepseek/deepseek-v3.2` or `qwen/qwen-2.5-72b-instruct` or `meta-llama/llama-3.3-70b` | [30][31] | High | any non-primary vendor |
| Realism thresholds (pre-reg) | TV(error-types)≤0.10; \|Δρ\|≤0.10; TV(topology)≤0.15 | this dossier §7 | Med | tighten/loosen pre-reg before curve |
| Mode-B repair | Reiter minimal hitting set / MaxSAT (Tier-2, ref only) | [32] | High | — |

### 8B. Gotchas

1. **TDDiscourse ships only `(docid, e_i, e_j, label)` triples** (4-col TSV, no header) → **must join raw text + event offsets from TimeBank-Dense / TimeBank 1.2** (timeml.github.io / LDC) [7][1].
2. **NarrativeTime repo URL had to be dug from the PDF footnotes** → `github.com/text-machine-lab/nt`, MIT, branch `master` (verified); JSONL in `corpus/timebank/nt_format/`, gold logic in `narrative_time/event_relations.py` [1][3][4].
3. **GQR Allen uses `<`/`>` for before/after** (13 tokens `=,<,>,d,di,s,si,f,fi,m,mi,o,oi`), not `b`/`bi` — remap label names [13].
4. **Convex point algebra: WIDEN the only non-convex relation `≠={<,>}` to `⊤` (VAGUE)** to keep PC complete, and **measure the bite lost** [14][19][20].
5. **Converses + identity must be ALGEBRA-SEEDED (`*.conv` + `=`/`{=}`), NEVER LLM-read** [13][14].
6. **Full Allen / full RCC-8 PC is sound but INCOMPLETE** (closure-detectable rate = LOWER BOUND); the **NarrativeTime start-point point-algebra arm is EXACT** [16][19][20].
7. **naive == full PC on length-2 acyclic queries is a PREDICTION, not a bug** — stratify by hop≥3 / μ≥1 to expose the iteration gap [21].
8. **T0 is zero-LLM-spend and runs first** (a-priori gold-graph envelope go/no-go); reserve LLM budget for T1/T2 [26 motivates the small real-text closure reach].
9. **METRE is F1-trained (not recall-oriented)** → tune its threshold to **matched per-edge recall** and **report ρ**; **no public METRE/PoT repo** → reimplement [28][21].
10. **Citation fix:** the "≥50%–97% multiple-relation" and "ILP doesn't improve F1" facts are **Kougia et al. arXiv:2406.11486** (not "Knez & Sun") [27].
11. **Free-tier OpenRouter models** have rate-limit + data-retention caveats — avoid for the main run [29].
12. **LLM contamination caveat:** NarrativeTime/TimeBank may be in LLM pretraining (GitHub) → potential test-set leak; read from raw text spans only [1].

### 8C. Follow-up questions (could not be fully resolved)
- Exact numeric semantics of NarrativeTime's `time` coordinate per **branch** (is it a global float ordering or per-branch local?) — `get_event_relation` gates on same-branch, but the absolute scale across branches needs a quick empirical check on `tbd_clear.jsonl`.
- Whether a downloadable **METRE checkpoint** exists (none found) — otherwise the reader-agnosticity arm must train/approximate a multi-label reader.
- Whether the **Path-of-Thoughts** authors release code (none found as of the v2, Mar 2026 listing) — otherwise reimplement graph-extraction + ASP/CLINGO per the paper.

---

## Sources
See `research_out.json` `sources[]` for the indexed list with URLs and contributions.


## Sources

[1] [NarrativeTime: Dense Temporal Annotation on a Timeline (arXiv:1908.11443 PDF)](https://arxiv.org/pdf/1908.11443) — Repo URL github.com/text-machine-lab/nt found in footnotes 1 & 6; 102,313 TLINKs excl. inverses; extended MATRES at qiangning/MATRES; TDDiscourse references event IDs not EIIDs; LLM test-set-leak warning.

[2] [NarrativeTime (LREC-COLING 2024 ACL Anthology)](https://aclanthology.org/2024.lrec-main.1054/) — Canonical publication; TimeBankNT corpus, full TLINK coverage, double expert annotation, TimeML conversion tools, baselines.

[3] [text-machine-lab/nt GitHub repository](https://github.com/text-machine-lab/nt) — MIT license; corpus/timebank/nt_format/*.jsonl (tbd_a1/a2/clear), nt_converted_to_tml/, narrative_time/ package, utils/nt2tml.py converter; branch master verified.

[4] [NarrativeTime event_relations.py (gold-relation logic)](https://raw.githubusercontent.com/text-machine-lab/nt/master/narrative_time/event_relations.py) — Decodes gold derivation: per-event numeric `time` coord, bracket types {[B],{U},{U],[U}}, 7 relations REL_TO_ID, (type1,type2)-keyed CONVERSION_TABLE, same-branch-only (cross-branch=VAGUE), get_event_relation(); start-point comparison for convex point algebra arm.

[5] [TLEX: Extracting Exact Timelines from TimeML Temporal Graphs (arXiv:2406.05265)](https://arxiv.org/abs/2406.05265) — Worked TimeML-graph -> point-algebra TCSP -> timeline extraction with inconsistency/indeterminacy detection; reusable as start-point ordering oracle.

[6] [pyTLEX: Python TimeLine EXtraction library (EACL 2024 demo, FIU COGNAC)](https://github.com/pyTLEX-Team/pyTLEX) — Maintained Python TLEX implementation (Ocal & Finlayson); TimeML -> TCSP -> timelines; usable to cross-check NarrativeTime start-point orderings on nt_converted_to_tml. Also aclanthology.org/2024.eacl-demo.4/.

[7] [TDDiscourse / TDDMan GitHub repository](https://github.com/aakanksha19/TDDiscourse) — Verified TSV format: 4 tab-sep columns docid e_i e_j relation, no header; codes a/b/i/ii/s (after/before/includes/is_included/simultaneous), no vague; TDDMan splits 4000/650/1500; only (pair,label) triples -> must join text+offsets from TimeBank-Dense; TDDAuto is auto-derived (do not use).

[8] [TDDiscourse: A Dataset for Discourse-Level Temporal Ordering (SIGDial 2019)](https://aclanthology.org/W19-5929/) — Non-circularity anchor verified verbatim: first dataset for event pairs >1 sentence apart, manually annotating global pairs that cannot be inferred automatically; long-distance, not auto-inferable.

[9] [CogComp/MATRES GitHub repository](https://github.com/CogComp/MATRES) — Format docid,verb1,verb2,eiid1,eiid2,relation; files timebank.txt/aquaint.txt/platinum.txt + rawdata/; verb events, main-axis only; TempEval-3/TBAQ source text.

[10] [qiangning/MATRES (extended, entire TempEval-3)](https://github.com/qiangning/MATRES) — Extended MATRES covering the whole TempEval-3 (verbal events); the version whose statistics are commonly cited.

[11] [A Multi-Axis Annotation Scheme for Event Temporal Relations (MATRES, Ning/Wu/Roth ACL 2018)](https://arxiv.org/pdf/1804.07828) — Start-points-only design = convex point algebra over t_start (labels before/after/equal/vague); 2-sentence sliding window (local) => deduction envelope ~empty (gate control); IAA .84 Cohen kappa; Q1/Q2 vague mapping.

[12] [GQR: Fast Reasoner for Binary Qualitative Constraint Calculi](https://github.com/m-westphal/gqr) — Primary composition-table source; calculus defined by data/<cal>/calculus/*.comp + *.conv (+ *.weights); no .spec; ships random-instance generation.

[13] [GQR Allen composition + converse files (allen.comp / allen.conv)](https://raw.githubusercontent.com/m-westphal/gqr/master/data/allen/calculus/allen.comp) — Verbatim grammar 'r1 : r2 :: ( set )' and 'r :: converse'; 13 base tokens =,<,>,d,di,s,si,f,fi,m,mi,o,oi (< = before, > = after); verified cells b.b={<}, b.d={<dsmo}, d.di=full, o.o={<mo}, m.mi={=ffi}.

[14] [GQR point algebra composition + converse (point.comp / point.conv)](https://raw.githubusercontent.com/m-westphal/gqr/master/data/point/calculus/point.comp) — Complete 3x3 over {<,=,>}: <o<=<, >o>=>, <o>=universal, >o<=universal, = identity; conv = / < ->> / > ->< . Basis for convex point algebra arm + non-convex != widening rule.

[15] [GQR RCC-8 composition table (rcc8.comp)](https://raw.githubusercontent.com/m-westphal/gqr/master/data/rcc8/calculus/rcc8.comp) — 8 base relations DC,EC,PO,EQ,TPP,NTPP,TPPI,NTPPI; verified cells DC.DC=universal, TPP.TPP={TPP,NTPP}, NTPP.NTPP={NTPP}.

[16] [Renz & Nebel, Efficient Methods for Qualitative Spatial Reasoning (JAIR 2001)](https://arxiv.org/abs/1106.0679) — A(n,d,l) random model: n nodes, avg degree d, avg label-size l; label draw rule; phase transition d~8-10; RCC-8 NP-complete with maximal tractable subclasses H8/C8/Q8 (hard set NP8=76); >=500 instances/point; basis for the scenario-then-abstract consistent-QCN recipe.

[17] [Renz & Nebel et al., A Survey of Qualitative Spatial and Temporal Calculi (arXiv:1606.00133)](https://arxiv.org/abs/1606.00133) — Algebraic-closure (a-closure / path-consistency) algorithm generalizing to all calculi; PC1 point algebra (<,=,>; {<,=}=<=; <o<=<; <o>=universal); composition/converse roles.

[18] [Mackworth 1977, Consistency in Networks of Relations (Artificial Intelligence 8:99-118)](https://www.semanticscholar.org/paper/Consistency-in-Networks-of-Relations-Mackworth/70f3161f62a4a43580eb47d2157e98e880738594) — PC-2 path-consistency; path-consistency <=> checking every length-2 path <=> 3-consistency; basis of the iterated-fixpoint closure spec.

[19] [Vilain & Kautz 1986, Constraint Propagation Algorithms for Temporal Reasoning (point algebra)](https://www.semanticscholar.org/paper/Constraint-propagation-algorithms-for-temporal-a-Vilain-Kautz/dcff7aa8ca9327ed1297cff206202bd3565eb8c1) — Point algebra (=,<,<=,!=) decidable in PTIME by local consistency => PC is COMPLETE for convex/pointizable classes (EXACT certificate on NT start-point arm).

[20] [Nebel & Burckert 1995, ORD-Horn maximal tractable subclass of Allen (JACM 42(1):43-66)](https://dl.acm.org/doi/10.1145/200836.200848) — ORD-Horn is the maximal tractable subclass of Allen IA; strictly contains the point algebra; adding any other relation makes consistency NP-complete; PC complete on ORD-Horn.

[21] [Path-of-Thoughts: Extracting/Following Paths for Robust Relational Reasoning (arXiv:2412.17963)](https://arxiv.org/abs/2412.17963) — PRIMARY baseline: per-path INDEPENDENT reasoning, outputs ALL possible relations, no cross-path intersection/contradiction detection; CLINGO/ASP symbolic reasoner; StepGame+CLUTRR. No public repo found -> reimplement. Matched abstention = path-agreement.

[22] [Wang et al. 2022, Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171) — Self-consistency voting baseline; matched abstention = vote margin over k samples.

[23] [LINC: Neurosymbolic Logical Reasoning with FOL Provers (Olausson et al., EMNLP 2023)](https://arxiv.org/abs/2310.15164) — LLM->FOL->Prover9 with majority vote over formalizations; repo github.com/benlipkin/linc; matched abstention = agreement across formalizations; cannot see joint inconsistency of individually-popular steps.

[24] [DSR-LM: Improved Logical Reasoning via Differentiable Symbolic Programming (Findings ACL 2023)](https://arxiv.org/abs/2305.03742) — Induces weighted symbolic rules with Scallop, no closure; rule-induction baseline; abstention = induced-rule answer confidence; supports table-held-fixed ablation isolating PC.

[25] [Large Language Models can Learn Rules (HtT, Zhu et al. 2023)](https://arxiv.org/abs/2310.07064) — Hypotheses-to-Theories: induction (generate+verify rules->library) + deduction; rule-induction baseline alternative to DSR-LM; +10-30% accuracy, transferable rules.

[26] [Beyond Pairwise: Global Zero-shot Temporal Graph Generation (Eirew, Bar, Dagan; EMNLP 2025)](https://arxiv.org/abs/2502.11114) — ILP COMMIT baseline: whole-graph generation, M=5 samples, sum+normalize -> ILP (Ning 2018a) uniqueness/symmetry/transitivity; OmniTemp dataset; repo github.com/AlonEirew/GlobalZeroShotTRE; NarrativeTime+Warshall closure stays local/sparse (corroborates limited naive-closure reach).

[27] [Kougia et al. 2024, Analysing zero-shot TRE on clinical notes using temporal consistency (ACL 2024.bionlp-1.6)](https://arxiv.org/abs/2406.11486) — CITATION FIX: source of '>1 relation for >=50%, up to 97% (Gemma BatchQA)' and 'ILP consistency does NOT improve F1' -- NOT 'Knez & Sun'. Uniqueness+transitivity consistency analysis.

[28] [Only One Relation Possible? Modeling Ambiguity in Event TRE (METRE; Hu, Huang, Feng 2024)](https://arxiv.org/abs/2408.07353) — METRE multi-label reader (Tier-2 reader-agnosticity arm): predicts each relation's possibility independently, VAGUE = >1 possible; TB-Dense/MATRES/UDS-T; F1-trained -> match recall + report rho; no public repo/checkpoint found.

[29] [OpenRouter — Gemini 2.5 Flash-Lite pricing](https://openrouter.ai/google/gemini-2.5-flash-lite) — PRIMARY model: $0.10/Mtok input, $0.40/Mtok output; reliable structured/JSON output; Gemini 2.5 Flash $0.30/$2.50; Llama-3.3-70B free tier (rate-limit/retention caveats).

[30] [OpenRouter — DeepSeek V3.x pricing](https://openrouter.ai/deepseek/deepseek-chat-v3.1) — Alt-primary / second-family reader: V3.2 $0.23/$0.34, V3 (chat) $0.20/$0.80, V3.1 $0.21/$0.79 (164K ctx, structured tool calling).

[31] [OpenRouter — Qwen2.5-72B-Instruct pricing](https://openrouter.ai/qwen/qwen-2.5-72b-instruct) — Second-family (Alibaba) reader option: $0.36/Mtok input, $0.40/Mtok output.

[32] [Reiter 1987, A Theory of Diagnosis from First Principles (AI 32(1):57-95)](https://doi.org/10.1016/0004-3702(87)90062-2) — Mode-B repair: minimal-hitting-set diagnosis over conflict (empty-collapse) set; MaxSAT/hitting-set formulation preferring lowest-confidence edge retraction (Tier-2, reference only).

[33] [Allen 1983, Maintaining Knowledge about Temporal Intervals (CACM 26(11))](https://dl.acm.org/doi/10.1145/182.358434) — Independent authoritative Allen 13x13 composition table for cross-checking the loaded GQR table (unit-test cells b.b, b.d, d.di, o.o).

## Follow-up Questions

- What is the exact numeric semantics of NarrativeTime's per-event `time` coordinate across timeline `branch`es (global float ordering vs. per-branch local scale)? get_event_relation only compares within-branch, so the cross-branch absolute scale needs a quick empirical check on tbd_clear.jsonl before the start-point point-algebra gold is trusted.
- Is there any downloadable METRE checkpoint or training code (none found for arXiv:2408.07353)? If not, the reader-agnosticity / multi-label-reader arm must train or approximate a multi-label temporal reader and tune it to matched per-edge recall.
- Have the Path-of-Thoughts authors released code (none found as of the v2 March-2026 listing)? If not, the PRIMARY real-text baseline (graph extraction + path identification + ASP/CLINGO per-path reasoning) must be reimplemented from the paper.

---
*Generated by AI Inventor Pipeline*
