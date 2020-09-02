import random
print('VAMOS JOGAR PAR OU IMPAR')
cont = 0
jogador = 0
derrota = 0
while derrota == 0:
    computador = random.randint(0, 5)
    jogador = int(input('Digite um valor: '))
    parImpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = jogador + computador
    if soma % 2 == 0 and parImpar == 'P':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
        cont += 1
        print('VOCÊ VENCEU! Vamos jogar novamente!')
    if soma % 2 == 0 and parImpar == 'I':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
        derrota += 1
        print(f'Você perdeu!\n==> {cont} vitória(s) consecutiva(s)!')
    if soma % 2 != 0 and parImpar == 'P':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        derrota += 1
        print(f'Você perdeu!\n==> {cont} vitória(s) consecutiva(s)!')
    if soma % 2 != 0 and parImpar == 'I':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        cont += 1
        print('VOCÊ VENCEU! Vamos jogar novamente!')
    if parImpar not in 'PI':
        print('ERRO! Digite `P` ou `I`')
        break
