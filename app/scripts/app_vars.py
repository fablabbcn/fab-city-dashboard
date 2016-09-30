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
authors     = "Massimo, Mariana, Julien"

licenceCC   = 'GPL' 

############################
### variables for app config

### local static dir name
static_dir  = '/static'          ### for local dev

### index root for server
URLroot_ = 'flask'


####################################
### BOOTSTRAP MODULES / USER PROFILE
#
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
    "inf_pa" : "infos/mod_participation.html",         #form/comment
    #},

    ##"tools" : {
    "too_da" : "tools/mod_dashboard.html",            #row + col
    "too_pl" : "tools/mod_choose_place.html",           #row
    "too_id" : "tools/mod_choose_indicator.html",     #row
    #},    
}

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
                        { "600px" : [ {"inf_co": 6 }        ]      }, 
                      ],
    "only_dashboard"    : [
                        { "200px" : [ {"too_da" : 12 }      ]    }, 
                        { "50px" : [   {"too_pl" : 3 },
                                        {"too_id": 3 }
                                    ] },
                        { "400px" : [ {"wor_ma" : 12 } ] },  ### row 1

                      ],        
        
    ### CARTO TYPOLOGY ##################
    "world"       : [
                        { "500px" : [ {"wor_ma": 12 }  ]      }, 
                        { "50px" : [   {"too_pl" : 3 },
                                        {"too_id": 3 }
                                    ] },
                      ],


} ### end user_profiles dict
