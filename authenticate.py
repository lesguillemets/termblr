#!/usr/bin/env python2
from __future__ import print_function
import oauth2 as oauth
import sys
import os
import urlparse

import const
import messages as msg
import helpers.wrkeys

import pytumblr

request_token_url = "http://www.tumblr.com/oauth/request_token"
authorize_url = "http://www.tumblr.com/oauth/authorize"
access_token_url = "http://www.tumblr.com/oauth/access_token"

def authenticate():
    filepath = os.path.dirname(os.path.realpath(__file__))
    
    if os.path.isfile(os.path.join(filepath, '.usrinfo')):
        # if authentication is already done.
        print(msg.auth_already_done)
        override = raw_input(msg.prompt)
        if override != 'Y':
            print(msg.auth_abort)
            return 0
    
    # Authentication has not been done or the user wants to override it.
    
    consumer = oauth.Consumer(const.consumer_key, const.consumer_secret)
    client = oauth.Client(consumer)
    # Hi, it's me.
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        print(msg.auth_req_token_status_unsuccessful.format(resp['status']))
        return 1
    
    request_token = dict(urlparse.parse_qsl(content))
    print(msg.auth_visit_and_authenticate.format(
        "{}?oauth_token={}".format(authorize_url, request_token['oauth_token'])
    ))
    
    # parse http://localhost/tumblr?oauth_token={}&oauth_verifier={}#_=_
    redirected_url = raw_input(msg.prompt)
    oauth_keys = urlparse.parse_qs(
        urlparse.urlparse(redirected_url).query)
    
    # authenticate
    token = oauth.Token(request_token['oauth_token'],
                        request_token['oauth_token_secret'])
    token.set_verifier(oauth_keys['oauth_verifier'])
    client = oauth.Client(consumer, token)
    resp, content = client.request(access_token_url, "POST")
    access_token = dict(urlparse.parse_qsl(content))
    client = pytumblr.TumblrRestClient(
        const.consumer_key,
        const.consumer_secret,
        access_token['oauth_token'],
        access_token['oauth_token_secret']
    )
    print(msg.auth_successful.format(client.info()['user']['name']))
    helpers.wrkeys.write_oauth_keys(access_token)

if __name__ == '__main__':
    authenticate()
