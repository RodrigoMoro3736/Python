numero = int(input('Digite um numero inteiro: '))
resto = numero % 2
if resto == 0:
    print('{} é um número PAR!'.format(numero))
else:
    print('{} é um número IMPAR!'.format(numero))
