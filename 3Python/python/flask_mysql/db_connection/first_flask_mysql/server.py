from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from friend import Friend

app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    # be prepared to log all queries to the terminal
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends=friends)

# relevant code snippet from server.py
# from friend import Friend
@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    # We don't want to render on a POST
    return redirect('/')

@app.route('/lookup')
def get_by_id():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "id": request.form["id"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    friend = Friend.get_by_id(data)
    print(friend)
    return render_template("index.html", friend=friend)


if __name__ == "__main__":
    app.run(debug=True)

