from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def index():
    # return 'What the what?'
    return render_template('index.html', phrase="hello", times=5)

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<string:name>')
def hello(name):
    print(name)
    return "Hello, " + name + " from the /hello/&lt;name&gt; route"

@app.route('/users/<string:username>/<int:id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":
    app.run(debug=True)

