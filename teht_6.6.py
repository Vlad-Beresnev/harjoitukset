import math

def laske_yksikkohinta(halkaisija_cm, hinta_eur):
    # Muunna halkaisija senttimetreistä metreiksi
    sade_m = (halkaisija_cm / 100) / 2
    # Laske pinta-ala neliömetreinä
    pinta_ala_m2 = math.pi * sade_m ** 2
    # Laske yksikköhinta (euroa per neliömetri)
    yksikkohinta = hinta_eur / pinta_ala_m2
    return yksikkohinta

# Pääohjelma
print("Pizza 1:")
halkaisija1 = float(input("Anna pizzan halkaisija (cm): "))
hinta1 = float(input("Anna pizzan hinta (€): "))

print("\nPizza 2:")
halkaisija2 = float(input("Anna pizzan halkaisija (cm): "))
hinta2 = float(input("Anna pizzan hinta (€): "))

yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

print(f"\nPizza 1 yksikköhinta: {yksikkohinta1:.2f} €/m²")
print(f"Pizza 2 yksikköhinta: {yksikkohinta2:.2f} €/m²")

if yksikkohinta1 < yksikkohinta2:
    print("\nPizza 1 antaa paremman vastineen rahalle!")
elif yksikkohinta2 < yksikkohinta1:
    print("\nPizza 2 antaa paremman vastineen rahalle!")
else:
    print("\nMolemmat pizzat antavat yhtä hyvän vastineen rahalle!")
