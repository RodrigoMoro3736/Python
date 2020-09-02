import random
from operator import itemgetter
from time import sleep
jogadores = {}
cont = 1
print('Valores sorteados:')
for c in range(1, 5):
    jogadores[f'jogador{c}'] = random.randint(1, 6)
for k, v in jogadores.items():
    print(f'   O {k} tirou {v}')
    sleep(0.5)
print('Ranking dos jogadores:')
for final, valor in sorted(jogadores.items(), key=itemgetter(1), reverse=True):
    print(f'   {cont}º lugar: {final} com {jogadores[final]}')
    cont += 1
    sleep(0.5)
