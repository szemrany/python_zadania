import math

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = float(input('Podaj c: '))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'Pole trójkąta wynosi: {pole:.2f}')
else:
    print('Z podanych boków nie można zbudować trójkąta')
