#!/usr/bin/env python2
# coding:utf-8
from textwrap import dedent

prompt = '\t>>  '

auth_already_done = dedent(
    '''\
    It seems you've already authenticated this app.
    Do you want to overwrite this authentication? [Y/n]
    (Note : even if you overwrite the existing authentication,
    your permission for that remains until you explicitly revoke access
    via https://www.tumblr.com/settings/apps .)
    ''')

auth_abort = "Aborting."

auth_req_token_status_unsuccessful = dedent(
    '''\
    Got response code {}. Please try again later. Aborting.
    ''')

auth_visit_and_authenticate = dedent(
    '''\
    Go to the following link and authenticate this app.
    (Make sure you're logged in to tumblr in that browser.)
    
    {}
    
    Your browser will be redirected to http://localhost/... and blah,
    resulting in 404 NOT FOUND being displayed.
    Don't worry and paste the address here.
    ''')

auth_successful = dedent(
    '''\
    Authentication successful.
    You're now logged in as {}.
    ''')
