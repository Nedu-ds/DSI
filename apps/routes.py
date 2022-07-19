from ast import Try
from flask import Blueprint, redirect, render_template, request, url_for, flash, session
from .models import User, db

routes = Blueprint('routes',__name__)

#Index
@routes.route('/')
def home():
    if 'username' in session:
        username = session['username']
        perfil = session['perfil']
    return render_template("home/index.html", usuario = username, perfil = perfil)

#Dashboard
@routes.route('/dashboard')
def dashboard():  
    return render_template("home/dashboard.html")

#Not found
@routes.app_errorhandler(404)
def error_404(error):
    return render_template('home/notfound.html'), 404

#Before request
@routes.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['routes.home','routes.usuarios','routes.dashboard']:
        return redirect (url_for('routes.login'))
    elif 'username' in session and request.endpoint in ['routes.login',]:
        return redirect(url_for('routes.home'))

#After request
@routes.after_request
def after_request(response):
    return response

#Users
@routes.route('/usuarios')
def usuarios():
    all_users = User.query.all()
    return render_template("home/usuarios.html", users = all_users)

#Insert Users
@routes.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        try:      
            usuario = request.form['usuario']
            password = request.form['password']
            perfil = request.form['perfil']

            new_user = User(usuario, password, perfil)
            db.session.add(new_user)
            db.session.commit()
            flash("Usuario creado exitosamente", 'success')
        except Exception as e:
            flash("El nombre de usuario ya existe, por favor escriba uno diferente", 'error')
        return redirect(url_for('routes.usuarios'))

#Update Users   
@routes.route('/update', methods = ['GET','POST'])
def update():
    if request.method == 'POST':
        users = User.query.get(request.form.get('id'))
        
        users.username = request.form['usuario']
        users.perfil = request.form['perfil']
        
        db.session.commit()
        flash("Usuario modificado exitosamente", 'success')
        return redirect(url_for('routes.usuarios'))

#Delete Users
@routes.route('/delete', methods = ['GET','POST'])
def delete():
    user = User.query.get(request.form.get('id'))
    db.session.delete(user)
    db.session.commit()
    flash("Usuario eliminado exitosamente", 'success')
    return redirect(url_for('routes.usuarios'))

#Login
@routes.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username = username).first()
        perfil = user.perfil
        if user is not None and user.verify_password(password):
            session['username'] = username
            session['perfil'] = perfil
            return redirect(url_for('routes.home'))
        else:
            flash('Usuario o contraseña incorrectos') 
    return render_template("home/login.html")
    
#Logout
@routes.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('routes.login'))
