from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User

def invalid_credentials(form, Field):
    """ Username and password checker """
    username_entered = form.username.data 
    password_entered = field.data
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object in None:
        raise ValidationError("User or password is incorrect")
    elif password_entered != user_object.password:
        raise ValidationError("User or password is incorrect")

class RegistrationForm(FlaskForm):
    """Registrationn form"""
    username = StringField('username_label',validators=[InputRequired(message='Username required'),Length(min=4,max=25,message='Username must between 4 and 25 characters')])
    password = PasswordField('password_label',validators=[InputRequired(message='Password required'),Length(min=4,max=25,message='Password must between 4 and 25 characters')])
    confirm_psw = PasswordField('confirm_psw_label',validators=[InputRequired(message='Password required'),EqualTo('password',message='Password mst match')])
    submit_button = SubmitField('Create')

    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("User already exists")

class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('username_label',validators=[InputRequired(message='Username required'),Length(min=4,max=25,message='Username must between 4 and 25 characters')])
    password = PasswordField('password_label',validators=[InputRequired(message='Password required'),Length(min=4,max=25,message='Password must between 4 and 25 characters'), invalid_credentials])
    submit_button = SubmitField('Login')