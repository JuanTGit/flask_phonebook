from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Register')