import os.path
#!/usr/bin/env python
# coding=utf-8

import os

site_setting = {'debug': True,
                'gzip': True,
                'static_path': os.path.join(os.path.dirname(__file__), 'static'),
                }

port = 8000
