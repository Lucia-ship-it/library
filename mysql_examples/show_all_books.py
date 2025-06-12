from create_connection import connection

conn = connection()

# cursor bez dictionary
cursor = conn.cursor()
cursor.execute("SELECT * FROM Books")
books = cursor.fetchall()
cursor.close()

print(books)

# cursor s dictionary
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM Books")
books = cursor.fetchall()
cursor.close()

print(books)

conn.close()