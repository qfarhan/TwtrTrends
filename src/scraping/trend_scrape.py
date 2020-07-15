
import tweepy
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
config_values = config['TwtrTrends' ]

auth = tweepy.OAuthHandler(config_values['consumer_key'], config_values['consumer_secret'])
auth.set_access_token(config_values['access_token'], config_values['access_token_secret'])

api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(str(tweet) + '\n')
