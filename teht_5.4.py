kaupungit = []

for i in range(5):
    kaupunki = input(f"Anna {i + 1}. kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("\nKaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)
