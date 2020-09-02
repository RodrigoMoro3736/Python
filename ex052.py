num = int(input('Digite um número inteiro para ver se é um número primo: '))

if num == 1:
    print('O número 1 NÃO é um número primo!')
elif num == 2 or num == 3 or num == 5 or num == 7 or num == 11:
    print(f'O número {num} é SIM um número primo!')
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
    print(f'O número {num} NÃO é um número primo!')
else:
    print(f'O número {num} é SIM um número primo!')
