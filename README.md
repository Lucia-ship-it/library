# 📚 Knihovní systém v Pythonu + MySQL

Tento projekt je jednoduchý konzolový systém pro správu knihovny pomocí jazyka **Python** a databáze **MySQL**. Umožňuje:

- registraci a identifikaci členů,
- výpůjčku a vrácení knih,
- zobrazení dostupných knih a aktuálně vypůjčených knih.

## 🔧 Požadavky

- Python 3.7+
- Knihovna [`mysql-connector-python`](https://pypi.org/project/mysql-connector-python/)
- MySQL server (např. MariaDB nebo MySQL Community Server)

Nainstaluj potřebné balíčky:
```bash
pip install mysql-connector-python
```

## Úkoly
V skriptu `library.py` najdeš tyto jednotlivé úkoly, které je tvým úkolem dokončit:
- TODO 1: změň na svoje heslo (connect_to_db)
- TODO 2: dovnitř cursor.execute napiš příkaz pro vytvoření tabulky Members (create_tables_if_not_exist)
- TODO 3: implementuj správnou práci s kurzorem (find_member_by_name)
- TODO 4: Uprav příkaz tak, aby vybral pouze dostupné knihy (get_available_books)
- TODO 5: do proměnné loans ulož všechny výpůjčky uživatele, které kurzor našel (get_user_loans)
- TODO 6: vytvoř nový záznam o půjčce a akutalizuj knihu s daným id, celé připojení commitni, aby se vše uložilo (borrow_book_db)

**Řešení** najdeš v souboru `library_solution`.