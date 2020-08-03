from Hiven.Websocket.websocket_handler import *
from Hiven.Objects.bot_user import *
from Hiven.Methods.send import *


class Bot:
    def __init__(self, token, debug=False, output=False):
        self.TOKEN = token
        self.user = None
        self.restURL = "https://api.hiven.io/v1"
        self.WEBSOCKET = "wss://swarm-dev.hiven.io/socket?encoding=json&compression=text_json"
        self.HEARTBEAT = 0
        self.OUTPUT = output
        self.DEBUG = debug

    def login(self):
        WebSocket(self.TOKEN, self.DEBUG, self.OUTPUT)

    def send(self, message, room_id):
        send_message(message, room_id, self.TOKEN, self.restURL)

    class get_user:
        def __init__(self, username):
            headers = {
                'user-agent': 'hiven.py',
            }

            r = requests.get(f'{self.restURL}/users/{username.lower()}', headers=headers).json()
            if r['success']:
                data = r['data']
                self.success = True
                self.id = data['id']
                self.name = data['name']
                self.username = data['username']
                self.user_flags = data['user_flags']
                self.bot = data['bot']
                self.location = data['location']
                self.website = data['website']
                self.bio = data['bio']
            else:
                self.success = False
