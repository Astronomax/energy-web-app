#!/bin/bash
pip install pipenv
pipenv install -r requirements.txt
"db.create_all()\nquit()" | flask shell
