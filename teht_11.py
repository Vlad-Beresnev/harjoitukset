# Tehtävä 11 – Periytyminen (Inheritance)


# ── Exercise 1 ─────────────────────────────────────────────────────────────
# Class hierarchy: Julkaisu → Kirja / Lehti

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi}')
        print(f'Kirjoittaja: {self.kirjoittaja}')
        print(f'Sivumäärä: {self.sivumaara}')


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi}')
        print(f'Päätoimittaja: {self.paatoimittaja}')


print('=== Tehtävä 1 ===')
aku_ankka = Lehti('Aku Ankka', 'Aki Hyyppä')
hytti = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)

aku_ankka.tulosta_tiedot()
print()
hytti.tulosta_tiedot()


# ── Exercise 2 ─────────────────────────────────────────────────────────────
# Auto base class (from chapter 9) + Sähköauto / Polttomoottoriauto subclasses

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

    def tulosta_tiedot(self):
        print(f'{self.rekisteritunnus}: nopeus {self.nopeus} km/h, matka {self.kuljettu_matka} km')


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'  Akkukapasiteetti: {self.akkukapasiteetti} kWh')


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'  Tankin koko: {self.tankin_koko} l')


print()
print('=== Tehtävä 2 ===')

sahko = Sahkoauto('ABC-15', 180, 52.5)
poltto = Polttomoottoriauto('ACD-123', 165, 32.3)

sahko.kiihdyta(120)
poltto.kiihdyta(100)

sahko.kulje(3)
poltto.kulje(3)

sahko.tulosta_tiedot()
poltto.tulosta_tiedot()
