import pymysql

conn = pymysql.connect(
        host="mysql80.r4.websupport.sk",
        user="luciakobzova",
        password='.,;c6a[M;l:O*9&W[{w,',
        database="luciakobzova",
        port=3314
    )

if conn:
    print("Success")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books;")
    books = cursor.fetchall()
    print(books)
    cursor.close()

    conn.close()
