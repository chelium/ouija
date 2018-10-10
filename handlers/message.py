import os
import tornado.web
from twilio.rest import Client


class MessageHandler(tornado.web.RequestHandler):

    async def get(self):
        self.render('message.html')

    async def post(self):
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID', None)
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN', None)
        from_number = self.get_argument('from')
        to_number = self.get_argument('to')

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body = self.get_body_argument('message'),
            from_ = from_number,
            to = to_number
        )
