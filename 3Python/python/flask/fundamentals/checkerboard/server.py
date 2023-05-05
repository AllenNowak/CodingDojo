from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def index():
    color1 = 'red'
    color2 = 'black'
    return render_template("index.html", rows=8, cols=8, color1=color1, color2=color2)

@app.route('/<int:y>')
def index_sq(y=4):
    x = 8
    color1 = 'red'
    color2 = 'black'
    return render_template("index.html", rows=x, cols=y, color1=color1, color2=color2)

@app.route('/<int:x>/<int:y>')
def index_xy(x=8, y=8):
    color1 = 'black'
    color2 = 'blue'
    return render_template("index.html", rows=x, cols=y, color1=color1, color2=color2)

# Add a default route?

if __name__=="__main__":
    app.run(debug=True)
