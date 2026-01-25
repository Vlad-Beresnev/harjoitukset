import random

try:
    N = int(input("Anna arvottavien pisteiden määrä: "))
    n = 0

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            n += 1

    pi_likiarvo = 4 * n / N
    print(f"Piin likiarvo on: {pi_likiarvo}")

except ValueError:
    print("Virheellinen syöte.")
except ZeroDivisionError:
    print("Pisteiden määrän tulee olla suurempi kuin nolla.")
