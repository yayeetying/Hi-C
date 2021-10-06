#Team Name: Hi-C; Yaying Liang Li, Andy Lin, Josephine Lee
#SoftDev
#K10 -- analyzing the different versions of flask sample code
#2021-10-05

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

# Terminal outputs that flask is restarting with stat, debugger is active, and a process ID?
# The existing print statements continue to print out in the terminal, and the web page continues to say "no hablo queso!".
# A warning telling the user they are on a development server and thus not to push is thrown though. Kinda ironic because the app is set to debug mode.
