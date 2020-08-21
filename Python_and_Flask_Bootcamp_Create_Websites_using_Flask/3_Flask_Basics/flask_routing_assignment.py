from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome! Go to /pupppy_latin/name to se your name in puppy latin!</h1>'

@app.route('/puppy_latin/<name>')
def puppylatin(name):
    latin_name = ''
    if name[-1] == 'y':
        latin_name = name[:-1] + 'iful'
    else:
        latin_name = name + 'y'
    return '<h1>Hi {}! Your puppy latin name is {}</h1>'.format(name, latin_name)

if __name__ == '__main__':
    app.run(debug=True)
