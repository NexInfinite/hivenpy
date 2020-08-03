from Hiven.Websocket.websocket_handler import *
from Hiven.Methods.send import *
from Hiven.Methods.get_user import *


class Bot:
    def __init__(self, token, debug=False, output=False):
        self.TOKEN = token
        self.restURL = "https://api.hiven.io/v1"
        self.WEBSOCKET = "wss://swarm-dev.hiven.io/socket?encoding=json&compression=text_json"
        self.HEARTBEAT = 0
        self.OUTPUT = output
        self.DEBUG = debug
        self.ws = WebSocket(self.TOKEN, self.DEBUG, self.OUTPUT, self)
        self.user = None
        self.get_user = GetUser

    def login(self):
        self.ws.start()

    def send(self, message, room_id):
        send_message(message, room_id, self.TOKEN, self.restURL)
