from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/sourceselection")
def sourceselection():
    return "You went to gcc.pythonanywhere.com/sourceselection"


if __name__ == "__main__":
    app.run()
