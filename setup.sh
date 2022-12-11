#!/bin/sh

git config --local core.hooksPath .githooks/

python3 -m venv venv

. ./venv/bin/activate

pip3 install -r requirements.txt

