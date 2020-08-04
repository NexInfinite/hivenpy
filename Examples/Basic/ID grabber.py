from Hiven.client import Bot, events

bot = Bot("Your token here")


@events.event
def on_ready():
    print(f"Logged in as {bot.user.name}")


@events.event
def on_message(ctx):
    message = ctx.message
    if ctx.author.id != bot.user.id:
        if message.content == "!id":
            user = bot.get_user(ctx.author.username)
            ctx.send(f"The id of `{user.username}` is `{user.id}`")


bot.login()
