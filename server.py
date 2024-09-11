from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/cv')
def cleiton_cv():
    return render_template("cleiton_cv.html")

if __name__  == "__main__":
    app.run(debug=True)
