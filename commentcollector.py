def printcomments(file_id):
    from googleapiclient.discovery import build

    # server to server authentication
    from google.oauth2 import service_account

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

    SERVICE_ACCOUNT_FILE = 'client_id_server.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service_comments = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results_comments_list = service_comments.comments().list(fileId=file_id,
                                                             fields='comments, nextPageToken',
                                                             includeDeleted='false',
                                                             # startModifiedTime='2018-09-01T00:00:00Z',
                                                             pageSize=100).execute()
    received_comments = results_comments_list.get('comments',    [])
    received_comments.reverse()

    if not received_comments:
        print('No comments found.')
    else:
        for comment in received_comments:
            comment_created_datetime = comment['createdTime']
            comment_author = comment['author']
            comment_id = comment['id']
            comment_display_name = comment_author['displayName']
            comment_content = comment['content']

            print(comment_created_datetime,  ' ', comment_display_name, ' ', comment_content)


def getcomments(file_id):
    from googleapiclient.discovery import build

    # server to server authentication
    from google.oauth2 import service_account

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

    SERVICE_ACCOUNT_FILE = 'client_id_server.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service_comments = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results_comments_list = service_comments.comments().list(fileId=file_id,
                                                             fields='comments, nextPageToken',
                                                             includeDeleted='false',
                                                             # startModifiedTime='2018-09-01T00:00:00Z',
                                                             pageSize=100).execute()
    received_comments = results_comments_list.get('comments', [])
    received_comments.reverse()

    if not received_comments:
        print('No comments found.')
    else:
        for comment in received_comments:
            comment_created_datetime = comment['createdTime']
            comment_author = comment['author']
            comment_id = comment['id']
            comment_display_name = comment_author['displayName']
            comment_content = comment['content']
            return comment
