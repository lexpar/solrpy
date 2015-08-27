# bootstrap easy_install
from setuptools import setup, find_packages

setup(
    name = 'solrpy3',
    version = '0.1',
    url = 'https://github.com/lexpar/solrpy/tree/python3',
    license = 'MIT',
    packages=find_packages(),
    install_requires = [],
    description = 'Fork of solrpy 0.9.7 implementing python3 support.',
    tests_require = ["nose>=0.10.1"],
    test_suite = 'nose.collector',

    classifiers=
    [
        'License :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

)
