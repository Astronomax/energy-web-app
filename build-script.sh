#!/bin/bash
pip install pipenv
pipenv install -r requirements.txt
flask shell
db.create_all()
quit()
