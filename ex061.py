priTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 0
while contador < 10:
    print(priTermo, end=' → ')
    priTermo += razao
    contador += 1
print('FIM')
