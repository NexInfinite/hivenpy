import requests

from Hiven.websocket_handler import *


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

    def send(self, message, house_id, room_id):
        headers = {
            'authorization': self.TOKEN,
            'user-agent': 'hiven.py',
            'content-type': 'application/json'
        }

        data = '{"content": \"' + message + '\"}'

        r = requests.post(f'{self.restURL}/rooms/{room_id}/messages', headers=headers, data=data)

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
