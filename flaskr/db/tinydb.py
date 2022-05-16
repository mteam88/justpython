from tinydb import TinyDB, Query
import flask_bcrypt
bcrypt = flask_bcrypt.Bcrypt()

accountdb = TinyDB('accountdb.json')

UserQuery=Query()

def register_user(registrationform):
    hashedpasswd = hashsaltpassword(registrationform.password.data)
    accountdb.insert({'username': registrationform.username.data, 'password': hashedpasswd})

def is_user(loginform):
    'returns True if login form correlates to a user else False'
    return bool(accountdb.search((UserQuery.username == loginform.username.data) & (UserQuery.password.test(bcrypt.check_password_hash,loginform.password.data))))

def username_exists(form):
    return bool(accountdb.search((UserQuery.username == form.username.data)))

def hashsaltpassword(password: str):
    return bcrypt.generate_password_hash(password).decode('utf-8')