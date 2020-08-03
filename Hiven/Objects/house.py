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
