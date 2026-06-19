#!/usr/bin/env python3
"""Forward-closure (least-fixpoint UNION) kinship discharge in ACTUAL SWI-Prolog.

The iter-3 prolog.py emits a simple-path right-fold `solve_/4`, which is INCOMPLETE for
the finite kinship composition table: a single association order can hit an UNDEFINED
composition and miss a derivation the engine's full fixpoint finds (this is exactly the
iteration / closure advantage). For a COHERENT human-auditable trace that reproduces the
certified engine, we emit a program that computes the SAME forward-union least fixpoint:

  der(A,T,B)  closed under  der(A,T1,B), der(B,T2,C), comp(T1,T2,T3) => der(A,T3,C)
  and under converse (every edge asserted both directions),

then reads back  setof(R, der(qsrc,qtgt,R), Rs)  --  identical to engine.query_modeA's D set.
The discharge runs swipl as a subprocess (honest python-checked fallback if unavailable),
and is cross-checked against the engine's forward_closure type set (matches_engine).
"""
from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from prolog import _atom  # reuse the verified atom-quoting from iter-3 prolog.py


def emit_fixpoint_program(kin, edges, qsrc, qtgt) -> str:
    lines = [
        "% Closure-certified kinship deduction -- forward-union least-fixpoint trace program.",
        "% der(A,T,B): T derivable for the directed pair A->B; closed under the finite",
        "% composition table comp/3 + total converse conv/2 (both-direction seeding).",
        ":- dynamic der/3.",
        "% ---- composition rules comp(T1,T2,T3) ----",
    ]
    for t1, row in kin.composition_rules.items():
        for t2, t3 in row.items():
            lines.append(f"comp({_atom(t1)},{_atom(t2)},{_atom(t3)}).")
    lines.append("% ---- total converse conv(T,Tc) ----")
    for t, tc in kin._conv.items():
        lines.append(f"conv({_atom(t)},{_atom(tc)}).")
    lines.append("% ---- seed: extracted atomic edges seed(A,T,B) ----")
    seen = set()
    for e in edges:
        t = e["type"]
        a, b = e["a"], e["b"]
        if t not in kin.base or a == b:
            continue
        if (a, t, b) in seen:
            continue
        seen.add((a, t, b))
        lines.append(f"seed({_atom(a)},{_atom(t)},{_atom(b)}).")
    lines += [
        "% ---- add a directed edge + its converse (idempotent) ----",
        "add_edge(A,T,B) :- ( der(A,T,B) -> true ; assertz(der(A,T,B)) ),",
        "                   conv(T,Tc), ( der(B,Tc,A) -> true ; assertz(der(B,Tc,A)) ).",
        "init_seed :- forall(seed(A,T,B), add_edge(A,T,B)).",
        "% ---- batch forward-chaining to least fixpoint ----",
        "one_pass :- findall(d(A,T3,C),",
        "             ( der(A,T1,B), der(B,T2,C), comp(T1,T2,T3), \\+ der(A,T3,C) ), L0),",
        "           sort(L0, L), ( L == [] -> true",
        "             ; ( forall(member(d(A,T,C),L), add_edge(A,T,C)), one_pass ) ).",
        f"run :- init_seed, one_pass,",
        f"       ( setof(R, der({_atom(qsrc)},R,{_atom(qtgt)}), Rs) -> true ; Rs = [] ),",
        "       forall(member(R,Rs), (write('RESULT:'), write(R), nl)), halt.",
        ":- initialization(run).",
    ]
    return "\n".join(lines) + "\n"


def _parse_results(stdout: str):
    out = set()
    for ln in (stdout or "").splitlines():
        ln = ln.strip()
        if ln.startswith("RESULT:"):
            out.add(ln[len("RESULT:"):].strip())
    return sorted(out)


def discharge_fixpoint(kin, edges, qsrc, qtgt, engine_types, outpath: Path = None,
                       timeout: float = 25.0) -> dict:
    """Run the forward-closure program in swipl; cross-check vs the engine's type set."""
    program = emit_fixpoint_program(kin, edges, qsrc, qtgt)
    engine_types = sorted(set(engine_types))
    if outpath is not None:
        Path(outpath).write_text(program)
    swipl = shutil.which("swipl")
    if not swipl:
        return {"engine": "python-fallback", "executed_in_swipl": False,
                "note": "swipl unavailable; engine forward_closure is authoritative",
                "prolog_results": None, "engine_types": engine_types,
                "matches_engine": None, "program_chars": len(program),
                "program": program}
    tmp = None
    path = str(outpath) if outpath is not None else None
    if path is None:
        with tempfile.NamedTemporaryFile("w", suffix=".pl", delete=False) as fh:
            fh.write(program); path = fh.name; tmp = path
    try:
        proc = subprocess.run([swipl, "-q", "-g", "true", "-t", "halt", "-s", path],
                              capture_output=True, text=True, timeout=timeout)
        results = _parse_results(proc.stdout)
        executed = (proc.returncode == 0)
        return {"engine": "swipl-subprocess", "executed_in_swipl": executed,
                "prolog_results": results, "engine_types": engine_types,
                "matches_engine": (results == engine_types) if executed else None,
                "stdout_tail": (proc.stdout or "")[-400:], "stderr_tail": (proc.stderr or "")[-300:],
                "exit_code": proc.returncode, "program_chars": len(program), "program": program}
    except subprocess.TimeoutExpired:
        return {"engine": "swipl-subprocess", "executed_in_swipl": False, "prolog_results": None,
                "engine_types": engine_types, "matches_engine": None, "note": "timeout",
                "program_chars": len(program), "program": program}
    finally:
        if tmp:
            try:
                Path(tmp).unlink()
            except OSError:
                pass


if __name__ == "__main__":
    import glob
    import json
    from kinship import Kinship, query_modeA
    base = ("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/"
            "gen_art/gen_art_dataset_1/full_data_out")
    comp = json.load(open(sorted(glob.glob(base + "/full_data_out_*.json"))[0]))["metadata"]["composition_table"]
    kin = Kinship(comp)
    edges = [{"a": "Lena", "b": "Joshua", "type": "sibling"},
             {"a": "Joshua", "b": "Lynn", "type": "SO"},
             {"a": "Lynn", "b": "Andrea", "type": "child"}]
    out = query_modeA(kin, edges, "Lena", "Andrea")
    d = discharge_fixpoint(kin, edges, "Lena", "Andrea", out["types"])
    print("engine types:", out["types"])
    print("prolog:", d["prolog_results"], "matches_engine:", d["matches_engine"],
          "executed:", d["executed_in_swipl"])
