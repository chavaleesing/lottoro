import sqlite3


def db_create_connection():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    return conn

def db_initial_table(conn):
    try:
        conn.execute('CREATE TABLE lottery_buying (name TEXT, lottery_number TEXT, UNIQUE(name,lottery_number))')
        print("Table lottery_buying created successfully")
        conn.close()
    except Exception:
        cur = conn.cursor()
        cur.execute('DELETE FROM lottery_buying')
        conn.commit()
        print("Clear data in lottery_buying table successfully")
        conn.close()
