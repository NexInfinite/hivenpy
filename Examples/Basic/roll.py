from random import randint

from Hiven.client import Bot, events

TOKEN = "[Your token]"
bot = Bot(TOKEN)

@events.event
def on_ready():
    print(f"Using {bot.user.name}")

@events.event
def on_message(ctx):
    if ctx.author.id != bot.user.id:
        if ctx.message.content == "!roll":
            ctx.send(randint(1, 6))

bot.login()
