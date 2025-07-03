# Vytvořte tabulku produkty, která bude obsahovat následující sloupce: - 

# id: Primární klíč (unikátní identifikátor produktu). 
# nazev: Název produktu (textový řetězec).
# cena: Cena produktu (číslo s desetinnou čárkou).
# skladem: Počet kusů produktu skladem (celé číslo).

# Vložte do tabulky několik záznamů, například: - 
# Produkt 1: Mobilní telefon, 15 000 Kč, 20 kusů skladem. 
# Produkt 2: Notebook, 25 000 Kč, 10 kusů skladem.
# Produkt 3: Sluchátka, 2 500 Kč, 50 kusů skladem.

import pymysql

try:
    conn = pymysql.connect(
            host="mysql80.r4.websupport.sk",
            port=3314,
            user="luciakobzova",
            password='.,;c6a[M;l:O*9&W[{w,',
            database="luciakobzova"            
        )
    print("Připojení k databázi bylo úspěšné.")
except pymysql.connect.Error as err:
     print(f"Chyba při připojování: {err}")

cursor = conn.cursor()

try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produkty (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(200) NOT NULL,
        price DECIMAL(10,2),
        in_storage INT
        )
    ''')
    print("Tabulka 'Produkty' byla vytvořena.")

except pymysql.connector.Error as err:
    print(f"Chyba při vytváření tabulky: {err}")
print("Připojení k databázi bylo uzavřeno.")

# try:
#     cursor.execute("INSERT INTO Produkty (name, price, in_storage) VALUES ('Mobilní telefon2', 18000, 2)") #cisla nemozu obsahovat medzety!
#     cursor.execute("INSERT INTO Produkty (name, price, in_storage) VALUES ('Notebook', 25000, 10), ('Sluchátka', 2500, 50);")
#     conn.commit()
#     print("Záznam byl vložen.")
# except pymysql.connector.Error as err:
#     print(f"Chyba při vkládání dat: {err}")
    

cursor.execute("SELECT * FROM Produkty")
produkty = cursor.fetchall()
print(produkty)

# Vytvořte tabulku uzivatele, která bude obsahovat následující sloupce:
# - id: Primární klíč (unikátní identifikátor uživatele).
# - jmeno: Jméno uživatele (textový řetězec).
# - email: E-mailová adresa uživatele.

# Vytvořte tabulku objednavky, která bude obsahovat následující sloupce:
# - id: Primární klíč (unikátní identifikátor objednávky).
# - uzivatel_id: Cizí klíč odkazující na id v tabulce uzivatele.
# - datum: Datum objednávky.
# - castka: Celková částka objednávky

# try:
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Uzivatele(
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         jmeno VARCHAR(50) NOT NULL,
#         email VARCHAR(255)
#     );
# ''')
#     print("Tabulka 'Produkty' byla vytvořena.")

# except pymysql.connector.Error as err:
#     print(f"Chyba při vytváření tabulky: {err}")
# print("Připojení k databázi bylo uzavřeno.")

# try:
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Objednavky(
#         id INT PRIMARY KEY  AUTO_INCREMENT,
#         id_uzivatel INT,
#         datum DATE,
#         castka DECIMAL(10,2),
#         FOREIGN KEY (id_uzivatel) REFERENECES Uzivatele(id)
#     );
# ''')
# except pymysql.connector.Error as err:
#     print(f"Chyba při vytváření tabulky: {err}")
# print("Připojení k databázi bylo uzavřeno.")



# # .Vložte několik záznamů do tabulek uzivatele a objednavky.
# # Napište dotaz, který vrátí všechny objednávky od konkrétního uživatele, například uživatele s id = 1.





# cursor.execute("INSERT INTO Uzivatele(jmeno, email) VALUES ('janko mrkvicka', 'mrkvicka@email.cz'), ('sara novotna', 'sara01@gmail.com');")
# conn.commit()

# cursor.execute("INSERT INTO Objednavky(datum, castka) VALUES ('2024-01-15', 4567), ('20224-02-20, 879);")

# Select *
# from Objednavky
# where id_uzivatel = 1


# #dalsie zadanie, zadanie 3
# Dotaz na celkový počet objednávek každého uživatele:
# - Vypište jména uživatelů a celkový počet jejich objednávek.Dotaz na celkovou částku všech objednávek každého uživatele:
# - Vypište jména uživatelů a součet všech částek jejich objednávek.Dotaz na uživatele bez objednávek:
# - Vypište jména uživatelů, kteří zatím nemají žádné objednávky.


# Select u.name, COUNT(o.id), SUM(o.castka)
# From Uzivatele u
# JOIN Objednavky o ON u.id=o.id_uzovatele
# GROUP BY u.name;

# Select u.name
# From Uzivatele u
# LEFT JOIN Objednavky o ON u.id=o.id_uzovatele
# GROUP BY u.name
# HAVING o.id IS NULL;

