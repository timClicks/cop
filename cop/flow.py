#! /usr/env/bin python

from itertools import cycle

from .utils import  coroutine

@coroutine
def broadcast(*targets):
    while 1:
        data = (yield)
        (t.send(data) for t in targets)

@coroutine
def loadbalance(targets):
    targets = list(targets)
    while 1:
        data = (yield)
        (t.send(data) for t in cycle(targets))

