import pytest
import twint
import datetime
import time


def test_twin_user_tweets():
    """
    Check tweets for user and save it into Jsonn format
    """
    c = twint.Config()
    tweets = {}
    c.Username = 'LMDShow'
    #Number of Tweets to pull (Increments of 20).

    c.lang = 'es'
    c.Store_object = True
    c.Store_json = tweets
    twint.run.Search(c)
    print(tweets)


def test_twin_user_tweets_last_week():
    """
    Check tweets for user and save it into Jsonn format
    """
    date = datetime.datetime.now()
    untilDate = date.strftime('%Y-%m-%d')
    sinceDate = (
        date +
        datetime.timedelta(-date.weekday(), weeks=-1)).strftime('%Y-%m-%d')
    c = twint.Config()
    tweets_last_week = {}
    c.Username = 'LMDShow'
    #Number of Tweets to pull (Increments of 20).

    c.lang = 'es'
    c.Since = sinceDate
    c.Until = untilDate
    c.Store_object = True
    c.Store_json = tweets_last_week
    twint.run.Search(c)
    print(tweets_last_week)


def test_twin_user_tweets_by_keyword():
    """
    Check tweets for user and save it into Jsonn format
    """
    c = twint.Config()
    tweets_keyword = {}
    c.Username = 'LMDShow'
    #Number of Tweets to pull (Increments of 20).

    c.lang = 'es'
    c.Search = 'jugar'
    c.Store_object = True
    c.Store_json = tweets_keyword
    twint.run.Search(c)
    print(tweets_keyword)


def test_twin_user_information():
    """
    Check tweets for user and save it into Jsonn format
    """
    c = twint.Config()
    bio = []
    c.Username = 'LMDShow'
    c.lang = 'es'
    c.Store_object = True
    c.Store_object_tweets_list = bio
    c.User_full = True
    twint.run.Lookup(c)
    print(bio)


if __name__ == '__main__':
    tic = time.perf_counter()
    test_twin_user_tweets()
    test_twin_user_tweets_last_week()
    test_twin_user_tweets_by_keyword()
    test_twin_user_information()
    toc = time.perf_counter()
    time = toc - tic
    print(time)