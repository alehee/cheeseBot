import discord
import json
import time
import datetime
import random
from requests import get

class Cheese:
    token = json.load(open('token.json'))['token']

    intents = discord.Intents.default()
    intents.members = True
    intents.presences = True
    client = discord.Client(intents=intents)

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
        self.welcome_usernames = json.load(open('database.json'))['welcome']
        self.welcome_strs = ["Howdy partner :cowboy:", "He's clearly up to something :unamused:", "Wanna some cheeeeese? :cheese: :cheese: :cheese:", "I don't believe it\nMust be a robot\nBeep boop :robot:"]
        self.channel_id = json.load(open('database.json'))['channel_id']

    async def processMessage(self, message):
        if message.author == self.client.user or not message.content.startswith('>'):
            return

        elif message.content == '>check':
            await message.channel.send("Howdy! :cowboy: I'm alive and completly fine!\nBy the way did you know that now is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " :alarm_clock:")

        elif message.content == '>help':
            await message.channel.send(self.helpMessage)

        elif message.content == '>events' or message.content == '>event':
            response = "Here's some events you should remember about :calendar:\n"
            data = self.getDatabase()
            events = data['events']
            if len(events) > 0:
                for key in events:
                    response += key + ': ' + events[key] + '\n'
                await message.channel.send(response)
            else:
                await message.channel.send("There's no events yet :calendar:")

        elif len(message.content.split(' ')) > 1 and message.content.startswith('>eventadd '):
            event_data = message.content.replace('>eventadd ', '').strip().split(' ')
            name = ' '.join(event_data[:-1])
            date = event_data[-1]
            try:
                dt = datetime.datetime.strptime(date, '%Y-%m-%d')
                data = self.getDatabase()
                data['events'][name] = date
                self.saveDatabase(data)
                await message.channel.send('Your event has been saved successfully! :bookmark_tabs:')
            except Exception as e:
                print(str(e))
                await message.channel.send('There has been a problem with your event! :disappointed_relieved:\n Check if the command format is correct:\n>eventadd [name] [date in format yyyy-MM-dd]')
        
        elif len(message.content.split(' ')) > 1 and message.content.startswith('>eventdel '):
            name = message.content.replace('>eventdel ', '').strip()
            try:
                data = self.getDatabase()
                data['events'].pop(name)
                self.saveDatabase(data)
                await message.channel.send('Your event has been deleted successfully!\nYou can forget about it! :hourglass:')
            except Exception as e:
                print(str(e))
                await message.channel.send("Oh no! There's a problem with the command :face_with_spiral_eyes:\nCheck if the event exists or the command format!")

        elif len(message.content.split(' ')) > 1 and message.content.startswith('>event '):
            today = datetime.date.today()
            data = self.getDatabase()
            events = data['events']
            name = message.content.replace('>event ', '').strip()
            try:
                date = events[name]
                date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                if date > today:
                    delta = date - today
                    await message.channel.send("It's gonna be LEGEN-\nwait for it ...\nDARY!\nLEGENDARY!!\nIn " + str(delta.days) + " days :clock1:")
                elif date < today:
                    delta = today - date
                    await message.channel.send("It's been " + str(delta.days) + " days since that memorable day! :disguised_face:")
                else:
                    await message.channel.send("IT'S HAPPENING! IT'S HAPPENING! :confetti_ball: :tada:")
            except Exception as e:
                print(str(e))
                await message.channel.send("Not this time :cold_face:\nCheck if the event exists or the command format!")

        elif message.content == '>welcomes' or message.content == '>welcome':
            response = "We're welcoming only VIPs :sunglasses:\n"
            data = self.getDatabase()
            welcomes = data['welcome']
            if len(welcomes) > 0:
                for name in welcomes:
                    response += name + '\n'
                await message.channel.send(response)
            else:
                await message.channel.send("There's no VIPs to welcome yet :sob:")

        elif message.content == '>welcomechange':
            data = self.getDatabase()
            option = not data['welcome_option']
            data['welcome_option'] = option
            self.welcome_option = option
            self.saveDatabase(data)
            option_str = 'enabled'
            if not option:
                option_str = 'disabled'
            await message.channel.send('Welcoming option is now ' + option_str + ' :handshake:')

        elif len(message.content.split(' ')) > 1 and message.content.startswith('>welcomeadd '):
            name = message.content.replace('>welcomeadd ', '').strip()
            data = self.getDatabase()
            data['welcome'].append(name)
            self.welcome_usernames = data['welcome']
            self.saveDatabase(data)
            await message.channel.send('Successfully added ' + name + ' to the welcome list :partying_face:')

        elif len(message.content.split(' ')) > 1 and message.content.startswith('>welcomedel '):
            name = message.content.replace('>welcomedel ', '').strip()
            data = self.getDatabase()
            data['welcome'].remove(name)
            self.welcome_usernames = data['welcome']
            self.saveDatabase(data)
            await message.channel.send('I see. ' + name + ' is not a VIP. He will not be welcomed anymore :rage:')

        elif message.content == '>meme':
            data = json.loads(get("https://meme-api.herokuapp.com/gimme").text)
            while data['nsfw'] != False:
                data = json.loads(get("https://meme-api.herokuapp.com/gimme").text)
            meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
            await message.channel.send(embed=meme)

    async def welcomeUser(self, username):
        str_index = random.randint(0, len(self.welcome_strs)-1)
        await self.client.get_channel(self.channel_id).send(username + ' just logged in to discord!\n' + self.welcome_strs[str_index])
    
    def getDatabase(self):
        return json.load(open('database.json'))
    
    def saveDatabase(self, data):
        open('database.json', 'w').write(json.dumps(data))