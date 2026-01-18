perch = int(input('Anna kuhan pituus (cm): '))
if perch < 37:
    print(f'Kuha on alikokoinen, tarvitset vähintään {37 - perch} cm lisää.')
else:
    print('Kuha on sallittu.')