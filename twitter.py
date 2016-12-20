#! /usr/bin/python
import tweepy
import time
from keys import keys
 
SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
   
followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)

if(api.verify_credentials):
	try:
		print("We successfully Logged In To Twitter:", SCREEN_NAME)
	except:
		print 'Uh-Oh something went wrong'
	else:
		print(time.strftime('%a - %B - %d - %Y - %H:%M:%S'))
 
for f in friends:
    if f not in followers:
        print "Unfollow {0}?".format(api.get_user(f).screen_name)
        if raw_input("Y/N?") == 'y' or 'Y':
            api.destroy_friendship(f)
