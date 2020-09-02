dicMaster = {}
gols = []
cont = 1
dicMaster['nome'] = str(input('Nome do jogador: ')).title()
partidas = int(input(f'Quantas partidas {dicMaster["nome"]} jogou? '))
for c in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
dicMaster['gols'] = gols.copy()
dicMaster['total'] = sum(gols)
print('==-' * 15)
print(dicMaster)
print('==-' * 15)
for k, v in dicMaster.items():
    print(f'O campo `{k}` tem o valor `{v}`.')
print('==-' * 15)
print(f'O jogador {dicMaster["nome"]} jogou {partidas} partidas.')
for v2 in dicMaster["gols"]:
    print(f'   => Na partida {cont}, fez {v2} gols.')
    cont += 1
print(f'Foi um total de {dicMaster["total"]} gols.')
