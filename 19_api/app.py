# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask, render_template, urllib3, json
app = Flask(__name__)

@app.route("/")
def rest_demo():
    http = urllib3.PoolManager

if __name__ == "__main__":
    app.debug = True
    app.run()
