from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User
from flask_app.models.sighting_model import Sighting
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import datetime

# what happens when 2 controllers register the same route route?
@app.route('/dashboard')
def home():
    if 'logged_in' not in session:
        return redirect('/')
    
    reporter = User.get_by_id(session['user_id'])
    
    sightings = Sighting.get_all()
    return render_template('dashboard.html', sightings=sightings, reporter=reporter )

@app.route('/new')
@app.route('/new/sighting')
def add_new():
    if 'logged_in' not in session:
        return redirect('/')
    
    reporter = User.get_by_id(session['user_id'])
    return render_template('new.html', reporter=reporter)

@app.route('/add', methods=['POST'])
def create_sighting():
    if 'logged_in' not in session:
        return redirect('/')

    data = getFormValues(request.form, None)
    data['reported_by_id'] = session['user_id']

    if not Sighting.validate(data):
        return redirect('/new')
    
    _id = Sighting.save(data)

    return redirect('/dashboard')

def getFormValues(form, sighting_id):
    user_id = session['user_id']
    data = {
        'user_id': user_id,
        **form
    }
    if( sighting_id ):           # Recipe id
        data['id'] = sighting_id
    
    return data

@app.route('/show/<int:id>')
def show_sighting_by_id(id):
    if 'logged_in' not in session:
        return redirect('/')

    sighting = Sighting.get_by_sighting_id({'id': id})
    print('\n\n\n\n---------------')
    print(sighting)

    # sightings from the db best be valid
    # if not Sighting.validate(data):
    #     return redirect('/new')
    
    # We need the current user && the name of the reporting user
    user = User.get_by_id(session['user_id'])

    return render_template('show.html', sighting=sighting, user=user)



# Attribution: https://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers
@staticmethod
def ordinalize(n):
    return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(10<=n%100<=20 and n or n % 10, 'th')


@app.route('/edit/<int:id>')
def edit_sighting(id):
    if 'logged_in' not in session:
        return redirect('/')

    sighting = Sighting.get_by_sighting_id({'id': id})
    if not sighting:
        redirect('/dashboard')
    uid = {'id': session['user_id']}
    user = User.get_by_id(uid)

    return render_template('edit.html', sighting = sighting, user=user )

@app.route('/update/<int:id>', methods=['POST'])
def update_sighting(id):
    if 'logged_in' not in session:
        return redirect('/')

    data = getFormValues(request.form, id)

    #validate or redirect
    if not Sighting.validate(data):
        print ('\n\n\nValidation failed')
        return redirect(f'/edit/{id}')
    
    Sighting.update(data)
    
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete_sighting(id):
    if 'logged_in' not in session:
        return redirect('/')

    Sighting.delete({'id':id})    
    return redirect('/dashboard')
