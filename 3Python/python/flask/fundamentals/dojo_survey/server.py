from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key="hulk_smash"

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print('\n'*3 + '-'*15)
    print('Request ---->', request.form)

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['pace'] = request.form['pace']           # FT or PT radio buttons
    session['comments'] = request.form['comments_text']
    # Handle the multi-selects
    for key in ['webfun', 'python', 'mern', 'java', 'c#']:
        setSessionByKey(request.form, key)
    print('\n'*3 + '-'*15)
    print('Session ---->', session)
    return redirect('/show_results')

# def setSessionForCheckboxes(form, key):
#     if key in request.form and request.form[key] != '':
#         session[key] = form[key]
#     else:
#         session[key] = ''
#     return

def setSessionByKey(form, key):
    session[key] = form[key] if key in form and form[key] != '' else ''
    return

@app.route('/show_results')
def show():

    data = {
        'name': ['name'],
        'location': session['location'],
        'language': session['language'],
        'pace': session['pace'],            # FT or PT radio
        'webfun' : session['webfun'],
        'python' : session['python'],
        'mern' : session['mern'], 
        'java' : session['java'], 
        'c#' : session['c#'],
        'comments': session['comments']
    }
    return render_template('results.html')

# def set_key_value(key='foo', val=''):
#     session[key] = val
#     print(session)

# # poor design. getter shouldn't mutate the session
# def get_key_value(key='foo'):
#     print(session)
#     if key in session:
#         keyval = session[key]
#     else:
#         keyval = ''
#         session[key] = keyval
#     return keyval

@app.route('/destroy_session')
def session_clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

