# test_sinks.py

import sys
from StringIO import StringIO

from cop.sinks import blackhole, collection, printer, writer
from cop.sources import iterable

# These two are equivalent, data is sent to stdout.
# At the moment, we're testing that this doesn't blow up.
# patches welcome to make this more robust

def test_printer():
    iterable('123', printer())

def test_writer_on_std_file_descriptors():
    iterable('123', writer(sys.stdout))
    #iterable('123', writer(sys.stderr))

def test_writer_on_filelike():
    f = StringIO()
    iterable('123', writer(f, 'write'))
    f.seek(0)
    result = f.read()
    assert result == '123'

def test_writer_supports_multiple_modes():
    f = StringIO()
    iterable('123', writer(f, 'writelines'))
    f.seek(0)
    result = f.read()
    print result
    assert result == '123'

def test_collection_with_lists():
    c = list()
    iterable('abc', collection(c))
    assert c == ['a', 'b', 'c'] 

def test_collection_with_sets():
    s = set()
    iterable('abc', collection(s))
    for letter in 'abc':
        assert letter in s

def test_blackhole():
    iterable('anything', blackhole())
