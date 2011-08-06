#!/usr/bin/env python
# coding=utf-8

from tornado import web

from apps.index.view import IndexHandler

handlers = [(r"/", IndexHandler),
            (r"/(apple-touch-icon\.png)", web.StaticFileHandler),
            ]
