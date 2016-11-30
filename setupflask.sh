#!/bin/bash
# Andrew Berg CEN4020 Leadboards Just My Type
echo Setting up flask
sudo pip install --upgrade pip setuptools
sudo pip install virtualenv
virtualenv flask
source ./flask/bin/activate
pip install flask
python createdb.py
python leaderboards.py