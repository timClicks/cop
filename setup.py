#!/usr/bin/env python2

from distutils.core import setup
import cop

setup(
    name="cop",
	version="0.2",
	description="Coroutines for dataflow pipelines",
	long_description=cop.__doc__,
	author="Tim McNamara",
	author_email="code@timmcnamara.co.nz",
	url="https://github.com/timClicks/cop",
	packages=['cop'],
	license="Apache 2",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
    ],

)