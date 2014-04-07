#!/usr/bin/env python2
# coding:utf-8
from __future__ import print_function
#from __future__ import unicode_literals # can't just data ="path/to/my/file"
import const
import pytumblr
import urllib2
import Queue
import sys
import threading
from postprinter import PostPrinter
from textwrap import dedent
from colors import prettify
from urllib import urlretrieve
import os,sys
from postimage import PostImage
import helpers.wrkeys

client = pytumblr.TumblrRestClient(
    const.consumer_key,
    const.consumer_secret,
    helpers.wrkeys.read_oauth_keys()['oauth_token'],
    helpers.wrkeys.read_oauth_keys()['oauth_token_secret'],
)

class Myapp(object):
    """ base class."""
    
    def __init__(self, tracked_tags, workernum=5, client=client):
        self.tracked_tags = tracked_tags
        self.client = client
        self.freshqueue()
        self.workernum = workernum
    
    def imgfetcher(self):
        while not self.imgqueue.empty():
            target = self.imgqueue.get()
            if not os.path.isfile(target.fname):
                try:
                    print("downloading Image from {}...".format(
                                target.url))
                    sys.stdout.flush()
                    urlretrieve(target.url,target.fname)
                except IOError:
                    pass
            else:
                print("skipping Image from {}".format(
                    target.url))
                sys.stdout.flush()
            self.imgqueue.task_done()

    def freshqueue(self):
        self.readqueue = Queue.Queue()
        for tag in self.tracked_tags:
            self.readqueue.put(tag)
        self.readqueue.put(None)
        self.tlqueue = Queue.Queue()
        self.imgqueue = Queue.Queue()
    
    def readworker(self,**args):
        while not self.readqueue.empty():
            tag = self.readqueue.get()
            if tag is None:
                self.readdashboard()
                continue
            print(" {} {}".format(
                prettify('reading','green','blue'),tag.encode("utf-8")))
            if not args:
                posts = self.client.tagged(tag.encode('utf-8'))
            else:
                posts = self.client.tagged(tag.encode('utf-8'), **args)
            print(" {} : {}".format(tag.encode('utf-8'),len(posts)))
            for post in posts:
                if post['type'] == 'photo':
                    self.add_to_imgqueue(post)
                self.tlqueue.put(post)
            self.readqueue.task_done()
            print(" {}: {}".format(
                prettify('Job done','magenta','cyan'),
                tag.encode('utf-8')))
            sys.stdout.flush()
    
    def readdashboard(self, **args):
        print(" {} dashboard".format(
            prettify('reading','green','blue')))
        posts = self.client.dashboard()['posts']
        for post in posts:
            #print(post)
            if post['type'] == 'photo':
                self.add_to_imgqueue(post)
            self.tlqueue.put(post)
        self.readqueue.task_done()
        print(" dashboard has been read.")
    
    def add_to_imgqueue(self, post, maxwidth=500):
        if post['type'] != 'photo':
            raise ValueError("Only Photo posts are accepted.")
        else:
            for (i,photo) in enumerate(post['photos']):
                alt_sizes = sorted(photo['alt_sizes'],
                                   key=lambda x:x['width'], reverse=True)
                if alt_sizes[0]['width'] <= maxwidth:
                    alt_size = alt_sizes[0]
                else:
                    alt_size = next((al for al in alt_sizes
                                     if al['width'] <= maxwidth))
                self.imgqueue.put(
                    PostImage(alt_size['url'], post['id'], i))
    
    
    def read(self):
        readers , fetchers = [], []
        for i in range(self.workernum):
            readers.append(threading.Thread(target=self.readworker))
            readers[-1].start()
        self.readqueue.join()
        print(prettify("ALL READ.", "blue", "green", 'bold'))
        for i in range(self.workernum):
            fetchers.append(threading.Thread(target=self.imgfetcher,))
            fetchers[-1].daemon=True
            fetchers[-1].start()
        self.imgqueue.join()
        print("DONE")
    
    def showtl(self,n=10):
        tl = []
        while not self.tlqueue.empty():
            tl.append(self.tlqueue.get())
        tl.sort(key=lambda x:x['timestamp'])
        for post in reversed(tl[-n:]):
            self.printpost(post)
            sys.stdout.flush()
    @staticmethod
    def printpost(post):
        print(PostPrinter().show(post))
    
    def tryme(self,n=10):
        self.read()
        self.showtl(n)


tracked_tags = ["firefox", "monospaced"]
a = Myapp(tracked_tags)
a.tryme(20)
sys.exit()
