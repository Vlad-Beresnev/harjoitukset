nimet = set()
nimi = str(input('Anna nimi: '))
while nimi != '':
    if nimi in nimet:
        print('Aiemmin syötetty nimi.')
    else:
        print('Uusi nimi.')
        nimet.add(nimi)
    nimi = str(input('Anna nimi: '))
print(nimet)