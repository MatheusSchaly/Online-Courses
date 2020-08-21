import os
from flask import Flask, render_template, redirect, url_for, flash
from forms import AddPuppyForm, AddOwnerForm, DelPuppyForm
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Creating the app
app = Flask(__name__)

# Setting the database
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating the database
db = SQLAlchemy(app)
Migrate(app, db)

# Creating the models
class Puppy(db.Model):

    __tablename__ = 'puppy'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}."
        else:
            return f"Puppy name is {self.name} and has no owner assigned yet."

class Owner(db.Model):

    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

# Creating the views
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/adding_puppy', methods=['GET', 'POST'])
def puppy():
    form = AddPuppyForm()
    if form.validate_on_submit():
        name = form.name.data
        new_puppy = Puppy(name)
        db.session.add(new_puppy)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('add_puppy.html', form=form)

@app.route('/showing_list')
def list():
    puppies = Puppy.query.all()
    owner_list = Owner.query.all()
    print(type(owner_list))
    if owner_list:
        print('Hello')
        owner = owner_list[-1].name
    return render_template('list.html', puppies=puppies, owner=owner)

@app.route('/deleting_puppy', methods=['GET', 'POST'])
def delete_puppy():
    form = DelPuppyForm()
    if form.validate_on_submit():
        id = form.id.data
        puppy = Puppy.query.get(id)
        db.session.delete(puppy)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('del_puppy.html', form=form)

@app.route('/adding_owner', methods=['GET', 'POST'])
def owner():
    form = AddOwnerForm()
    if form.validate_on_submit():
        flash('is now a puppy owner!')
        name = form.name.data
        puppy_id = form.puppy_id.data
        new_owner = Owner(name, puppy_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('add_owner.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
