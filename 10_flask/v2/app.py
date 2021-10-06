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

app.run()

# The "about to print __name__..." is printed on one line in the terminal, and then "__main__" is printed on the next line.
# The website's content doesn't change from the previous sameple apps though (still "No hablo queso!")
# A warning telling the user they are on a development server and thus not to push is thrown though.
