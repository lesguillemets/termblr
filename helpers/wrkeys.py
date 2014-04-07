#!/usr/bin/env python2
'''Read and write user information.'''
import os

flpath = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    os.pardir,
    '.userinfo'
)

def write_oauth_keys(access_token):
    with open(flpath,'w') as f:
        f.write(__encode(access_token['oauth_token']))
        f.write('\n')
        f.write(__encode(access_token['oauth_token_secret']))
    
    return 0

def read_oauth_keys():
    with open(flpath,'r') as f:
        oauth_token, oauth_token_secret = f.readlines()
    return {
        'oauth_token' : __decode(oauth_token.strip()),
        'oauth_token_secret' : __decode(oauth_token_secret.strip()),
    }

def __decode(string):
    return string

def __encode(string):
    return string
