import random

arpakuutio_maara = int(input("Kuinka monta arpakuutiota haluat? "))
arpakuutiot = []

for i in range(arpakuutio_maara):
    input("Paina Enter arvataksesi arpakuution silmäluvun...")
    silmaluku = random.randint(1, 6)
    print(f"Arpakuutio {i + 1}: {silmaluku}")
    arpakuutiot.append(silmaluku)

print(f"\nKaikki arpakuutiot: {arpakuutiot}")
print(f"Silmälukujen summa: {sum(arpakuutiot)}")