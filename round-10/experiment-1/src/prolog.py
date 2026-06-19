#!/usr/bin/env python3
"""(iii) Human-auditable trace-graph discharged in ACTUAL SWI-Prolog.

For a solved query we emit a self-contained Prolog program:
  comp(T1,T2,T3).   % composition rules[t1][t2]=t3 (gender-agnostic types)
  conv(T,Tc).       % total converse over the 11 types
  rel(A,R,B).       % extracted atomic edges, asserted BOTH directions via conv/2
  solve_(A,B,R,Vis) % bounded transitive composition (visited-set => no infinite loops)
  run               % setof(R, solve(qsrc,qtgt,R), Rs) and print each derived R

DISCHARGE order (each labelled honestly in the output):
  1. pyswip   -- consult the .pl file and query run/0 in-process.
  2. subprocess -- `swipl -q -g run -t halt -s f.pl`, capture stdout/stderr/exit.
  3. python-checked -- if neither runs, compute the SAME simple-path derivation in
     Python and label it 'NOT executed in SWI-Prolog' (never implying execution).

`solve_paths` is the Python mirror of solve_/4 (identical algorithm) used both for the
honest fallback and as an exact cross-check that the Prolog engine agrees.
"""
from __future__ import annotations

import shutil
import subprocess
import tempfile
from collections import defaultdict
from pathlib import Path


def _atom(x) -> str:
    """Quote any token as a Prolog atom (names are Capitalized => must be quoted; types
    contain hyphens => must be quoted). Escape embedded quotes/backslashes."""
    s = str(x).replace("\\", "\\\\").replace("'", "\\'")
    return f"'{s}'"


def emit_program(kin, edges: list[dict], qsrc, qtgt) -> str:
    lines = [
        ":- style_check(-singleton).",
        "% ---- composition rules comp(T1,T2,T3) ----",
    ]
    for t1, row in kin.composition_rules.items():
        for t2, t3 in row.items():
            lines.append(f"comp({_atom(t1)},{_atom(t2)},{_atom(t3)}).")
    lines.append("% ---- total converse conv(T,Tc) ----")
    for t, tc in kin._conv.items():
        lines.append(f"conv({_atom(t)},{_atom(tc)}).")
    lines.append("% ---- extracted atomic edges rel(A,R,B) (both directions) ----")
    seen = set()
    for e in edges:
        t = e["type"]
        a, b = e["a"], e["b"]
        if t not in kin.base or a == b:
            continue
        f1 = (a, t, b)
        if f1 not in seen:
            seen.add(f1)
            lines.append(f"rel({_atom(a)},{_atom(t)},{_atom(b)}).")
        tc = kin.conv_type(t)
        f2 = (b, tc, a)
        if f2 not in seen:
            seen.add(f2)
            lines.append(f"rel({_atom(b)},{_atom(tc)},{_atom(a)}).")
    lines += [
        "% ---- bounded transitive composition ----",
        "solve(A,B,R) :- solve_(A,B,R,[A]).",
        "solve_(A,B,R,_) :- rel(A,R,B).",
        "solve_(A,B,R,Vis) :- rel(A,R1,M), \\+ member(M,Vis), "
        "solve_(M,B,R2,[M|Vis]), comp(R1,R2,R).",
        "run :- ( setof(R, solve(%s,%s,R), Rs) -> true ; Rs = [] ),"
        % (_atom(qsrc), _atom(qtgt)),
        "       forall(member(R,Rs), (write('RESULT:'), write(R), nl)).",
    ]
    return "\n".join(lines) + "\n"


def _parse_results(stdout: str) -> set:
    out = set()
    for ln in (stdout or "").splitlines():
        ln = ln.strip()
        if ln.startswith("RESULT:"):
            out.add(ln[len("RESULT:"):].strip())
    return out


def discharge_subprocess(program: str, timeout: float = 20.0) -> dict:
    swipl = shutil.which("swipl")
    if not swipl:
        return {"ok": False, "engine": None, "results": None, "stdout": "", "stderr": "swipl not found",
                "exit_code": None}
    with tempfile.NamedTemporaryFile("w", suffix=".pl", delete=False) as fh:
        fh.write(program)
        path = fh.name
    try:
        proc = subprocess.run([swipl, "-q", "-g", "run", "-t", "halt", "-s", path],
                              capture_output=True, text=True, timeout=timeout)
        res = _parse_results(proc.stdout)
        return {"ok": proc.returncode == 0, "engine": "subprocess", "results": sorted(res),
                "stdout": proc.stdout[-4000:], "stderr": proc.stderr[-2000:],
                "exit_code": proc.returncode}
    except subprocess.TimeoutExpired:
        return {"ok": False, "engine": "subprocess", "results": None, "stdout": "",
                "stderr": "timeout", "exit_code": None}
    finally:
        try:
            Path(path).unlink()
        except OSError:
            pass


def discharge_pyswip(program: str) -> dict:
    """Consult the program in-process and query run-like solve via pyswip."""
    try:
        from pyswip import Prolog
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "engine": None, "results": None, "error": f"pyswip import: {e}"}
    with tempfile.NamedTemporaryFile("w", suffix=".pl", delete=False) as fh:
        # pyswip shares one global engine; use a fresh module per call to avoid clashes
        fh.write(program)
        path = fh.name
    try:
        pl = Prolog()
        path_pl = path.replace("\\", "/")
        list(pl.query(f"consult('{path_pl}')"))
        # extract qsrc/qtgt from the program's run/0 goal
        rows = list(pl.query("forall(true,true)"))  # noop to ensure engine alive
        # re-run solve directly: parse the run goal target out of the program
        import re
        m = re.search(r"setof\(R, solve\('([^']*)','([^']*)',R\)", program)
        if not m:
            return {"ok": False, "engine": None, "results": None, "error": "no goal"}
        qsrc, qtgt = m.group(1), m.group(2)
        res = set()
        for sol in pl.query(f"solve('{qsrc}','{qtgt}',R)"):
            res.add(str(sol["R"]))
        return {"ok": True, "engine": "pyswip", "results": sorted(res)}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "engine": "pyswip", "results": None, "error": str(e)}
    finally:
        try:
            Path(path).unlink()
        except OSError:
            pass


def solve_paths(kin, edges: list[dict], qsrc, qtgt, max_depth: int = 14) -> set:
    """Python mirror of solve_/4: bounded simple-path right-fold composition over the
    directed rel-graph (both directions). Returns the set of derivable relation types."""
    rel = defaultdict(list)
    seen = set()
    for e in edges:
        t = e["type"]
        a, b = e["a"], e["b"]
        if t not in kin.base or a == b:
            continue
        if (a, t, b) not in seen:
            seen.add((a, t, b)); rel[a].append((t, b))
        tc = kin.conv_type(t)
        if (b, tc, a) not in seen:
            seen.add((b, tc, a)); rel[b].append((tc, a))

    def solve_(A, B, vis, depth):
        out = set()
        for (R, M) in rel.get(A, ()):
            if M == B:
                out.add(R)
        if depth >= max_depth:
            return out
        for (R1, M) in rel.get(A, ()):
            if M in vis:
                continue
            sub = solve_(M, B, vis | {M}, depth + 1)
            for R2 in sub:
                t3 = kin.compose_types(R1, R2)
                if t3 is not None:
                    out.add(t3)
        return out

    return solve_(qsrc, qtgt, {qsrc}, 0)


def discharge(kin, edges, qsrc, qtgt, prefer="subprocess") -> dict:
    """Discharge a query, trying real SWI-Prolog first, with an honest python fallback.
    Always returns the python-reference set for cross-checking."""
    program = emit_program(kin, edges, qsrc, qtgt)
    py_ref = sorted(solve_paths(kin, edges, qsrc, qtgt))
    order = ["subprocess", "pyswip"] if prefer == "subprocess" else ["pyswip", "subprocess"]
    record = None
    for eng in order:
        r = discharge_subprocess(program) if eng == "subprocess" else discharge_pyswip(program)
        if r.get("ok"):
            record = r
            break
        record = record or r
    if record and record.get("ok"):
        prolog_set = record["results"]
        return {"engine": record["engine"], "executed_in_swipl": True,
                "prolog_results": prolog_set, "python_reference": py_ref,
                "prolog_matches_python": (prolog_set == py_ref),
                "stdout_tail": record.get("stdout", "")[-800:],
                "stderr_tail": record.get("stderr", ""), "exit_code": record.get("exit_code"),
                "program_chars": len(program)}
    # neither real engine ran -> honest python-checked fallback
    return {"engine": "python-fallback", "executed_in_swipl": False,
            "note": "validated by a Python re-implementation of the Prolog rules, "
                    "NOT executed in SWI-Prolog",
            "prolog_results": None, "python_reference": py_ref,
            "prolog_matches_python": None, "program_chars": len(program),
            "last_error": (record or {}).get("stderr") or (record or {}).get("error")}


if __name__ == "__main__":
    import json, glob
    from kinship import Kinship, query_modeA
    base = ("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/"
            "gen_art/gen_art_dataset_1/full_data_out")
    comp = json.load(open(sorted(glob.glob(base + "/full_data_out_*.json"))[0]))["metadata"]["composition_table"]
    kin = Kinship(comp)
    edges = [{"a": "Lena", "b": "Joshua", "type": "sibling"},
             {"a": "Joshua", "b": "Lynn", "type": "SO"},
             {"a": "Lynn", "b": "Andrea", "type": "child"}]
    print("program:\n", emit_program(kin, edges, "Lena", "Andrea"))
    print("discharge:", json.dumps(discharge(kin, edges, "Lena", "Andrea"), indent=2)[:1500])
    print("engine Mode-A:", query_modeA(kin, edges, "Lena", "Andrea"))
