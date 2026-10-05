#!/usr/bin/env bash
# Render the CV page to files/cv.pdf with headless Chrome, using the print styles
# in _sass/_print.scss. The site must already be served, e.g. with:
#   bundle exec jekyll serve --config _config.yml,_config.dev.yml
# Usage: scripts/cv-pdf.sh [url]   (default: http://localhost:4000/cv/)
set -euo pipefail

URL="${1:-http://localhost:4000/cv/}"
OUT="$(cd "$(dirname "$0")/.." && pwd)/files/cv.pdf"

CHROME="${CHROME:-}"
if [ -z "$CHROME" ]; then
  for c in google-chrome google-chrome-stable chromium chromium-browser \
           "/c/Program Files/Google/Chrome/Application/chrome.exe" \
           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
    if command -v "$c" >/dev/null 2>&1 || [ -x "$c" ]; then CHROME="$c"; break; fi
  done
fi
[ -n "$CHROME" ] || { echo "Chrome not found; set CHROME=/path/to/chrome" >&2; exit 1; }

# Windows Chrome needs a Windows-style output path
OUT_ARG="$OUT"
if command -v cygpath >/dev/null 2>&1; then OUT_ARG="$(cygpath -w "$OUT")"; fi

"$CHROME" --headless=new --disable-gpu --no-sandbox \
  --no-pdf-header-footer \
  --run-all-compositor-stages-before-draw --virtual-time-budget=10000 \
  --print-to-pdf="$OUT_ARG" "$URL" 2>/dev/null

echo "Wrote $OUT"
