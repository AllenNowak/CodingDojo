# users_controller.py
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo

@app.route('/')
@app.route('/index.html')
@app.route('/dojos')
def read_all():
    all_dojos = Dojo.read_all()
    print('All Dojos = ', all_dojos)
    return render_template("dojos.html", all_dojos=all_dojos)

@app.route('/dojos/<int:id>')
def show_ninjas_in_one_dojo(id):
    dojo = Dojo.read_one(id)
    # handle the joined ninjas in the dojo
    # data = {
    #     'id': dojo.id,
    #     'name': dojo.name,
    #     'created_at': dojo.created_at,
    #     'updated_at': dojo.updated_at,
    #     'ninjas' : dojo.ninjas
    # }
    return render_template("show_dojo.html", dojo = dojo)

@app.route('/add_dojo', methods=['post'])
def add_dojo():
    print('\n\n\n\n------------------ Request Form:')
    print(request.form)
    Dojo.create(request.form)

    return redirect("/dojos")
