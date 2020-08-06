import datetime


class typing_ctx_obj:
    def __init__(self, ctx):
        self.room_id = ctx['room_id']
        self.house_id = ctx['house_id']
        self.user_id = ctx['author_id']
        self.timestamp = ctx['timestamp']
        self.time = datetime.datetime.fromtimestamp(float(ctx['timestamp']) / 1e3)
