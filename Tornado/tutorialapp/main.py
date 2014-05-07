import os
import json

import tornado.ioloop
import tornado.web


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


def main():
    root = os.path.realpath(__file__).rpartition("/")[0]+'/../../Javascript'
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/jsonp_service", JSONPHandler),
        (r"/post_service", PostForAjaxHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, dict(path=root)),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__=='__main__':
    main()