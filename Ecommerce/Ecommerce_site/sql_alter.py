import sqlite3

try:
    conn = sqlite3.connect('db.sqlite3')

    sql = """ALTER TABLE Product
    ADD tag TEXT DEFAULT 'default'"""

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print("ALTERING OK")
    cursor.close()

except sqlite3.Error as e:
    print("Error while Altering Table", e)
finally:
    if (conn):
        conn.close()
        print("Connection Closed")
