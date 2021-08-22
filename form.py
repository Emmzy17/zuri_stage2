from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=100)])
	message = TextAreaField('Message', validators=[DataRequired()])
	submit = SubmitField('Submit')
	
