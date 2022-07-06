from urllib import response
from urllib.request import Request
from flask import Blueprint, redirect, render_template, request, make_response, session

routes = Blueprint('routes',__name__)

@routes.route('/')
def home():
    
    return render_template("home/index.html")


@routes.route('/dashboard')
def dashboard():
    
         
    return render_template("home/dashboard.html")


#Not found
