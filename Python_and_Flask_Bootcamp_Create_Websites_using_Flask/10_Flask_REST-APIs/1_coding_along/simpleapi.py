from flask import Flask
# Resource allows us to create a resource to connect to
# Api is a wrapper around the entire application that allows
# the resource to actually connect
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app) # Wrapping our application

class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
