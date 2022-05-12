from flask import Blueprint, render_template, request, flash, url_for, redirect
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from .. import logic

account_bp = Blueprint(
  "account_bp", __name__
)
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
      if logic.isuser(form):
          return redirect(url_for(''))
      else:
        return redirect(url_for('/register'))
  return render_template('login.html', error=error)

@account_bp.route("/register", methods=['GET', 'POST'])
def register():
  error = None
  if request.method == 'POST':
      if request.form['username'] != 'admin' or request.form['password'] != 'admin':
          error = 'Invalid Credentials. Please try again.'
      else:
          return redirect(url_for(''))
  return render_template('register.html', error=error)