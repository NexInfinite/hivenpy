class bot_user:
    def __init__(self, ctx):
        user = ctx['user']
        self.id = user['id']
        self.name = user['name']
        self.username = user['username']
        self.user_flags = user['user_flags']
