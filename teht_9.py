import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus = max(0, min(self.huippunopeus, self.nopeus + muutos))

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

# Testataan Auto-luokkaa
auto = Auto("ABC-123", 142)
print(auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Nopeus: {auto.nopeus}")

auto.kiihdytä(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus}")

# Autokilpailu
autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i+1}", random.randint(100, 200)))

while not any(auto.kuljettu_matka >= 10000 for auto in autot):
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

print(f"\n{'Rekisteri':<12}{'Huippunopeus':>14}{'Nopeus':>10}{'Matka':>10}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<12}{auto.huippunopeus:>14}{auto.nopeus:>10}{auto.kuljettu_matka:>10.0f}")
