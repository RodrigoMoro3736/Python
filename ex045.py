import random

lista = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(lista)

jogador = int(input("""Vamos Jogar JOKENPÔ!
1 - Pedra
2 - Papel
3 - Tesoura
Digite 1, 2 ou 3 : """))

print('Computador: {}'.format(computador))

if jogador < 1 or jogador > 3:
    print('ERRO! Digite um dos 3 números!')
elif computador == 'Pedra' and jogador == 1:
    print('Empate!')
elif computador == 'Pedra' and jogador == 2:
    print('Você venceu!')
elif computador == 'Pedra' and jogador == 3:
    print('O computador venceu!')
elif computador == 'Papel' and jogador == 1:
    print('O computador venceu!')
elif computador == 'Papel' and jogador == 2:
    print('Empate!')
elif computador == 'Papel' and jogador == 3:
    print('Você venceu!')
elif computador == 'Tesoura' and jogador == 1:
    print('Você venceu!')
elif computador == 'Tesoura' and jogador == 2:
    print('O computador venceu!')
elif computador == 'Tesoura' and jogador == 3:
    print('Empate!')
