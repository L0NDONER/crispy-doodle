#! /usr/bin/python3

import tweepy
import sys
import time

from keys import keys


SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

# Twitter API Handling

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# If succesful API login

if(api.verify_credentials):
    try:
        print("We successfully Logged In To Twitter!", SCREEN_NAME,
              time.strftime("%a - %B - %d - %Y - %H:%M:%S"))
    except:
        # Throws an error message if somethings wrong
        print("Uh oh something went wrong")

    else:
        print("The script ran succesfully")  # Tells me the script ran


# If not succesful API login

if not api.verify_credentials():
    raise Exception("Invalid credentials")

# Twitter unfollow


followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)

for f in friends:
    if f not in followers:
        print "Unfollow {0}?".format(api.get_user(f).screen_name)
        if raw_input("Y/N?") == 'y' or 'Y':
            api.destroy_friendship(f)
sys.exit()

