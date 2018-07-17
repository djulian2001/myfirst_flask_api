#!/bin/bash

mkdir -p "./section${1}/code"

cd "./section${1}"

/usr/local/bin/python3.6 -m venv venv

cat <<-EOF > requirements.txt
Flask
Flask-JWT
Flask-RESTful
Flask-SQLAlchemy
EOF

source "venv/bin/activate"

pip install --upgrade pip

pip install -r requirements.txt

# pip install Flask-SQLAlchemy

deactivate
