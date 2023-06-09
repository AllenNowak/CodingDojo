from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

#@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    '''
    return 'Hello World!'  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode. 
                            # app.run(debug=True, host="localhost", port=8000) to run on the designated port
    '''
    # Instead of returning a string,
    # we'll return the result of the render_template method, passing in the anme of our HTML file
    return render_template('index.html')

@app.route('/')
def index():
    # return 'What the what?'
    return render_template('index.html', phrase="hello", times=5)

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>')  # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name + " from the /hello/&lt;name&gt; route"

@app.route('/users/<username>/<id>')    # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":
    app.run(debug=True)

