#! /usr/env/bin python

import codecs

import time
import requests

from .util import coroutine

@coroutine
def printer():
    while 1:
        item = (yield)
        print item

@coroutine
def blackhole():
    while 1:
        abyss = (yield)

@coroutine
def store():
    """
    Pseudo-code really ...
    """
    raise NotImplementedError
    db.open()
    try:
        while 1:
            item = (yield)
            db.save(item)
    except GeneratorExit:
        db.close()
