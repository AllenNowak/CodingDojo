from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.User_model import User

@app.route('/')
def default():
    # Dashboard route
    pass


# Registration render shared (or context specific) template
# Login render shared (or context specific) template

# Registration Handle Post & redirect to dashboard
# Login Handle Post & redirect to dashboard

# If you arrive @ login route w/ session['user.id'] then redirect to dashboard
# Logout

