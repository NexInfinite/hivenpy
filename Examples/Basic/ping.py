from Hiven.client import Bot, events  #import events

bot = Bot("Your Bot Token")

@events.event
def on_message(ctx):  # this method gets called when a someone sends a message
    if ctx.author.id != bot.user.id:  # checks if author of message is not bot account to prevent spam
        if ctx.message.content == "ping":  # checks if message content is "ping"
            ctx.send("pong")  # sends "pong"

bot.login()
