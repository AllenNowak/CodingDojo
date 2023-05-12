# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhhh"  # Needed when working with Session state
DB = 'dojos_and_ninjas_schema'

