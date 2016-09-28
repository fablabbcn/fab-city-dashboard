from app import app
from flask import Flask, render_template #, Markup

from werkzeug.routing import Rule
#app = Flask(__name__)

### import global variables for Z2N
from .scripts.app_vars    import title, metas, description, subtitle, version, authors, licenceCC, static_dir, URLroot_
from .scripts.app_scripts import *


global_names = {
        'titleApp'          : title,             # name/brand of the app
        'subtitleApp'       : subtitle,          # explanation of what the app does
        'metas'             : metas,             # meta for referencing
        'description'       : description,       # description of the app
        'version'           : version,           # explanation of what the app does
        'authors'           : authors,           # authors in metas
        'licenceCC'         : licenceCC
    }



@app.route('/')
@app.route('/index')
def index():
    print '-'*10 , 'VIEW INDEX', '-'*50
    return render_template("index.html",
                           index = True,
                           glob  = global_names,
                           )

### automatically creates specific routes for every dataset in collections
@app.route('/<selection>')
def data_render_map(selection):
    
    print
    print '-'*10, 'VIEW RENDERING', selection, '-'*50
    print 'selection :', selection
    
    #call python script here if you want before rendering data
    
    return render_template("test_render.html",
                           glob = global_names,
                           map_ = True,
                           force= False,
                           )

