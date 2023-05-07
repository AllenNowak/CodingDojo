from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

presidents = [
    {'first_name' : 'George', 'last_name' : 'Washington' },
    {'first_name' : 'John',   'last_name' : 'Adams' },
    {'first_name' : 'Thomas', 'last_name' : 'Jefferson' },
    {'first_name' : 'James',  'last_name' : 'Madison' },
    {'first_name' : 'James',  'last_name' : 'Monroe' },
]

@app.route('/')
def index():
    # return 'What the what?'
    return render_template('index.html', data=presidents)


if __name__=="__main__":
    app.run(debug=True)

