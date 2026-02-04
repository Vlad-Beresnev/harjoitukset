lentoasemat = {}

while True:
    valinta = input("Haluatko syöttää uuden lentoaseman (uusi), hakea tiedot (haku) vai lopettaa (lopeta): ")

    if valinta == "lopeta":
        break
    elif valinta == "uusi":
        icao = input("Syötä ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao] = nimi
    elif valinta == "haku":
        icao = input("Syötä ICAO-koodi: ")
        if icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")
    else:
        print("Virheellinen valinta.")
