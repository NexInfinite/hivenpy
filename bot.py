import json

import requests
import websocket

try:
    import thread
except ImportError:
    import _thread as thread
import time

events_obj = []
events_name = []


class Bot:
    def __init__(self, token, auth, debug=False, output=False):
        self.TOKEN = token,
        self.WEBSOCKET = "wss://swarm-dev.hiven.io/socket?encoding=json&compression=text_json"
        self.HEARTBEAT = 0,
        self.AUTH = auth,
        self.OUTPUT = output
        if debug:
            websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.WEBSOCKET,
                                         on_message=lambda ws, msg: self.on_message(ws, msg),
                                         on_error=lambda ws, msg: self.on_error(ws, msg),
                                         on_close=lambda ws: self.on_close(ws),
                                         on_open=lambda ws: self.on_open(ws))

    def on_message(self, ws, context):
        context_json = json.loads(context)
        if context_json["op"] == 1:
            self.HEARTBEAT = context_json["d"]["hbt_int"]
        else:
            if self.OUTPUT:
                print(context_json)
            if context_json['e'] == "MESSAGE_CREATE":
                ctx_json = context_json['d']
                ctx = ctx_obj(ctx_json, self)
                on_message = events.find_event("on_message")
                if on_message:
                    on_message(ctx)
            elif context_json['e'] == "TYPING_START":
                ctx_json = context_json['d']
                ctx = typing_ctx_obj(ctx_json)
                on_typing = events.find_event("on_typing")
                if on_typing:
                    on_typing(ctx)


    @staticmethod
    def on_error(ws, error):
        print(error)

    @staticmethod
    def on_close(ws):
        print("### closed ###")

    def on_open(self, ws):
        ws.send('{"op": 2, "d":{"token": "' + self.TOKEN[0] + '"}}')

        def run(*args):
            while True:
                time.sleep(self.HEARTBEAT / 1000)
                ws.send('{"op": 3}')

        thread.start_new_thread(run, ())

    def send_message(self, message, house_id, room_id):
        headers = {
            'authority': 'api.hiven.io',
            'accept': 'application/json, text/plain, */*',
            'authorization': self.AUTH[0],
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://app.hiven.io',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://app.hiven.io/houses/{house_id}/rooms/{room_id}',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

        data = '{"content": \"' + message + '\"}'

        r = requests.post(f'https://api.hiven.io/v1/rooms/{room_id}/messages', headers=headers, data=data)

    def login(self):
        self.ws.run_forever()


class events:
    @staticmethod
    def event(func):
        events_obj.append(func)
        events_name.append(func.__name__)
        return func

    @staticmethod
    def find_event(name):
        try:
            func = events_obj[events_name.index(name)]
            return func
        except Exception as e:
            return False


class ctx_obj:
    def __init__(self, ctx_json, bot):
        self.bot = bot
        self.message = self.Message(ctx_json)
        self.author = self.Author(ctx_json)
        self.room_id = ctx_json['room_id']
        self.house_id = ctx_json['house_id']

    class Message:
        def __init__(self, ctx_json):
            self.content = ctx_json['content']
            self.timestamp = ctx_json['timestamp']
            self.id = ctx_json['id']
            self.mentions = ctx_json['mentions']

    class Author:
        def __init__(self, ctx_json):
            author_json = ctx_json['author']
            self.username = author_json['username']
            self.name = author_json['name']
            self.id = author_json['id']

    def send(self, message):
        self.bot.send_message(message=message, house_id=self.house_id, room_id=self.room_id)


class typing_ctx_obj:
    def __init__(self, ctx_json):
        self.room_id = ctx_json['room_id']
        self.house_id = ctx_json['house_id']
        self.user_id = ctx_json['author_id']
        self.timestamp = ctx_json['timestamp']
