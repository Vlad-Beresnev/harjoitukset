luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print(f"Luku {luku} ei ole alkuluku.")
else:
    on_alkuluku = True
    
    for i in range(2, luku):
        if luku % i == 0:
            on_alkuluku = False
            break
    
    if on_alkuluku:
        print(f"Luku {luku} on alkuluku.")
    else:
        print(f"Luku {luku} ei ole alkuluku.")
