import mysql.connector
import sshtunnel
import commentcollector
import json
from datetime import datetime

commentslist = commentcollector.getcomments('1IPDyDzqnCR2VQf1liPh-j_5eUEjQmz9ABnFNAYPZ4sI')
text_aaa = "aaaaaaa"
sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

_username = 'gcc'
_password = 'commentcollector123'
_bind_address = 'gcc.mysql.pythonanywhere-services.com'
_bid_port = int(3306)

db_user = 'gcc'
db_password = 'gccpassword'
db_host = '127.0.0.1'
db_target = 'gcc$google_comments_DB'

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='gcc', ssh_password=_password,
    remote_bind_address=(_bind_address, _bid_port)
) as tunnel:
    connection = mysql.connector.connect(
        user='gcc', password=db_password,
        host=db_host, port=tunnel.local_bind_port,
        database=db_target,
    )
    print(connection)
    query = connection.cursor()

    datetime_today = datetime.now()

    add_comments = ("INSERT INTO table_test "
               "(json_test, text_test, datetime_test)"
               "VALUES (%(json_test)s, %(text_test)s, %(datetime_test)s)")

    # comments data for query

    data_comments = {
        'json_test': json.dumps(commentslist),
        'text_test': text_aaa,
        'datetime_test': datetime_today,
    }

    query.execute(add_comments, data_comments)

    connection.commit()
    print(query.rowcount, "record inserted.")
    connection.close()