import pytest
import twint
import datetime
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def test_twin_user_tweets():
    """
    Check tweets for user and save it into Jsonn format
    """
    c = twint.Config()
    tweets = {}
    c.Username = 'LMDShow'
    #Number of Tweets to pull (Increments of 20).
    #c.Limit = 20

    c.lang = 'es'
    c.Store_object = True
    c.Store_json = tweets
    twint.run.Search(c)


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
    #c.Limit = 20
    c.lang = 'es'
    c.Since = sinceDate
    c.Until = untilDate
    c.Store_object = True
    c.Store_json = tweets_last_week
    twint.run.Search(c)


def test_twin_user_tweets_by_keyword():
    """
    Check tweets for user and save it into Jsonn format
    """
    c = twint.Config()
    tweets_keyword = {}
    c.Username = 'LMDShow'
    #Number of Tweets to pull (Increments of 20).
    #c.Limit = 20

    c.lang = 'es'
    c.Search = 'jugar'
    c.Store_object = True
    c.Store_json = tweets_keyword
    twint.run.Search(c)


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


if __name__ == '__main__':
    initTime = time.perf_counter()
    tasks = [
        test_twin_user_tweets, test_twin_user_tweets_last_week,
        test_twin_user_tweets_by_keyword, test_twin_user_information
    ]

    with ThreadPoolExecutor(max_workers=1) as executor:
        tasks = [executor.submit(t) for t in tasks]
        as_completed(tasks)

    endTime = time.perf_counter()
    time = initTime - endTime
    print(time)