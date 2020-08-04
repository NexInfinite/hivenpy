class member_exit_obj:
    def __init__(self, ctx):
        self.user = self.User(ctx)
        self.house_id = ctx['house_id']

    class User:
        def __init__(self, ctx):
            self.id = ctx['id']