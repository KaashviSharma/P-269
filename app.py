
# Import Libraries
import os
from flask import Flask,request,jsonify,render_template,redirect,url_for
app = Flask(__name__)
@app.route('/')
def index():
	return render_template("home.html")
if __name__ =="__main__":
	app.run()
# Initilize the Flask



# Route and define the index function to render the home.html.




# Call the app.run()



