from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired

class AuthForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password:', [
        validators.DataRequired(),
        validators.EqualTo('confirm_password', message='Passwords must match'),
        validators.Length(min=8, message='Password must be at least 8 characters long')
    ])
    confirm_password = PasswordField('Confirm Password:')
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name: ', validators=[DataRequired()])
    organization = StringField('Organization: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password:', [
        validators.DataRequired(),
        validators.Length(min=8, message='Password must be at least 8 characters long')
    ])    
    submit = SubmitField('Login')



