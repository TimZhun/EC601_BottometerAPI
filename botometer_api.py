
import tweepy
import configparser
import botometer

#read configs
config = configparser.ConfigParser()
config.read('config.ini')

rapidapi_key = config['botometer']['rap_key']
consumer_key = config['botometer']['api_key']
consumer_secret = config['botometer']['api_key_secret']
access_token = config['botometer']['access_token']
access_token_secret = config['botometer']['access_token_secret']

# authentication 

twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
  }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@TamirlanN')
print(result)

# Check a single account by id
result = bom.check_account(49124003)
print(result)