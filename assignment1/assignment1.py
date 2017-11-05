# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 18:30:24 2017

@author: AkshayKC
"""

from flask import Flask
import psycopg2
from flask import jsonify

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

@app.route("/")
def get():
    cur.execute("select * from india")
    all = cur.fetchall()
    return jsonify(all)
        
value = (700157, 'Hela Battala', 'West Bengal', 22.6131, 88.4398, 0)
cur.execute("select exists(select 1 from india where key = %s LIMIT 1)", [value[0]]) 
res = cur.fetchone()[0]
print(res)    

@app.route("/post_location")   
def post_location():
    if res:
        return "This pincode already exists in the table"
    else:
        cur.execute('insert into india values (%s, %s, %s, %s, %s, %s)', value)
        conn.commit()
    
#To check if the inserted value is in database or not
@app.route("/test")   
def test():
    cur.execute("select * from india where key = 700157")
    all = cur.fetchall()
    return jsonify(all)

 
if __name__ == "__main__":
    app.run()