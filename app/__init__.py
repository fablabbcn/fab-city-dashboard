'''          FAB CITY - VISUALIZAR 2016
--------------------------------------------
A web application powered by Flask and d3.js
to generate networks/datavisualisations
------------------------------------------
licence CC : BY - SA
---------------------------------------------

project by :
    - FABLAB BARCELONA
    - PING
    

developpers :
    - Massimo M
    - Mariana Q
    - Julien P

with the support of :
    MediaLab Prado - Visualizar 2016
    
---------------------------------------------

'''

from flask import Flask
import os

from .scripts.app_vars import static_dir ### custom static directory


app = Flask(__name__)  ### default call
#app = Flask(__name__, static_path = static_dir ) ### change static directory adress to custom for Flask


from app import views
