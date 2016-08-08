import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
#        greeting = self.get_argument('greeting', 'Hello')
#        self.write(greeting + ', liyuling user!')
        self.write("this is a demo update")

urls = [(r"/", IndexHandler)]