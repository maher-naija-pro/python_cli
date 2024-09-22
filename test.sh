#!/bin/bash
[[ -d venv ]] && source  venv/bin/activate
rm -rf ~/.nd
python -m pytest -l -vvv --cache-clear  --color yes --code-highlight yes  --new-first   tests

