#! /usr/env/bin python

from .utils import  coroutine

@coroutine
def delimit(delimiter, target):
    _buffer = []
    while True:
        data = (yield)
        for char in data:
            if char == delimiter:
                target.send(''.join(_buffer))
                _buffer = []
            else:
                _buffer.append(char)

@coroutine
def grep(pattern, target):
    while 1:
        line = (yield)
        if pattern in line:
            target.send(line)

@coroutine
def filter(fun, target):
    while 1:
        item = (yield)
        if fun(item):
            target.send(item)

@coroutine
def transform(fun, target):
    while 1:
        item = (yield)
        target.send(fun(item))

# FLOW

@coroutine
def broadcast(*targets):
    while 1:
        data = (yield)
        (t.send(data) for t in targets)
