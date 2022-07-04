from flask import Blueprint, render_template, request

routes = Blueprint('routes',__name__)

@routes.route('/')
def home():
    return render_template("home/index.html")


@routes.route('/dashboard')
def dashboard():
    return render_template("home/dashboard.html")

#Not found
@routes.app_errorhandler(404)
def error_404(error):
    return render_template('home/notfound.html'), 404