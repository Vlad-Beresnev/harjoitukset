import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

maakoodi = input("Syötä maakoodi (esim. FI): ")

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

sql = f"SELECT type, COUNT(*) FROM airport WHERE iso_country = '{maakoodi}' GROUP BY type"

cursor.execute(sql)
tulokset = cursor.fetchall()

if tulokset:
    print(f"Lentokentät maassa {maakoodi}:")
    for rivi in tulokset:
        print(f"{rivi[0]}: {rivi[1]} kpl")  # type: ignore
else:
    print(f"Ei lentokenttiä maassa {maakoodi} tai virheellinen maakoodi.")

cursor.close()
conn.close()
