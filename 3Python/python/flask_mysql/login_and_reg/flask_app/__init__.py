from flask import Flask
DB="login"

app = Flask(__name__)
app.secret_key = "shhhhhh"