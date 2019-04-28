
from flask import Flask
from flask import render_template


import commentcollector
import json
import comments_collector_DB

from flask import Flask


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


fileID = '1IPDyDzqnCR2VQf1liPh-j_5eUEjQmz9ABnFNAYPZ4sI'
json_comments = commentcollector.getcomments(fileID)
# comments_collector_DB.addToDB(json_comments)
comments=json.dumps(json_comments)
@app.route('/')
def hello() -> str:
    return str(comments)


if __name__ == "__main__":
    app.run()
