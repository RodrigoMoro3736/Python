# formatação de cores
# \033[0;33;44m

# o \033[   m é onde vão as formatações de cores
# tem 3 campos.. primeiro estilo ; segundo texto ; terceiro fundo

# estilo:
# 0 none
# 1 negrito
# underline
# 7 negativo

# texto:
# de 30 até 37
# branco, vermelho, verde, amarelo, azul, roxo, piscina, cinza

# fundo:
# de 40 até 47
# branco, vermelho, verde, amarelo, azul, roxo, piscina, cinza

print('\033[7;30;41m teste\033[m')
print('\033[32mTESTE 01\033[m  e \033[31mTESTE 02\033[m!!!')
print('teste {}teste2{} teste3'.format('\033[4;34m', '\033[m'))

cores = {'limpa': '\033[m',
         'none': '\033[0m',
         'negrito': '\033[1m',
         'underline': '\033[4m',
         'negativo': '\033[7m',
         'textoBranco': '\033[30m',
         'textoVermelho': '\033[31m',
         'textoVerde': '\033[32m',
         'textoAmarelo': '\033[33m',
         'textoAzul': '\033[34m',
         'textoRoxo': '\033[35m',
         'textoPiscina': '\033[36m',
         'textoCinza': '\033[37m',
         'fundoBranco': '\033[40m',
         'fundoVermelho': '\033[41m',
         'fundoVerde': '\033[42m',
         'fundoAmarelo': '\033[43m',
         'fundoAzul': '\033[44m',
         'fundoRoxo': '\033[45m',
         'fundoPiscina': '\033[46m',
         'fundoCinza': '\033[47m', }

print('teste {}teste2{}'.format(cores['azul'], cores['limpa']))
