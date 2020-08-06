import random
from db import db_create_connection


def random_lottery_result():
    rand_number = random.randint(0, 999999)
    lottery_result = f"{rand_number:06}"
    return lottery_result

def get_win_user(lottery_result):
    try:
        two_digits_result = lottery_result[-2:]
        conn = db_create_connection()
        cur = conn.cursor()
        cur.execute(f"select name from lottery_buying where lottery_number like '%{two_digits_result}' ")
        data = cur.fetchall()
        win_user = None
        if data:
            win_user = ", ".join({"K."+d[0] for d in data})  
        return win_user
    except Exception as e:
        raise e
    finally:
        conn.close()

def add_lottery_buying(name, lottery_number):
    try:
        conn = db_create_connection()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO lottery_buying (name,lottery_number) VALUES('{name}','{lottery_number}');")
        conn.commit()
    except Exception as e:
        raise e
    finally:
        conn.close()

def validate_lottery_number(lottery_number):
    return lottery_number.isdigit() and len(lottery_number) == 2
