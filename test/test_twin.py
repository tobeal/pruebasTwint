import pytest
import twint
import datetime
import time
from twitter_extractor import twitterExtractor
from concurrent.futures import ThreadPoolExecutor, as_completed


def test_twin_user_tweets():
    """
    Get tweets for user and save it into Json format
    """
    twitter = twitterExtractor()

    twitter.test_twin_user_tweets('tobeal96', 'es', 20)


def test_twin_user_tweets_last_week():
    """
    Get tweets of the last week for user and save it into Json format
    """
    twitter = twitterExtractor()

    twitter.test_twin_user_tweets_last_week('tobeal96', 'es', 20)


def test_twin_user_tweets_by_keyword():
    """
    Get tweets by keyword for user and save it into Json format
    """
    twitter = twitterExtractor()
    twitter.test_twin_user_tweets_by_keyword('video', 'tobeal96', 'es', 20)


def test_twin_user_information():
    """
    Get user info and save it into Json format
    """
    twitter = twitterExtractor()

    twitter.test_twin_user_information('tobeal96', 'es', 20)


def test_twin_user_tweets_min_likes(min_likes: int = 500):
    """
    Get tweets with at min likes define by user(default = 500) and save it into Json format
    Args:

    min_likes (:obj:`int`): the min_likes of user tweets.
    """
    twitter = twitterExtractor()

    twitter.test_twin_user_tweets_min_likes(500, 'tobeal96', 'es', 20)


def test_twin_all_tweets_by_keyword():
    """
    Get user info and save it into Json format
    """
    twitter = twitterExtractor()

    twitter.test_twin_all_tweets_by_keyword('jugar', 'es', 20)


"""

def test_twin_popular_tweets_last_week():

   # Get Popular tweets from the last week and save it into Json format

    twitter = twitterExtractor()

    twitter.test_twin_popular_tweets_last_week('es', 20)
"""

if __name__ == '__main__':
    test_twin_user_tweets()
    test_twin_user_tweets_last_week()
    test_twin_user_tweets_by_keyword()
    test_twin_user_information()
    test_twin_user_tweets_min_likes()
    test_twin_all_tweets_by_keyword()
    #test_twin_popular_tweets_last_week()
