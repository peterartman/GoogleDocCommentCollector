import commentcollector
import comments_collector_DB

import json

fileID = '18qODvBsWxVJyp7G3ui5_77rl53D-NEIPunxWRBa882Q'


def main():
    commentcollector.printcomments(fileID)
    comments = commentcollector.getcomments(fileID)
    # comments_collector_DB.addToDB(comments)
    # tu jest problem:
    # zawiesza sie przy wykonywaniu polecen z konsoli
    print(json.dumps(comments))


if __name__ == '__main__':
    main()