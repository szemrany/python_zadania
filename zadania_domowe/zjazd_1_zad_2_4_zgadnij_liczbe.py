import random

liczba_wylosowana = random.randint(0, 1000)
proby = 0

while True:
    liczba_zgadywana = int(input("zgadnij liczbę z zakresu 0-999: "))
    proby += 1
    if liczba_zgadywana == liczba_wylosowana:
        print(f"Brawo! Zgadłeś! Liczba prób: {proby}")
        break;
    elif liczba_zgadywana > liczba_wylosowana:
        print(f'Nie zgadłeś, podana liczba jest za duża!')
    elif liczba_zgadywana < liczba_wylosowana:
        print(f'Nie zgadłeś, podana liczba jest za mała!')
    else:
        print(f'Podaj prawidłową wartość, liczbę od 0 do 999!')



