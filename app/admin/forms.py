import os
# Flask-WTF v0.13 renamed Flask to FlaskForm
#try:
from flask_wtf import FlaskForm             # Try Flask-WTF v0.13+
#except ImportError:
#    from flask_wtf import Form as FlaskForm     # Fallback to Flask-WTF v0.12 or older
from wtforms import TextField, TextAreaField, SubmitField,StringField, BooleanField, FormField, validators
from flask_wtf.file import FileField, FileAllowed, FileRequired


# Role - Form
class RoleForm(FlaskForm):
    name = StringField('role')
    submit = SubmitField('+')

# User - Form
class UserForm(FlaskForm) :
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])
    submit = SubmitField('Save')

# Avatar - Form
class AvatarUploadForm(FlaskForm):
    photo = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only, jpg or png!')
    ])
    submit = SubmitField('Save')
