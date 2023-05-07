from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def hello_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hi_name(name):
    if is_alpha_or_ws(name):
        name_str = str(name)
        print(name_str)
        return "Hi " + name_str.title()
        
    return "Names only consider letters from a to z"

# https://stackoverflow.com/questions/29460405/checking-if-string-is-only-letters-and-spaces-python
def is_alpha_or_ws(string):
    if all(x.isalpha() or x.isspace() for x in string):
        return True
    return False
        

# the variable names in the route must exactly match the function parameters defined below
@app.route('/repeat/<int:reps>/<string:str>')
def repeat_str(reps, str):
    if not is_alpha_or_ws(str):
        return 'I only repeat letters from a-z'
    count = int(reps)
    return (str + '\n') * count


# These routes are vestigial from the Hello Flask unit
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id
# end of vestigial code



# 404 Handler & app runner

@app.errorhandler(404)
def not_found(e):
    return 'Sorry! No response. Try again'

# NB.: app.run(debug=True) should be the VERY LAST statement in the server.py
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

    