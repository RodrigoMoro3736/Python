valores = []
valoresPares = []
valoresImpares = []
while True:
    valores.append(int(input('Digite um número: ')))
    condicao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if condicao == 'N':
        break
    elif condicao == 'S':
        continue
    else:
        condicao = str(input('ERRO! Digite SIM ou NÃO! : ')).strip().upper()[0]
for i, valor in enumerate(valores):
    if valor % 2 == 0:
        valoresPares.append(valor)
    else:
        valoresImpares.append(valor)
print('==-' * 10)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {valoresPares}')
print(f'A lista de ímpares é {valoresImpares}')
