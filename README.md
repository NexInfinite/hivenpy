# Hiven.py
Welcome to the unofficial hivenpy api wrapper. So far we only have self bots as bot account aren't made yet. 
This is a work in progress project made by NexInfinite, CanCodes, and Xenen.

# How to use

### Installation
To install Hiven.py type 
```python
pip install hivenpy
```

### Getting your token
Make a bot account for your hiven bot.
Open up chrome dev tools.
Go to the network tab.
![Image not found](https://github.com/NexInfinite/hivenpy/blob/master/Images/networktab.PNG?raw=true)
Press Ctrl-R then click on the messages cell.
<br><br>
![Image not found](https://github.com/NexInfinite/hivenpy/blob/master/Images/messagesimages.PNG?raw=true)
<br><br>
Go to the headers tab then scroll down and copy your token.
![Image not found](https://github.com/NexInfinite/hivenpy/blob/master/Images/authimage.png?raw=true)

### Setup
Open command prompt and type `pip install hivenpy`.In your main.py file add 
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
You can see a list of all examples in the folder names [Examples](Examples).

# Please note
~~At the moment we don't have a pip package set up as it's not at that stage yet but you can still make 
self bots with this.~~ We now have a [pip package](https://pypi.org/project/hivenpy/1.6/)! Download it to try everything out.
This is a work in progress project so everything is going to change soon. This is temporary so you can start making
and experimenting with new bots now.
<br><br>
There is also no documentation as of yet but there will be in the future. Feel free to message me on hiven
@nexinfinite (I am in the hiven testers chat) to get some support. The house will be public soon, we are 
waiting for that to be released.
