import simplejson as json
from tinydb.storages import  MemoryStorage
from tinydb import TinyDB, Query, where

db = TinyDB('g:/python/section2/python_practice/files/database.db')

# db = TinyDB(storage = MemoryStorage, default_table ='users')

users = db.table("users")
todos = db.table("todos")

Users = Query()
Todos = Query()


print(users.search(Users.id ==7))

print(users.search(where('address')['zipcode'] == '90566-7771'))
print(users.search(where('address').zipcode == '90566-7771'))
# users.insert({'name' : 'kim', 'email' : 'test@google.com'})
# todos.insert({'name' : 'homework', 'complete' : False})

# with open('g:/python/section2/python_practice/files/users.json', 'r') as infile:
#     r = json.loads(infile.read())
#     for u in r:
#         users.insert(u)

# users.purge()
# todos.purge()
