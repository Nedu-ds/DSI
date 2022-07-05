from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'jasdoqjwel;asdflj'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:J23s_C21x!p7@localhost/dsi'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from flask_sqlalchemy import SQLAlchemy

    db = SQLAlchemy()
    db.init_app(app)

    from .routes import routes
    from .auth import auth
    from .models import models

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(models, url_prefix='/')

    return app