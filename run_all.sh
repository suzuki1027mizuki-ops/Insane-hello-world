#!/usr/bin/env bash
# すべての Hello World を実行して出力を確かめ、ルール検査をかける。
set -u
cd "$(dirname "$0")"
PY="${PYTHON:-python}"
export PYTHONIOENCODING=utf-8
status=0

for f in hello/*.py; do
  out="$("$PY" "$f" 2>&1 | tr -d '\r')"
  if [ "$out" = "hello world" ]; then
    echo "PASS  $f"
  else
    echo "FAIL  $f -> $out"
    status=1
  fi
done

echo
ls hello/*.py | "$PY" tools/check_rules.py || status=1
exit $status
