# Team dinoClock: Yaying Liang Li, Thomas Yu
# SoftDev
# K19 -- A RESTful Joruney Skyward

from flask import Flask, render_template
from urllib import request
import json

app = Flask(__name__)

@app.route("/")
def rest_demo():
    http = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=qsb4nvuGri4tJe3q6REknzJbP5xO1OZnJBDfLKMG") #HTTP Response object (containing the JSON info)
    print(http)

    j = json.load(http) #j is a dictionary (key-value pairs) of the JSON info
    print(j)

    link = j['url'] #get the value of the 'url' key
    print(link)

    explanation = j['explanation'] #get the value of the 'explanation' key
    print(explanation)

    #render an html template with the picture (using url) and explanation
    return render_template("main.html", pic = link, description = explanation)


if __name__ == "__main__":
    app.debug = True
    app.run()
