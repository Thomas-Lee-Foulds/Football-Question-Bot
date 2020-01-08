import time
import sys
import tweepy
import requests
from image_getter import get_media_url
from tweet_former import generate_tweet
from player_selector import get_unique_name

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

INTERVAL = 60 * 60 * 3

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    
    media_ids = []
   
    print("Getting the tweet:")
    player_1 = get_unique_name()
    print(player_1)
    player_2 = get_unique_name()
    print(player_2)
    media_url_1 = get_media_url(player_1)
    media_url_2 = get_media_url(player_2)
    media_urls = [media_url_1, media_url_2]
    res_1 = api.media_upload(media_url_1)
    res_2 = api.media_upload(media_url_2)
    media_ids.append(res_1.media_id)
    media_ids.append(res_2.media_id)

    tweet = generate_tweet(player_1,player_2)
    api.update_status(tweetstatus=tweet, media_ids=media_ids)
    media_urls = []
    media_ids = []
    time.sleep(INTERVAL)