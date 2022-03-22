import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# creer chemin de la base de donné

basedir = os.path.abspath('')

# configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# creer une instance de la bd
db = SQLAlchemy(app)


# Models

class User(db.Model):
    # pour changer le nom de la table correspondate
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.Text)
    firstName = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, lastName, firstName, age):
        self.lastName = lastName
        self.firstName = firstName
        self.age = age

    def __repr__(self):
        return f"firstname : {self.firstName} ({self.id})"
