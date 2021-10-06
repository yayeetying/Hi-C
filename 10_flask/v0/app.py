#Team Name: Hi-C; Yaying Liang Li, Andy Lin, Josephine Lee
#SoftDev
#K10 -- analyzing the different versions of flask sample code
#2021-10-05

from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?

app.run()  # Q4: Where have you seen similar construcs in other languages?
                
# This is the same code as K09's sample code. Andy had an issue with loading the Flask site on his home network, but on Stuy's network, it worked.
# We tried to reproduce this but to no luck, as the problem seems to be a Python install not taking effect or a reboot that was needed
# (which occured before class Monday). Once the website loaded, the return statement was printed onto the web page.
# A warning telling the user they are on a development server and thus not to push is thrown though.
