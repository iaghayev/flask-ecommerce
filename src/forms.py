

from flask_wtf import FlaskForm
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from wtforms import StringField, PasswordField, SubmitField, IntegerField

from src.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label='Login')

class ContactForm(FlaskForm):
    name = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    subject = StringField(label='Subject:', validators=[Length(min=2, max=50), DataRequired()])
    message = StringField(label='Message:', validators=[Length(min=20, max=255), DataRequired()])
    submit = SubmitField(label='Send Request')

class CommentForm(FlaskForm):
    comment = StringField(label='Comment:', validators=[Length(min=4, max=255), DataRequired()])
    submit = SubmitField(label='Comment')