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

#jak to spustit na macu:
        #Open the integrated terminal in VS Code.
        # Run python3 -m venv .venv to create a virtual environment.
        # Activate it with source .venv/bin/activate.
        # Run pip install PyMySQL inside the activated environment.
# zadat do terminalu
# python3 -m venv .venv
# source .venv/bin/activate
# pip install PyMySQL
