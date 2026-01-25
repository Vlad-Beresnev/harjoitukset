while True:
    tuuma = float(input("Anna tuuma-arvo: "))
    if tuuma < 0:
        print("Ojhelma päättyy.")
        break
    cm = tuuma * 2.54
    print(f"Senttimetreinä: {cm:.2f}")