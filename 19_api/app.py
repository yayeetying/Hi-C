# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask, render_template
from urllib import request
import json

app = Flask(__name__)

@app.route("/")
def rest_demo():
    http = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=qsb4nvuGri4tJe3q6REknzJbP5xO1OZnJBDfLKMG") #HTTP Response object (containing the JSON info?)
    print(http)
    j = json.load(http) #j is a dictionary of the JSON info
    print(j)
    link = j['url']
    print(link)
    return link
    

if __name__ == "__main__":
    app.debug = True
    app.run()
