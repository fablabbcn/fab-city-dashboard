# -*- encoding: utf-8 -*-

import os

######################################
### vars for name application / metas
title       = "Fabcity Dashboard" 
subtitle    = "subtitle"
version     = "beta 0.1" 
metas       = """
dataviz,data visualisation,graph,force layout,force directed layout,
resilience,dashboard,index,indices,urban resilience,smart cities,
Medialab,Medialab Prado,Visualizar 2016,Fablab, Fablab Barcelona,PING,
opensource,open source,open data,creative commons,github,
d3,d3.js,javascript,python,flask,HTML,CSS,JSON,bootstrap,bower"""

description = "description"
authors     = "Massimo Menichinelli, Mariana Quintero, Julien Paris"

licenceCC   = 'GPL' 

############################
### variables for app config

### local static dir name
static_dir  = '/static'          ### for local dev

### index root for server
URLroot_ = 'flask'


######################################################################################################################
### BOOTSTRAP MODULES / USER PROFILES -- JINJA CREATES TEMPLATES GIVEN A SPECIFIC USER PROFILE
### modules_html_dict : indices to get modules html adresses
### user_profiles     : dict to give instructions to Jinja template generator (instructed then in user_driven_template.html)
#######################################################################################################################

modules_html_dict = {
    
    ##"lab" : {
    "lab_ma" : "labs/mod_lab_map.html",               #d3 + leaflet
    "lab_if" : "labs/mod_lab_infos.html",             #text
    "lab_id" : "labs/mod_lab_indicators.html",        #d3
    "lab_pr" : "labs/mod_lab_projects.html",          #leaflet
    "lab_da" : "labs/mod_lab_dashboard.html",         #d3
    #}, 

    ##"city" :    {
    "cit_ma" : "cities/mod_city_map.html",              #d3 + leaflet
    "cit_if" : "cities/mod_city_infos.html",            #text
    "cit_id" : "cities/mod_city_indicators.html",       #d3
    "cit_pr" : "cities/mod_city_projects.html",         #leaflet
    "cit_da" : "cities/mod_city_dashboard.html",        #d3
    #},
    
    ##"region" :  {
    "reg_ma"  : "regions/mod_region_map.html",           #d3 + leaflet
    "reg_if"  : "regions/mod_region_infos.html",         #text
    "reg_id"  : "regions/mod_region_indicators.html",    #d3
    "reg_pr"  : "regions/mod_region_projects.html",      #leaflet
    "reg_da"  : "regions/mod_region_dashboard.html",     #d3
    #},
    
    ##"country" : {
    "cou_ma" : "countries/mod_country_map.html",           #d3 + leaflet
    "cou_if" : "countries/mod_country_infos.html",         #text
    "cou_id" : "countries/mod_country_indicators.html",    #d3
    "cou_pr" : "countries/mod_country_projects.html",      #leaflet
    "cou_da" : "countries/mod_country_dashboard.html",     #d3
    #},

    ##"world" : {
    "wor_ma" : "world/mod_world_map.html",           #d3 + leaflet
    "wor_if" : "world/mod_world_infos.html",         #text
    "wor_id" : "world/mod_world_indicators.html",    #d3
    "wor_pr" : "world/mod_world_projects.html",      #leaflet
    "wor_da" : "world/mod_world_dashboard.html",     #d3
    #},
    
    ##"concepts" : {
    "con_re" : "concepts/mod_resilience_concept.html",    #text / illustration
    "con_an" : "concepts/mod_resilience_anecdote.html",   #text / illustration
    "con_fa" : "concepts/mod_fabcity_concept.html",       #text / illustration
    
    ##"infos" : {
    "inf_ab" : "infos/mod_about.html",                 #text
    "inf_co" : "infos/mod_contact.html",               #text
    "inf_in" : "infos/mod_intro.html",                 #text
    "inf_re" : "infos/mod_intro_resilience.html",      #text
    "inf_pa" : "infos/mod_participation.html",         #form/comment

    #},

    ##"tools" : {
    "too_da" : "tools/mod_dashboard.html",            #row + col
    "too_pl" : "tools/mod_choose_place.html",           #row
    "too_id" : "tools/mod_choose_indicator.html",     #row
    #},    
}

############################################################################################
### order of modules /// format for one user  : "analitic"      : ["row_01" [ ], "row_02" } ,
user_profiles = {
    
    ### USER TYPOLOGY ##############################################################
    ### url called return var user_profile in views.py and set bootstrap
    "analytic"      : [ # HEIGHT in px // module/number of columns (max 12 col)
                        { "400px" : [ {"wor_ma" : 9 }, {"wor_id": 3 } ] },  ### row 1
                        { "50px" :  [ {"too_pl" : 12 } ] },                 ### row 2
                        { "600px" : [ {"con_re" : 4 }] },                   ### row 3
                      ],
    "citizen"       : [
                        { "400px" : [ {"inf_in" : 12 } ] }, 
                        { "400px" : [ {"reg_ma" : 2 }, {"reg_id": 5 } ] },    
                        { "50px" :  [ {"too_pl" : 12 } ] }, 
                        { "600px" : [ {"con_re" : 6 }, {"wor_ma": 6 } ] }, 
                      ],
    "civic_leader"  : [
                        { "400px" : [ {"reg_ma" : 9 }, {"reg_id": 3 } ] },    
                        { "50px" :  [ {"too_pl" : 12 } ] }, 
                        { "600px" : [ {"con_re" : 4 }, {"wor_ma": 8 } ] }, 
                      ],
    "maker"         : [
                        { "400px" : [ {"reg_ma" : 9 }, {"reg_id": 3 } ] },    
                        { "50px" :  [ {"too_pl" : 12 } ] }, 
                        { "600px" : [ {"con_re" : 4 }, {"wor_ma": 8 } ] }, 
                      ],
    "fab_manager"   : [
                        { "400px" : [ {"reg_ma" : 9 }, {"reg_id": 3 } ] },    
                        { "50px" :  [ {"too_pl" : 12 } ] }, 
                        { "600px" : [ {"con_re" : 4 }, {"wor_ma": 8 } ] }, 
                      ],
     
    ### DASHBOARD TYPOLOGY ##################
    "only_infos"       : [
                        { "400px" : [ {"inf_in" : 12 }      ]    }, 
                        { "400px" : [ {"inf_ab" : 2 }, {"inf_pa": 5 } ] },    
                        { "200px" : [ {"inf_co": 12 }        ]      }, 
                      ],
    "only_dashboard"    : [
                        { "200px" : [ {"too_da" : 12 }      ]    }, 
                        { "50px" : [   {"too_pl" : 3 },
                                        {"too_id": 3 }
                                    ] },
                        { "400px" : [ {"wor_ma" : 12 } ] },  ### row 1

                      ],   
    "demo"       : [
                        { "400px" : [ {"inf_in" : 12 }      ]    }, 
                        { "400px" : [ {"inf_re" : 12 }      ]    }, 
                        { "200px" : [ {"inf_co": 12 }        ]      }, 
                      ],     
        
    ### CARTO-USER TYPOLOGY ##################
    "carto"       : [
                        { "520px" : [ {"wor_ma": 12 }  ]      }, 
                        { "50px" : [   {"too_pl" : 6 },
                                        {"too_id": 6 }
                                    ] },
                      ],

   ### CARTO-USER TYPOLOGY ##################
    "introApp"    : [
                        { "200px" : [ {"inf_in": 12 }  ]      }, 
                        { "100px" : [ {"con_re": 12 }  ]      }, 
                        { "500px" : [ {"wor_ma": 12 }  ]      }, 
                      ],



} ### end user_profiles dict


########################################################################
### GEOJSON ROUTING  // code names for corresponding .geojson file name

root_basemaps = "/data_custom/geojson_basemaps/" 

geoJSON_dict = {
    ### "regions" - "metropolitan_areas_OECD" == folders name in /data_custom/geojson_basemaps
    ### "country": "AUS", "regions" : "xxx" == filename of the .geojson file

    ########################################################################
  
        "World" :           {   "country": "", "regions" : "all_countries",
                                "metropolitan_areas_OECD" : ""},
        "Europe":           {   "country": "", "regions" : "all_countries",
                                "metropolitan_areas_OECD" : ""},
        "USA"   :           {   "country": "", "regions" : "all_countries",
                                "metropolitan_areas_OECD" : ""},  
        "CentralAmerica" :  {   "country": "", "regions" : "all_countries",
                                "metropolitan_areas_OECD" : ""},  
        "SouthAmerica"   :  {   "country": "", "regions" : "all_countries",
                                "metropolitan_areas_OECD" : ""},
        "MiddleEast"     :  {   "country": "", "regions" : "all_countries",
                                "metropolitan_areas_OECD" : ""},
        "Asia"           :  {   "country": "", "regions" : "all_countries",
                                "metropolitan_areas_OECD" : ""},
        "Africa"         :  {   "country": "", "regions" : "all_countries",
                                "metropolitan_areas_OECD" : ""},
        "Oceania"   : {         "country": "", "regions" : "all_countries",
                                "metropolitan_areas_OECD" : ""}, 
    
    ########################################################################
    
    "AUS"   : { "country": "AUS", "regions" : "AUS_admin_level_4" ,
                    "metropolitan_areas_OECD" : "AUS_MAs_2016"},
    "AUT"   : {     "country": "AUT", "regions" : "AUT_admin_level_4" ,
                    "metropolitan_areas_OECD" : "AUT_MAs_2016"},
        "BEL"   : { "country": "BEL", "regions" : "BEL_admin_level_4" ,
                    "metropolitan_areas_OECD" : "BEL_MAs_2016"},
    "CAN"   : { "country": "CAN", "regions" : "CAN_admin_level_4" ,
                    "metropolitan_areas_OECD" : "CAN_MAs_2016"},
    "CHE"   : { "country": "CHE", "regions" : "CHE_admin_level_4" ,
                    "metropolitan_areas_OECD" : "CHE_MAs_2016"},
    "CHL"   : { "country": "CHL", "regions" : "CHL_admin_level_4" ,
                    "metropolitan_areas_OECD" : "CHL_MAs_2016"},
    "COL"   : { "country": "COL", "regions" : "COL_admin_level_4" ,
                    "metropolitan_areas_OECD" : "COL_MAs_2016"},
    "CZE"   : { "country": "CZE", "regions" : "CZE_admin_level_4" ,
                    "metropolitan_areas_OECD" : "CZE_MAs_2016"},
        "DEU"   : { "country": "DEU", "regions" : "DEU_admin_level_4" ,
                    "metropolitan_areas_OECD" : "DEU_MAs_2016"},
        "DNK"   : { "country": "DNK", "regions" : "DNK_admin_level_4" ,
                    "metropolitan_areas_OECD" : "DNK_MAs_2016"},
        "ESP"   : { "country": "ESP", "regions" : "ESP_admin_level_4" ,
                    "metropolitan_areas_OECD" : "ESP_MAs_2016"},
    "EST"   : { "country": "EST", "regions" : "EST_admin_level_4" ,
                    "metropolitan_areas_OECD" : "EST_MAs_2016"},
        "FIN"   : { "country": "FIN", "regions" : "FIN_admin_level_4" ,
                    "metropolitan_areas_OECD" : "FIN_MAs_2016"},
        "FRA"   : { "country": "FRA", "regions" : "FRA_admin_level_4" ,
                    "metropolitan_areas_OECD" : "FRA_MAs_2016"},
        "GBR"   : { "country": "GBR", "regions" : "GBR_admin_level_4" ,
                    "metropolitan_areas_OECD" : "GBR_MAs_2016"},
    "GRC"   : { "country": "GRC", "regions" : "GRC_admin_level_4" ,
                    "metropolitan_areas_OECD" : "GRC_MAs_2016"},
    "HUN"   : { "country": "HUN", "regions" : "HUN_admin_level_4" ,
                    "metropolitan_areas_OECD" : "HUN_MAs_2016"},
    "IRL"   : { "country": "IRL", "regions" : "IRL_admin_level_4" ,
                    "metropolitan_areas_OECD" : "IRL_MAs_2016"},
        "ITA"   : { "country": "ITA", "regions" : "ITA_admin_level_4" ,
                    "metropolitan_areas_OECD" : "ITA_MAs_2016"},
    "JPN"   : { "country": "JPN", "regions" : "JPN_admin_level_4" ,
                    "metropolitan_areas_OECD" : "JPN_MAs_2016"},
    "KOR"   : { "country": "KOR", "regions" : "KOR_admin_level_4" ,
                    "metropolitan_areas_OECD" : "KOR_MAs_2016"},
    "LUX"   : { "country": "LUX", "regions" : "LUX_admin_level_4" ,
                    "metropolitan_areas_OECD" : "LUX_FUAs_2016"},
    "MEX"   : { "country": "MEx", "regions" : "MEX_admin_level_4" ,
                    "metropolitan_areas_OECD" : "MEX_MAs_2016"},
        "NLD"   : { "country": "NLD", "regions" : "NLD_admin_level_4" ,
                    "metropolitan_areas_OECD" : "NLD_MAs_2016"}, ## Netherlands
        "NOR"   : { "country": "NOR", "regions" : "NOR_admin_level_4" ,
                    "metropolitan_areas_OECD" : "NOR_MAs_2016"},
    "POL"   : { "country": "POL", "regions" : "POL_admin_level_4" ,
                    "metropolitan_areas_OECD" : "POL_MAs_2016"},
        "PRT"   : { "country": "PRT", "regions" : "PRT_admin_level_4" ,
                    "metropolitan_areas_OECD" : "PRT_MAs_2016"},
    "SVK"   : { "country": "SVK", "regions" : "SVK_admin_level_4" ,
                    "metropolitan_areas_OECD" : "SVK_MAs_2016"},
    "SVN"   : { "country": "SVN", "regions" : "SVN_admin_level_4" ,
                    "metropolitan_areas_OECD" : "SVN_MAs_2016"},
    "SWE"   : { "country": "SWE", "regions" : "SWE_admin_level_4" ,
                    "metropolitan_areas_OECD" : "SWE_MAs_2016"},
        "USA"   : { "country": "USA", "regions" : "USA_admin_level_4" ,
                    "metropolitan_areas_OECD" : "USA_MAs_2016"},
}

