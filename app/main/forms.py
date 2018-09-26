from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validatrors import DataRequired


class NameForm(FlaskForm):
	name = StringField('What is your name?', validatrors=[DataRequired()])
	submit = SubmitField('Submit')