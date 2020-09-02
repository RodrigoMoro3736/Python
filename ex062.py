priTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 0
while contador < 10:
    print(priTermo, end=' → ')
    priTermo += razao
    contador += 1
condicao1 = 1
while condicao1 != 0:
    condicao1 = int(input('\nDeseja mostrar mais termos?\nDigite quantos termos (0 para sair): '))
    contador2 = condicao1
    while contador2 > 0:
        print(priTermo, end=' → ')
        priTermo += razao
        contador2 = contador2 - 1
print('FIM')
