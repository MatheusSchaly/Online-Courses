from user import User

# This is to mimic the models
users = [User(1, 'Jose', 'mypassword'),
         User(2, 'Mimi', 'secret')
]

# Dictonary comprehension
# Creates this: {'Jose': User_Object_Jose}
username_table = {u.username: u for u in users}
# Creates this: {'1': User_Object_1}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    # check if user exists
    # if so, return user
    user = username_table.get(username, None) # If not found, return None
    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
