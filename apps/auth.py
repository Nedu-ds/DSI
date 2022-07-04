from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "LOGIN"

@auth.route('/logout')
def logout():
    return "LOGOUT"

@auth.route('/sign-up')
def sign_up():
    return "SIGN UP"