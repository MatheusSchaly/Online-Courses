# We need these env variables because we are doing the authentication locally
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
#############################################################################
from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

blueprint = make_google_blueprint(client_id='748128872032-ibo0kdrukqbtgbul9qpmnj26nc8v3fhd.apps.googleusercontent.com',
                                  client_secret='cltrVNFtjcxjWFOuk6Ogikl3',
                                  offline=True, scope=['profile', 'email'])

app.register_blueprint(blueprint, url_prefix='/login') # Goes to Google login page
#############################################################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    # RETURN ERROR INTERNAL SERVER ERROR IF NOT LOGGED IN!!
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text # Checks if there is actually something in the response
    email = resp.json()['email']
    #######################################################
    return render_template('welcome.html', email=email)

@app.route('/login/google')
def login():
    if not google.authorized: # From Flask-Dance
        return render_template(url_for('google.login')) # From Flask-Dance
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text # Checks if there is actually something in the response
    email = resp.json()['email']
    return render_template('welcome.html', email=email)

if __name__ == '__main__':
    app.run()

# OAuth - Open Authorization
