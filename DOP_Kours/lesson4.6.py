import tornado.ioloop
import tornado.web
from os import listdir
from os.path import getsize, join

class MainHandler(tornado.web.RequestHandler):
    def get(self):

        path = self.get_argument('path', '.')

        filenames = listdir(path)
        sizes = {fi: getsize(join(path, fi)) for fi in filenames}

        html = ''
        for fi, size in sizes.items():
            html += '<p><b>{}:</b> {}</p>'.format(fi, size)
        self.write(html)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()