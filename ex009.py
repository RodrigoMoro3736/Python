num = int(input('Digite um número para ver a sua taboada: '))
mult = 0
while (mult <= 10):
    print('{} x {} = {}'.format(num, mult, num * mult))
    mult += 1
