# 📚 Knihovní systém v Pythonu + MySQL

Tento projekt je jednoduchý konzolový systém pro správu knihovny pomocí jazyka **Python** a databáze **MySQL**. Umožňuje:

- registraci a identifikaci členů,
- výpůjčku a vrácení knih,
- zobrazení dostupných knih a aktuálně vypůjčených knih.

## 🔧 Požadavky

- Python 3.7+
- Knihovna pro připojení k mysql serveru (jedna z násleudjících):
    - [`mysql-connector-python`](https://pypi.org/project/mysql-connector-python/)
    - [`PyMySQL`](https://pypi.org/project/PyMySQL/)
- MySQL server (např. MariaDB nebo MySQL Community Server)

Nainstaluj potřebné balíčky:
```bash
pip install mysql-connector-python
```
nebo:
```bash
pip install PyMySQL
```
## Různé knihovny
Ve složce `/mysql-connector` najdeš impolemntaci systému používající knihovnu `mysql-connector-python` (oficiální knihovna).

Ve složce `/pymysql` najdeš implementaci systému používající knihovnu `PyMySQL`.

Zbytek věcí funguje stejně v obou implementacích.