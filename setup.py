# -*- coding: utf8 -*-

from setuptools import setup, find_packages

from nosees import __version__


setup(
    name='nosees',
    description='Replace elaticsearch-py with mock elasticsearch client.',
    version=__version__,
    author='fatelei',
    author_email='fatelei@gmail.com',
    packages=find_packages(
        where='.',
        exclude=('tests',)
    ),
    install_requires=[
        'fake_elasticsearch',
        'mock'
    ],
    entry_points={
        'nose.plugins.0.10': [
            'nosees = nosees.main:FakeElasticsearchPlugin',
        ]
    }
)
