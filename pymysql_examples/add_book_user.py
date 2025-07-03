from create_connection import connection

name = input("Zadejte jméno knihy: ")
author = input("Zadejte méno autora: ")
conn = connection()

cursor = conn.cursor()
cursor.execute("INSERT INTO Books (Title, Author) VALUES (%s, %s)", (name, author))
conn.commit()
cursor.close()
conn.close()