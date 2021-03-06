import _thread as thread
import websocket
import asyncio
import json
import time

from Hiven.Objects.bot_user import *
from Hiven.Objects.house import *
from Hiven.Objects.member_enter import *
from Hiven.Objects.member_exit import *
from Hiven.Objects.message import *
from Hiven.Objects.message_update import *
from Hiven.Objects.typing import *

from Hiven.Events.events import *


class WebSocket:
    def __init__(self, token, debug=False, output=False, outer=None):
        self.restURL = "https://api.hiven.io/v1"
        self.WEBSOCKET = "wss://swarm-dev.hiven.io/socket?encoding=json&compression=text_json"
        self.HEARTBEAT = 0
        self.TOKEN = token
        self.OUTPUT = output
        self.outer = outer
        if debug:
            websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.WEBSOCKET,
                                         on_message=lambda ws, msg: self.on_message(ws, msg),
                                         on_open=lambda ws: self.on_open(ws))

    def start(self):
        self.ws.run_forever()

    def on_open(self, ws):
        ws.send('{"op": 2, "d":{"token": "' + self.TOKEN + '"}}')

        def run():
            while True:
                time.sleep(self.HEARTBEAT / 1000)
                ws.send('{"op": 3}')

        thread.start_new_thread(run, ())

    def on_message(self, ws, context):
        context_json = json.loads(context)
        if context_json["op"] == 1:
            self.HEARTBEAT = context_json["d"]["hbt_int"]
        else:
            loop = asyncio.get_event_loop()
            ctx_json = context_json['d']
            event = context_json['e']
            if self.OUTPUT:
                print(context_json)
            if event == "MESSAGE_CREATE":
                ctx = ctx_obj(ctx_json, self.outer)
                loop.run_until_complete(events.call(ctx, "on_message"))
            elif event == "TYPING_START":
                ctx = typing_ctx_obj(ctx_json)
                loop.run_until_complete(events.call(ctx, "on_typing"))
            elif event == "HOUSE_JOIN":
                ctx = house_ctx_obj(ctx_json)
                loop.run_until_complete(events.call(ctx, "on_house_join"))
            elif event == "HOUSE_MEMBER_ENTER":
                ctx = member_enter_obj(ctx_json)
                loop.run_until_complete(events.call(ctx, "on_member_enter"))
            elif event == "INIT_STATE":
                self.outer.user = bot_user(ctx_json)
                loop.run_until_complete(events.call(None, "on_ready"))
            elif event == "HOUSE_MEMBER_EXIT":
                ctx = member_exit_obj(ctx_json)
                loop.run_until_complete(events.call(ctx, "on_member_exit"))
            elif event == "MESSAGE_UPDATE":
                ctx = message_update_obj(ctx_json)
                loop.run_until_complete(events.call(ctx, "on_message_update"))
