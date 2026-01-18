cabin_class = str(input("Anna ship's cabin class: "))
if cabin_class == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif cabin_class == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif cabin_class == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif cabin_class == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka.')