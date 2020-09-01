

from tinydb import Query, TinyDB

db = TinyDB('./db.json')

User = Query()

ing = db.insert({'original_url': 'https://password-generator.josiasdev.best',  'short_url': 'bawzz'})
print(ing)

data = db.search(User['original_url'] == 'https://password-generator.josiasdev.best')

print(data)

