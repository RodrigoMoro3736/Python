num = int(input('Digite um número inteiro: '))
contador = num
num1 = 0
num2 = 1
num3 = 0
print('0', end=', ')
while contador > 1:
    num3 = num1 + num2
    num1 = num3
    num2 = num3 - num2
    print(num3, end=', ')
    contador = contador - 1
print('FIM')
