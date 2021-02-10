#!usr/bin/python

# Copyright 2021 BISITE Research Group
# See LICENSE for details.
import pytest
import twint
import datetime
import time
import json


class twitterExtractor:
    """

    Extracts data from TWITTER by twin = https://github.com/twintproject/twint
    """
    def test_twin_user_tweets(self, username: str, lang: str, limit: int):
        """
        Get tweets for user and save it into Json format
        Args:
            username(:obj:`str`): the username used for searching tweets
            lang(:obj:`str`): the language used
            limit(:obj:`int`): number of Tweets to pull (Increments of 20).
        """
        c = twint.Config()
        c.Username = username
        tweets = {}
        #Number of Tweets to pull (Increments of 20).
        c.Limit = limit
        c.lang = lang
        c.Pandas = True
        twint.run.Search(c)
        Tweets_df = twint.storage.panda.Tweets_df
        return Tweets_df.to_dict(orient='records')

    def test_twin_user_tweets_last_week(self, username: str, lang: str,
                                        limit: int):
        """
        Get tweets of the last week for user and save it into Json format
        Args:
            username(:obj:`str`): the username used for searching tweets
            lang(:obj:`str`): the language used
            limit(:obj:`int`): number of Tweets to pull (Increments of 20).
        """
        date = datetime.datetime.now()
        untilDate = date.strftime('%Y-%m-%d')
        sinceDate = (
            date +
            datetime.timedelta(-date.weekday(), weeks=-1)).strftime('%Y-%m-%d')
        c = twint.Config()
        c.Username = username
        #Number of Tweets to pull (Increments of 20).
        c.Limit = limit
        c.lang = lang
        c.Since = sinceDate
        c.Until = untilDate
        c.Pandas = True
        twint.run.Search(c)
        Tweets_df = twint.storage.panda.Tweets_df
        return Tweets_df.to_dict(orient='records')

    def test_twin_user_tweets_by_date(self, username: str, keyword: str,
                                      lang: str, limit: int, from_date: str,
                                      to_date: str):
        """
        Get tweets of the specific date for user and save it into Json format
        Args:
            username(:obj:`str`): the username used for searching tweets
            keyword(:obj:`str`): the keyword used for searching tweets
            lang(:obj:`str`): the language used
            limit(:obj:`int`): number of Tweets to pull (Increments of 20).
            from_date(:obj:`str`): Start date to seacrh tweets.
            to_date(:obj:`str`): End date to saerch tweets.
        """
        date = datetime.datetime.now()
        untilDate = date.strftime('%Y-%m-%d')
        sinceDate = (
            date +
            datetime.timedelta(-date.weekday(), weeks=-1)).strftime('%Y-%m-%d')
        c = twint.Config()
        c.Username = username
        #Number of Tweets to pull (Increments of 20).
        c.Limit = limit
        c.lang = lang
        c.Search = keyword
        c.Since = from_date
        c.Until = to_date
        c.Pandas = True
        twint.run.Search(c)
        Tweets_df = twint.storage.panda.Tweets_df
        return Tweets_df.to_dict(orient='records')

    def test_twin_all_tweets_by_date(self, keyword: str, lang: str, limit: int,
                                     from_date: str, to_date: str):
        """
        Get tweets of the specific date for all and save it into Json format
        Args:
            keyword(:obj:`str`): the keyword used for searching tweets
            lang(:obj:`str`): the language used
            limit(:obj:`int`): number of Tweets to pull (Increments of 20).
            from_date(:obj:`str`): Start date to seacrh tweets.
            to_date(:obj:`str`): End date to saerch tweets.
        """
        c = twint.Config()
        c.Search = keyword
        #Number of Tweets to pull (Increments of 20).
        c.Limit = limit
        c.lang = lang
        c.Since = from_date
        c.Until = to_date
        c.Pandas = True
        twint.run.Search(c)
        Tweets_df = twint.storage.panda.Tweets_df
        return Tweets_df.to_dict(orient='records')

    def test_twin_user_tweets_by_keyword(self, keyword: str, username: str,
                                         lang: str, limit: int):
        """
        Get tweets by keyword for user and save it into Json format
        Args:
            username(:obj:`str`): the username used for searching tweets
            keyword(:obj:`str`): the keyword used for searching tweets
            lang(:obj:`str`): the language used
            limit(:obj:`int`): number of Tweets to pull (Increments of 20).
        """
        c = twint.Config()
        c.Username = username
        #Number of Tweets to pull (Increments of 20).
        c.Limit = limit
        c.lang = lang
        c.Search = keyword
        c.Pandas = True
        twint.run.Search(c)
        Tweets_df = twint.storage.panda.Tweets_df
        return Tweets_df.to_dict(orient='records')

    def test_twin_user_information(self, username: str, lang: str, limit: int):
        """
        Get user info and save it into Json format
        Args:
            username(:obj:`str`): the username used for searching tweets
            lang(:obj:`str`): the language used
            limit(:obj:`int`): number of Tweets to pull (Increments of 20).
        """
        c = twint.Config()
        c.Limit = limit
        c.Username = username
        c.lang = lang
        c.Pandas = True
        c.User_full = True
        twint.run.Lookup(c)
        User_df = twint.storage.panda.User_df
        return User_df.to_dict(orient='records')

    def test_twin_user_tweets_min_likes(self, min_likes: int, username: str,
                                        lang: str, limit: int):
        """
        Get tweets with at min likes define by user(default = 500) and save it into Json format
        Args:

            min_likes (:obj:`int`): the min_likes of user tweets.
            username(:obj:`str`): the username used for searching tweets
            lang(:obj:`str`): the language used
            limit(:obj:`int`): number of Tweets to pull (Increments of 20).
        """
        c = twint.Config()
        c.Limit = limit
        c.Username = username
        c.lang = lang
        c.Pandas = True
        c.Min_likes = min_likes
        twint.run.Search(c)
        Tweets_df = twint.storage.panda.Tweets_df
        return Tweets_df.to_dict(orient='records')

    def test_twin_all_tweets_by_keyword(self, keyword: str, lang: str,
                                        limit: int):
        """
        Get user info and save it into Json format
        Args:
            keyword(:obj:`str`): the keyword used for searching tweets
            lang(:obj:`str`): the language used
            limit(:obj:`int`): number of Tweets to pull (Increments of 20).
        """
        c = twint.Config()
        c.Limit = limit
        c.Search = keyword
        c.lang = lang
        c.Pandas = True
        twint.run.Search(c)
        Tweets_df = twint.storage.panda.Tweets_df
        return Tweets_df.to_dict(orient='records')


"""
    def test_twin_popular_tweets_last_week(self, lang: str, limit: int):

        Get Popular tweets from the last week and save it into Json format
        Args:
            username(:obj:`str`): the username used for searching tweets
            lang(:obj:`str`): the language used
            limit(:obj:`int`): number of Tweets to pull (Increments of 20).

        popular_tweets_last_week = {}
        date = datetime.datetime.now()
        untilDate = date.strftime('%Y-%m-%d')
        sinceDate = (
            date +
            datetime.timedelta(-date.weekday(), weeks=-1)).strftime('%Y-%m-%d')

        c = twint.Config()
        c.Popular_tweets = True
        c.lang = lang
        c.Limit = limit
        c.Since = sinceDate
        c.Until = untilDate
        c.Store_object = True
        c.Store_json = popular_tweets_last_week
        twint.run.Search(c)
"""