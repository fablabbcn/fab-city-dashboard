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
modules_index = {
    
    ##"lab" : {
    "lab_ma" : "mod_lab_map.html",          #d3 + leaflet
    "lab_if" : "mod_lab_infos.html",             #text
    "lab_id" : "mod_lab_indicators.html",        #d3
    "lab_pr" : "mod_lab_projects.html",          #leaflet
    "lab_da" : "mod_lab_dashboard.html",         #d3
    #}, 

    ##"city" :    {
    "cit_ma" : "mod_city_map.html",              #d3 + leaflet
    "cit_if" : "mod_city_infos.html",            #text
    "cit_id" : "mod_city_indicators.html",       #d3
    "cit_pr" : "mod_city_projects.html",         #leaflet
    "cit_da" : "mod_city_dashboard.html",        #d3
    #},
    
    ##"region" :  {
    "reg_ma"  : "mod_region_map.html",           #d3 + leaflet
    "reg_if"  : "mod_region_infos.html",         #text
    "reg_id"  : "mod_region_indicators.html",    #d3
    "reg_pr"  : "mod_region_projects.html",      #leaflet
    "reg_da"  : "mod_region_dashboard.html",     #d3
    #},
    
    ##"country" : {
    "cou_ma" : "mod_country_map.html",           #d3 + leaflet
    "cou_if" : "mod_country_infos.html",         #text
    "cou_id" : "mod_country_indicators.html",    #d3
    "cou_pr" : "mod_country_projects.html",      #leaflet
    "cou_da" : "mod_country_dashboard.html",     #d3
    #},

    ##"world" : {
    "wor_ma" : "mod_country_map.html",           #d3 + leaflet
    "wor_if" : "mod_country_infos.html",         #text
    "wor_id" : "mod_country_indicators.html",    #d3
    "wor_pr" : "mod_country_projects.html",      #leaflet
    "wor_da" : "mod_country_dashboard.html",     #d3
    #},
    
    ##"concepts" : {
    "con_re" : "mod_resilience_concept.html",    #text / illustration
    "con_an" : "mod_resilience_anecdote.html",   #text / illustration
    "con_fa" : "mod_fabcity_concept.html",       #text / illustration
    
    ##"infos" : {
    "inf_ab" : "mod_about.html",                 #text
    "inf_co" : "mod_contact.html",               #text
    "inf_pa" : "mod_participation.html",         #form/comment
    #},

    ##"tools" : {
    "tool_da" : "mod_dashboard.html",            #row + col
    "tool_la" : "mod_choose_lab.html",           #row
    "tool_ci" : "mod_choose_city.html",          #row
    "tool_re" : "mod_choose_region.html",        #row
    "tool_co" : "mod_choose_country.html",       #row
    "tool_id" : "mod_choose_indicator.html",     #row
    #},    
}

### order of modules /// format for one user  : "analitic"      : ["row_01" [ ], "row_02" } ,
user_profiles = {
    "analytic"      : [ # HEIGHT in px // module/number of columns (max 12 col)
                        { "400px" : [ {"reg_ma" : 9 }, {"reg_id": 3 } ] },  ### row 1
                        { "50px" :  [ {"tool_la" : 12 } ] },                ### row 2
                        { "600px" : [ {"con_re" : 4 }, {"wor_ma": 8 } ] },  ### row 3
                      ],
        
    "citizen"       : [
                        { "400px" : [ {"reg_ma" : 9 }, {"reg_id": 3 } ] },    
                        { "50px" :  [ {"tool_la" : 12 } ] }, 
                        { "600px" : [ {"con_re" : 4 }, {"wor_ma": 8 } ] }, 
                      ],
        
    "civic leader"  : [
                        { "400px" : [ {"reg_ma" : 9 }, {"reg_id": 3 } ] },    
                        { "50px" :  [ {"tool_la" : 12 } ] }, 
                        { "600px" : [ {"con_re" : 4 }, {"wor_ma": 8 } ] }, 
                      ],
        
    "maker"         : [
                        { "400px" : [ {"reg_ma" : 9 }, {"reg_id": 3 } ] },    
                        { "50px" :  [ {"tool_la" : 12 } ] }, 
                        { "600px" : [ {"con_re" : 4 }, {"wor_ma": 8 } ] }, 
                      ],
    "fab manager"   : [
                        { "400px" : [ {"reg_ma" : 9 }, {"reg_id": 3 } ] },    
                        { "50px" :  [ {"tool_la" : 12 } ] }, 
                        { "600px" : [ {"con_re" : 4 }, {"wor_ma": 8 } ] }, 
                      ],
}
