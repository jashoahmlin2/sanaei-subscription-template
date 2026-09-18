#!/usr/bin/env bash
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FILE="$ROOT/index.html"
[[ -s "$FILE" ]] || { echo 'FAIL: index.html missing or empty'; exit 1; }
grep -q '<!doctype html>' "$FILE" || { echo 'FAIL: doctype missing'; exit 1; }
grep -q '{{.subUrl}}' "$FILE" || { echo 'FAIL: subUrl variable missing'; exit 1; }
grep -q '{{range \$i, \$link := .links}}' "$FILE" || { echo 'FAIL: links range missing'; exit 1; }
grep -q 'format=info' "$FILE" || { echo 'FAIL: live status endpoint missing'; exit 1; }
if command -v go >/dev/null 2>&1; then
  TMP="$(mktemp -d)"
  trap 'rm -rf "$TMP"' EXIT
  cat > "$TMP/check.go" <<'GO'
package main
import("html/template";"os")
func main(){ _,err:=template.ParseFiles(os.Args[1]); if err!=nil { panic(err) } }
GO
  go run "$TMP/check.go" "$FILE"
fi
echo 'PASS: HTML and Go template checks passed.'
