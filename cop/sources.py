#! /usr/env/bin python

import codecs

import time
import requests

from .utils import coroutine

def entropy(target, length=1024):
    with open('/dev/urandom') as f:
        for count in xrange(length):
            target.send(f.read(1))

def fd(path, target, mode='rb', encoding='utf-8', *a, **kw):
    with codecs.open(path, encoding=encoding, mode=mode, *a, **kw) as f:
        while 1:
            data = f.read(1024 * 10)
            if not data:
                break
            target.send(data)

def follow(path, target):
    thefile.seek(0,2)
    # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            # Sleep briefly
            continue
        target.send(line)

def web(url, target, method='get', *a, **kw):
    request = dict(
        get=requests.get,
        head=requests.head,
        patch=requests.patch,
        post=requests.post,
        put=requests.put)
    for body_part in request[method](url, *a, **kw).content:
        target.send(body_part)

def iterable(iterable, target):
    for elem in iterable:
        target.send(elem)

