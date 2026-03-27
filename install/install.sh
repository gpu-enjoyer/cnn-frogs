#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install -r install/req.txt

deactivate
