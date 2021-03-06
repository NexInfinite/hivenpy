# Hiven.py
Welcome to the unofficial hivenpy api wrapper. So far we only have self bots as bot account aren't made yet. 
This is a work in progress project made by NexInfinite, CanCodes, and Xenen.

> Please note that this is in beta and is not fully complete!

# How to use

### Installation
To install Hiven.py type 
```python
pip install hivenpy
```

### Getting your token
Make a bot account for your hiven bot. Open up the console by pressing Command+Option+J (Mac) Control+Shift+J (Windows, Linux, Chrome OS).
<br><br>
![Image not found](https://github.com/NexInfinite/hivenpy/blob/master/Images/console.png?raw=true)
<br>Type `localStorage['hiven-auth']` and hit enter.
<br><br>
![Image not found](https://github.com/NexInfinite/hivenpy/blob/master/Images/Local%20Storage.png?raw=true)
<br>Your token is where the red lines are.


### Setup
Download the code and place it in your project. You will then need to add 
```python
from Hiven.client import Bot, events
```
This will import the bot and events. After this you will need to type
```python
TOKEN = "Your token from before"
bot = Bot(TOKEN)
```
You can also set `debug=True` if you want debugs from the websocket and `output=True` if you want outputs 
from each websocket message.

### Making your bot
Next you will need to setup the events and login to the bot. To do this please type:
```python
@events.event
def on_message(ctx):
    if ctx.author.id != bot.user.id:  
        # Do stuff

bot.login()
```
Congratulations! You now have a self bot for hiven! 

# Examples
You can see a list of all examples in the folder names [Examples](https://github.com/NexInfinite/hivenpy/tree/master/Examples).

# Please note
~~At the moment we don't have a pip package set up as it's not at that stage yet but you can still make 
self bots with this.~~ We now have a [pip package](https://pypi.org/project/hivenpy/)! Download it to try everything out.
This is a work in progress project so everything is going to change soon. This is temporary so you can start making
and experimenting with new bots now.
<br><br>
There is also no documentation as of yet but there will be in the future. Feel free to message me on hiven
@nexinfinite (I am in the hiven testers chat) to get some support. The house will be public soon, we are 
waiting for that to be released.
