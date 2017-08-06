#!/bin/sh
export FLASK_APP=$1
echo "File: $FLASK_APP"
flask run --host=0.0.0.0 --port=8000


