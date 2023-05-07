from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
# def index():
#     return render_template("index.html", num=3, color="lime")	# notice the 2 new named arguments!

@app.route('/play')
# def playground():
#     return render_template("index.html", num=5, color="blue")

@app.route('/play/<int:num>')    # count & color w default values
# def playground_x(num=3):
#     return render_template("index.html", num=num, color="yellow")

@app.route('/play/<int:num>/<string:color>')    # count & color w default values
def playground_x_colored(num=4, color='yellow'):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)
