#! /usr/bin/python

# Get Twitter Data

from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from pymongo import MongoClient

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "Tsttw9p06eUjr2xoKWv9NTkYq"
CONSUMER_SECRET = "87ofvyPQJYcAox1QA8ufwTlWF8fvsHXgwitpHHOGFh6ite4jFd"

OAUTH_TOKEN = "963172028-TbzKMTWu9oJFldex6F3OGtj53qq1J67vlY4o8Gci"
OAUTH_TOKEN_SECRET = "BbimPAEyAZ5wP0mv2f2u1wthBeTtjNPOXGHK3ZZhUStHe"


def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print 'Please go here and authorize: ' + authorize_url

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
    else:
        oauth = get_oauth()
        f = open("egypt_ids.csv",'r')
	ids = ""
	r = 1
	for i in range(r):
		if i == r-1:
        		ids += str(f.readline().split(',')[1])	
        	else:
			ids += str(f.readline().split(',')[1])+','	
	print ids
        #r = requests.get(url="https://api.twitter.com/1.1/statuses/lookup.json?id=22643118444646400,22648223323656192,22700735934234625,22717768642072576,22718171173621760", auth=oauth)
	url = "https://api.twitter.com/1.1/statuses/lookup.json?id=" + ids.strip()
	print url
        r = requests.get(url=url,  auth=oauth)
        print r.json()
	#client = MongoClient("74.74.175.42",27017)
	#db = client.test
	#data = db.data	
	#data.insert(r.json())
