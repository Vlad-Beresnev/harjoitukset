def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

# Pääohjelma (testaus)
testilista = [5, 10, 15, 20, 25]
tulos = laske_summa(testilista)
print(f"Lista: {testilista}")
print(f"Lukujen summa: {tulos}")
