from flask import Flask, flash, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (BooleanField, StringField, SubmitField,
                    TextField, RadioField, SelectField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoClass(FlaskForm):
    breed = StringField('What breed are you?*', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered?')
    food_choice = SelectField('Pick your favorite food:',
                              choices=[('chicken', 'Chicken'),
                                       ('beef', 'Beef'),
                                       ('fish', 'Fish')])
    mood = RadioField('Please choose your mood:',
                      choices=[('happy', 'Happy'),
                               ('excited', 'Excited')])
    feedback = TextField('Any other feedback:')
    submit = SubmitField('Submit')

class ConfirmForm(FlaskForm):
    submit = SubmitField('Confirm')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = InfoClass()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['food_choice'] = form.food_choice.data
        session['mood'] = form.mood.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thankyou'))
    return render_template('home.html', form=form)

@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    form = ConfirmForm()
    if form.validate_on_submit():
        flash('Submitted successfully!')
        return redirect(url_for('home'))
    return render_template('thankyou.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)








    #
