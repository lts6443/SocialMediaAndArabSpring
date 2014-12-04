#! /usr/bin/python


from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from pymongo import MongoClient
import sys
import re

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
    if len(sys.argv) == 3:
        count = int(sys.argv[1])
        if sys.argv[2] == 'True':
            lastRecord = True
        else:
            lastRecord = False
    else:
        print("You suck!")
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
    else:
        oauth = get_oauth()
        f = open("egypt_ids.csv",'r')
	ids = ""
	r = 50 
        for i in range(count):
            f.readline()
	for i in enumerate(range(r)):
		if i == r-1:
        		ids += str(f.readline().split(',')[0])	
        	else:
			ids += str(f.readline().split(',')[0])+','	
	url = "https://api.twitter.com/1.1/statuses/lookup.json?id=" + ids.strip()
        r = requests.get(url=url,  auth=oauth)
	json = r.json()
	s = ""
	for i,tweet in enumerate(json):
		s += '{"text":"'
		text = re.sub(r'"',r'',tweet["text"])
		text = re.sub(r'(\r\n|\n)',r'',text)
		s += text
		s += '","created_at":"'
		s += tweet["created_at"]
		if lastRecord and i == len(json)-1:
			s += '"}'
		else:
			s += '"},'	
	try:
		print s.encode('utf-8')
	except UnicodeError:
		pass
