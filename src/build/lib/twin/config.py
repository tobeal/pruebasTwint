#!flask/bin/python

# Copyright 2021 BISITE Research Group
# See LICENSE for details..

import os

# api config
PORT = 5000
HOST = '0.0.0.0'
URL_PREFIX = '/twin/v1'
DEBUG_MODE = True
USE_HTTPS = not DEBUG_MODE
SSL_KEY = './certs/server.key'
SSL_CERT = './certs/server.crt'

