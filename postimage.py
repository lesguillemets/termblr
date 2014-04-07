#!/usr/bin/env python2
# coding:utf-8
import os

class PostImage(object):
    """
    tells us where to save images.
    """
    
    pwd = os.path.dirname(__file__)
    def __init__(self, url, post_id, n=0):
        self.url = url
        ext = os.path.splitext(url)[1]
        self.fname = os.path.join(
            self.pwd, 'cache',"{}_{}{}".format(n,post_id,ext))
    
    @classmethod
    def id_and_num_to_file(cls, post_id, url,n=0):
        ext=os.path.splitext(url)[1]
        return os.path.join(
            cls.pwd, 'cache',"{}_{}{}".format(n,post_id,ext))
