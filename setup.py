# bootstrap easy_install
from setuptools import setup, find_packages

setup(
    name = 'solrpy3',
    version = '1',
    author = 'Alex Parmentier',
    author_email = 'a.g.parmentier@gmail.com',
    url = 'https://github.com/lexpar/solrpy/tree/python3',
    license = 'MIT',
    packages=['solr'],
    install_requires = [],
    description = 'Fork of solrpy 0.9.7 implementing python3 support.',
    tests_require = ["nose>=0.10.1"],
    test_suite = 'nose.collector',

    classifiers=
    [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only'

    ],

)
