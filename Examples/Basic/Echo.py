from Hiven.client import Bot, events

bot = Bot("Your token here")


@events.event
def on_ready():
    print(f"Logged in as {bot.user.name}")


@events.event
def on_message(ctx):
    if ctx.author.id != bot.user.id:
        ctx.send(f"**{ctx.author.name}** just said **{ctx.message.content}**")


bot.login()
