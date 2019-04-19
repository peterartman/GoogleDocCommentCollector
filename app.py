from __future__ import print_function
import commentcollector
import json
import comments_collector_DB

from flask import Flask


app = Flask(__name__)

fileID = '1IPDyDzqnCR2VQf1liPh-j_5eUEjQmz9ABnFNAYPZ4sI'
json_comments = commentcollector.getcomments(fileID)
# comments_collector_DB.addToDB(json_comments)
comments=json.dumps(json_comments)
@app.route('/')
def hello() -> str:
    return str(comments)


if __name__ == "__main__":
    app.run()
