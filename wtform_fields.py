from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    """Registrationn form"""
    username = StringField('username_label')
    password = PasswordField('password_label')
    confirm_psw = PasswordField('confirm_psw_label')

