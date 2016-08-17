######################################################
#    http://pep8online.com/ Status Checked           #
#    Python Twitter unfollow bot                     #
#    Version 1.0.0.1                                 #
#    Author: L0NDONER                                #
#    Updated 17 August 2016                          #
######################################################

unfollow.py

=========================================================

A Python Twitter Unfollow bot that works from the linux command line.

==========================================================
=
It will unfollow everyone in your twitter list that is not following you.

It works on a Yes / No basis so it is not in any way automated.

Disclaimer

I hold no liability for what you do with this bot or what happens to you by using this bot. Abusing this bot can get you banned from Twitter, so make sure to read up on proper usage of the Twitter API.

Dependencies

You will need to install tweepy:

sudo pip install tweepy

You will also need to create an app account on https://dev.twitter.com/apps

    Sign in with your Twitter account
    Create a new app account
    Modify the settings for that app account to allow read & write
    Generate a new OAuth token with those permissions

==================================================================
I created another python script called keys.py
in that I set it up excatly like this

#! /usr/bin/python
keys = dict(
	

screen_name = "*********",
    consumer_key = '************************',
    consumer_secret = '*********************************',
    access_token = '*******************************',
)

replace the ******* with your own Twitter API keys

====================================================================





