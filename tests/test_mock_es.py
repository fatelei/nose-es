# -*- coding: utf8 -*-

import unittest

from nosees.plugin import mock_es


class TestMockEs(unittest.TestCase):

    def test_mock_es(self):
        mock_es()

        from elasticsearch import Elasticsearch
        from fake_elasticsearch.cli import FakeElasticsearch
        
        cli = Elasticsearch()
        self.assertTrue(isinstance(cli, FakeElasticsearch))
