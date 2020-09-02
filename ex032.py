ano = int(input('Digite um ano para saber se ele é bissexto: '))
bissexto = ano % 4
mult100 = ano % 100
mult400 = ano % 400
if bissexto == 0 and mult100 != 0 or mult400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
