# -*- encoding: utf-8 -*-

from app import app
from flask import Flask, render_template, jsonify

import pandas as pd
import makerlabs.fablabs_io as fio

from werkzeug.routing import Rule
# app = Flask(__name__)

# import global variables for Z2N
from .scripts.app_vars import title, metas, description, subtitle, version, authors, license, static_dir, URLroot_, fabcities

# import var dictionaries
from .scripts.app_vars import modules_html_dict, geoJSON_dict, root_basemaps, root_stats_json, regions_names

# import local scripts ### not in use so far... to get datas remotely from APIs
from .scripts.app_scripts import *

# gather global names
global_names = {
    'titleApp': title,  # name/brand of the app
    'subtitleApp': subtitle,  # explanation of what the app does
    'metas': metas,  # meta for referencing
    'description': description,  # description of the app
    'version': version,  # explanation of what the app does
    'authors': authors,  # authors in metas
    'license': license
}


def selectedRegionSpecs(selectedRegion, level):

    # print ("selectedRegionSpecs / selectedRegion : ", selectedRegion)

    regionSpecs = geoJSON_dict[selectedRegion]

    # print ("selectedRegionSpecs / regionSpecs : ", regionSpecs)

    countryLevel = "_admin_level_4"
    # level country --> display country's regions
    regionLevel = "OECD_admin_level_4"
    # level country --> display country's regions

    if selectedRegion not in regions_names and level == "regions":
        stats_js_name = selectedRegion + countryLevel
    else:
        stats_js_name = "countries_dict"

    temp_specs = regionSpecs

    temp_specs["geojson_js_var"] = regionSpecs["regions"]
    temp_specs[
        "geojson_url"] = root_basemaps + "regions/" + selectedRegion + "/" + regionSpecs[
            level] + ".geojson"

    temp_specs["dflt_data_js_var"] = stats_js_name
    temp_specs["dflt_data_url"] = root_stats_json + stats_js_name + ".js"

    # print ("selectedRegionSpecs / temp_specs : ", temp_specs)
    # format like :
    # temp_specs = {  'regions'    : 'all_countries',
    #                   'country'    : '',
    #                   'metropolitan_areas_OECD': '',
    #                   'geojson_url': u'/data_custom/geojson_basemaps/regions/World/all_countries.geojson',
    #                   'js_var'     : 'all_countries'}

    return temp_specs


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
    print

    print 'user profile/region :', user_profile, regionSelected
    print

    ### generate template corresponding to user_profile
    user_specs = generateTemplate(user_profile)
    print "user_specs", user_specs
    print

    ### generate template corresponding to user_profile
    region_specs = selectedRegionSpecs(
        regionSelected, "regions")  ###### "regions" var NOT GENERAL ENOUGH
    print "region_specs", region_specs
    print

    return render_template("user_driven_template.html",
                           index          = False,
                           glob           = global_names,
                           user_profile   = user_profile,     ### settings for user_profile from user_profiles
                           user_specs     = user_specs,       ### description of every row for template
                           regionSelected = regionSelected,   ### specs to
                           region_specs   = region_specs,     ### specs for Jinja / get corresponding geojson (js var names and urls)
                           mod_incl       = modules_html_dict ### global dict to get corresponding .html modules
                           )


@app.route('/test_blank')
def test_blank():
    print '-' * 10, 'VIEW BLANK TEST', '-' * 50
    return render_template(
        "blank_map_test.html",
        index=True,
        glob=global_names, )


# automatically creates specific routes for every dataset in collections
@app.route('/test_leaflet/<selection>')
def data_leaflet_map(selection):

    print
    print '-' * 10, 'VIEW RENDERING / Leaflet ', selection, '-' * 50
    print 'selection :', selection

    # find datas corresponding to selection

    # call python script here if you want to compute indicators before rendering data

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

    # find datas corresponding to selection

    # call python script here if you want to compute indicators before rendering data

    # preferences bootstrap / modules

    return render_template(
        "test_d3leaflet.html",
        glob=global_names,
        map_=True,
        force=False, )


# Tests by massimo
@app.route("/api/cities")
def fabicites_list():
    return jsonify(fabcities)

@app.route("/api/labs")
def labs_map():
    labs_geojson = fio.get_labs(format="geojson")
    return labs_geojson

@app.route("/oecd/regional-data")
def regional_data():
    regional_data = pd.read_csv(
        app.static_folder + "/data_custom/json_stats/OECD/regional.csv",
        encoding="utf-8")
    # return regional_data.to_html()
    return regional_data.to_json(orient='records')


@app.route("/oecd/national-data")
def national_data():
    national_data = pd.read_csv(
        app.static_folder + "/data_custom/json_stats/OECD/national.csv",
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


@app.route("/oecd/nat-regio-city")
def oecd_nat_regio_city():
    return render_template(
        "oecd-nat-regio-city.html",
        glob=global_names,
        map_=True,
        force=False, )


@app.route("/oecd/nat-regio-city-slider")
def oecd_nat_regio_city_slider():
    return render_template(
        "oecd-nat-regio-city-slider.html",
        glob=global_names,
        map_=True,
        force=False, )
