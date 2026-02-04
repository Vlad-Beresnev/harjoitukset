def vuodenaika(kuu_numero):
    vuodenaikat = [
        'talvi',  
        'talvi',  
        'kevät',  
        'kevät',  
        'kevät',  
        'kesä',   
        'kesä',   
        'kesä',   
        'syksy',  
        'syksy',  
        'syksy',  
        'talvi'   
    ]
    if not 1 <= kuu_numero <= 12:
        return 'Virheellinen kuukauden numero!'
    return f"{kuu_numero}. kuukausi kuuluu vuodenaikaan: {vuodenaikat[kuu_numero-1]}."
    
try:
    kuu_numero = int(input('Kirjoita kuukauden numero (1–12): '))
except ValueError:
    print('Syötteen täytyy olla kokonaisluku.')
else:
    print(vuodenaika(kuu_numero))
