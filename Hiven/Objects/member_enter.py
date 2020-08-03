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
