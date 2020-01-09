import time
import sys
import tweepy
from urllib import request
from image_getter import get_media_url
from tweet_former import generate_tweet
from player_selector import get_unique_name

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
GOOGLE_API = environ['GOOGLE_API']
SEARCH_ENGINE_ID = environ['SEARCH_ENGINE_ID']

INTERVAL = 60 * 60
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    
    media_ids = []
    print("Getting the tweet:")
    player_1 = get_unique_name()
    player_2 = get_unique_name()
    media_url_1 = get_media_url(player_1, GOOGLE_API,SEARCH_ENGINE_ID)
    media_url_2 = get_media_url(player_2, GOOGLE_API,SEARCH_ENGINE_ID)
    
    request.urlretrieve(media_url_1, str(player_1) + ".jpg")
    res = api.media_upload(str(player_1) + ".jpg")
    media_ids.append(res.media_id)
    
    request.urlretrieve(media_url_2, str(player_2) + ".jpg")
    res = api.media_upload(str(player_2) + ".jpg")
    media_ids.append(res.media_id)

    tweet = generate_tweet(player_1,player_2)
    api.update_status(status=tweet, media_ids=media_ids)
    media_urls = []
    media_ids = []
    time.sleep(INTERVAL)