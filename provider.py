import random
from db import db_create_connection


def random_lottery_result():
    rand_number = random.randint(0, 999999)
    lottery_result = f"{rand_number:06}"
    return lottery_result

def get_win_user(lottery_result):
    two_digits_result = lottery_result[-2:]
    conn = db_create_connection()
    cur = conn.cursor()
    cur.execute(f"select name from lottery_buying where lottery_number like '%{two_digits_result}' ")
    data = cur.fetchall()
    conn.close()
    win_user = None
    if data:
        win_user = ", ".join({d[0] for d in data})  
    return win_user
