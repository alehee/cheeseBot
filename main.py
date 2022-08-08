from cheese import Cheese

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