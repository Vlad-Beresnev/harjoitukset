import requests

# ── Exercise 1 ─────────────────────────────────────────────────────────────
# Fetch and print a random Chuck Norris joke

print('=== Tehtävä 1: Chuck Norris -vitsi ===')

try:
    vastaus = requests.get('https://api.chucknorris.io/jokes/random')
    if vastaus.status_code == 200:
        print(vastaus.json()['value'])
    else:
        print('Vitsiä ei voitu hakea.')
except requests.exceptions.RequestException:
    print('Yhteysvirhe: vitsiä ei voitu hakea.')


# ── Exercise 2 ─────────────────────────────────────────────────────────────
# Ask for a city name and print current weather + temperature in Celsius

API_AVAIN = '4d130245e9df76b3c37dd66cdb984fd0'

print()
print('=== Tehtävä 2: Säätiedot ===')

kaupunki = input('Anna paikkakunnan nimi: ')

try:
    pyynto = f'https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={API_AVAIN}&lang=fi'
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        data = vastaus.json()
        kuvaus = data['weather'][0]['description']
        lampotila = data['main']['temp'] - 273.15
        print(f'Säätila: {kuvaus}')
        print(f'Lämpötila: {lampotila:.1f} °C')
    else:
        print('Paikkakuntaa ei löydy tai tietoja ei voitu hakea.')
except requests.exceptions.RequestException:
    print('Yhteysvirhe: säätietoja ei voitu hakea.')
