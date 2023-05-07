from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
@app.route('/<int:y>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def index_xy(x=8, y=8, color1='black', color2='green'):
    return render_template("index.html", rows=x, cols=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)
