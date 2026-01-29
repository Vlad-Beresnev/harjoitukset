luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    
    if syote == "":
        break
    
    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte. Anna numero.")

if len(luvut) >= 5:
    luvut.sort(reverse=True)
    print("\nViisi suurinta lukua:")
    for i in range(5):
        print(luvut[i])
elif len(luvut) > 0:
    luvut.sort(reverse=True)
    print(f"\nSyötit vain {len(luvut)} lukua. Kaikki luvut suuruusjärjestyksessä:")
    for luku in luvut:
        print(luku)
else:
    print("\nEt syöttänyt yhtään lukua.")
