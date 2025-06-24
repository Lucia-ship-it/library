import pymysql

def connection() :
    conn = pymysql.connect(
            host="localhost",
            user="root",
            password="1111",
            database="library"
        )
    return conn