#!flask/bin/python

# Copyright 2020 AIR Institute
# See LICENSE for details.

from flask_restx import Api

api = Api(version='1.0',
          title='Twin api',
          description="**Twin project's Flask RESTX API**")