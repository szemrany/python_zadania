wysokosc = int(input('podaj wysokość choinki: '))

wynik = ''
spacja = wysokosc - 1
gwiazdka = 1
i = 0

while i < wysokosc:
    wynik += ' ' * spacja
    wynik += '*' * gwiazdka
    wynik += '\n'
    i += 1
    spacja -= 1
    gwiazdka += 2
print(wynik)
