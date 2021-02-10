#!flask/bin/python

# Copyright 2021 BISITE Research Group
# See LICENSE for details.

import datetime
from flask_restx import Resource
import json
from twin import config
from twin.run import api
from twin.core import cache, limiter
from twin.twinApi.api.twint_parsers import twint_argument_parser
from twin.utils import handle400error, handle404error, handle500error

from twin.twitter_extractor import twitterExtractor

twin_ns = api.namespace('twin', description='Obtain information from Twitter.')


@twin_ns.route('/user/tweets')
class GetUserTweets(Resource):
    @api.response(400, 'Invalid parameters')
    @api.expect(twint_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    def get(self):

        try:
            args = twint_argument_parser.parse_args()
            username = args['username']
            lang = args['lang']
            limit = args['limit']

            twin_extractor = twitterExtractor()
            json_data = twin_extractor.test_twin_user_tweets(
                username, lang, limit)
        except:
            return handle500error(twin_ns)

        if not json_data:
            return handle404error(twin_ns, 'No data was found')

        return json_data


@twin_ns.route('/user/tweets_last_week')
class GetUserTweetsLastWeek(Resource):
    @api.response(400, 'Invalid parameters')
    @api.expect(twint_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    def get(self):

        try:
            args = twint_argument_parser.parse_args()
            username = args['username']
            lang = args['lang']
            limit = args['limit']
            twin_extractor = twitterExtractor()
            json_data = twin_extractor.test_twin_user_tweets_last_week(
                username, lang, limit)
        except:
            return handle500error(twin_ns)

        if not json_data:
            return handle404error(twin_ns, 'No data was found')

        return json_data


@twin_ns.route('/user/keyword_tweets')
class GetUserKeywordTweets(Resource):
    @api.response(400, 'Invalid parameters')
    @api.expect(twint_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    def get(self):

        try:
            args = twint_argument_parser.parse_args()
            keyword = args['keyword']
            lang = args['lang']
            limit = args['limit']
            twin_extractor = twitterExtractor()
            json_data = twin_extractor.test_twin_user_tweets_by_keyword(
                '#BarackObama', 'BarackObama', 'es', 20)
        except:
            return handle500error(twin_ns)

        if not json_data:
            return handle404error(twin_ns, 'No data was found')

        return json_data


@twin_ns.route('/user/information')
class GetUserInformation(Resource):
    @api.response(400, 'Invalid parameters')
    @api.expect(twint_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    def get(self):

        try:
            args = twint_argument_parser.parse_args()
            username = args['username']
            lang = args['lang']
            limit = args['limit']
            twin_extractor = twitterExtractor()
            json_data = twin_extractor.test_twin_user_information(
                username, lang, limit)
        except:
            return handle500error(twin_ns)

        if not json_data:
            return handle404error(twin_ns, 'No data was found')

        return json_data


@twin_ns.route('/user/min_likes_tweets')
class GetUserMinLikesTweets(Resource):
    @api.response(400, 'Invalid parameters')
    @api.expect(twint_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    def get(self):

        try:
            args = twint_argument_parser.parse_args()
            username = args['username']
            minimum_likes = args['likes']
            lang = args['lang']
            limit = args['limit']
            twin_extractor = twitterExtractor()
            json_data = twin_extractor.test_twin_user_tweets_min_likes(
                minimum_likes, username, lang, limit)
        except:
            return handle500error(twin_ns)

        if not json_data:
            return handle404error(twin_ns, 'No data was found')

        return json_data


@twin_ns.route('/all/tweets_by_date')
class GetTweetsByDateAndKeyword(Resource):
    @api.response(400, 'Invalid parameters')
    @api.expect(twint_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    def get(self):

        try:
            args = twint_argument_parser.parse_args()
            username = args['username']
            keyword = args['keyword']
            from_date = args['from_date']
            to_date = args['to_date']
            lang = args['lang']
            limit = args['limit']
            twin_extractor = twitterExtractor()
            json_data = twin_extractor.test_twin_user_tweets_by_date(
                username, keyword, lang, limit, from_date, to_date)
        except:
            return handle500error(twin_ns)

        if not json_data:
            return handle404error(twin_ns, 'No data was found')

        return json_data


@twin_ns.route('/all/keyword_tweets')
class GetAllKeywordTweets(Resource):
    @api.response(400, 'Invalid parameters')
    @api.expect(twint_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    def get(self):

        try:
            args = twint_argument_parser.parse_args()
            keyword = args['keyword']
            lang = args['lang']
            limit = args['limit']
            twin_extractor = twitterExtractor()
            json_data = twin_extractor.test_twin_all_tweets_by_keyword(
                keyword, lang, limit)
        except:
            return handle500error(twin_ns)

        if not json_data:
            return handle404error(twin_ns, 'No data was found')

        return json_data