import sqlite3

DB_NAME = "agrobot.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            product TEXT PRIMARY KEY,
            price TEXT
        )
    ''')
    cursor.execute("INSERT OR IGNORE INTO prices VALUES ('Kartoshka', '8 000 - 11 000 so''m')")
    cursor.execute("INSERT OR IGNORE INTO prices VALUES ('Piyoz', '3 000 - 4 500 so''m')")
    cursor.execute("INSERT OR IGNORE INTO prices VALUES ('Sabzi', '4 000 - 6 000 so''m')")
    conn.commit()
    conn.close()

def get_all_prices():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT product, price FROM prices")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_price_in_db(product, price):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE prices SET price = ? WHERE product = ?", (price, product))
    conn.commit()
    conn.close()