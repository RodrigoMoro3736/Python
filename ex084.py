nomes = []
nomeMaior = []
nomeMenor = []
maior = menor = 0
while True:
    nome = str(input('Nome: ')).title()
    nomes.append(nome)
    peso = float(input('Peso: '))
    if maior == 0 and menor == 0:
        maior = peso
        nomeMaior.append(nome)
        menor = peso
        nomeMenor.append(nome)
    else:
        if peso == maior:
            nomeMaior.append(nome)
        if peso > maior:
            maior = peso
            nomeMaior.clear()
            nomeMaior.append(nome)
        if peso == menor:
            nomeMenor.append(nome)
        if peso < menor:
            menor = peso
            nomeMenor.clear()
            nomeMenor.append(nome)
    condicao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if condicao == 'N':
        break
print(f'Ao todo vc cadastrou {len(nomes)} pessoas.')
print(f'Maior peso: {maior:.1f}Kg de {nomeMaior}')
print(f'Menor peso: {menor:.1f}Kg de {nomeMenor}')
