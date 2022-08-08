import discord
import json
import time

class Cheese:
    token = json.load(open('token.json'))['token']
    client = discord.Client()

    async def processMessage(self, message):
        if message.author == self.client.user or not message.content.startswith('>'):
            return

        if message.content == '>check':
            await message.channel.send("Howdy! I'm alive and completly fine.\nBy the way did you know that now is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))