import pymysql
from datetime import date

DB_NAME = "UKOLY"

def create_database_if_not_exists(cursor, db_name):
    cursor.execute(
        "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s",
        (db_name,)
    )

    if not cursor.fetchone():
        cursor.execute(f"CREATE DATABASE {db_name}")
        return False
    return True

def connect_to_db():
    try:
        conn = pymysql.connect(
            host="mysql80.r4.websupport.sk",
            port=3314,
            user="luciakobzova",
            password=".,;c6a[M;l:O*9&W[{w,"
        )
        cursor = conn.cursor()
        # databse_already_created = create_database_if_not_exists(cursor, DB_NAME)
        cursor.close()
        conn.close()

    except pymysql.Error as e:
        raise ValueError(f"Chyba připojení nebo nastavení databáze: {e}")
