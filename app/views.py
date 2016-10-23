# -*- encoding: utf-8 -*-

from app import app
from flask import Flask, render_template, jsonify

import pandas as pd
import makerlabs.fablabs_io as fio

from werkzeug.routing import Rule

# import global variables for Z2N
from .scripts.app_vars import title, metas, description, subtitle, version, authors, license, static_dir, URLroot_, fabcities


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

@app.route('/')
@app.route('/index')
def index():
    print '-' * 10, 'VIEW INDEX', '-' * 50
    return render_template(
        "index.html",
        index=True,
        glob=global_names, )

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

@app.route('/viz_format')
def info():
    return render_template('modules/mod_viz.html')
