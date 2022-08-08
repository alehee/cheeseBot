import discord
import json
import time

class Cheese:
    token = json.load(open('token.json'))['token']
    client = discord.Client()

    helpMessage = """cheeseBot :cheese: handles following commands:

        >check
            prints if i'm alive and timestamp of the message
    
        >help
            prints all the commands and configurations

        >events or >event
            prints all of the saved events
            
        >eventadd [name] [date in format yyyy-MM-dd]
            adds event to the database, for example '>eventadd Party 2022-11-28'
            
        >eventdel [name]
            deletes event from the database, for example '>eventdel Party'
            
        >event [name]
            prints data about event and count days till event
            
        >welcomes or >welcome
            prints all users that will be welcomed on login to discord
        
        >welcomechange
            switches on/off the welcome feature
        
        >welcomeadd [name]
            adds user to be welcomed
            
        >welcomedel [name]
            deletes user from welcome feature
            
        >meme
            sends random SFW meme to the channel
    """

    def __init__(self):
        self.welcome_option = json.load(open('database.json'))['welcome_option']

    async def processMessage(self, message):
        if message.author == self.client.user or not message.content.startswith('>'):
            return

        elif message.content == '>check':
            await message.channel.send("Howdy! :cowboy: I'm alive and completly fine!\nBy the way did you know that now is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " :alarm_clock:")

        elif message.content == '>help':
            await message.channel.send(self.helpMessage)

        elif message.content == '>events' or message.content == '>event':
            await message.channel.send('Still working on this feature!')

        elif message.content == '>eventadd':
            await message.channel.send('Still working on this feature!')
        
        elif message.content == '>eventdel':
            await message.channel.send('Still working on this feature!')

        elif len(message.content.split(' ')) == 2 and message.content.startswith('>event '):
            event_name = message.content.split(' ')[1]
            await message.channel.send('Still working on this feature!')

        elif message.content == '>welcomes' or message.content == '>welcome':
            await message.channel.send('Still working on this feature!')

        elif message.content == '>welcomechange':
            await message.channel.send('Still working on this feature!')

        elif len(message.content.split(' ')) == 2 and message.content.startswith('>welcomeadd '):
            welcome_name = message.content.split(' ')[1]
            await message.channel.send('Still working on this feature!')

        elif len(message.content.split(' ')) == 2 and message.content.startswith('>welcomedel '):
            welcome_name = message.content.split(' ')[1]
            await message.channel.send('Still working on this feature!')

        elif message.content == '>meme':
            await message.channel.send('Still working on this feature!')