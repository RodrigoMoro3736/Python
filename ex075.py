num1 = (str(input('Digite um número: ')))
num2 = (str(input('Digite outro número: ')))
num3 = (str(input('Digite mais um número: ')))
num4 = (str(input('Digite o último número: ')))
numeros = (num1 + num2 + num3 + num4)
print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count("9")} vez(es)')
if numeros.count('3') != 0:
    print(f'O valor 3 apareceu na {(numeros.index("3") + 1)}ª posicão')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram:', end=' ')
for c in range(0, 4):
    if int(numeros[c]) % 2 == 0:
        print(numeros[c], end=' ')
    c += 1
