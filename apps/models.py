from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(256))
    perfil = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, username, password, perfil):
        self.username = username
        self.password = password
        # self.password = self.__create_password(password)
        self.perfil = perfil

    # def __create_password(self, password):
    #     return generate_password_hash(password)

    # def verify_password(self, password):
    #     return check_password_hash(self.password, password)