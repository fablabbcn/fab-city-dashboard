'''          FAB CITY - VISUALIZAR 2016
--------------------------------------------
A web application powered by Flask and d3.js
to generate networks/datavisualisations
------------------------------------------
licence CC : BY - SA
---------------------------------------------
project by :


with the support of :

---------------------------------------------

'''

from flask import Flask
import os

#from FabCity_vars_app import static_dir ### custom static directory


app = Flask(__name__)
#app = Flask(__name__, static_path = static_dir ) ### change static directory adress to custom for Flask


#### TEST to change static folder's path instead of 'app = Flask(__name__, static_path = static_dir )'
#### from snippet / url : http://flask.pocoo.org/snippets/102/


from app import views
