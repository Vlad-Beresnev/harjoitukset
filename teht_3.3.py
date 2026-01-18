sukupuoli = str(input('Anna sukupuoli: '))
hem = int(input('Anna hemoglobiiniarvo: '))
if sukupuoli == 'mies' or sukupuoli == 'Mies':
    if 134 <= hem <= 195:
        print('hemoglobiiniarvo on normaali')
    elif hem < 134:
        print('hemoglobiiniarvo on alhainen')
    elif hem > 195:
        print('hemoglobiiniarvo on korkea')
if sukupuoli == 'nainen' or sukupuoli == 'Nainen':
    if 117 <= hem <= 175:
        print('hemoglobiiniarvo on normaali')
    elif hem < 117:
        print('hemoglobiiniarvo on alhainen')
    elif hem > 175:
        print('hemoglobiiniarvo on korkea')