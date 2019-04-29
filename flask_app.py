

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return render_template("index.html")


@app.route("/comments")
def comments():
    # return "fileID " + request.form["fileID"]
    return render_template("comments.html")


@app.route("/sourceselection")
def sourceselection():
    return "You are on webpage gcc.pythonanywhere.com/sourceselection"


if __name__ == "__main__":
    app.run()
