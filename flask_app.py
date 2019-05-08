from googleapiclient.discovery import build
from flask import Flask, render_template, request
from google.oauth2 import service_account

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SERVICE_ACCOUNT_FILE = 'client_id_server.json'

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=creds)

def main():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/fileinformation', methods=['POST'])
    def fileinformation():
        if request.method == 'POST':
            try:
                sourceurl = request.form['fileurl']
                if sourceurl.find("https://docs.google.com/document/") == 0:
                    right_border = sourceurl.rfind('/')
                    left_border = sourceurl.rfind('/', 0, right_border)
                    fileid_form_request = sourceurl[left_border + 1:right_border]
                    # return data_form_request
                    # google drive api from here
                    try:
                        file = service.files().get(fileId=fileid_form_request).execute()
                        file_title = file['name']
                        return render_template('fileinformation.html', data_form_request=fileid_form_request,
                                               message='',
                                               file_title=file_title)
                    except:
                        file_title = 'Title unknown'
                        return render_template('fileinformation.html',
                                               data_form_request=fileid_form_request, message='', file_title=file_title)
                    # google drive api to here

                else:
                    message = 'No fileID. Please check URL for Google Doc again'
                    return render_template('fileinformation.html',
                                           data_form_request='', message=message)
            except:
                return 'Error again'

    if __name__ == "__main__":
        app.run(debug=True)