import random
from db import db_create_connection


def random_lottery_result():
    rand_number = random.randint(0, 999999)
    lottery_result = f"{rand_number:06}"
    return lottery_result


