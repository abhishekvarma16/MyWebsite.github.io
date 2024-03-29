from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/aboutme')
def me():
    return render_template("aboutme.html")


if __name__ == '__main__':
    app.run(debug=True)
