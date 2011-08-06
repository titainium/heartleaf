#!/usr/bin/env python
# coding=utf-8

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application

from settings import site_setting
from settings import port
from url import handlers

def main():
    app = Application(handlers, **site_setting)
    server = HTTPServer(app)
    
    server.bind(port)
    server.start()
    IOLoop.instance().start()

if __name__ == "__main__":
    main()
