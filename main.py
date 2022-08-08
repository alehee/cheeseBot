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
### ==========

cheese.client.run(cheese.token)