from flask import Blueprint, render_template, request, flash, url_for, redirect
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from .. import logic
from .. import db

account_bp = Blueprint("account_bp", __name__)
class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.Length(min=6, max=30)
    ])


@account_bp.route("/login", methods=["GET", "POST"])
def login():
  error = None
  form = RegistrationForm(request.form)
  if request.method == 'POST' and form.validate():
      if db.is_user(form):
          return redirect(url_for('homehandler'))
      else:
        return redirect(url_for('account_bp.register'))
  return render_template('views/login.html', error=error)

@account_bp.route("/register", methods=['GET', 'POST'])
def register():
  error = None
  form = RegistrationForm(request.form)
  if request.method == 'POST':
    if form.validate():
      db.register_user(form)
      return redirect(url_for('homehandler'))
    else:
      error = '''Invalid username or password. Your username must be at least 4 
         characters and at most 25. Your password must be at least 6 characters and at most 30.'''
  return render_template('views/register.html', error=error)
