from datetime import datetime
from flask import Flask, jsonify, request
from provider import get_win_user, random_lottery_result, add_lottery_buying, validate_lottery_number
from db import db_create_connection, db_initial_table


app = Flask(__name__)
conn = db_create_connection()
db_initial_table(conn)

lottery_result = random_lottery_result()

@app.route('/lotto/showResult', methods=['GET'])
def show_lottery_result():
    try:
        data = get_win_user(lottery_result)
        if data:
            result_msg = f'Congrats !!! {data} You won the lottery prize :)'
        else:
            result_msg = f'Unfortunately, The lottery took your money. No one win this prize T_T'
        return {
            "status": "success",
            "data": result_msg,
            "result_number": f'The Lottery result is: {lottery_result}'}
    except Exception as e:
        return {"error": str(e), "status": "error"}, 400

@app.route('/lotto/buy', methods=['POST'])
def lottery_buying():
    try:
        req_data = request.get_json()
        name = req_data["name"]
        lottery_number = req_data["lottery_number"]
        if validate_lottery_number(lottery_number):
            add_lottery_buying(name, lottery_number)
            return {
                "data": f"User {name} bought number: {lottery_number} successfully.", 
                "status": "success"}
        else:
            return {
                "error": f"Sorry, Lotto service sell only 2 digits lottery , Pls try ex: 82, 09, 33 ..", 
                "status": "error"}, 400
    except Exception as e:
        return {"error": str(e), "status": "error"}, 400
