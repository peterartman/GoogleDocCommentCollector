from __future__ import print_function
from googleapiclient.discovery import build


# server to server authentication SERVICE_ACCOUNT_FILE = 'client_id_server.json'
from google.oauth2 import service_account

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SERVICE_ACCOUNT_FILE = 'client_id_server.json'


def main():
    # Start input form user
    print('Enter file id:')
    file_id = input()
    # End of input

    # File IDs:                                Restrictions:  Comments:
    # 1IPDyDzqnCR2VQf1liPh-j_5eUEjQmz9ABnFNAYPZ4sI  public         35
    # 1h3iBLl5_u4W0w4ScH7NKxxMP2t23LE8dwlXz7geRjRA  public         33
    # 1XzgO8nJccx-L9Bnsmecn-n-u0L46OyL7gAkRh0EKzLI  public         5

    # test file 1: 18qODvBsWxVJyp7G3ui5_77rl53D-NEIPunxWRBa882Q
    # test file 2: 1iLJ6tDs14ACwqsqHskB3YcM1yb1C7xprrsulq0QQbBk

    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service_comments = build('drive', 'v3', credentials=creds)
    service_replies = build('drive', 'v3', credentials=creds)


    # Call the Drive v3 API
    results_comments_list = service_comments.comments().list(fileId=file_id,
                                                             fields='comments, nextPageToken',
                                                             includeDeleted='false',
                                                             # startModifiedTime='2018-09-01T00:00:00Z',
                                                             pageSize=100).execute()
    received_comments = results_comments_list.get('comments',    [])
    received_comments.reverse()
    total_comments = 0
    total_replies = 0

    if not received_comments:

        print('No comments found.')
    else:
        for comment in received_comments:
            comment_created_datetime = comment['createdTime']
            comment_author = comment['author']
            comment_id = comment['id']
            comment_display_name = comment_author['displayName']
            comment_content = comment['content']
            total_comments = total_comments + 1

            print(comment_created_datetime,  ' ', comment_display_name, ' ', comment_content)

            results_replies_list = service_replies.replies().list(fileId=file_id,
                                                                  commentId=comment_id,
                                                                  fields='replies, nextPageToken',
                                                                  includeDeleted='false',
                                                                  pageSize=100).execute()
            received_replies = results_replies_list.get('replies', [])
            if not received_replies:
                print('No replies found.')
            else:
                print(' Replies:')
                for reply in received_replies:
                    reply_created_time = reply['createdTime']
                    reply_author = reply['author']
                    reply_display_name = reply_author['displayName']
                    reply_content = reply['content']
                    total_replies = total_replies + 1

                    print(' ', reply_created_time, ' ', reply_display_name, ' ', reply_content)
                print()
                print(' Replies for this comment: ', len(received_replies))
                print()
        print()
        print('Total comments: ', total_comments)
        print('Total replies: ', total_replies)
        print()
        # print('Comments type: ', ' ', type(received_comments))
        # print('Replies type: ', ' ', type(received_comments))
        # print(type(items))
        # print(items[0])
        # print(json.dumps(received_replies)
        # print(json.dumps(received_replies)


if __name__ == '__main__':
    main()
