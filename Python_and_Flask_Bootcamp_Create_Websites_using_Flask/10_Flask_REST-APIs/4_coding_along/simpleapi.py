from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

api = Api(app)
jwt = JWT(app, authenticate, identity)

{'name': 'Rufus'}
puppies = []

# Models
##################################################
class Puppy(db.Model):

    name = db.Column(db.String(80), primary_key=True)

    def __init__(self, name):
        self.name = name

    def json(self): # Flask api requires you to return a json representation of that object
        return {'name':self.name}
##################################################


class PuppyNames(Resource):

    def get(self, name):
        pup = Puppy.query.filter_by(name=name).first()
        if pup:
            return pup.json()
        else:
            return {'name':None}, 404

    def post(self, name): # The name will be passed through the URL
        pup = Puppy(name=name)
        db.session.add(pup)
        db.session.commit()
        return pup.json()

    def delete(self, name):
        pup = Puppy.query.filter_by(name=name).first()
        db.session.delete(pup)
        db.session.commit()
        return {'note': 'delete success'}

class AllNames(Resource):

    # @jwt_required() # Now, if you want all the puppies, you have to get authenticated first
    def get(self):
        puppies = Puppy.query.all()
        return [pup.json() for pup in puppies]

# This end point connects with the PuppyNames class so that
# you can call its methods
api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames, '/puppies')

if __name__ == '__main__':
    app.run(debug=True)
