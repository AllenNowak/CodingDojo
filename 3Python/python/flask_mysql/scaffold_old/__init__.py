# __init__.py
from flask import Flask
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "sssshhhhhh"
DATABASE = 'my_db'

