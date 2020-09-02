valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    condicao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if condicao == 'N':
        break
indicenum5 = []
for indice, valor in enumerate(valores):
    if valor == 5:
        indicenum5.append(indice)
valores.sort(reverse=True)
print('==-' * 10)
print(f'Foram digitados {len(valores)} números')
print(f'Em ordem decrescente: {valores}')
print('O valor 5 está na lista!' if valores.count(5) > 0 else 'O valor 5 não está na lista!', end=' ')
if indicenum5 != []:
    print(f'E se encontra na(s) posição(ões): {indicenum5}')
