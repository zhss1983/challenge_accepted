#! /usr/bin/bash

python3 -m venv cenv
source cenv/bin/activate
python -m pip install --upgrade pip
pip install aiohttp getch

python division/run_client.py
