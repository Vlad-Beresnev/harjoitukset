import math

item1 = float(input('Anna leiviskät: '))
item2 = float(input('Anna naulat: '))
item3 = float(input('Anna luodit: '))

items_list = (item1, item2, item3)
grams = sum(items_list) / 2.2
kilograms = int(grams // 1)
grams = int(round(grams - kilograms, 3) * 1000)
if grams == 1000:
    kilograms += 1
    grams = 0
print("Massa nykymittojen mukaan:")
print(f"{kilograms} kilogrammaa ja {grams} grammaa.")