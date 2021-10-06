#Team Name: Hi-C; Yaying Liang Li, Andy Lin, Josephine Lee
#SoftDev
#K10 -- analyzing the different versions of flask sample code
#2021-10-05

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

# The terminal prints out "the name of this module is..." and then the name.
# There is an if statement for if the caller is main - in other words, if the file is NOT imported.
# If the file is the main file, then Flask runs this script in debug mode and independently runs the
# program. We assume this conditional is there for when this script is used in conjunction with another script.
