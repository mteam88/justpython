from tinydb import TinyDB, Query
import bcrypt

accountdb = TinyDB('accountdb.json')

UserQuery=Query()

def register_user(registrationform):
    hashedpasswd = hashsaltpassword(registrationform.password.data)
    accountdb.insert({'username': registrationform.username.data, 'password': hashedpasswd})

def is_user(loginform):
    'returns True if login form correlates to a user else False'
    return (accountdb.search((UserQuery.username == loginform.username.data) & (UserQuery.password == hashsaltpassword(loginform.password.data))))

def hashsaltpassword(password: str):
    salt = bcrypt.gensalt()
    return str(bcrypt.hashpw(bytes(registrationform.username.data, encoding='utf-8'), salt))