# -*- coding: utf8 -*-

from fake_elasticsearch.cli import FakeElasticsearch
from mock import patch


def mock_es():
    patcher = patch('elasticsearch.Elasticsearch', FakeElasticsearch)  
    patcher.start()
