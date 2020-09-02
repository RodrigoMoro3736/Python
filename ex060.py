num = int(input('Digite um número para ver seu fatorial: '))
calc = num
total = num
if num == 0:
    print('0 fatorial é = 1')
else:
    while calc > 1:
        total = total * (calc - 1)
        calc -= 1
    print(f'{num} fatorial é = {total}')
