from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users

class RegistrationForm(FlaskForm):
    email = StringField('Email',
            validators = [
                DataRequired(),
                Email()
            ]
        )
    username = StringField('Username',
            validators = [
                DataRequired(),
                Length(min=2,max=30)
            ]
        )
    password = PasswordField('Password',
            validators = [
                DataRequired(),
                Length(min=6,max=50)
            ]
        )
    confirm_password = PasswordField('Confirm Password',
            validators = [
                DataRequired(),
                EqualTo('password')
            ]
        )
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        username = Users.query.filter_by(Username = username.data).first()

        if username:
            raise ValidationError('Username taken')

    def validate_email(self, email):
        user = Users.query.filter_by(Email = email.data).first()

        if user:
            raise ValidationError('Email already in use')
class PostForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
        )
    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
        )
    title = StringField('Title',
            validators = [
                DataRequired(),
                Length(min=1,max=100)
            ]
        )
    content = StringField('Text',
            validators = [
                DataRequired(),
                Length(min=1,max=1000)
            ]
        )
    submit = SubmitField('Post!')
