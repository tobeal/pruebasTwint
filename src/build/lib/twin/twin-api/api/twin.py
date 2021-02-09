#!flask/bin/python

# Copyright 2020 AIR Institute
# See LICENSE for details.

import datetime
from flask_restx import Resource

from twin import config
from twin.run import api
from twin.core import cache, limiter
from twin.utils import handle400error, handle404error, handle500error

from twin.twitter_extractor import twitterExtractor

twin_ns = api.namespace('twin', description='Obtain information from Twitter.')


@twin_ns.route('/tweets')
class GetTweets(Resource):
    @api.response(400, 'Invalid parameters')
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    def get(self):
        """
        Returns a JSON object with the historic information of the weather.
        Information is extracted from https://dev.meteostat.net/.
        If pagination info is not provided, all information is served.
        """

        try:
            json_data = twitterExtractor.test_twin_user_tweets(
                'BarackObama', 'es', 20)
        except:
            return handle500error(twin_ns)

        if not json_data:
            return handle404error(twin_ns, 'No data was found')

        return json_data
