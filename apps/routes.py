from flask import Blueprint, redirect, render_template, request, url_for, flash
from .models import User, db

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

@routes.route('/usuarios')
def usuarios():
    all_users = User.query.all()
    return render_template("home/usuarios.html", users = all_users)

@routes.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        perfil = request.form['perfil']

        new_user = User(usuario, password, perfil)
        db.session.add(new_user)
        db.session.commit()

        flash("Usuario creado exitosamente")
        return redirect(url_for('routes.usuarios'))
    
@routes.route('/update', methods = ['GET','POST'])
def update():
    if request.method == 'POST':
        users = User.query.get(request.form.get('id'))
        
        users.usuario = request.form['usuario']
        users.perfil = request.form['perfil']

        db.session.commit()

        flash("Usuario modificado exitosamente")
        return redirect(url_for('routes.usuarios'))

@routes.route('/delete', methods = ['GET','POST'])
def delete():
    user = User.query.get(request.form.get('id'))
    db.session.delete(user)
    db.session.commit()
    flash("Usuario eliminado exitosamente")
    return redirect(url_for('routes.usuarios'))