import mysql.connector
import os
from dotenv import load_dotenv

icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")

try:
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user=os.getenv('USER_NAME'),
        password=os.getenv('DB_PASSWORD'),
        autocommit=True
    )
except mysql.connector.Error as err:
    print(f"Error connecting: {err}")
    exit()

cursor = conn.cursor()

sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao_koodi}'"

cursor.execute(sql)
tulos = cursor.fetchone()  

if tulos:
    print(f"Lentokentän nimi: {tulos[0]}")  # type: ignore
    print(f"Sijaintikunta: {tulos[1]}")  # type: ignore
else:
    print("Lentokenttää ei löytynyt tällä ICAO-koodilla.")

cursor.close()
conn.close()