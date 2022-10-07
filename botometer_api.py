
import tweepy
import configparser
import pandas as pd 

#read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['tweeter']['api_key']
api_key_secret = config['tweeter']['api_key_secret']
access_token = config['tweeter']['access_token']
access_token_secret = config['tweeter']['access_token_secret']

# authentication 
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api =tweepy.API(auth)
public_tweets = api.home_timeline()
