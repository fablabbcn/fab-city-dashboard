from app import app
import os
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, SQLAlchemyAdapter
from flask import Blueprint
from flask_user.signals import user_sent_invitation, user_registered

# This part below is based on the flask-user example under BSD license

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

# Load and create Models Database
from .models import User, Role, UserInvitation
db.create_all()

# Add User to Flask-User
db_adapter = SQLAlchemyAdapter(db, User, UserInvitationClass=UserInvitation)
user_manager = UserManager(db_adapter, app)


@user_registered.connect_via(app)
def after_registered_hook(sender, user, user_invite):
    sender.logger.info("USER REGISTERED")

@user_sent_invitation.connect_via(app)
def after_invitation_hook(sender, **extra):
    sender.logger.info("USER SENT INVITATION")

# Create user admin default
if not User.query.filter(User.username==os.getenv('ADMIN_USER')).first():
        user1 = User(username=os.getenv('ADMIN_USER'), email=os.getenv('ADMIN_EMAIL'), is_enabled=True,
                password=user_manager.hash_password(os.getenv('ADMIN_PASSWORD')))
        user1.roles.append(Role(name='admin'))
        db.session.add(user1)
        db.session.commit()

# This part above is based on the flask-user example under BSD license

# Blueprint
admin = Blueprint('admin', __name__, template_folder='./templates', static_folder="./static", static_url_path="/static")

# Views
from . import views
 
