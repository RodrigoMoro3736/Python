def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
nomeJogador = str(input('Nome do jogador: ')).title()
golsJogador = input('Número de gols: ')
ficha(nomeJogador, golsJogador)
