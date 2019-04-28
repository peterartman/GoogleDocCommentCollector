from __future__ import print_function
import commentcollector
import json
import comments_collector_DB

from flask import Flask
from flask import render_template


app = Flask(__name__)

fileID = '1IPDyDzqnCR2VQf1liPh-j_5eUEjQmz9ABnFNAYPZ4sI'
json_comments = commentcollector.getcomments(fileID)
# comments_collector_DB.addToDB(json_comments)
comments=json.dumps(json_comments)
@app.route('/')
def index() -> str:
    return str(comments)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/sourceselection")
def sourceselection():
    return "You went to gcc.pythonanywhere.com/sourceselection"


if __name__ == "__main__":
    app.run()
