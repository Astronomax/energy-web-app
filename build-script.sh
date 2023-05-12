#!/bin/bash
pip install -r requirements.txt
printf 'db.create_all()\nquit()' | python3 -m flask shell
