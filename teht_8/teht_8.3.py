import mysql.connector
from geopy.distance import distance
import os
from dotenv import load_dotenv

load_dotenv()

def get_coordinates(cursor, icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return result
    else:
        return None

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

icao1 = input("Syötä ensimmäisen lentoaseman ICAO-koodi: ")
icao2 = input("Syötä toisen lentoaseman ICAO-koodi: ")

coords1 = get_coordinates(cursor, icao1)
coords2 = get_coordinates(cursor, icao2)

if coords1 and coords2:
    dist = distance(coords1, coords2).km
    print(f"Lentokenttien välinen etäisyys on: {dist:.2f} km")
else:
    if not coords1:
        print(f"Lentoasemaa {icao1} ei löytynyt.")
    if not coords2:
        print(f"Lentoasemaa {icao2} ei löytynyt.")

cursor.close()
conn.close()
