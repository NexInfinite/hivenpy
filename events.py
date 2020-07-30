events_obj = []
events_name = []


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

    @staticmethod
    def call(ctx, name):
        func = events.find_event(name)
        if func:
            func(ctx)