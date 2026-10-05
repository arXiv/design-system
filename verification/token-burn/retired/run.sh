#!/usr/bin/env bash
# Token-burn test runner for the arXiv design-system repo.
#
# Each run: copies the repo (minus tests/ and .git) into a clean temp
# workspace, runs a headless Claude agent on one task prompt inside it,
# captures the full transcript, diffs the workspace to collect artifacts,
# computes metrics, and generates a designer review page.
#
# Usage:
#   bash verification/token-burn/run.sh                 # full battery: all tasks × 2 reps
#   bash verification/token-burn/run.sh --task 03       # one task only
#   bash verification/token-burn/run.sh --reps 1        # override repetitions
#   bash verification/token-burn/run.sh --smoke         # cheap plumbing check (no build)
#   bash verification/token-burn/run.sh --variant digest --repo-dir path/  # test an
#       alternate repo structure (defaults to this repo, variant "baseline")
set -uo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$HERE/../.." && pwd)"
# Pinned (not the "sonnet" alias) so runs stay comparable across the
# pre-/post-reorg baselines even if the CLI's alias moves to a newer Sonnet.
MODEL="claude-sonnet-4-6"; REPS=2; TASK_FILTER=""; VARIANT="baseline"; SMOKE=0
SRC_DIR="$REPO_ROOT"

while [[ $# -gt 0 ]]; do case "$1" in
  --task)     TASK_FILTER="$2"; shift 2;;
  --reps)     REPS="$2"; shift 2;;
  --variant)  VARIANT="$2"; shift 2;;
  --model)    MODEL="$2"; shift 2;;
  --repo-dir) SRC_DIR="$(cd "$2" && pwd)"; shift 2;;
  --smoke)    SMOKE=1; shift;;
  *) echo "unknown arg: $1" >&2; exit 1;;
esac; done

STAMP="$(date +%Y%m%d-%H%M%S)"
RUN_DIR="$HERE/runs/$STAMP-$VARIANT"
mkdir -p "$RUN_DIR"
LOG="$RUN_DIR/run.log"
say() { echo "[$(date +%H:%M:%S)] $*" | tee -a "$LOG"; }

if [[ $SMOKE -eq 1 ]]; then
  TASKS=("$HERE/smoke/smoke.md"); REPS=1
elif [[ -n "$TASK_FILTER" ]]; then
  TASKS=("$HERE"/tasks/"$TASK_FILTER"*.md)
else
  TASKS=("$HERE"/tasks/*.md)
fi

say "run: variant=$VARIANT model=$MODEL reps=$REPS tasks=${#TASKS[@]} src=$SRC_DIR"

for task in "${TASKS[@]}"; do
  name="$(basename "$task" .md)"
  for rep in $(seq 1 "$REPS"); do
    cell="$RUN_DIR/$name-r$rep"
    mkdir -p "$cell"
    ws="$(mktemp -d "${TMPDIR:-/tmp}/tokenburn-XXXXXX")"
    say "start $name rep $rep  (workspace $ws)"
    rsync -a --exclude '.git' --exclude 'verification' --exclude 'planning' --exclude 'node_modules' \
      "$SRC_DIR/" "$ws/repo/"
    cp -a "$ws/repo" "$ws/pristine"

    # Scrub host-session env (base-URL overrides, OAuth flags, nested-session
    # markers) so the child CLI authenticates exactly like a fresh terminal
    # `claude` using the user's own stored credentials.
    SCRUB=()
    while IFS= read -r var; do SCRUB+=("-u" "$var"); done < <(
      env | grep -iE '^(CLAUDE|ANTHROPIC|USE_(STAGING|LOCAL)_OAUTH|AI_AGENT|BAGGAGE)' | cut -d= -f1)
    start_ts=$(date +%s)
    ( cd "$ws/repo" && env "${SCRUB[@]}" claude -p "$(cat "$task")" \
        --model "$MODEL" \
        --permission-mode bypassPermissions \
        --output-format stream-json --verbose \
        > "$cell/transcript.jsonl" 2> "$cell/stderr.log" )
    status=$?
    end_ts=$(date +%s)
    echo "{\"exit\": $status, \"wall_seconds\": $((end_ts - start_ts))}" > "$cell/run-info.json"
    [[ $status -ne 0 ]] && say "WARNING: $name rep $rep exited $status (see stderr.log)"

    python3 "$HERE/report.py" collect "$cell" "$ws" "$task" >> "$LOG" 2>&1 \
      || say "WARNING: collect failed for $name rep $rep"
    rm -rf "$ws"
    say "done  $name rep $rep  ($((end_ts - start_ts))s)"
  done
done

python3 "$HERE/report.py" textpass "$RUN_DIR" >> "$LOG" 2>&1 \
  || say "WARNING: text pass failed (review page will show raw messages)"
python3 "$HERE/report.py" report "$RUN_DIR" >> "$LOG" 2>&1
python3 "$HERE/report.py" index "$HERE/runs" >> "$LOG" 2>&1
say "review page: $RUN_DIR/review.html"
