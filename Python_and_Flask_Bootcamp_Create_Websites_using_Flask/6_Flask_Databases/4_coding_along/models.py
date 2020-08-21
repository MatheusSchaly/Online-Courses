import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

####
class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # ONE TO MANY
    # Puppy to Many Toys
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')
    # ONE TO ONE
    # Puppy to One Onwer
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and onwer is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner yet!"

    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.item_name)

class Toy(db.Model):

    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Columns(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(df.Integer, primary_key=True)
    name = db.Column(db.Text)

    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
