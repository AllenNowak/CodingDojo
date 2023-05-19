from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book

@app.route('/')
@app.route('/authors')
def index():
    authors = Author.get_all()
    return render_template("authors.html", authors=authors)

@app.route('/add_author', methods=['POST'])
def new_author():
    aid = Author.save(request.form)
    return redirect('/')
