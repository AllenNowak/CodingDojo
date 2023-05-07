from flask import Flask, render_template, request, redirect, session
  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key="hulk_smash"

@app.route('/')
def index():
    bump_counter_by(1)
    bump_counter_by(1, 'monotonic_visits')
    if 'jump_step' in session:
        default_jump = session['jump_step']
    else:
        default_jump = 2

    return render_template('index.html', default_jump=default_jump)

@app.route('/add')
@app.route('/add/<int:num>', methods=['POST', 'GET'])
def increment_counter(num=2):
    bump_counter_by(num-1)

    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    jump = int(request.form['jumper'])
    session['jump_step'] = jump
    bump_counter_by(jump-1)

    return redirect('/')

def bump_counter_by(num, key='visits'):
    # print('visits', session['visits'])
    # print('monotonic visits', session['monotonic_visits'])
    print(session)
    if key in session:
        session[key] += num
    else:
        session[key] = 1
    return


@app.route('/destroy_session')
def session_clear():
    session.pop('visits')
    # session.pop('monotonic_visits')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

