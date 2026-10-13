#!/usr/bin/env bash
# The repo quality gate. The global pre-commit hook runs it before every commit.
# Bypass one commit with --no-verify.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
python3 -m unittest discover -s tests -q
