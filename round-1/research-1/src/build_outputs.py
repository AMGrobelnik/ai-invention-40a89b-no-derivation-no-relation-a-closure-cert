"""Build research_out.json from research_report.md + the verified source list."""
import json
from pathlib import Path

WS = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_research_1")
answer = (WS / "research_report.md").read_text(encoding="utf-8")

sources = [
    (1, "https://arxiv.org/pdf/1908.11443", "NarrativeTime: Dense Temporal Annotation on a Timeline (arXiv:1908.11443 PDF)",
     "Repo URL github.com/text-machine-lab/nt found in footnotes 1 & 6; 102,313 TLINKs excl. inverses; extended MATRES at qiangning/MATRES; TDDiscourse references event IDs not EIIDs; LLM test-set-leak warning."),
    (2, "https://aclanthology.org/2024.lrec-main.1054/", "NarrativeTime (LREC-COLING 2024 ACL Anthology)",
     "Canonical publication; TimeBankNT corpus, full TLINK coverage, double expert annotation, TimeML conversion tools, baselines."),
    (3, "https://github.com/text-machine-lab/nt", "text-machine-lab/nt GitHub repository",
     "MIT license; corpus/timebank/nt_format/*.jsonl (tbd_a1/a2/clear), nt_converted_to_tml/, narrative_time/ package, utils/nt2tml.py converter; branch master verified."),
    (4, "https://raw.githubusercontent.com/text-machine-lab/nt/master/narrative_time/event_relations.py", "NarrativeTime event_relations.py (gold-relation logic)",
     "Decodes gold derivation: per-event numeric `time` coord, bracket types {[B],{U},{U],[U}}, 7 relations REL_TO_ID, (type1,type2)-keyed CONVERSION_TABLE, same-branch-only (cross-branch=VAGUE), get_event_relation(); start-point comparison for convex point algebra arm."),
    (5, "https://arxiv.org/abs/2406.05265", "TLEX: Extracting Exact Timelines from TimeML Temporal Graphs (arXiv:2406.05265)",
     "Worked TimeML-graph -> point-algebra TCSP -> timeline extraction with inconsistency/indeterminacy detection; reusable as start-point ordering oracle."),
    (6, "https://github.com/pyTLEX-Team/pyTLEX", "pyTLEX: Python TimeLine EXtraction library (EACL 2024 demo, FIU COGNAC)",
     "Maintained Python TLEX implementation (Ocal & Finlayson); TimeML -> TCSP -> timelines; usable to cross-check NarrativeTime start-point orderings on nt_converted_to_tml. Also aclanthology.org/2024.eacl-demo.4/."),
    (7, "https://github.com/aakanksha19/TDDiscourse", "TDDiscourse / TDDMan GitHub repository",
     "Verified TSV format: 4 tab-sep columns docid e_i e_j relation, no header; codes a/b/i/ii/s (after/before/includes/is_included/simultaneous), no vague; TDDMan splits 4000/650/1500; only (pair,label) triples -> must join text+offsets from TimeBank-Dense; TDDAuto is auto-derived (do not use)."),
    (8, "https://aclanthology.org/W19-5929/", "TDDiscourse: A Dataset for Discourse-Level Temporal Ordering (SIGDial 2019)",
     "Non-circularity anchor verified verbatim: first dataset for event pairs >1 sentence apart, manually annotating global pairs that cannot be inferred automatically; long-distance, not auto-inferable."),
    (9, "https://github.com/CogComp/MATRES", "CogComp/MATRES GitHub repository",
     "Format docid,verb1,verb2,eiid1,eiid2,relation; files timebank.txt/aquaint.txt/platinum.txt + rawdata/; verb events, main-axis only; TempEval-3/TBAQ source text."),
    (10, "https://github.com/qiangning/MATRES", "qiangning/MATRES (extended, entire TempEval-3)",
     "Extended MATRES covering the whole TempEval-3 (verbal events); the version whose statistics are commonly cited."),
    (11, "https://arxiv.org/pdf/1804.07828", "A Multi-Axis Annotation Scheme for Event Temporal Relations (MATRES, Ning/Wu/Roth ACL 2018)",
     "Start-points-only design = convex point algebra over t_start (labels before/after/equal/vague); 2-sentence sliding window (local) => deduction envelope ~empty (gate control); IAA .84 Cohen kappa; Q1/Q2 vague mapping."),
    (12, "https://github.com/m-westphal/gqr", "GQR: Fast Reasoner for Binary Qualitative Constraint Calculi",
     "Primary composition-table source; calculus defined by data/<cal>/calculus/*.comp + *.conv (+ *.weights); no .spec; ships random-instance generation."),
    (13, "https://raw.githubusercontent.com/m-westphal/gqr/master/data/allen/calculus/allen.comp", "GQR Allen composition + converse files (allen.comp / allen.conv)",
     "Verbatim grammar 'r1 : r2 :: ( set )' and 'r :: converse'; 13 base tokens =,<,>,d,di,s,si,f,fi,m,mi,o,oi (< = before, > = after); verified cells b.b={<}, b.d={<dsmo}, d.di=full, o.o={<mo}, m.mi={=ffi}."),
    (14, "https://raw.githubusercontent.com/m-westphal/gqr/master/data/point/calculus/point.comp", "GQR point algebra composition + converse (point.comp / point.conv)",
     "Complete 3x3 over {<,=,>}: <o<=<, >o>=>, <o>=universal, >o<=universal, = identity; conv = / < ->> / > ->< . Basis for convex point algebra arm + non-convex != widening rule."),
    (15, "https://raw.githubusercontent.com/m-westphal/gqr/master/data/rcc8/calculus/rcc8.comp", "GQR RCC-8 composition table (rcc8.comp)",
     "8 base relations DC,EC,PO,EQ,TPP,NTPP,TPPI,NTPPI; verified cells DC.DC=universal, TPP.TPP={TPP,NTPP}, NTPP.NTPP={NTPP}."),
    (16, "https://arxiv.org/abs/1106.0679", "Renz & Nebel, Efficient Methods for Qualitative Spatial Reasoning (JAIR 2001)",
     "A(n,d,l) random model: n nodes, avg degree d, avg label-size l; label draw rule; phase transition d~8-10; RCC-8 NP-complete with maximal tractable subclasses H8/C8/Q8 (hard set NP8=76); >=500 instances/point; basis for the scenario-then-abstract consistent-QCN recipe."),
    (17, "https://arxiv.org/abs/1606.00133", "Renz & Nebel et al., A Survey of Qualitative Spatial and Temporal Calculi (arXiv:1606.00133)",
     "Algebraic-closure (a-closure / path-consistency) algorithm generalizing to all calculi; PC1 point algebra (<,=,>; {<,=}=<=; <o<=<; <o>=universal); composition/converse roles."),
    (18, "https://www.semanticscholar.org/paper/Consistency-in-Networks-of-Relations-Mackworth/70f3161f62a4a43580eb47d2157e98e880738594", "Mackworth 1977, Consistency in Networks of Relations (Artificial Intelligence 8:99-118)",
     "PC-2 path-consistency; path-consistency <=> checking every length-2 path <=> 3-consistency; basis of the iterated-fixpoint closure spec."),
    (19, "https://www.semanticscholar.org/paper/Constraint-propagation-algorithms-for-temporal-a-Vilain-Kautz/dcff7aa8ca9327ed1297cff206202bd3565eb8c1", "Vilain & Kautz 1986, Constraint Propagation Algorithms for Temporal Reasoning (point algebra)",
     "Point algebra (=,<,<=,!=) decidable in PTIME by local consistency => PC is COMPLETE for convex/pointizable classes (EXACT certificate on NT start-point arm)."),
    (20, "https://dl.acm.org/doi/10.1145/200836.200848", "Nebel & Burckert 1995, ORD-Horn maximal tractable subclass of Allen (JACM 42(1):43-66)",
     "ORD-Horn is the maximal tractable subclass of Allen IA; strictly contains the point algebra; adding any other relation makes consistency NP-complete; PC complete on ORD-Horn."),
    (21, "https://arxiv.org/abs/2412.17963", "Path-of-Thoughts: Extracting/Following Paths for Robust Relational Reasoning (arXiv:2412.17963)",
     "PRIMARY baseline: per-path INDEPENDENT reasoning, outputs ALL possible relations, no cross-path intersection/contradiction detection; CLINGO/ASP symbolic reasoner; StepGame+CLUTRR. No public repo found -> reimplement. Matched abstention = path-agreement."),
    (22, "https://arxiv.org/abs/2203.11171", "Wang et al. 2022, Self-Consistency Improves Chain of Thought Reasoning",
     "Self-consistency voting baseline; matched abstention = vote margin over k samples."),
    (23, "https://arxiv.org/abs/2310.15164", "LINC: Neurosymbolic Logical Reasoning with FOL Provers (Olausson et al., EMNLP 2023)",
     "LLM->FOL->Prover9 with majority vote over formalizations; repo github.com/benlipkin/linc; matched abstention = agreement across formalizations; cannot see joint inconsistency of individually-popular steps."),
    (24, "https://arxiv.org/abs/2305.03742", "DSR-LM: Improved Logical Reasoning via Differentiable Symbolic Programming (Findings ACL 2023)",
     "Induces weighted symbolic rules with Scallop, no closure; rule-induction baseline; abstention = induced-rule answer confidence; supports table-held-fixed ablation isolating PC."),
    (25, "https://arxiv.org/abs/2310.07064", "Large Language Models can Learn Rules (HtT, Zhu et al. 2023)",
     "Hypotheses-to-Theories: induction (generate+verify rules->library) + deduction; rule-induction baseline alternative to DSR-LM; +10-30% accuracy, transferable rules."),
    (26, "https://arxiv.org/abs/2502.11114", "Beyond Pairwise: Global Zero-shot Temporal Graph Generation (Eirew, Bar, Dagan; EMNLP 2025)",
     "ILP COMMIT baseline: whole-graph generation, M=5 samples, sum+normalize -> ILP (Ning 2018a) uniqueness/symmetry/transitivity; OmniTemp dataset; repo github.com/AlonEirew/GlobalZeroShotTRE; NarrativeTime+Warshall closure stays local/sparse (corroborates limited naive-closure reach)."),
    (27, "https://arxiv.org/abs/2406.11486", "Kougia et al. 2024, Analysing zero-shot TRE on clinical notes using temporal consistency (ACL 2024.bionlp-1.6)",
     "CITATION FIX: source of '>1 relation for >=50%, up to 97% (Gemma BatchQA)' and 'ILP consistency does NOT improve F1' -- NOT 'Knez & Sun'. Uniqueness+transitivity consistency analysis."),
    (28, "https://arxiv.org/abs/2408.07353", "Only One Relation Possible? Modeling Ambiguity in Event TRE (METRE; Hu, Huang, Feng 2024)",
     "METRE multi-label reader (Tier-2 reader-agnosticity arm): predicts each relation's possibility independently, VAGUE = >1 possible; TB-Dense/MATRES/UDS-T; F1-trained -> match recall + report rho; no public repo/checkpoint found."),
    (29, "https://openrouter.ai/google/gemini-2.5-flash-lite", "OpenRouter — Gemini 2.5 Flash-Lite pricing",
     "PRIMARY model: $0.10/Mtok input, $0.40/Mtok output; reliable structured/JSON output; Gemini 2.5 Flash $0.30/$2.50; Llama-3.3-70B free tier (rate-limit/retention caveats)."),
    (30, "https://openrouter.ai/deepseek/deepseek-chat-v3.1", "OpenRouter — DeepSeek V3.x pricing",
     "Alt-primary / second-family reader: V3.2 $0.23/$0.34, V3 (chat) $0.20/$0.80, V3.1 $0.21/$0.79 (164K ctx, structured tool calling)."),
    (31, "https://openrouter.ai/qwen/qwen-2.5-72b-instruct", "OpenRouter — Qwen2.5-72B-Instruct pricing",
     "Second-family (Alibaba) reader option: $0.36/Mtok input, $0.40/Mtok output."),
    (32, "https://doi.org/10.1016/0004-3702(87)90062-2", "Reiter 1987, A Theory of Diagnosis from First Principles (AI 32(1):57-95)",
     "Mode-B repair: minimal-hitting-set diagnosis over conflict (empty-collapse) set; MaxSAT/hitting-set formulation preferring lowest-confidence edge retraction (Tier-2, reference only)."),
    (33, "https://dl.acm.org/doi/10.1145/182.358434", "Allen 1983, Maintaining Knowledge about Temporal Intervals (CACM 26(11))",
     "Independent authoritative Allen 13x13 composition table for cross-checking the loaded GQR table (unit-test cells b.b, b.d, d.di, o.o)."),
]

follow_up = [
    "What is the exact numeric semantics of NarrativeTime's per-event `time` coordinate across timeline `branch`es (global float ordering vs. per-branch local scale)? get_event_relation only compares within-branch, so the cross-branch absolute scale needs a quick empirical check on tbd_clear.jsonl before the start-point point-algebra gold is trusted.",
    "Is there any downloadable METRE checkpoint or training code (none found for arXiv:2408.07353)? If not, the reader-agnosticity / multi-label-reader arm must train or approximate a multi-label temporal reader and tune it to matched per-edge recall.",
    "Have the Path-of-Thoughts authors released code (none found as of the v2 March-2026 listing)? If not, the PRIMARY real-text baseline (graph extraction + path identification + ASP/CLINGO per-path reasoning) must be reimplemented from the paper.",
]

out = {
    "title": "Implementation/Resource Dossier for the Closure-Certified Text-to-Logic Deduction Module",
    "summary": (
        "Verified, executor-ready specifications for the closure-certified temporal-deduction pipeline: "
        "(1) corpus access+parse formats for NarrativeTime (repo github.com/text-machine-lab/nt, MIT, nt_format JSONL with per-event numeric `time` coordinate + bracket-type interval model + same-branch get_event_relation), "
        "TDDMan (4-col TSV, codes a/b/i/ii/s, join text from TimeBank-Dense; long-distance non-auto-inferable gold), and MATRES (start-point convex point algebra, 2-sentence window = N*~=0 gate control); "
        "(2) machine-readable GQR composition/converse tables for Allen (13 tokens with < / > for before/after), convex point algebra (with the only-non-convex != -> universal widening rule), and RCC-8, each with verified unit-test cells; "
        "(3) Mackworth PC-2 iterated a-closure pseudocode + the precise naive single-pass-intersection contrast (naive==full on length-2, diverges at hop>=3 / cyclomatic>=1) + soundness/completeness tractability facts (point-algebra arm EXACT, full Allen/RCC-8 a LOWER BOUND); "
        "(4) the Renz-Nebel A(n,d,l) model plus the scenario-then-abstract recipe for guaranteed-consistent synthetic QCNs with independent density/hop/cyclomatic/recall knobs; "
        "(5) baseline configs each with a matched abstention signal (Path-of-Thoughts, self-consistency, LINC, DSR-LM/HtT, ILP-commit Eirew et al. M=5, METRE) and a corrected citation (the >=50-97% multiple-relation + ILP-no-F1-gain facts are Kougia et al. arXiv:2406.11486, not 'Knez & Sun'); "
        "(6) OpenRouter model choice (primary google/gemini-2.5-flash-lite $0.10/$0.40, second-family DeepSeek-V3.2/Qwen2.5-72B/Llama-3.3-70B) with arithmetic showing <$10 and a disk-cache + hard cost-guard strategy; and "
        "(7) the operationalized three-part realism-matching statistic (per-edge error-type TV<=0.10, cross-edge soundness-correlation |dro|<=0.10 via ICC, topology histogram TV<=0.15) with J(E) vs r^E. Includes a full decision table, a 12-item gotchas list, and 3 unresolved follow-ups."
    ),
    "answer": answer,
    "sources": [{"index": i, "url": u, "title": t, "summary": s} for (i, u, t, s) in sources],
    "follow_up_questions": follow_up,
}

(WS / "research_out.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
print("Wrote research_out.json:", (WS / "research_out.json").stat().st_size, "bytes")

# ---- struct output expected by the harness ----
struct = {
    "title": "Implementation/Resource Dossier for the Closure-Certified Text-to-Logic Deduction Module",
    "layman_summary": (
        "A verified how-to dossier telling the downstream builders exactly which temporal datasets, "
        "math lookup tables, reasoning algorithm, AI models, and statistics to use (with real URLs) so they implement instead of guess."
    ),
    "summary": out["summary"],
    "out_expected_files": {"output": "research_out.json"},
    "upload_ignore_regexes": [r"(^|/)__pycache__/", r"(^|/)\.repl_agent\.ptylog$"],
    "answer": answer,
    "sources": out["sources"],
    "follow_up_questions": follow_up,
}
(WS / ".terminal_claude_agent_struct_out.json").write_text(json.dumps(struct, indent=2, ensure_ascii=False), encoding="utf-8")
print("Wrote .terminal_claude_agent_struct_out.json:", (WS / ".terminal_claude_agent_struct_out.json").stat().st_size, "bytes")
print("title len:", len(struct["title"]), "| layman len:", len(struct["layman_summary"]), "| summary len:", len(struct["summary"]))
print("answer chars:", len(answer), "| sources:", len(sources))
# sanity: every [n] citation marker in the answer must have a matching source index
import re
cited = set(int(x) for x in re.findall(r"\[(\d+)\]", answer))
have = set(i for (i, *_rest) in sources)
missing = sorted(cited - have)
print("cited-but-missing source indices:", missing)
print("uncited source indices:", sorted(have - cited))
