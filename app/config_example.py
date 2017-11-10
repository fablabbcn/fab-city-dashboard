import os

#Flask settings
os.environ['SECRET_KEY'] = '22222'
os.environ['UPLOADED_PHOTOS_DEST'] = "app/upload_photos"
#Flask-Mail settings
os.environ['MAIL_USERNAME'] = 'email@example.com'
os.environ['MAIL_PASSWORD'] = 'password'
os.environ['MAIL_DEFAULT_SENDER'] = 'email@example.com'

#Admin user default
os.environ['ADMIN_USER'] = 'user'
os.environ['ADMIN_EMAIL'] = 'email@example.com'
os.environ['ADMIN_PASSWORD'] = 'password'