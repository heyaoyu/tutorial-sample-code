import tornado.ioloop
import tornado.web

import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class JSONPHandler(tornado.web.RequestHandler):
    def get(self):
        callback = self.get_argument('callback', 'callback');
        result = {"str":"sever_string"}
        self.write(callback+'('+json.dumps(result)+')')

def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/jsonp_service", JSONPHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__=='__main__':
    main()