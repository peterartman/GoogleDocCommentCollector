from commentcollector import *
from comments_collector_DB import addToDB

import json

fileID = '18qODvBsWxVJyp7G3ui5_77rl53D-NEIPunxWRBa882Q'


def main():
    printcomments(fileID)

    comments = getcomments(fileID)
    addToDB(comments)
    json.dumps(comments)


if __name__ == '__main__':
    main()