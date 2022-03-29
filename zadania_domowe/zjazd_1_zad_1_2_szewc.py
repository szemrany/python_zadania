dzien = int(input('Podaj dzien oddania butów do szewca (1-7): '))
naprawa = int(input('Podaj ile dni bedzie trwala naprawa: '))

if dzien + naprawa <= 7:
    odbior = dzien + naprawa
else:
    odbior = dzien + naprawa - 7

if odbior == 1:
    dzien = 'poniedziałek'
elif odbior == 2:
    dzien = 'wtorek'
elif odbior == 3:
    dzien = 'sroda'
elif odbior == 4:
    dzien = 'czwartek'
elif odbior == 5:
    dzien = 'piątek'
elif odbior == 6:
    dzien = 'sobota'
elif odbior == 7:
    dzien = 'niedziela'

print(f'Buty do odbioru w dniu: {dzien}')
