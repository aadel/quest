#!/bin/bash

cd /app/api
pip install pipenv
pipenv install
pipenv run fastapi run main.py
