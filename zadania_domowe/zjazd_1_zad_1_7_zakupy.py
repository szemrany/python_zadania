nazwa = input('Co chcesz kupić? ')
cena = float(input('Podaj cenę towaru: '))
ilosc = float(input('Podaj ilość towaru: '))

print(f'Za {nazwa}, który chcesz kupić, zapłacisz {cena * ilosc:.2f} zł')
