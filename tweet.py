#!/usr/bin/python

import tweepy
import sys

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

data = sys.stdin.read()
if len(data) == 0:
    print "Error: no data"
if len(data) < 140:
    api.update_status(data)
else:
    print "to long!"

#print 141*"-"
#info = raw_input(">")
#if len(info) < 140:
#    api.update_status(info)
#    print 141*"-"
#    print "\n"
#
#else:
#    print "To long!"
