# users_controller.py
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user_model import User

@app.route('/')
def index():
    return render_template("index.html")

# CRUD
# Creates
@app.route('/users/new')
def new():
    return render_template("create.html")

@app.route('/users/save', methods=['POST'])
def save():
    id = User.save(request.form)
    return redirect(f"/users/{id}")

# Reads
@app.route('/users/<int:id>')
def get_one_user(id):
    user = User.get_user_by_id(id)
    print('\n\nUser : {user}')
    return render_template("details_page.html", user=user)

@app.route('/users')
def read_all():
    all_users = User.read_all()
    print('All Users = ', all_users)
    return render_template("read_all.html", all_users=all_users)

# Updates
@app.route('/users/<int:id>/edit')
def edit_page(id):
    user = User.get_user_by_id(id)
    print(f'\n\n\n{user}\n\n\n')
    return render_template("edit.html", user = user)

@app.route('/users/<int:id>/update', methods=['POST'])
def update(id):
    data = {
        'id': id,
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email": request.form['email']
    }
    User.update(data)
    return redirect(f"/users/{id}")


# Deletes
@app.route('/users/<int:id>/destroy')
def delete_user(id):
    # data = {
    #     'id' : id
    # }
    # User.destroy(data)
    print('\n'*3+ '-'*10 + f'Trying to destroy user # {id}')
    result = User.destroy_user_by_id(id)
    print('-'*10 + '\n'*3)
    # do we / how do we handle a False that says user wasn't destroyed?
    # what if we only bruise its ego a little?
    return redirect("/users")


# @app.route('/create',methods=['POST'])
# def create():
#     data = {
#         "name":request.form['name'],
#         "bun": request.form['bun'],
#         "meat": request.form['meat'],
#         "calories": request.form['calories']
#     }
#     Burger.save(data)
#     return redirect('/burgers')



# @app.route('/burgers')
# def burgers():
#     return render_template("results.html",all_burgers=Burger.get_all())


# @app.route('/show/<int:burger_id>')
# def detail_page(burger_id):
#     data = {
#         'id': burger_id
#     }
#     return render_template("details_page.html",burger=Burger.get_one(data))

# @app.route('/edit_page/<int:burger_id>')
# def edit_page(burger_id):
#     data = {
#         'id': burger_id
#     }
#     return render_template("edit_page.html", burger = Burger.get_one(data))




