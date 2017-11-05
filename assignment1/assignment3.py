# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 22:59:07 2017

@author: AkshayKC
"""

import requests
from shapely.geometry import shape, Point
from flask import Flask

r = requests.get('https://gist.githubusercontent.com/ramsingla/6202001/raw/1dc42df3c6d8f4db95b7f7b65add1f520578ab33/map.geojson')
data = r.json()

# Provide the location to search for in format longitude, latitude
point = Point(77.1614, 28.4993)

app = Flask(__name__)

@app.route("/")
def get():
    return "Everything is fine, please go to http://127.0.0.1:5000/get_location to get the location of given longitude and latitude"

@app.route("/get_location")
def get_location():
    # check each polygon to see if it contains the point
   for feature in data['features']:
       polygon = shape(feature['geometry'])
       if polygon.contains(point):
            res = "Given Longitude and Latitude falls in : " + feature['properties']['name'] 
            return res

if __name__ == "__main__":
    app.run()
