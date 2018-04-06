#!/bin/sh

websocketd --port 8443 --ssl --sslcert=/home/pimgeek/www/ssl/hintsnet-dev.cert --sslkey=/home/pimgeek/www/ssl/hintsnet-dev.key ws.py
