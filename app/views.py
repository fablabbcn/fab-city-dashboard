# -*- encoding: utf-8 -*-

from app import app
from flask import Flask, render_template

import pandas as pd

from werkzeug.routing import Rule
# app = Flask(__name__)

# import global variables for Z2N
from .scripts.app_vars import title, metas, description, subtitle, version, authors, licenceCC, static_dir, URLroot_

# import var dictionaries : user_profiles, regions dicts...
from .scripts.app_vars import user_profiles, modules_html_dict, geoJSON_dict, root_basemaps

# import local scripts
from .scripts.app_scripts import *

# gather global names
global_names = {
    'titleApp': title,  # name/brand of the app
    'subtitleApp': subtitle,  # explanation of what the app does
    'metas': metas,  # meta for referencing
    'description': description,  # description of the app
    'version': version,  # explanation of what the app does
    'authors': authors,  # authors in metas
    'licenceCC': licenceCC
}


# inform jinja how to create template corresponding to user
def generateTemplate(userProfile):

    canvas = []

    canvas_raw = user_profiles[
        userProfile]  ## return a list of rows' dictionaries with following format
    ### [   { "400px" : [ {"reg_ma" : 9 }, {"reg_id": 3 } ] },
    ###     { "50px" :  [ {"tool_la" : 12 } ] },
    ###     { "600px" : [ {"con_re" : 4 }, {"wor_ma": 8 } ] },
    ### ],,

    counter = 1

    for row in canvas_raw:

        for height, modules in row.items():

            row_id = "row_" + str(counter)
            temp_template = {"row": row_id, "height": height, "columns": []}

            for module in modules:
                index_module = modules.index(module)
                for mod_name, mod_size in module.items():
                    mod_dict = {"index_module": index_module,
                                "module": mod_name,
                                "width": mod_size}
                    temp_template["columns"].append(mod_dict)

        canvas.append(temp_template)
        counter += 1

    return canvas


def selectedRegionSpecs(selectedRegion):
    
    regionSpecs                = geoJSON_dict[selectedRegion]
    regionSpecs["js_var"]      = regionSpecs[""]
    regionSpecs["geojson_url"] = root_basemaps +"regions/"+ regionSpecs[""] + ".geojson"
    
    return regionSpecs

@app.route('/')
@app.route('/index')
def index():
    print '-' * 10, 'VIEW INDEX', '-' * 50
    return render_template(
        "index.html",
        index=True,
        glob=global_names, )


@app.route('/user/<user_profile>/<regionSelected>')
def user_entry(user_profile, regionSelected):
    print '-' * 10, 'VIEW USER TEMPLATE', '-' * 50

    print 'user profile/region :', user_profile, regionSelected

    ### generate template corresponding to user_profile
    user_specs = generateTemplate(user_profile)
    print "user_specs", user_specs

    return render_template("user_driven_template.html",
                           index          = True,
                           glob           = global_names,
                           user_profile   = user_profile,     ### settings for user_profile from user_profiles
                           user_specs     = user_specs,       ### description of every row for template
                           regionSelected = regionSelected,
                           mod_incl       = modules_html_dict ### global dict to get corresponding .html modules
                           )


@app.route('/test_blank')
def test_blank():
    print '-' * 10, 'VIEW BLANK TEST', '-' * 50
    return render_template(
        "blank_map_test.html",
        index=True,
        glob=global_names, )


### automatically creates specific routes for every dataset in collections
@app.route('/test_leaflet/<selection>')
def data_leaflet_map(selection):

    print
    print '-' * 10, 'VIEW RENDERING / Leaflet ', selection, '-' * 50
    print 'selection :', selection

    #find datas corresponding to selection

    #call python script here if you want to compute indicators before rendering data

    return render_template(
        "test_leaflet.html",
        glob=global_names,
        map_=True,
        force=False, )


@app.route('/test_d3leaflet/<selection>')
def data_d3leaflet_map(selection):

    print
    print '-' * 10, 'VIEW RENDERING / D3 + Leaflet ', selection, '-' * 50
    print 'selection :', selection

    #find datas corresponding to selection

    #call python script here if you want to compute indicators before rendering data

    #preferences bootstrap / modules

    return render_template(
        "test_d3leaflet.html",
        glob=global_names,
        map_=True,
        force=False, )


# Tests by massimo
@app.route("/oecd/regional-data")
def regional_data():
    regional_data = pd.read_csv(
        app.static_folder+"/data_custom/json_stats/OECD/regional.csv",
        encoding="utf-8")
    # return regional_data.to_html()
    return regional_data.to_json(orient='records')

@app.route("/oecd/national-data")
def national_data():
    national_data = pd.read_csv(
        app.static_folder+"/data_custom/json_stats/OECD/national.csv",
        encoding="utf-8")
    # return national_data.to_html()
    return national_data.to_json(orient='records')

@app.route("/oecd/test")
def oecd_test():
    return render_template(
        "oecd.html",
        glob=global_names,
        map_=True,
        force=False, )

@app.route("/oecd/nat-regio")
def oecd_nat_regio():
    return render_template(
        "oecd-nat-regio.html",
        glob=global_names,
        map_=True,
        force=False, )
