def addToDB(comments_json):
    import mysql.connector
    import sshtunnel

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

        sql_insert_query = "INSERT INTO json_col VALUES %s"

        # Do stuff
        cursor = connection.cursor()
        cursor.execute(sql_insert_query, comments_json)
        connection.commit()
        # print(myDB.rowcount, "record inserted.")
        connection.close()