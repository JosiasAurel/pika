

from tinydb import Query, TinyDB

db = TinyDB('./db.json')

User = Query()

db.insert({'original_url': 'https://password-generator.josiasdev.best',  'short_url': 'bawzz'})

data = db.search(User['original_url'] == 'https://password-generator.josiasdev.best')

print(data)

