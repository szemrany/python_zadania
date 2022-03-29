
liczby = 0
suma = 0
min = 1000000000
max = 0

while True:
    liczba = input("podaj liczbę (wpisz stop żeby zakończyć): ")
    if liczba == 'stop':
        break
    else:
        liczba = float(liczba)
    liczby += 1
    suma += liczba
    if liczba > max:
        max = liczba
    if liczba < min:
        min = liczba

print(f'liczba podanych liczb: {liczby}')
print(f'suma: {suma}')
print(f'średnia: {suma / liczby:.2f}')
print(f'minimum: {min:.2f}')
print(f'maksimum: {max:.2f}')


