from __future__ import print_function
from googleapiclient.discovery import build
from flask import Flask, render_template
from google.oauth2 import service_account


def main():

    app = Flask(__name__)

    @app.route('/')
    def index():
        file_id = '1iLJ6tDs14ACwqsqHskB3YcM1yb1C7xprrsulq0QQbBk'
        # If modifying these scopes, delete the file token.pickle.
        scopes = ['https://www.googleapis.com/auth/drive.readonly']
        service_account_file = 'client_id_server.json'
        creds = service_account.Credentials.from_service_account_file(
            service_account_file, scopes=scopes)

        service_comments = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results_comments_list = service_comments.comments().list(fileId=file_id,
                                                                 fields='comments, nextPageToken',
                                                                 includeDeleted='false',
                                                                 # startModifiedTime='2018-09-01T00:00:00Z',
                                                                 pageSize=100).execute()
        received_comments = results_comments_list.get('comments', [])
        received_comments.reverse()
        total_comments = 0
        for comment in received_comments:
            total_comments = total_comments + 1
        return render_template("index.html", name=total_comments)

    @app.route('/comments')
    def comments():
        return render_template("comments.html")

    @app.route('/sourceselection')
    def sourceselection():
        return "You are on webpage gcc.pythonanywhere.com/sourceselection"

    @app.route('/example', methods=['GET', 'POST'])
    def example():
        return 'This is example test'

    if __name__ == "__main__":
        app.run(debug=True)