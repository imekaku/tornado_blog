import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from setting import LISTEN_HOST, LISTEN_PORT
from router import urls

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls
        tornado.web.Application.__init__(self, handlers)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(LISTEN_PORT)
    tornado.ioloop.IOLoop.instance().start()
