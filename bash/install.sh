#!/bin/bash


this_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$this_dir/.."

python3 -m venv .venv
source .venv/bin/activate
pip install -r bash/req.txt

deactivate
