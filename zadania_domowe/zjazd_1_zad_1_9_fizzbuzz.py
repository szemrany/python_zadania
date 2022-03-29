liczba = 1
while liczba <= 100:
    if liczba % 15 == 0:
        print('FizzBuzz')
    elif liczba % 5 == 0:
        print('Buzz')
    elif liczba % 3 == 0:
        print('Fizz')
    else:
        print(liczba)
    liczba += 1

