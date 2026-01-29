def gallona_litroiksi(gallonat):
    return gallonat * 3.785

# Pääohjelma
while True:
    gallonat = float(input("Anna bensiinin määrä gallonoina: "))
    
    if gallonat < 0:
        print("Lopetetaan.")
        break
    
    litrat = gallona_litroiksi(gallonat)
    print(f"{gallonat} gallonaa on {litrat:.2f} litraa.\n")
