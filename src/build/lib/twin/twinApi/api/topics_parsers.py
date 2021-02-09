#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from flask_restx import reqparse

twint_argument_parser = reqparse.RequestParser()

twint_argument_parser.add_argument(
    'username',
    location='args',
    type=str,
    required=True,
    default=None,
    help='The username to make the tweets search')

twint_argument_parser.add_argument('keyword',
                                   location='args',
                                   type=str,
                                   required=True,
                                   default=None,
                                   help='The keyword to make tweets search')

twint_argument_parser.add_argument('limit',
                                  location='args',
                                  type=int,
                                  required=False,
                                  default=None,
                                  help='Numbers of tweets to retrieve.')

twint_argument_parser.add_argument(
    'lang',
    location='args',
    type=str,
    required=False,
    default=None,
    help=
    "Language of the tweet to retrieve. The language must be ISO coded. For example, English code would be 'en'."
)
