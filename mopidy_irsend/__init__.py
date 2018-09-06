from __future__ import unicode_literals

import os

from mopidy import config, ext


__version__ = '0.1.0'


class Extension(ext.Extension):

    dist_name = 'Mopidy-LCD'
    ext_name = 'LCD'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['rs'] = config.Integer()
        schema['en'] = config.Integer()
        schema['d4'] = config.Integer()
        schema['d5'] = config.Integer()
        schema['d6'] = config.Integer()
        schema['d7'] = config.Integer()
        return schema

    def setup(self, registry):
        from .actor import LCDFrontend
        registry.add('frontend', LCDFrontend)

