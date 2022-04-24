#!/bin/sh
. ./env/bin/activate
PORT=5000

# WEB APP
gunicorn -b 0.0.0.0:$PORT run:app -k gevent&
# With logging
# gunicorn -b 0.0.0.0:5000 run:app -k gevent 2>&1 | tee server_log.txt &

exit 0
