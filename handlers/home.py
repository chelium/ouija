import tornado.web


class HomeHandler(tornado.web.RequestHandler):

    async def get(self):
        self.render("home.html")
