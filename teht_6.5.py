def karsi_parittomat(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

# Pääohjelma (testaus)
alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu = karsi_parittomat(alkuperainen)

print(f"Alkuperäinen lista: {alkuperainen}")
print(f"Karsittu lista: {karsittu}")
