#!/bin/sh

cp .env.sample .env

python3 -m venv venv
. venv/bin/activate

pip install -r requirements.txt
python server.py