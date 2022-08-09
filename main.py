from cheese import Cheese

VERSION = '1.0.0.0t'
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
    if (str(old_member.status) == 'offline') and (str(new_member.status) == 'online' or str(new_member.status) == 'idle') and (new_member.nick in cheese.welcome_usernames):
        await cheese.welcomeUser(new_member.nick)
### ==========

cheese.client.run(cheese.token)