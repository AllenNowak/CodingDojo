from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.User_model import User
from flask_app.models.Recipe_model import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import datetime

# what happens when 2 controllers register the same route route?
@app.route('/success')
def success():
    if 'logged_in' not in session:
        return redirect('/')
    
    recipes = Recipe.get_all()
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

    data = getFormValues(request.form, None)

    if not Recipe.validate(data):
        return redirect('/new')
    
    r_id = Recipe.save(data)

    return redirect('/success')

def getFormValues(form, recipe_id):
    user_id = session['user_id']
    data = {
        'user_id': user_id,
        **form
    }
    if( recipe_id ):           # Recipe id
        data['id'] = recipe_id
    
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

@app.route('/update/<int:id>', methods=['POST'])
def update_recipe(id):
    if 'logged_in' not in session:
        return redirect('/')

    data = getFormValues(request.form, id)

    #validate or redirect
    if not Recipe.validate(data):
        print ('\n\n\nValidation failed')
        return redirect(f'/edit/{id}')
    
    Recipe.update(data)
    
    return redirect('/success')

@app.route('/delete/<int:id>')
def delete_recipe(id):
    if 'logged_in' not in session:
        return redirect('/')

    Recipe.delete({'id':id})    
    return redirect('/success')
