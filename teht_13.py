import math
import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

app = Flask(__name__)


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = int(math.isqrt(number))
    for divisor in range(3, limit + 1, 2):
        if number % divisor == 0:
            return False
    return True


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user=os.getenv("USER_NAME"),
        password=os.getenv("DB_PASSWORD"),
        autocommit=True,
    )


@app.get("/alkuluku/<int:number>")
def prime_endpoint(number: int):
    return jsonify({"Number": number, "isPrime": is_prime(number)})


@app.get("/kentta/<string:icao>")
def airport_endpoint(icao: str):
    icao_code = icao.upper()

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT name, municipality FROM airport WHERE ident = %s",
            (icao_code,),
        )
        result = cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

    # Assignment-minimal fallback for unknown ICAO.
    if not result:
        return jsonify({"ICAO": icao_code, "Name": None, "Municipality": None})

    return jsonify(
        {
            "ICAO": icao_code,
            "Name": result[0],
            "Municipality": result[1],
        }
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)
