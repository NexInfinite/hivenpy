from Hiven.client import Bot, events

bot = Bot("GhdMRlZc29czF8f3MvckIoUtZUNh18DiUlOuSRn00jFqgAdzIQy1JGDY2QZHn5sGNG6RycmmLM2Ft4MeSxCskRChWe1dIbivUSBPrZhhEXDrsNvYM1ttWu3bJerYzTcw")


@events.event
def on_ready():
    print(f"Logged in as {bot.user.name}")


@events.event
def on_message(ctx):
    if ctx.author.id != bot.user.id:
        ctx.send(f"**{ctx.author.name}** just said **{ctx.message.content}**")


bot.login()
