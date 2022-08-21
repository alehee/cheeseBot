from cheese import Cheese

VERSION = '1.1.0.0'
print('Running cheeseBot v. {0}'.format(VERSION))

cheese = Cheese()

### Events handle
@cheese.client.event
async def on_ready():
    print('Logged in as {0}'.format(cheese.client.user))

@cheese.client.event
async def on_message(message):
    await cheese.processMessage(message)

@cheese.client.event
async def on_member_update(old_member, new_member):
    if (str(old_member.status) == 'offline') and (str(new_member.status) == 'online' or str(new_member.status) == 'idle') and (new_member.nick in cheese.welcome_usernames or new_member.name in cheese.welcome_usernames):
        username = new_member.nick
        if (new_member.name in cheese.welcome_usernames):
            username = new_member.name
        await cheese.welcomeUser(username)
### ==========

cheese.client.run(cheese.token)