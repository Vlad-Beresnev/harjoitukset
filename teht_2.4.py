import math

numero1 = float(input('Kirjoita numero (1): '))
numero2 = float(input('Kirjoita numero (2): '))
numero3 = float(input('Kirjoita numero (3): '))

num_list = (numero1, numero2, numero3)
keskiarvo = sum(num_list) / len(num_list)

print(f'summa: {sum(num_list)}')
print(f'tulos: {math.prod(num_list)}')
print(f'keskiarvo: {keskiarvo}')