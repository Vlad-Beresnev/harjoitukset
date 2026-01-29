import random

def heita_noppaa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

# Pääohjelma
tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

silmaluku = 0
while silmaluku != tahkojen_maara:
    silmaluku = heita_noppaa(tahkojen_maara)
    print(f"Noppa heitti: {silmaluku}")

print(f"Sait maksimisilmäluvun {tahkojen_maara}!")
