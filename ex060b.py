num = int(input('Digite um número para ver o seu fatorial: '))
total = num
calc = num
if num == 0:
    print('0 fatorial é = 1')
else:
    for c in range(1, num):
        total = total * (calc - 1)
        calc = calc - 1
    print(f'{num} fatorial é = {total}')
