from datetime import datetime
from flask import Flask, jsonify, request
from provider import get_win_user, random_lottery_result
from db import db_create_connection, db_initial_table


app = Flask(__name__)
conn = db_create_connection()
db_initial_table(conn)

lottery_result = random_lottery_result()

@app.route('/lotto/showResult', methods=['GET'])
def show_lottery_result():
    data = get_win_user(lottery_result)
    if data:
        result_msg = f'Congrats !!! K.{data} You won lottery Prize :)'
    else:
        result_msg = f'Unfortunately, The lottery took your money. No one win this prize T_T'
    return {
        "result_msg": result_msg,
        "result_number": f'The Lottery result is: {lottery_result}'
    }


@app.route('/lotto/buy', methods=['POST'])
def lottery_buying():
    req_data = request.get_json()
    name = req_data["name"]
    lottery_number = req_data["lottery_number"]
    conn = db_create_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"INSERT INTO lottery_buying (name,lottery_number) VALUES('{name}','{lottery_number}');")
        conn.commit()
        result = {"result": f"K.{name} bought {lottery_number} successfully"}
    except Exception as e:
        result = {"error": str(e)}
    conn.close()
    return result
