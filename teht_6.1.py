import random

def heita_noppaa():
    return random.randint(1, 6)

# Pääohjelma
silmaluku = 0
while silmaluku != 6:
    silmaluku = heita_noppaa()
    print(f"Noppa heitti: {silmaluku}")

print("Sait kuutosen!")
