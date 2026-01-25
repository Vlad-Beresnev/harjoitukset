yritykset = 0
max_yritykset = 5

oikea_kayttajatunnus = "python"
oikea_salasana = "rules"

while yritykset < max_yritykset:
    kayttajatunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        yritykset += 1
        if yritykset < max_yritykset:
            print("Väärä tunnus tai salasana, yritä uudelleen.")

if yritykset == max_yritykset:
    print("Pääsy evätty")
