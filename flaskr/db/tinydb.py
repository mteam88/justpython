from tinydb import TinyDB, Query
import bcrypt

accountdb = TinyDB('accountdb.json')

def registerUser(registrationform):
    salt = bcrypt.gensalt()
    hashedpasswd = str(bcrypt.hashpw(bytes(registrationform.username.data, encoding='utf-8'), salt))

    accountdb.insert({'username': registrationform.username.data, 'password': hashedpasswd})