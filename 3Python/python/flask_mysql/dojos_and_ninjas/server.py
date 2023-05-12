from flask_app import app
# import the entire controller file
from flask_app.controllers import dojos_controller, ninjas_controller

if __name__=="__main__":
    app.run(debug=True)