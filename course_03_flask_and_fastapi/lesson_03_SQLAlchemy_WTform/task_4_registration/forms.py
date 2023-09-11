from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp

class RegisterForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8), Regexp(regex=r'^.*(?=.*\d)(?=.*[a-zA-Z]).*$')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    birthdate = DateField('Birthday date', validators=[DataRequired()])
    agreement = BooleanField('I agree to the processing of personal data', false_values=None)
