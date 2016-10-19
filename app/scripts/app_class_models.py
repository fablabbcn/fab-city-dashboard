# -*- encoding: utf-8 -*-

# UNFINISHED
# sketch for function dealing with geojsons datas
import json
from .geoboxes import geoboxes_cities, geoboxes_countries, geoboxes_regions


# find location/geobox/polygon from location name
class Location(object):
    def __init__(self, location_name):
        self.loc_name = location_name
        self.lat_ = float()
        self.long_ = float()
        self.gpsDict = []

    def findLocation(self):

        # from self.loc_name get GPS lg/lat
        # MISSING !!!

        return gpsDict

    def findGeobox(self):

        # from self.loc_name get GPS box
        # MISSING !!!

        return gpsDict

    def findPolygon(self):

        # from self.loc_name get GPS box
        # MISSING !!!

        return gpsDict


    # global GeoJSON converter
class GeoJSON(object):
    def __init__(self):

        self.GeoJSON_collection = {"type": "FeatureCollection", "features": []}

        self.GeoJSON_feature = {"type": "Feature",
                                "geometry": {
                                    "type": "",
                                    "coordinates": ""
                                },
                                "properties": {
                                    "name": "",
                                    "type": "",
                                }},

    # create point feature
    def GeoPoint(coordList, properties):

        point = self.GeoJSON_feature
        point["geometry"]["type"] = "Point"
        point["geometry"]["coordinates"] = coordList
        point["properties"] = properties

        return point

    #create point feature
    def GeoLine(coordList, properties):

        point = self.GeoJSON_feature
        point["geometry"]["type"] = "LineString"
        point["geometry"]["coordinates"] = coordList
        #FORMAT :
        # [
        #    [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
        #    [100.0, 1.0], [100.0, 0.0] ]
        #  ]
        point["properties"] = properties

        return point

    # create point feature
    def GeoPoint(coordList, properties):

        point = self.GeoJSON_feature
        point["geometry"]["type"] = "Polygon"
        point["geometry"]["coordinates"] = coordList  #FORMAT :
        # [
        #    [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
        #    [100.0, 1.0], [100.0, 0.0]
        #  ]
        point["properties"] = properties

        return point
