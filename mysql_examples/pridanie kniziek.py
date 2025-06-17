import pymysql

conn = pymysql.connect(
        host="mysql80.r4.websupport.sk",
        user="luciakobzova",
        password='.,;c6a[M;l:O*9&W[{w,',
        database="luciakobzova",
        port=3314
    )
# name = input("Zadejte název knížky: ")
# author = input("Zadejte jméno autora: ")

# #sqpl: přidat knihu "kytice" od "karel Jaromír Erben"
# cursor = conn.cursor()

# #vykonat SQL příkaz
# cursor.execute("INSERT INTO Books (Title, Author) VALUES ('Kytice', 'Karel Jaromír Erben');")
# conn.commit()

# # kontrola, že se knížka opravdu přidala
# cursor.execute("SELECT * FROM Books")
# books = cursor.fetchall()
# for book in books:
#     print(book[1])
# cursor.close()
# conn.close()

#f string je menej bezpecna verze, lebo sql injection
# (f"ïnsert.....{name}..")
# bezpecnejsie : (insert .... (%s, %s), name, author)

# #sqpl: přidat knihu "kytice" od "karel Jaromír Erben"
# cursor = conn.cursor()

# #vykonat SQL příkaz
# cursor.execute("INSERT INTO Books (Title, Author) VALUES (%s, %s);",(name,author))
# conn.commit()

# # kontrola, že se knížka opravdu přidala
# cursor.execute("SELECT * FROM Books")
# books = cursor.fetchall()
# for book in books:
#     print(book[1])
# cursor.close()
# conn.close()

#připojení k dtabázi
import pymysql # mysql

def connection():
    conn = pymysql.connect(
        host="mysql80.r4.websupport.sk",
        user="luciakobzova",
        password='.,;c6a[M;l:O*9&W[{w,',
        database="luciakobzova",
        port=3314
    )

    return conn

def find_all_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    cursor.close()
    return books

def add_book(conn, name, author):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Books (Title, Author) VALUES (%s, %s);", (name, author))
    conn.commit()
    cursor.close()

name = input("Zadejte název knížky: ")
author = input("Zadejte jméno autora: ")
conn = connection()
add_book(conn, name, author)
books = find_all_books(conn)
for book in books:
    print(book)