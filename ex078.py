numeros = []
for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {c}: ')))
print('==-' * 20)
print(f'Você digitou os valores {numeros}')
maximo = []
minimo = []
for c, v in enumerate(numeros):
    if v >= max(numeros):
        maximo.append(c)
    if v <= min(numeros):
        minimo.append(c)
if numeros.count(max(numeros)) == 1:
    print(f'O maior valor digitado foi {max(numeros)} na posição: {numeros.index(max(numeros))}')
else:
    print(f'O maior valor digitado foi {max(numeros)} nas posições {maximo}')
if numeros.count(min(numeros)) == 1:
    print(f'O menor valor digitado foi {min(numeros)} na posição: {numeros.index(min(numeros))}')
else:
    print(f'O menor valor digitado foi {min(numeros)} nas posições {minimo}')
