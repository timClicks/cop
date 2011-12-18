#! /usr/env/bin python

try:
    from .utils import coroutine
except ValueError:
    # probably testing
    from utils import coroutine
"""
Steps are where the bulk of processing is carried out.
You are strongly recommended to look through the source
yourself to see how to build your own steps.

Most steps are fairly agnostic of type. Sections of the
stream may be coerced into lists, but in general nothing
should affect your data.

"""

@coroutine
def delimit(delimiter, target):
    """
    Attempts to split the stream at the given delimiter,
    providing each as a list: 

        >>> l33t = [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1]
        >>> from cop.sources import iterable
        >>> from cop.sinks import printer 
        >>> iterable(l33t, 
        ... delimit(0, 
        ... printer()))
        [1, 0]
        [1, 0]
        [0]
        [0]
        [1, 1, 1, 0]
        [0]
        [1]

    If you wish to avoid this behaviour, consider using
    `cop.steps.transform`:

        >>> from cop.steps import transform
        >>> def ints_to_str(li):
        ...     from os import linesep
        ...     as_str = ''.join(str(elem) for elem in li)
        ...     return as_str + linesep
        >>> iterable(l33t,
        ... delimit(0,
        ... transform(ints_to_str, # <- put function in here
        ... printer())))
        10
        10
        0
        0
        1110
        0
        1
    """

    _buffer = []
    while True:
        data = (yield)
        for char in data:
            _buffer.append(char)
            if char == delimiter:
                target.send(_buffer)
                _buffer = []


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

@coroutine
def until(fun, target):
    """
    Will send items to the target until the
    condition is reached. The condition
    should be in a form of a function
    which acts on each item in the stream.
    >>> from([1,4,1], keep_while(lambda a: a < 2, p()))
    1
    """
    while 1:
        item = (yield)
        if not fun(item):
            while 1:
                (yield)
        target.send(item)

@coroutine
def begin_at(fun, target):
    """
    Begin sending items to the target
    when a condition has been reached:

    >>> iterable([2, 3, 4, 3], begin_at(lambda a: a > 3, p()))
    4
    3
    """
    while True:
        item = (yield)
        if fun(item):
            target.send(item)
            while True:
                item = (yield)
                target.send(item)

@coroutine
def nth(n, target):
    """
    Plucks the nth item from the stream,
    sending it to target.

    >>> from("abc", nth(1, printer()))
    a
    """
    i = 0
    while True:
        item = (yield)
        i += 1
        if i == n:
            target.send(item)
            while True:
                abyss = (yield)

@coroutine
def slice(start, stop, target):
    """
    Sends items through to target which fit
    between start and stop. Unlike Python's
    slices, indicies are not allowed to be
    negative.


    >>> iterable(l33t, slice(0, 1, printer()))
    1
    0
    """
    # Yes, assert is unpythonic, but they're only called once
    assert isinstance(start, int), "The start index must be an int."
    assert isinstance(stop, int), "The stop index must be an int."
    assert start >= 0, "The start index must be non-negative."
    assert start < stop, "Stop index must be higher than the stop"
    i = 0
    while True:
        item = (yield)
        i += 1
        if start <= i <= stop:
            target.send(item)
        # once we hit the stop, no point checking from
        # now on
        elif i > stop:
            while True:
                limbo = (yield)

@coroutine
def sort(target):
    while 1:
        for item in sorted(i for i in (yield)): # possible?
            target.send(item)

if __name__ == "__main__":
    import doctest


    doctest.testmod(verbose=True)
    from copy import copy
    gg = globals()
    for f in copy(gg):
        doctest.run_docstring_examples(f, gg)
