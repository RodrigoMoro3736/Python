def leiaInt(num):
    while True:
        x = input(num)
        if x.isdigit():
            return x
            break
        else:
            print('ERRO! Digite um número inteiro válido!')
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
