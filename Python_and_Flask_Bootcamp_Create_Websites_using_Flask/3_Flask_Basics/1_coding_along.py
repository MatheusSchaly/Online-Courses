from flask import Flask

app = Flask(__name__)

# View 1
@app.route('/') #127.0.0.1:5000
def index():
    return '<h1>Hello Puppy!</h1>'

# View 2
@app.route('/information') #127.0.0.1:5000/information
def info():
    return '<h1>Puppies are cute!</h1>'

# View 3
@app.route('/puppy/<name>')
def puppy(name):
    return '100th letter: {}'.format(name[100])

if __name__ == '__main__':
    app.run(debug=True)
