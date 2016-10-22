# -*- encoding: utf-8 -*-

import os

# vars for name application / metas
title = "Fab City Dashboard"
subtitle = "subtitle"
version = "beta 0.15"
metas = """
dataviz,data visualisation,graph,force layout,force directed layout,
resilience,dashboard,index,indices,urban resilience,smart cities,
Medialab,Medialab Prado,Visualizar 2016,Fablab, Fablab Barcelona,PING,
opensource,open source,open data,creative commons,github,
d3,d3.js,javascript,python,flask,HTML,CSS,JSON,bootstrap,bower"""

description = "description"
authors = "Massimo Menichinelli, Mariana Quintero, Julien Paris"

license = 'AGPL'

fabcities = [
    {"id": 0, "name": "Barcelona", "type": "city", "city": "Barcelona", "region": "Catalonia", "country": "Spain", "countrycode": "ESP", "lat": 41.38506389999999, "long": 2.1734034999999494, "description": ''},
    {"id": 1, "name": "Boston", "type": "city", "city": "Boston", "region": "Massachussets", "country": "United States of America", "countrycode": "USA", "lat": 42.3600825, "long": -71.05888010000001, "description": ""},
    {"id": 2, "name": "Somerville", "type": "city", "city": "Boston", "region": "Massachussets", "country": "United States of America", "countrycode": "USA", "lat": 42.3875968, "long": -71.0994968, "description": ""},
    {"id": 3, "name": "Cambridge", "type": "city", "city": "Boston", "region": "Massachussets", "country": "United States of America", "countrycode": "USA", "lat": 42.3736158, "long": -71.1097335, "description": ""},
    {"id": 4, "name": "Ekurhuleni", "type": "region", "city": "Germiston",  "region": "Ekurhuleni", "country": "South Africa", "countrycode": "ZAF",  "lat": -26.2258734, "long": 28.170779400000015, "description": ""},
    {"id": 5, "name": "Kerala", "type": "state", "city": "Thiruvananthapuram", "region": "Kerala", "country": "India", "countrycode": "IND", "lat": 8.524139100000001, "long": 76.93663760000004, "description": ""},
    {"id": 6, "name": "Georgia", "type": "country", "city": "Tbilisi", "region": "Tbilisi", "country": "Georgia", "countrycode": "GEO", "lat": 41.7151377, "long": 44.82709599999998, "description": ""},
    {"id": 7, "name": "Shenzhen", "type": "city", "city": "Shenzhen", "region": "Guangdong", "country": "China", "countrycode": "CHN", "lat": 22.543096, "long": 114.05786499999999, "description": ""},
    {"id": 8, "name": "Amsterdam", "type": "city", "city": "Amsterdam", "region": "North Holland", "country": "Netherlands", "countrycode": "NLD", "lat": 52.3702157, "long": 4.895167899999933, "description": ""},
    {"id": 9, "name": "Toulouse", "type": "city", "city": "Toulouse", "region": "Aquitaine", "country": "France", "countrycode": "FRA", "lat": 43.604652, "long": 1.4442090000000007, "description": ""},
    {"id": 10, "name": "Occitane Region", "type": "region", "city": "Toulouse", "region": "Occitane Region", "country": "France", "countrycode": "FRA", "lat": 43.604652, "long": 1.4442090000000007, "description": ""},
    {"id": 11, "name": "Paris", "type": "city", "city": "Paris", "region": "Ile-de-France", "country": "France", "countrycode": "FRA", "lat": 48.85661400000001, "long": 2.3522219000000177, "description": ""},
    {"id": 12, "name": "Bhutan", "type": "country", "city": "Thimphu", "region": "Thimphu District", "country": "Bhutan", "countrycode": "BTN", "lat": 27.4727924, "long": 89.63928629999998, "description": ""},
    {"id": 13, "name": "Sacramento", "type": "city", "city": "Sacramento/Roseville", "region": "California", "country": "United States of America", "countrycode": "USA", "lat": 38.58157189999999, "long": -121.49439960000001, "description": ""},
    {"id": 14, "name": "Santiago", "type": "city", "city": "Santiago", "region": "Santiago Metropolitan", "country": "Chile", "countrycode": "CHL", "lat": -33.4378305, "long": -70.65044920000003, "description": ""},
    {"id": 15, "name": "Detroit", "type": "city", "city": "Detroit", "region": "Michigan", "country": "United States of America", "countrycode": "USA", "lat": 42.33142699999999, "long": -83.0457538, "description": ""}
    ]



############################
# variables for app config

# local static dir name
static_dir = '/static'
# for local dev

# index root for server
URLroot_ = 'flask'

###############################################################################
# BOOTSTRAP MODULES / USER PROFILES -- JINJA CREATES TEMPLATES GIVEN A SPECIFIC USER PROFILE
# modules_html_dict : indices to get modules html adresses
# user_profiles     : dict to give instructions to Jinja template generator (instructed then in user_driven_template.html)
###############################################################################

modules_html_dict = {
    "empty": "empty_module.html",  # d3 + leaflet

    # Lab
    "lab_ma": "labs/mod_lab_map.html",  # d3 + leaflet
    "lab_if": "labs/mod_lab_infos.html",  # text
    #"lab_id" : "labs/mod_lab_indicators.html",        #d3
    "lab_pr": "labs/mod_lab_projects.html",  # leaflet
    "lab_da": "labs/mod_lab_dashboard.html",  # d3

    # City
    "cit_ma": "cities/mod_city_map.html",  # d3 + leaflet
    "cit_if": "cities/mod_city_infos.html",  # text
    "cit_pp": "cities/mod_city_infos3.html",  # text
    # "cit_id" : "cities/mod_city_indicators.html",       # d3
    "cit_pr": "cities/mod_city_projects.html",  # leaflet
    "cit_da": "cities/mod_city_dashboard.html",  # d3

    # Region
    "reg_ma": "regions/mod_region_map.html",  # d3 + leaflet
    "reg_if": "regions/mod_region_infos.html",  # text
    # "reg_id"  : "regions/mod_region_indicators.html",    # d3
    "reg_pr": "regions/mod_region_projects.html",  # leaflet
    "reg_da": "regions/mod_region_dashboard.html",  # d3

    # Country
    "cou_ma": "countries/mod_country_map.html",  # d3 + leaflet
    "cou_if": "countries/mod_country_infos.html",  # text
    # "cou_id" : "countries/mod_country_indicators.html",    # d3
    "cou_pr": "countries/mod_country_projects.html",  # leaflet
    "cou_da": "countries/mod_country_dashboard.html",  # d3

    # World
    "wor_ma": "world/mod_world_map.html",  # d3 + leaflet
    "wor_if": "world/mod_world_infos.html",  # text
    # "wor_id" : "world/mod_world_indicators.html",    # d3
    "wor_pr": "world/mod_world_projects.html",  # leaflet
    "wor_da": "world/mod_world_dashboard.html",  # d3
    "wor_de": "world/mod_world_map_demo.html",  # d3 + leaflet
    "wor_dc": "world/mod_world_map_demo2.html",  # d3 + leaflet

    # Concepts
    "con_re": "concepts/mod_resilience_concept.html",  # text / illustration
    "con_an": "concepts/mod_resilience_anecdote.html",  # text / illustration
    "con_fa": "concepts/mod_fabcity_concept.html",  # text / illustration

    # Infos
    "inf_ab": "infos/mod_about.html",  # text
    "inf_co": "infos/mod_contact.html",  # text
    "inf_in": "infos/mod_intro.html",  # text
    "inf_re": "infos/mod_intro_resilience.html",  # text
    "inf_pa": "infos/mod_participation.html",  # form/comment
    "inf_pr": "infos/mod_projects.html",  # form/comment
    "inf_la": "infos/mod_labs.html",

    # Tools
    "too_da": "tools/mod_full_dashboard.html",  # row + col
    "too_pi": "tools/mod_pie.html",  # row + col
    "too_pi": "tools/mod_graph.html",  # row + col
    "too_ch": "tools/mod_chart_horiz.html",  # row + col
    "too_cv": "tools/mod_chart_vert.html",  # row + col
    "too_tr": "tools/mod_treemap.html",  # row + col
    "too_re": "tools/mod_resilience.html",
    "too_pl": "tools/mod_choose_place.html",  # row
    "too_id": "tools/mod_choose_indicator.html",  # row
    "too_al": "tools/mod_choose_all.html",  # row
    "too_de": "tools/mod_choose_all_demo.html",  # row
}

# GEOJSON ROUTING  // code names for corresponding .geojson file name

# dflt_data_dict_basemap = {  "all_countries" : "countries_dict.js",
#                            "empty"         : ""
#                            }

root_stats_json = "data_custom/json_stats/"

root_basemaps = "data_custom/geojson_basemaps/"

regions_names = ["World", "Europe", "NorthAmerica", "CentralAmerica",
                 "SouthAmerica", "MiddleEast", "Asia", "Africa", "Oceania"]

geoJSON_dict = {
    # "regions" - "metropolitan_areas_OECD" == folders name in # /data_custom/geojson_basemaps
    # "country": "AUS", "regions" : "xxx" == filename of the .geojson file
    "World": {"country": "",
              "regions": "all_countries",
              "metropolitan_areas_OECD": ""},
    "Europe": {"country": "",
               "regions": "all_countries",
               "metropolitan_areas_OECD": ""},
    "NorthAmerica": {"country": "",
                     "regions": "all_countries",
                     "metropolitan_areas_OECD": ""},
    "CentralAmerica": {"country": "",
                       "regions": "all_countries",
                       "metropolitan_areas_OECD": ""},
    "SouthAmerica": {"country": "",
                     "regions": "all_countries",
                     "metropolitan_areas_OECD": ""},
    "MiddleEast": {"country": "",
                   "regions": "all_countries",
                   "metropolitan_areas_OECD": ""},
    "Asia": {"country": "",
             "regions": "all_countries",
             "metropolitan_areas_OECD": ""},
    "Africa": {"country": "",
               "regions": "all_countries",
               "metropolitan_areas_OECD": ""},
    "Oceania": {"country": "",
                "regions": "all_countries",
                "metropolitan_areas_OECD": ""},
    "AUS": {"country": "AUS",
            "regions": "AUS_admin_level_4",
            "metropolitan_areas_OECD": "AUS_MAs_2016"},
    "AUT": {"country": "AUT",
            "regions": "AUT_admin_level_4",
            "metropolitan_areas_OECD": "AUT_MAs_2016"},
    "BEL": {"country": "BEL",
            "regions": "BEL_admin_level_4",
            "metropolitan_areas_OECD": "BEL_MAs_2016"},
    "CAN": {"country": "CAN",
            "regions": "CAN_admin_level_4",
            "metropolitan_areas_OECD": "CAN_MAs_2016"},
    "CHE": {"country": "CHE",
            "regions": "CHE_admin_level_4",
            "metropolitan_areas_OECD": "CHE_MAs_2016"},
    "CHL": {"country": "CHL",
            "regions": "CHL_admin_level_4",
            "metropolitan_areas_OECD": "CHL_MAs_2016"},
    "COL": {"country": "COL",
            "regions": "COL_admin_level_4",
            "metropolitan_areas_OECD": "COL_MAs_2016"},
    "CZE": {"country": "CZE",
            "regions": "CZE_admin_level_4",
            "metropolitan_areas_OECD": "CZE_MAs_2016"},
    "DEU": {"country": "DEU",
            "regions": "DEU_admin_level_4",
            "metropolitan_areas_OECD": "DEU_MAs_2016"},
    "DNK": {"country": "DNK",
            "regions": "DNK_admin_level_4",
            "metropolitan_areas_OECD": "DNK_MAs_2016"},
    "ESP": {"country": "ESP",
            "regions": "ESP_admin_level_4",
            "metropolitan_areas_OECD": "ESP_MAs_2016"},
    "EST": {"country": "EST",
            "regions": "EST_admin_level_4",
            "metropolitan_areas_OECD": "EST_MAs_2016"},
    "FIN": {"country": "FIN",
            "regions": "FIN_admin_level_4",
            "metropolitan_areas_OECD": "FIN_MAs_2016"},
    "FRA": {"country": "FRA",
            "regions": "FRA_admin_level_4",
            "metropolitan_areas_OECD": "FRA_MAs_2016"},
    "GBR": {"country": "GBR",
            "regions": "GBR_admin_level_4",
            "metropolitan_areas_OECD": "GBR_MAs_2016"},
    "GRC": {"country": "GRC",
            "regions": "GRC_admin_level_4",
            "metropolitan_areas_OECD": "GRC_MAs_2016"},
    "HUN": {"country": "HUN",
            "regions": "HUN_admin_level_4",
            "metropolitan_areas_OECD": "HUN_MAs_2016"},
    "IRL": {"country": "IRL",
            "regions": "IRL_admin_level_4",
            "metropolitan_areas_OECD": "IRL_MAs_2016"},
    "ITA": {"country": "ITA",
            "regions": "ITA_admin_level_4",
            "metropolitan_areas_OECD": "ITA_MAs_2016"},
    "JPN": {"country": "JPN",
            "regions": "JPN_admin_level_4",
            "metropolitan_areas_OECD": "JPN_MAs_2016"},
    "KOR": {"country": "KOR",
            "regions": "KOR_admin_level_4",
            "metropolitan_areas_OECD": "KOR_MAs_2016"},
    "LUX": {"country": "LUX",
            "regions": "LUX_admin_level_4",
            "metropolitan_areas_OECD": "LUX_FUAs_2016"},
    "MEX": {"country": "MEx",
            "regions": "MEX_admin_level_4",
            "metropolitan_areas_OECD": "MEX_MAs_2016"},
    "NLD": {"country": "NLD",
            "regions": "NLD_admin_level_4",
            "metropolitan_areas_OECD": "NLD_MAs_2016"},
    "NOR": {"country": "NOR",
            "regions": "NOR_admin_level_4",
            "metropolitan_areas_OECD": "NOR_MAs_2016"},
    "POL": {"country": "POL",
            "regions": "POL_admin_level_4",
            "metropolitan_areas_OECD": "POL_MAs_2016"},
    "PRT": {"country": "PRT",
            "regions": "PRT_admin_level_4",
            "metropolitan_areas_OECD": "PRT_MAs_2016"},
    "SVK": {"country": "SVK",
            "regions": "SVK_admin_level_4",
            "metropolitan_areas_OECD": "SVK_MAs_2016"},
    "SVN": {"country": "SVN",
            "regions": "SVN_admin_level_4",
            "metropolitan_areas_OECD": "SVN_MAs_2016"},
    "SWE": {"country": "SWE",
            "regions": "SWE_admin_level_4",
            "metropolitan_areas_OECD": "SWE_MAs_2016"},
    "USA": {"country": "USA",
            "regions": "USA_admin_level_4",
            "metropolitan_areas_OECD": "USA_MAs_2016"},
}
