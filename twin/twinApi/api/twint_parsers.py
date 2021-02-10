#!flask/bin/python

# Copyright 2021 BISITE Research Group
# See LICENSE for details.

from flask_restx import reqparse

twint_argument_parser = reqparse.RequestParser()

twint_argument_parser.add_argument(
    'username',
    location='args',
    type=str,
    required=False,
    default=None,
    help='The username to make the tweets search')

twint_argument_parser.add_argument('keyword',
                                   location='args',
                                   type=str,
                                   required=False,
                                   default=None,
                                   help='The keyword to make tweets search')

twint_argument_parser.add_argument(
    'limit',
    location='args',
    type=int,
    required=False,
    default=20,
    help='Number of Tweets to pull (Increments of 20)..')
twint_argument_parser.add_argument('likes',
                                   location='args',
                                   type=int,
                                   required=False,
                                   default=50,
                                   help='Number of Minimum likes ')
twint_argument_parser.add_argument(
    'lang',
    location='args',
    type=str,
    required=True,
    default=None,
    help=
    "Language of the tweet to retrieve. The language must be ISO coded. For example, English code would be 'en'."
)
twint_argument_parser.add_argument(
    'from_date',
    location='args',
    type=str,
    required=False,
    default=None,
    help=
    'The start date to retrieve tweets from. The date must be in ISO 8601 format YYYY-mm-dd.'
)

twint_argument_parser.add_argument(
    'to_date',
    location='args',
    type=str,
    required=False,
    default=None,
    help=
    'The end date to retrieve tweets from. The date must be in ISO 8601 format YYYY-mm-dd.'
)