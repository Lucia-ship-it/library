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

conn = pymysql.connect(
        host="mysql80.r4.websupport.sk",
        user="luciakobzova",
        password='.,;c6a[M;l:O*9&W[{w,',
        database="luciakobzova",
        port=3314
    )

CREATE TABLE Produkty (
    id INT PRIMARY KEY,
    name VARCHAR(200),
    price FLOAT,
    availability int
    );





)