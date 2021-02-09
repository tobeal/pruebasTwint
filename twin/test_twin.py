import pytest
import twint
import datetime
import time
from twitter_extractor import twitterExtractor
from concurrent.futures import ThreadPoolExecutor, as_completed


def test_twin_user_tweets(username: str = 'BarackObama',
                          lang: str = 'es',
                          limit: int = 20):
    """
    Get tweets for user and save it into Json format
    Args:
        username(:obj:`str`): the username used for searching tweets
        lang(:obj:`str`): the language used
        limit(:obj:`int`): number of Tweets to pull (Increments of 20).
    """
    twitter = twitterExtractor()

    result = twitter.test_twin_user_tweets(username, lang, limit)
    return result


def test_twin_user_tweets_last_week(username: str = 'BarackObama',
                                    lang: str = 'es',
                                    limit: int = 20):
    """
    Get tweets of the last week for user and save it into Json format
    Args:
        username(:obj:`str`): the username used for searching tweets
        lang(:obj:`str`): the language used
        limit(:obj:`int`): number of Tweets to pull (Increments of 20).
    """
    twitter = twitterExtractor()

    result = twitter.test_twin_user_tweets_last_week(username, lang, limit)
    return result


def test_twin_user_tweets_by_keyword(keyword: str = '#BarackObama',
                                     username: str = 'BarackObama',
                                     lang: str = 'es',
                                     limit: int = 20):
    """
    Get tweets by keyword for user and save it into Json format
    Args:
        keyword(:obj:`str`): the keyword used for searching tweets
        username(:obj:`str`): the username used for searching tweets
        lang(:obj:`str`): the language used
        limit(:obj:`int`): number of Tweets to pull (Increments of 20).
    """
    twitter = twitterExtractor()
    result = twitter.test_twin_user_tweets_by_keyword(keyword, username, lang,
                                                      limit)
    return result


def test_twin_user_information(username: str = 'BarackObama',
                               lang: str = 'es',
                               limit: int = 20):
    """
    Get user info and save it into Json format
    Args:
        username(:obj:`str`): the username used for searching tweets
        lang(:obj:`str`): the language used
        limit(:obj:`int`): number of Tweets to pull (Increments of 20).
    """
    twitter = twitterExtractor()

    result = twitter.test_twin_user_information(username, lang, limit)
    return result


def test_twin_user_tweets_min_likes(min_likes: int = 20,
                                    username: str = 'BarackObama',
                                    lang: str = 'es',
                                    limit: int = 20):
    """
    Get tweets with at min likes define by user and save it into Json format
    Args:
        username(:obj:`str`): the username used for searching tweets
        lang(:obj:`str`): the language used
        limit(:obj:`int`): number of Tweets to pull (Increments of 20).
        min_likes (:obj:`int`): the min_likes of user tweets.
    """
    twitter = twitterExtractor()

    result = twitter.test_twin_user_tweets_min_likes(min_likes, username, lang,
                                                     limit)
    return result


def test_twin_all_tweets_by_keyword(keyword: str = '#BarackObama',
                                    lang: str = 'es',
                                    limit: int = 20):
    """
    Get tweet from a keyword, could be a hashtag and save it into Json format
    Args:
        keyword(:obj:`str`): the keyword used for searching tweets
        lang(:obj:`str`): the language used
        limit(:obj:`int`): number of Tweets to pull (Increments of 20).
    """
    twitter = twitterExtractor()

    result = twitter.test_twin_all_tweets_by_keyword(keyword, lang, limit)
    return result


"""

def test_twin_popular_tweets_last_week(lang: str = 'es',
                                    limit: int = 20):

   # Get Popular tweets from the last week and save it into Json format
    Args:
        lang(:obj:`str`): the language used
        limit(:obj:`int`): number of Tweets to pull (Increments of 20).

    twitter = twitterExtractor()

    twitter.test_twin_popular_tweets_last_week(lang, limit)
"""

if __name__ == '__main__':

    test_twin_user_tweets()
    test_twin_user_tweets_last_week()
    test_twin_user_tweets_by_keyword()
    test_twin_user_information()
    test_twin_user_tweets_min_likes()
    test_twin_all_tweets_by_keyword()
    #test_twin_popular_tweets_last_week()
