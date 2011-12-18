#! /usr/env/bin python

import codecs

import time
import requests

from .utils import coroutine

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
def collection(instance):
    """
    Takes an instance of a type with `append`, `add` or `insert`
    methods and fills up the collection with
    incoming data:
        
        >>> from cop.sources import iterable
        >>> li = list()
        >>> iterable('abc', collection(li))
        >>> print li
        ['a', 'b', 'c']
    """
    
    for method in ('append', 'add'):
        if hasattr(instance, method):
            use = method
    while 1:
        item = (yield)
        getattr(instance, use)(item)

@coroutine
def writer(dest, method='write'):
    write = getattr(dest, method)
    while 1:
        data = (yield)
        write(data)

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
