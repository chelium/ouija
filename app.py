import os
import tornado.ioloop
import tornado.web
import tornado.locks
from handlers import HomeHandler, MessageHandler


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/message", MessageHandler)
        ]
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            debug = True,
        )
        super(Application, self).__init__(handlers, **settings)


async def main():
    app = Application()
    app.listen("8888")

    shutdown_event = tornado.locks.Event()
    await shutdown_event.wait()


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
