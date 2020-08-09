from Hiven.Websocket.websocket_handler import *
from Hiven.Methods.send import *
from Hiven.Methods.get_user import *
from Hiven.Methods.ping import *

# Should we make this async???


class Bot:
    def __init__(self, token, debug=False, output=False):
        self.restURL = "https://api.hiven.io/v1"
        self.TOKEN = token
        self.user = None
        self.ws = WebSocket(self.TOKEN, debug, output, self)

    def login(self):
        self.ws.start()

    def send(self, message, room_id):
        send_message(message, room_id, self.TOKEN, self.restURL)

    def get_user(self, username):
        return GetUser(username, self)

    @staticmethod
    def ping():
        return Ping()
