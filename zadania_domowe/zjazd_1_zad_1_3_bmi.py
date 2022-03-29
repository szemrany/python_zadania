masa = float(input('Podaj masę ciała w kg: '))
wzrost = float(input('Podaj wzrost w cm: '))
bmi = masa / (wzrost / 100)**2
print(f'Twoje bmi: {bmi:.2f}')
