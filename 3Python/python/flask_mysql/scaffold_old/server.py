from flask import Flask, render_template  # Import Flask to allow us to create our app
from flask_app import app
from flask_app.controllers import things

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

if __name__=="__main__":
    app.run(debug=True)



