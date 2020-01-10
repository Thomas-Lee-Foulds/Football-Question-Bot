import time
import sys
import tweepy
from urllib import request
from image_getter import get_media_url
from tweet_former import generate_tweet
from player_selector import get_names

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
    media_urls = []
    i = 0
    print("Getting the tweet:")
    player_names = get_names()
    for player in player_names:
        media_urls.append(get_media_url(player, GOOGLE_API,SEARCH_ENGINE_ID))
    
    for url in media_urls:
        request.urlretrieve(url, str(player_names[i]) + ".jpg")
        res = api.media_upload(str(player_names[i]) + ".jpg")
        media_ids.append(res.media_id)
        i += 1
    
    
    tweet = generate_tweet(player_names)
    api.update_status(status=tweet, media_ids=media_ids)
    media_urls = []
    media_ids = []
    time.sleep(INTERVAL)