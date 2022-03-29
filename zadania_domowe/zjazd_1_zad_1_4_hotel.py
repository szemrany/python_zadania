wiek = int(input('Podaj wiek: '))
noc = int(input('Ile nocy: '))
if wiek < 18:
    cena = noc * 100
else:
    if noc >= 5:
        cena = noc * 150
    elif noc >= 2:
        cena = noc * 180
    else:
        cena = 200

if wiek >= 65:
    cena *= 0.9

print(f'Twoja cena: {cena:.2f} zł')
