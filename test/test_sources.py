import tempfile

from cop.sources import entropy, fd, follow, web, iterable
from cop.sinks import collection

def test_iterable_with_string():
    li = list()
    iterable(u'abc', collection(li))
    for letter in 'abc':
    	assert letter in li

def test_entropy():
	li = list()
	entropy(collection(li))
	assert li

def test_entropy_accepts_length():
	li = list()
	entropy(collection(li), 500)
	assert len(li) == 500

def test_fd():
	li = list()
	data = 'dummy data'
	with tempfile.NamedTemporaryFile(delete=False) as f:
		f.file.write(data)
	fd(f.name, collection(li))
	f.unlink(f.name)
	result = ''.join(li)
	assert result == data


