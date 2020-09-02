listaMaster = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        listaMaster[0].append(num)
    else:
        listaMaster[1].append(num)
listaMaster[0].sort()
listaMaster[1].sort()
print('==-' * 10)
print(f'Os valores pares: {listaMaster[0]}')
print(f'Os valores ímpares: {listaMaster[1]}')
