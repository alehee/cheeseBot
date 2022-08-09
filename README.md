# cheeseBot
<p align="center">
  <img src="https://github.com/alehee/cheeseBot/blob/main/git_res/logo.png" style="height:150px;">
</p>

Simple discord bot written in Python. Purpose of this project is to learn some bot-writing basics, so if you want to check some examples feel free! All of the documentation I used can be found in [discordpy docs](https://discordpy.readthedocs.io/en/stable/)

Bot is written for **single server handle only**, so the database is just a simple json file. If you want go worldwide with your bot prepare some proper database server!

All bot commands are triggered by '>' sign before the command.

**Bot is still in development, some options may not be working now!**

## Features
* check/help command

## Upcoming features
* events
* welcoming logged in discord *VIPs*
* random meme

## Commands
```
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
```

## Used technology
* Python 3

## Packages
* discord.py
* json
* [pyrandmeme](https://pypi.org/project/pyrandmeme/)

## Download and installation
You can download the master branch with code.

If you're trying to run it on yourself you need to prepare your token and save it in directory as *token.json*
```json
{
    "token": "your_token_here"
}
```

## Thank you!
Thank you for peeking at my project!

If you're interested check out my other stuff [here](https://github.com/alehee)
