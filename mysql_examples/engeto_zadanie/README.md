tento subor obsahuje vypracovane cvicenia z akademie na temu SQL databaza

1. Vytvořte tabulku produkty, která bude obsahovat následující sloupce: - 

id: Primární klíč (unikátní identifikátor produktu). 
nazev: Název produktu (textový řetězec).
cena: Cena produktu (číslo s desetinnou čárkou).
skladem: Počet kusů produktu skladem (celé číslo).

Vložte do tabulky několik záznamů, například: - 
Produkt 1: Mobilní telefon, 15 000 Kč, 20 kusů skladem. 
Produkt 2: Notebook, 25 000 Kč, 10 kusů skladem.
Produkt 3: Sluchátka, 2 500 Kč, 50 kusů skladem.

# Vytvořte tabulku uzivatele, která bude obsahovat následující sloupce:
# - id: Primární klíč (unikátní identifikátor uživatele).
# - jmeno: Jméno uživatele (textový řetězec).
# - email: E-mailová adresa uživatele.Vytvořte tabulku objednavky, která bude obsahovat následující sloupce:
# - id: Primární klíč (unikátní identifikátor objednávky).
# - uzivatel_id: Cizí klíč odkazující na id v tabulce uzivatele.
# - datum: Datum objednávky.
# - castka: Celková částka objednávky

# # .Vložte několik záznamů do tabulek uzivatele a objednavky.
# # Napište dotaz, který vrátí všechny objednávky od konkrétního uživatele, například uživatele s id = 1.


# cursor.execute('''
#     CREATE TABLE Uzivatele(
#       id INT PRIMARY KEY AUTO_INCREMENT,
#       jmeno VARCHAR(50) NOT NULL,
#       email: VARCHAR(255)
#   );
#''')


# cursor.execute(''''
#   CREATE TABLE Objednavky(
#     id INT PRIMARY KEY  AUTO_INCREMENT,
#     id_uzivatel INT,
#     datum date,
#     castka DECIMAL(10,2)
#     FOREIGN KEY (id_uzivatel) REFERENECES Uzivatele(id)
#   );
#''')

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

