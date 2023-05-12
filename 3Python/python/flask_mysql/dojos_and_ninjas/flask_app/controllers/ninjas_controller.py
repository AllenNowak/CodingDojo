from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/ninjas')
def new_ninja():
    dojos_list = Dojo.read_all()
    print(f'\n\n\n\n\n---------------------\n{dojos_list}')
    # data = {
    #     'id': Ninja.id,
    #     'first_name': Ninja.first_name,
    #     'last_name': Ninja.last_name,
    #     'age': Ninja.age,
    #     'dojo_id': Ninja.dojo_id,
    #     'created_at': Ninja.created_at,
    #     'updated_at': Ninja.updated_at,
    #     'dojos_list': dojos_list
    # }
    return render_template("add_ninja.html", dojos=dojos_list)

@app.route('/create_ninja', methods=['post'])
def create_ninja():
    foo = Ninja.create(request.form)
    print(foo)
    return redirect(f"/dojos/{request.form['dojo_id']}")


