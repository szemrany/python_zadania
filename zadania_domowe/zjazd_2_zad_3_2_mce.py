# wersja a

def sprawdz_dni(miesiac):
    miesiace = ['styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien', 'pazdziernik', 'listopad', 'grudzien']
    if miesiac.lower() in miesiace:
        nr_mca = miesiace.index(miesiac) + 1
        if nr_mca in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30
    else:
        return "nie znam takiego miesiaca"

miesiac = input("podaj nazwę miesiąca: ")
print(f'Miesiac {miesiac} ma {sprawdz_dni(miesiac)} dni')


# wersja b

def sprawdz_dni(miesiac):
    miesiace = ['styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien', 'pazdziernik', 'listopad', 'grudzien']
    if miesiac.lower() in miesiace:
        nr_mca = miesiace.index(miesiac) + 1
        if nr_mca in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif nr_mca == 2:
            rok = int(input('podaj rok'))
            if (rok % 4 == 0) and (rok % 100 != 0) or (rok % 400 == 0):
                return 29
            else:
                return 28
        else:
            return 30
    else:
        return "nie znam takiego miesiaca"

miesiac = input("podaj nazwę miesiąca: ")
print(f'Miesiac {miesiac} ma {sprawdz_dni(miesiac)} dni')
