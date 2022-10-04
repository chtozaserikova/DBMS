import psycopg2
from config import host, user, password, db_name

try:
    #connect to exist db
    connection = psycopg2.connect(
        host = host,
        user =user,
        password = password,
        database = db_name
    )

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print('Server version:', cursor.fetchone())
        # pass


except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')