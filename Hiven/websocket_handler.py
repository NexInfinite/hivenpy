import _thread as thread
import websocket
import json
import time

from Hiven.objects import *
from Hiven.events import *


class WebSocket:
    def __init__(self, token, debug=False, output=False):
        self.TOKEN = token
        self.user = None
        self.restURL = "https://api.hiven.io/v1"
        self.WEBSOCKET = "wss://swarm-dev.hiven.io/socket?encoding=json&compression=text_json"
        self.HEARTBEAT = 0
        self.OUTPUT = output
        if debug:
            websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.WEBSOCKET,
                                         on_message=lambda ws, msg: self.on_message(ws, msg),
                                         on_open=lambda ws: self.on_open(ws))
        self.ws.run_forever()

    def on_open(self, ws):
        ws.send('{"op": 2, "d":{"token": "' + self.TOKEN + '"}}')

        def run(*args):
            while True:
                time.sleep(self.HEARTBEAT / 1000)
                ws.send('{"op": 3}')

        thread.start_new_thread(run, ())

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
                events.call(ctx, "on_message")
            elif context_json['e'] == "TYPING_START":
                ctx_json = context_json['d']
                ctx = typing_ctx_obj(ctx_json)
                events.call(ctx, "on_typing")
            elif context_json['e'] == "HOUSE_JOIN":
                ctx_json = context_json['d']
                ctx = house_ctx_obj(ctx_json)
                events.call(ctx, "on_house_join")
            elif context_json['e'] == "HOUSE_MEMBER_ENTER":
                ctx_json = context_json['d']
                ctx = member_enter_obj(ctx_json)
                events.call(ctx, "on_member_enter")
            elif context_json['e'] == "INIT_STATE":
                ctx_json = context_json['d']
                self.user = bot_user(ctx_json)