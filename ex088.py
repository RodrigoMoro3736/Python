import random
from time import sleep
jogos = []
final = []
condicao = int(input('Quantos jogos vc quer q eu sorteie? '))
total = 1
while total <= condicao:
    contador = 0
    while True:
        numeroAleatorio = random.randint(1, 60)
        if numeroAleatorio not in jogos:
            jogos.append(numeroAleatorio)
            contador += 1
        if contador >= 6:
            break
    jogos.sort()
    final.append(jogos[:])
    jogos.clear()
    total += 1
print(f'Sorteando {condicao} jogos:')
for i, l in enumerate(final):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.5)
