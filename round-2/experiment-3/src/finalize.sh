#!/bin/bash
# Wait for the in-flight full run to finish, then re-run on cache (adds applicability),
# regenerate mini/preview, and report. ONE notification when everything is ready.
set -u
cd /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_3
MYWS="iter_2/gen_art/gen_art_experiment_3"
getpid(){ for pid in $(pgrep -f "method.py" 2>/dev/null); do c=$(readlink /proc/$pid/cwd 2>/dev/null); m=$(tr '\0' ' ' </proc/$pid/cmdline 2>/dev/null); echo "$c"|grep -q "$MYWS" && echo "$m"|grep -q -- "--n-target" && { echo $pid; return; }; done; }

echo "FINALIZE: waiting for in-flight full run ..."
until [ -z "$(getpid)" ]; do sleep 15; done
echo "FINALIZE: full run ended $(date +%H:%M:%S). First-pass result:"
grep -E "VERDICT=" logs/full.out | tail -1

echo "FINALIZE: cached re-run (adds applicability field, \$0) ..."
uv run python method.py --n-target 300 --concurrency 16 > logs/rerun.out 2>&1
echo "FINALIZE: re-run exit=$? $(date +%H:%M:%S)"
grep -E "VERDICT=" logs/rerun.out | tail -1
tail -3 logs/rerun.out

echo "FINALIZE: generating mini/preview variants ..."
SKILL_DIR="/ai-inventor/.claude/skills/aii-json"
"$SKILL_DIR/../.ability_client_venv/bin/python" "$SKILL_DIR/scripts/aii_json_format_mini_preview.py" --input "$(pwd)/method_out.json" > logs/variants.out 2>&1
echo "FINALIZE: variant exit=$?"
tail -4 logs/variants.out
ls -la full_method_out.json mini_method_out.json preview_method_out.json method_out.json 2>/dev/null
echo "FINALIZE DONE $(date +%H:%M:%S)"
