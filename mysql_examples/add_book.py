from create_connection import connection

conn = connection()

cursor = conn.cursor()
cursor.execute("INSERT INTO Books (Title, Author) VALUES ('Dášenka čili život štěněte', 'Karel Čapek')")
conn.commit()
cursor.close()
conn.close()