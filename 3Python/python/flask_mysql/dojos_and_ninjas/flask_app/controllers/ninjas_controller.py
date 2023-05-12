# users_controller.py
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/')
@app.route('/index.html')
@app.route('/dojos')
def read_all():
    all_dojos = Ninja.read_all()
    print('All Dojos = ', all_dojos)
    return render_template("dojos.html", all_dojos=all_dojos)

@app.route('/dojos/<int:id>')
def new_ninja(id):
    dojos_list = Dojo.read_all()
    print(f'\n\n---------------------\n{dojos_list}')
    data = {
        'id': Ninja.id,
        'first_name': Ninja.first_name,
        'last_name': Ninja.last_name,
        'age': Ninja.age,
        'dojo_id': Ninja.dojo_id,
        'created_at': Ninja.created_at,
        'updated_at': Ninja.updated_at,
        'dojos_list': dojos_list
    }
    return render_template("add_ninja.html", dojo=data)
    # return render_template("show_Ninja.html", dojo = dojo)

@app.route('/add_dojo', methods=['post'])
def add_dojo():
    Ninja.create(request.form)
    # name = request.form['name']
    # Ninja.create(name)

    return redirect("/dojos")

# # CRUD
# # Creates
# @app.route('/dojos/new')
# def new():
#     return render_template("create.html")

# @app.route('/users/save', methods=['POST'])
# def save():
#     id = User.save(request.form)
#     return redirect(f"/users/{id}")

# # Reads
# @app.route('/users/<int:id>')
# def get_one_user(id):
#     user = User.get_user_by_id(id)
#     print('\n\nUser : {user}')
#     return render_template("details_page.html", user=user)


# # Updates
# @app.route('/users/<int:id>/edit')
# def edit_page(id):
#     user = User.get_user_by_id(id)
#     print(f'\n\n\n{user}\n\n\n')
#     return render_template("edit.html", user = user)

# @app.route('/users/<int:id>/update', methods=['POST'])
# def update(id):
#     data = {
#         'id': id,
#         "first_name":request.form['first_name'],
#         "last_name":request.form['last_name'],
#         "email": request.form['email']
#     }
#     User.update(data)
#     return redirect(f"/users/{id}")


# # Deletes
# @app.route('/users/<int:id>/destroy')
# def delete_user(id):
#     # data = {
#     #     'id' : id
#     # }
#     # User.destroy(data)
#     print('\n'*3+ '-'*10 + f'Trying to destroy user # {id}')
#     result = User.destroy_user_by_id(id)
#     print('-'*10 + '\n'*3)
#     # do we / how do we handle a False that says user wasn't destroyed?
#     # what if we only bruise its ego a little?
#     return redirect("/users")


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




