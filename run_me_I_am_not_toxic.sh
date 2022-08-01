#! /usr/bin/bash

python3 -m venv env
. env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

python async_matrix/run_server.py & python division/division_client.py