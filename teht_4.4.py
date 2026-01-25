numerot = []

while True:
    syote = input("Syötä luku: ")
    if syote == "":
        break
    try:
        luku = float(syote)
        numerot.append(luku)
    except ValueError:
        print("Virheellinen syöte.")

if numerot:
    pienin = min(numerot)
    suurin = max(numerot)
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
