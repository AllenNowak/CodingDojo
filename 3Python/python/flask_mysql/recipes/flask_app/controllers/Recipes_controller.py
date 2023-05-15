from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.User_model import User
from flask_app.models.Recipe_model import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import datetime

# what happens when 2 controllers register the same route route?
# @app.route('/')
# def index():
#     return render_template("index.html")

# If you arrive @ login route w/ session['user_id'] then redirect to success
@app.route('/success')
def success():
    # print('\n'*4 + '-' * 10)
    # print('At success -> ')
    # print(session)
    # print('\n'*4 + '-' * 10)
    if 'logged_in' not in session:
        return redirect('/')
    
    # id = session['user_id']
    # user = User.get_by_id( session['user_id'] )     # TODO: this should be an object
    
    recipes = Recipe.get_all()
    # print(recipes)

    return render_template('welcome.html', recipes = recipes )

@app.route('/new')
def add_recipe():
    if 'logged_in' not in session:
        return redirect('/')
    return render_template('add.html')

@app.route('/add', methods=['POST'])
def create_recipe():
    if 'logged_in' not in session:
        return redirect('/')

    #build dictionary from Post
    data = getFormValues(request.form)

    #validate or redirect
    if not Recipe.validate(data):
        print ('\n\n\nValidation failed')
        return redirect('/')
    
    r_id = Recipe.save(data)
    print('New recipe id: ', r_id)
    # date_cookd = request.form['date_cooked']
    # print('Date Cooked: ', date_cookd)
    # dt_arr = date_cookd.split('-')
    # print(dt_arr)
    # x = datetime.datetime(int(dt_arr[0]), int(dt_arr[1]), int(dt_arr[2]))
    # print(x.strftime('%B'))
    # print('Ordinal day:', ordinalize(int(dt_arr[2])))

    # dt = DateFormat(data[date_cooked])
    # these don't work as is
    # print("\n\n\n------------", data['date_cooked'].strftime('%B %d,%Y'), '----------\n\n\n')
    # print("\n\n\n------------", "2022-11-05".strftime('%B %d,%Y'), '----------\n\n\n')
    #call model to insert into db

    return redirect('/success')

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

def getFormValues(form):
    print("\n\n\n")
    print("------------> Session Info ", session)
    print("------------> Form ", form)
    print("\n\n\n")
    
    uid = session['user_id']
    data = {
        'user_id': uid,
        **form
    }
    
    return data

# Attribution: https://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers
@staticmethod
def ordinalize(n):
    return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(10<=n%100<=20 and n or n % 10, 'th')


@app.route('/recipes/<int:id>')
def view_recipe(id):
    if 'logged_in' not in session:
        return redirect('/')

    recipe = Recipe.get_by_id({'id': id})
    if not recipe:
        redirect('/success')

    return render_template('view.html', recipe = recipe )

@app.route('/edit/<int:id>')
def edit_recipe(id):
    if 'logged_in' not in session:
        return redirect('/')

    recipe = Recipe.get_by_id({'id': id})
    if not recipe:
        redirect('/success')

    return render_template('edit.html', recipe = recipe )

@app.route('/delete/<int:id>')
def delete_recipe(id):
    pass



