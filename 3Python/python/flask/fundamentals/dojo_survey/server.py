from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key="hulk_smash"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
# @app.route('/add/<int:num>', methods=['POST', 'GET'])
def process():

    return redirect('/')



def set_key_value(key='foo', val=''):
    session[key] = val
    print(session)

# poor design. getter shouldn't mutate the session
def get_key_value(key='foo'):
    print(session)
    if key in session:
        keyval = session[key]
    else:
        keyval = ''
        session[key] = keyval
    return keyval

@app.route('/destroy_session')
def session_clear():
    session.clear()
    # session.pop('visits')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

