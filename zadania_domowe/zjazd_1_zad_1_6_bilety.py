wiek = int(input('Podaj wiek: '))
bilety = int(input('Ile biletów chcesz kupić: '))

if wiek >= 65:
    cena = 1.90
elif wiek >= 18:
    cena = 3.80
elif wiek >= 7:
    cena = 2.28
else:
    cena = 0

cena_bilety = bilety * cena
print(f'Do zapłaty: {cena_bilety:.2f}')
