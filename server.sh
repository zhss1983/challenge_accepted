#! /usr/bin/bash

python3 -m venv senv
source senv/bin/activate
python -m pip install --upgrade pip
pip install aiohttp pygame

python async_matrix/run_server.py