#!/usr/bin/env python
# coding=utf-8

from tornado import web

class IndexHandler(web.RequestHandler):
    def get(self):
        return self.render("templates/index.html")
