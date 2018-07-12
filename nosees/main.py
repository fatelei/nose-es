# -*- coding: utf8 -*-

import logging
import os


from nose.plugins import Plugin

from nosees.plugin import mock_es


log = logging.getLogger('nose.plugins.nosees')


class FakeElasticsearchPlugin(Plugin):
    name = 'nosees'

    def options(self, parser, env=os.environ):
        super(FakeElasticsearchPlugin, self).options(parser, env=env)

    def configure(self, options, conf):
        super(FakeElasticsearchPlugin, self).configure(options, conf)
        if not self.enabled:
            return

    def begin(self):
        if self.enabled:
            mock_es()
