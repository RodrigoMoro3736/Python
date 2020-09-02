preco = float(input('Digite o preço: R$'))
desc = round(preco - (preco * 0.05), 2)
print('O valor R${} com 5% de desconto fica: R${}'.format(preco, desc))
