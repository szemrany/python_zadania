import math


def stopy_na_metry(stopy: float) -> float:
    return stopy * 0.3048

stopy = float(input('Podaj dlugosc w stopach: '))
print(f'{stopy} stopy = {stopy_na_metry(stopy):.2f} m')

def wieksza(a: float, b: float) -> float:
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "liczby są równe"

a = float(input('podaj pierwszą liczbę: '))
b = float(input('podaj drugą liczbę: '))
print(f'Większa liczba to: {wieksza(a, b)}')

def srednia(a, b):
    return (a+b) / 2


print(srednia(2, 3))



def pole_kola(r):
    return 2 * math.pi * r

pole_kola(5)


def bmi(masa, wzrost):
    return masa / wzrost ** 2

print(f'Twoje bmi: {bmi(100, 1.9)}')

def pole_trojkata(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


print(pole_trojkata(4, 5, 7))

def kilometry_na_mile(km):
    return km * 0.621371192

def mile_na_kilometry(mile):
    return mile * 1.609344








