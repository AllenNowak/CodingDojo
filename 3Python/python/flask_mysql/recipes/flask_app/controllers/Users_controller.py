from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.User_model import User
from flask_app.models.Recipe_model import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
DEBUG = True


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    print('\n\n\n------------------------ Registration ------------------------ ')
    print(request.form)
    # ---------- Validate the form
    if not User.validate_registration(request.form):
        print ('\n\n\nValidation failed')
        return redirect('/')

    # else hash the password & save the info
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    print('\n\n\n-------------------- hashed pw: ', hashed_pw)

    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : hashed_pw

    }
    user_id = User.save(data)
    session['user_id'] = user_id
    session['logged_in'] = True
    session['first_name'] = request.form['first_name']
    print(f"At Regis: f_n: {session['first_name']}, r.f: {request.form['first_name']}] ")

    return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    # Is the user in the DB?
    # I also need to sanitize this input before executing the query
    found_in_db = User.get_by_email( { 'email': request.form['email']} )

    if not found_in_db:
        flash("Invalid Email / Password", "login_isues")
        return redirect('/')
    if not bcrypt.check_password_hash(found_in_db.password, request.form['password']):
        # db password didn't match given password
        flash("Invalid Email / Password", "login_isues")
        return redirect('/')

    # Since passwords matched, we can set the user's session info
    print('At login')
    session['logged_in'] = True
    session['user_id'] = found_in_db.id
    session['first_name'] = found_in_db.first_name
    return redirect('/success')


# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

