class ctx_obj:
    def __init__(self, ctx, bot):
        self.bot = bot
        self.message = self.Message(ctx)
        self.author = self.Author(ctx)
        self.room_id = ctx['room_id']
        self.house_id = ctx['house_id']

    class Message:
        def __init__(self, ctx):
            self.content = ctx['content']
            self.timestamp = ctx['timestamp']
            self.id = ctx['id']
            self.mentions = ctx['mentions']

    class Author:
        def __init__(self, ctx):
            author_json = ctx['author']
            self.username = author_json['username']
            self.name = author_json['name']
            self.id = author_json['id']

    def send(self, message):
        self.bot.send(message=message, house_id=self.house_id, room_id=self.room_id)


class typing_ctx_obj:
    def __init__(self, ctx):
        self.room_id = ctx['room_id']
        self.house_id = ctx['house_id']
        self.user_id = ctx['author_id']
        self.timestamp = ctx['timestamp']


class house_ctx_obj:
    def __init__(self, ctx):
        self.house = self.House(ctx)
        # rooms to come
        # users to come

    class House:
        def __init__(self, ctx):
            self.name = ctx['name']
            self.owner = self.Owner(ctx)
            self.id = ctx['id']


        class Owner:
            def __init__(self, ctx):
                self.id = ctx['owner_id']


class member_enter_obj:
    def __init__(self, ctx):
        self.house_id = ctx['house_id']
        self.joined_at = ctx['joined_at']
        self.roles = ctx['roles']
        self.user = self.User(ctx)

    class User:
        def __init__(self, ctx):
            user = ctx['user']
            self.website = user['website']
            self.username = user['username']
            self.user_flags = user['user_flags']
            self.name = user['name']
            self.location = user['location']
            self.id = user['id']
            self.emailed_verified = user['email_verified']
            self.bot = user['bot']
            self.bio = user['bio']


class bot_user:
    def __init__(self, ctx):
        user = ctx['user']
        self.id = user['id']
        self.name = user['name']
        self.username = user['username']
        self.user_flags = user['user_flags']
