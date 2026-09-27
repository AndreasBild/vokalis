#!/usr/bin/env bash
# ==============================================================================
# Vokalis Build & Validation Runner
# Executes all unit checks, JSON-LD schema audits, link & asset checks, and HTML5 a11y tests.
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
else
    echo "Error: Python 3 is required to run the validation suite." >&2
    exit 1
fi

chmod +x scripts/validate.py
"$PYTHON_BIN" scripts/validate.py "$@"
