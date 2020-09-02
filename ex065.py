num = []
contador = 1
while contador > 0:
    n = int(input('Digite um número inteiro: '))
    num.append(n)
    contador += 1
    condicao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if condicao == 'S':
        continue
    else:
        break
print('==-' * 10)
print(f'Você digitou {contador - 1} números!')
print(f'A média desses números é: {(sum(num)) / (contador - 1):.1f}')
