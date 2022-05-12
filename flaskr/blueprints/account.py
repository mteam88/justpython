from flask import Blueprint

account_bp = Blueprint(
  "account_bp", __name__
)


@account_bp.route("/login")
def login_user():
    return "login page!"