from flask_user import UserMixin
from . import db

# This part below is based on the flask-user example under BSD license 

# User -  Model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default=' ')
    reset_password_token = db.Column(db.String(100), nullable=False, server_default='')
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())
    is_enabled = db.Column(db.Boolean(), nullable=False, server_default='0')
    first_name = db.Column(db.String(100), nullable=False, server_default=u' ')
    last_name = db.Column(db.String(100), nullable=False, server_default=u' ')
    avatar_photo = db.Column(db.String(100), nullable=False, server_default=u' ')

    # role - relation
    roles = db.relationship('Role', secondary='users_roles',
        backref=db.backref('users', lazy='dynamic'))

# Role - Model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

# UserRoles - Table
class UserRoles(db.Model):
    __tablename__ = 'users_roles'
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'), primary_key=True)

# UserInvitation - Model
class UserInvitation(db.Model):
    __tablename__ = 'user_invite'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    # save the user of the invitee
    invited_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # token used for registration page to identify user registering
    token = db.Column(db.String(100), nullable=False, server_default='')

# This part above is based on the flask-user example under BSD license
