num = float(input('Digite quantos reais vc tem na carteira agora: R$'))
dol = round(num / 3.27, 2)
print('Você pode comprar US${} com R${} !'.format(dol, num))