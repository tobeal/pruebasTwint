import pytest
import twint
import datetime
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def test_twin_user_tweets():
    """
    Get tweets for user and save it into Json format
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
    Get tweets of the last week for user and save it into Json format
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
    Get tweets by keyword for user and save it into Json format
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
    Get user info and save it into Json format
    """
    c = twint.Config()
    bio = []
    c.Username = 'LMDShow'
    c.lang = 'es'
    c.Store_object = True
    c.Store_object_tweets_list = bio
    c.User_full = True
    twint.run.Lookup(c)


def test_twin_user_tweets_min_likes(min_likes: int = 500):
    """
    Get tweets with at min likes define by user(default = 500) and save it into Json format
    Args:

        min_likes (:obj:`int`): the min_likes of user tweets.
    """
    c = twint.Config()
    tweets_min_likes = {}
    c.Username = 'LMDShow'
    c.lang = 'es'
    c.Store_object = True
    c.Store_json = tweets_min_likes
    c.Min_likes = min_likes
    twint.run.Search(c)


def test_twin_all_tweets_by_keyword():
    """
    Get user info and save it into Json format
    """
    c = twint.Config()
    tweets_by_keyword = {}
    c.Search = 'jugar'
    c.lang = 'es'
    c.Store_object = True
    c.Store_json = tweets_by_keyword
    twint.run.Search(c)


def test_twin_popular_tweets_last_week():
    """
    Get Popular tweets from the last week and save it into Json format
    """
    popular_tweets_last_week = {}
    date = datetime.datetime.now()
    untilDate = date.strftime('%Y-%m-%d')
    sinceDate = (
        date +
        datetime.timedelta(-date.weekday(), weeks=-1)).strftime('%Y-%m-%d')

    c = twint.Config()
    c.Popular_tweets = True
    c.lang = 'es'
    c.Limit = 20
    c.Since = sinceDate
    c.Until = untilDate
    c.Store_object = True
    c.Store_json = popular_tweets_last_week
    twint.run.Search(c)


if __name__ == '__main__':
    initTime = time.perf_counter()
    #save task to run into threadpool
    tasks = [
        test_twin_user_tweets, test_twin_user_tweets_last_week,
        test_twin_user_tweets_by_keyword, test_twin_user_information,
        test_twin_user_tweets_min_likes, test_twin_all_tweets_by_keyword,
        test_twin_popular_tweets_last_week
    ]
    #threadpool to execute the tasks
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = [executor.submit(t) for t in tasks]
        as_completed(tasks)

    endTime = time.perf_counter()
    time = initTime - endTime
    print(time)