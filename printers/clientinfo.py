#!/usr/bin/env python2
from textwrap import dedent

def show_client_generalinfo(clientinfo):
    """
    Shows basic information about the user.
    Argument : clientinfo,
        which is the return value of
        pytumblr.TumblrRestClient.info()
    """
    return dedent(
        '''\
        You're logged in as {usrname}.
        '''
    )



#{u'user': {u'following': 28, u'blogs': [{u'ask_anon': False, u'updated': 1396790327, u'description': u'\u30b9\u30af\u30e9\u30c3\u30d7\u30d6\u30c3\u30af\uff0e', u'drafts': 0, u'title': u'Untitled', u'url': u'http://lesguillemets.tumblr.com/', u'messages': 1, u'tweet': u'N', u'share_likes': True, u'posts': 372, u'primary': True, u'queue': 0, u'admin': True, u'followers': 14, u'ask': True, u'facebook': u'N', u'type': u'public', u'facebook_opengraph_enabled': u'N', u'name': u'lesguillemets'}, {u'ask_anon': False, u'updated': 1353811721, u'description': u'twitter : @exumbra_insoIem', u'drafts': 0, u'title': u'les clefs', u'url': u'http://lesclefs.tumblr.com/', u'messages': 0, u'tweet': u'N', u'share_likes': False, u'posts': 11, u'primary': False, u'queue': 0, u'admin': True, u'followers': 0, u'ask': True, u'facebook': u'N', u'type': u'private', u'facebook_opengraph_enabled': u'N', u'name': u'lesclefs'}, {u'updated': 1353770025, u'description': u'', u'drafts': 0, u'title': u'les encriers', u'url': u'http://lesencriers.tumblr.com/', u'messages': 0, u'tweet': u'N', u'share_likes': False, u'posts': 4, u'primary': False, u'queue': 0, u'admin': True, u'followers': 0, u'ask': False, u'facebook': u'N', u'type': u'public', u'facebook_opengraph_enabled': u'N', u'name': u'lesencriers'}, {u'updated': 1396348945, u'description': u'', u'drafts': 0, u'title': u'mutsuteru twitpic', u'url': u'http://twitpic-mutsutel.tumblr.com/', u'messages': 0, u'tweet': u'N', u'share_likes': False, u'posts': 10, u'primary': False, u'queue': 0, u'admin': True, u'followers': 0, u'ask': False, u'facebook': u'N', u'type': u'public', u'facebook_opengraph_enabled': u'N', u'name': u'twitpic-mutsutel'}, {u'updated': 1363496119, u'description': u'2\u3064\u76ee\uff0e\u3053\u3063\u3061\u306f\u3044\u308d\u3044\u308d\u66f8\u304d\u6563\u3089\u304b\u3059\u306e\u306b\u3064\u304b\u3046\uff0e', u'drafts': 0, u'title': u'non lu', u'url': u'http://nonlu.tumblr.com/', u'messages': 0, u'tweet': u'N', u'share_likes': False, u'posts': 2, u'primary': False, u'queue': 0, u'admin': True, u'followers': 0, u'ask': False, u'facebook': u'N', u'type': u'public', u'facebook_opengraph_enabled': u'N', u'name': u'nonlu'}], u'default_post_format': u'html', u'name': u'lesguillemets', u'likes': 203}}
