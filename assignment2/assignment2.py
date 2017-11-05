# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 22:58:49 2017

@author: AkshayKC
"""

from flask import Flask
import psycopg2
from flask import jsonify
import pandas as pd
from math import radians, sin, cos, asin, sqrt

app = Flask(__name__)

conn = psycopg2.connect(dbname = "postgres", user = "postgres", password = "postgres")

print("Opened database successfully")

cur = conn.cursor()

cur.execute("select exists(select * from information_schema.tables where table_name=%s)", ('india',))
exists = cur.fetchone()[0]

if exists:
    pass
else:
    cur.execute("""
    create table india(
        key integer PRIMARY KEY, 
        place_name text, 
        admin_name1 text, 
        latitude float, 
        longitude float, 
        accuracy integer
    )
    """)
    #Please change the path accordingly
    with open('E:\IN2.csv', 'r') as f:
            next(f)  # Skip the header row.
            cur.copy_from(f, 'india', sep=',')

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers
    return c * r



@app.route("/")
def get():
    return "Everything is fine, please go to http://127.0.0.1:5000/get_using_postgres to see the results of 'earthdistance' function and http://127.0.0.1:5000/get_using_self to see the results of my function"

cur.execute("create extension cube")
cur.execute("create extension earthdistance")


@app.route("/get_using_postgres")
def get_using_postgres():
    #Please change the value of latitude and longitude in earth_distance function below for further testing
    cur.execute("select key, earth_distance(ll_to_earth(28.6333, 77.2167), ll_to_earth(india.latitude, india.longitude))/1000 from india")
    earth_dis = cur.fetchall()
    earth_pd = pd.DataFrame(earth_dis, columns = ["Pincode", "Distance"])
    within_1 = earth_pd[earth_pd['Distance'] < 1.0000]
    res = within_1['Pincode']
    res_list = res.tolist()
    return jsonify(res_list)

@app.route("/get_using_self")
def get_using_self():
    cur.execute("select * from india")
    all_new = cur.fetchall()
    all_pd = pd.DataFrame.from_records(all_new, columns = ["key", "place_name", "admin_name1", "latitude", "longitude", "accuracy"])
    values = [28.6333, 77.2167] #same values as used in get_using_postgres
    all_pd['distance'] = all_pd.apply(lambda row : haversine(values[0], values[1], row['latitude'], row['longitude']), axis = 1)
    within = all_pd[all_pd['distance'] < 1.0000]
    pin_codes = within['key']
    pin_codes_list = pin_codes.tolist()
    return jsonify(pin_codes_list)



if __name__ == "__main__":
    app.run()