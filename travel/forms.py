from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from werkzeug import datastructures
from wtforms.fields.simple import SubmitField
from wtforms.validators import InputRequired, Email, EqualTo
from wtforms.fields import StringField, TextAreaField, PasswordField, SubmitField
from flask_wtf.file import FileRequired, FileField, FileAllowed
from werkzeug.utils import secure_filename
import os

ALLOWED_FILES = {'png', 'jpg', 'PNG', 'JPG'}

class DestinationForm(FlaskForm):
    name = StringField('Destination Name', validators=[InputRequired('Please enter a destination name')])
    description = TextAreaField('Description', validators=[InputRequired('Please enter a description')])
    image = FileField('Destination Image', validators=[
            FileRequired(message='File Required'),
            FileAllowed(ALLOWED_FILES, message='Only supports png and jpg')
    ]) 
    currency = StringField('Currency', validators=[InputRequired('Input required')])

    submit = SubmitField("Create Destination")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('Please enter a username')])
    password = PasswordField('Password', validators=[InputRequired('Please enter a password')])

    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('Please enter a username')])
    email = StringField('Email', validators=[InputRequired('Please enter an email'), Email()])
    password = PasswordField('Passsword', validators=[InputRequired('Please enter a password')])
    confirm = PasswordField('Password Confirmation', validators=[InputRequired(), EqualTo('password', 'Passwords do not match')])

    submit = SubmitField('Login')

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', validators=[InputRequired()])
    
    submit = SubmitField('Comment')




