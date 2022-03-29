import random
liczba_1 = random.randint(1, 101)
liczba_2 = random.randint(1, 101)
suma = liczba_1 + liczba_2
odp = 0
while suma != odp:
    odp = int(input(f'Podaj sumę {liczba_1} i {liczba_2} '))
print('Prawidłowa odpowiedź')
