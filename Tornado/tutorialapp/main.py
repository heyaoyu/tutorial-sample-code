#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import json

import tornado.ioloop
import tornado.web
import tornado.websocket


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class JSONPHandler(tornado.web.RequestHandler):
    def get(self):
        callback = self.get_argument('callback', 'callback');
        result = {"str":"sever_string"}
        self.write(callback+'('+json.dumps(result)+')')

class PostForAjaxHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        self.write("Post response: "+self.get_argument("arg", ""))

class CometStreamHandler(tornado.web.RequestHandler):
    def on_connection_close(self):
        print "A connection closed."

    def get(self, *args, **kwargs):
        i = 0
        while True:
            self.write(unicode(i))
            self.flush()
            time.sleep(3)
            i += 1
            if i == 3:
                break

class WebSocketDemoHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"


def main():
    import platform
    os_name = platform.uname()[0]
    if os_name == 'Windows':
        import sys
        reload(sys)
        sys.setdefaultencoding('GBK')
    root = os.path.realpath(__file__).rpartition(os.sep)[0]+os.sep+".."+os.sep+".."+os.sep+"Javascript";
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/jsonp_service", JSONPHandler),
        (r"/post_service", PostForAjaxHandler),
        (r"/comet_service", CometStreamHandler),
        (r"/websocket_service", WebSocketDemoHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, dict(path=root)),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__=='__main__':
    main()