from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddPuppyForm(FlaskForm):

    name = StringField('Name of Puppy:')
    submit = SubmitField('Add Puppy')

class DelPuppyForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')

class AddOwnerForm(FlaskForm):

    name = StringField('Name of Owner:')
    puppy_id = IntegerField('Your Puppy id:')
    submit = SubmitField('Add Owner')
