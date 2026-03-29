import random


# --- Hissi ---

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi siirtyi kerrokseen {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi siirtyi kerrokseen {self.kerros}")

    def siirry_kerrokseen(self, kerros):
        while self.kerros < kerros:
            self.kerros_ylös()
        while self.kerros > kerros:
            self.kerros_alas()


# --- Talo ---

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissi_nro, kerros):
        self.hissit[hissi_nro].siirry_kerrokseen(kerros)

    def palohälytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät maantasokerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(0)


# --- Auto ---

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


# --- Kilpailu ---

class Kilpailu:
    def __init__(self, nimi, matka_km, autot):
        self.nimi = nimi
        self.matka_km = matka_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{'Rekisteri':<12}{'Huippunopeus':>14}{'Nopeus':>10}{'Matka':>10}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<12}{auto.huippunopeus:>14}{auto.nopeus:>10}{auto.kuljettu_matka:>10.0f}")

    def kilpailu_ohi(self):
        return any(auto.kuljettu_matka >= self.matka_km for auto in self.autot)


# --- Pääohjelma ---

# Testataan Hissiä
print("=== Hissitesti ===")
h = Hissi(0, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(0)

# Testataan Taloa
print("\n=== Talotesti ===")
talo = Talo(0, 10, 2)
talo.aja_hissiä(0, 7)
talo.aja_hissiä(1, 3)
talo.palohälytys()

# Autokilpailu Kilpailu-luokalla
print("\n=== The Great Junkyard Rally ===")
autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i+1}", random.randint(100, 200)))

kilpailu = Kilpailu("The Great Junkyard Rally", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        print(f"\n--- Tilanne tunnin {tunti} jälkeen ---")
        kilpailu.tulosta_tilanne()

print(f"\n--- Lopputilanne (tunti {tunti}) ---")
kilpailu.tulosta_tilanne()
