valores = []
num1 = int(input('Digite um valor: '))
valores.append(num1)
print('Adicionado ao final da lista...')
for c in range(0, 4):
    num = int(input('Digite um valor: '))
    if num > max(valores):
        valores.append(num)
        print(f'Adicionado ao final da lista...')
    elif num <= valores[0]:
        valores.insert(0, num)
        print(f'Adicionado na posição 0 da lista...')
    elif num <= valores[1]:
        valores.insert(1, num)
        print(f'Adicionado na posição 1 da lista...')
    elif num <= valores[2]:
        valores.insert(2, num)
        print(f'Adicionado na posição 2 da lista...')
    elif num <= valores[3]:
        valores.insert(3, num)
        print(f'Adicionado na posição 3 da lista...')
print('==-' * 10)
print(f'Os valores digitados em ordem: {valores}')
