## Testing purposes scripts

from asyncio import events
import json

def getDatabase():
    return json.load(open('database.json'))

def getEvents():
    data = getDatabase()
    events = data['events']
    return events

def getWelcome():
    data = getDatabase()
    option = data['welcome_option']
    users = data['welcome']
    return (option, users)

def addEvent(name, date):
    data = getDatabase()
    data['events'][name] = date
    open('database.json', 'w').write(json.dumps(data))

# "Boisko": "2022-08-10"
def delEvent(name):
    data = getDatabase()
    data['events'].pop(name)
    open('database.json', 'w').write(json.dumps(data))

arr = ['A', 'B', 'C']
#print(' '.join(arr[:-1]))

#print(getEvents())
#print(getWelcome())
#addEvent('Dentist', '2022-08-11')
#delEvent('Boisko')