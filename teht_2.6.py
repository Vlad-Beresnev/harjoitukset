import random

def lock_codes():
    dig3 = ""
    dig4 = ""
    for i in range(3):
        i = random.randint(0, 9)
        k = random.randint(1, 6)
        dig3 += str(i)
        dig4 += str(k)
    for i in range(1):
        i = random.randint(0, 6)
        dig4 += str(i)
    tulos = f"lock codes:\n3-digits: {dig3}\n4-digits: {dig4}"
    return tulos

print(lock_codes())