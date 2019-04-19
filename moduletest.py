import commentcollector
import json

fileID = '18qODvBsWxVJyp7G3ui5_77rl53D-NEIPunxWRBa882Q'


def main():
    commentcollector.printcomments(fileID)

    comments = commentcollector.getcomments(fileID)
    json.dumps(comments)


if __name__ == '__main__':
    main()