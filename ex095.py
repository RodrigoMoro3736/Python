dicMaster = {}
gols = []
masterLista = []
cont = 0
while True:
    dicMaster['nome'] = str(input('Nome do jogador: ')).title()
    partidas = int(input(f'Quantas partidas {dicMaster["nome"]} jogou? '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    dicMaster['gols'] = gols.copy()
    dicMaster['total'] = sum(gols)
    masterLista.append(dicMaster.copy())
    dicMaster.clear()
    gols.clear()
    while True:
        condicao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if condicao in 'SN':
            break
        print('ERRO! Digite S ou N!')
    if condicao == 'N':
        break
print('==-' * 15)
print('cod  nome           gols           total')
for k, v in enumerate(masterLista):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('==-' * 15)
while True:
    condicao2 = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if condicao2 == 999:
        break
    if condicao2 >= len(masterLista):
        print(f'ERRO! Não existe jogador com código {condicao2}')
    else:
        print(f' -- Levantamento do jogador {masterLista[condicao2]["nome"]}:')
        for i, g in enumerate(masterLista[condicao2]["gols"]):
            print(f' -- No jogo {i + 1} fez {g} gols.')
    print('==-' * 15)
    print('Fim do programa! Volte sempre!')
