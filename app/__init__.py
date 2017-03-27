# -*- encoding: utf-8 -*-
'''
FAB CITY DASHBOARD - VISUALIZAR'16
--------------------------------------------
A dashboard for all the Fab Cities where citizens can understand the existing resilience of cities and how the Maker movement is having an impact on this.
------------------------------------------
license: AGPL 3.0
---------------------------------------------

A project by: IAAC | Fab Lab Barcelona - Fab City Research Lab from the Fab City Global discussions.
Proposed at Visualizar'16 at Medialab Prado: http://fablabbcn.org/news/2016/05/12/visualizar.html

Participants at Visualizar'16:
    - Massimo Menichinelli (IAAC | Fab Lab Barcelona - Fab City Research Lab)
    - Mariana Quintero (IAAC | Fab Lab Barcelona - Fab City Research Lab)
    - Julien Paris (PING | LabSIC - Paris 13)
---------------------------------------------
'''

from flask import Flask
from flask_mail import Mail
from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)

# Setup config
from app.settings import ConfigClass
app.config.from_object(__name__+'.ConfigClass')

from app.settings import CreateAdminUser
app.config.from_object(__name__+'.CreateAdminUser')

# Upload photos config
uploaded_photos = UploadSet('photos', IMAGES)
configure_uploads(app, uploaded_photos)

# Initialize Flask-Mail
mail = Mail(app)



from app import views

# Load Blueprints
from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')

@app.route("/debug")
def debug():
    return "Hello world!"

if __name__ == "__main__":
    app.run()
