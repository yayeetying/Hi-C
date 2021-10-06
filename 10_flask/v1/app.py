#Team Name: Hi-C; Yaying Liang Li, Andy Lin, Josephine Lee
#SoftDev
#K10 -- analyzing the different versions of flask sample code
#2021-10-05

from flask import Flask
app = Flask(__name__) #create instance of class Flask called app

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

# The changes made here were that the terminal didn't print any statements, as no print statements were called.
# The "no hablo queso" did show up on the web page, though.

## Major Discovery!: print(<input>) prints the input into the terminal. return "<input>" prints the input onto the web page.

# A warning telling the user they are on a development server and thus not to push is thrown though.
