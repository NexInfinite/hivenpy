import datetime


class message_update_obj:
    def __init__(self, ctx):
        self.message = self.Message(ctx)
        self.author = self.Author(ctx)
        self.room_id = ctx['room_id']
        self.house_id = ctx['house_id']

    class Message:
        def __init__(self, ctx):
            self.content = ctx['content']
            self.timestamp = ctx['timestamp']
            self.time = datetime.datetime.fromtimestamp(float(ctx['timestamp']) / 1e3)
            self.id = ctx['id']
            self.mentions = ctx['mentions']

    class Author:
        def __init__(self, ctx):
            author_json = ctx['author']
            self.username = author_json['username']
            self.name = author_json['name']
            self.id = author_json['id']
            self.iconURL = f"https://media.hiven.io/v1/users/{author_json['id']}/icons/{author_json['icon']}"
