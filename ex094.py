dicTemp = {}
listaMaster = []
mulheres = []
mediaInicial = 0
while True:
    dicTemp['nome'] = str(input('Nome: ')).title()
    while True:
        dicTemp['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dicTemp['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F!')
    dicTemp['idade'] = int(input('Idade: '))
    mediaInicial += dicTemp['idade']
    listaMaster.append([dicTemp.copy()])
    if dicTemp['sexo'] == 'F':
        mulheres.append([dicTemp['nome']].copy())
    dicTemp.clear()
    while True:
        condicao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if condicao in 'SN':
            break
        print('ERRO! Digite S ou N!')
    if condicao == 'N':
        break
mediaFinal = mediaInicial / len(listaMaster)
print('==-' * 15)
print(f'- O grupo tem {len(listaMaster)} pessoas.')
print(f'A média de idade dessa(s) {len(listaMaster)} pessoa(s) é {mediaFinal:.1f} anos.')
if len(mulheres) != 0:
    print(f'A(s) mulher(es) cadastrada(s) foi(foram): {mulheres}')
if len(listaMaster) >= 2:
    print('Lista de pessoas que estão acima da idade média:')
    for valor in listaMaster:
        for v in valor:
            if v['idade'] > mediaFinal:
                print(v)
