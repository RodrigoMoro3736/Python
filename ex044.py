valor = float(input('Digite o valor do produto: '))
condicao = int(input("""1 - À vista em dinheiro ou cheque: 10% de desconto!
2 - À vista no cartão: 5% de desconto!
3 - Em até 2x no cartão: preço normal!
4 - 3x ou mais no cartão: 20% de juros!
Escolha a opção de pagamento: """))

if condicao < 1 or condicao > 4:
    print('ERRO! Escolha uma das 4 opções de pagamento!')
elif condicao == 1:
    valor10 = valor - (valor * 0.10)
    print('O valor R${:.2f} com 10% de desconto fica R${:.2f}'.format(valor, valor10))
elif condicao == 2:
    valor5 = valor - (valor * 0.05)
    print('O valor R${:.2f} com 5% de desconto fica R${:.2f}'.format(valor, valor5))
elif condicao == 3:
    print('O valor R${:.2f} não muda nessa condição de pagamento!'.format(valor))
elif condicao == 4:
    parcelas = int(input('Em quantas parcelas? : '))
    valor20 = valor + (valor * 0.2)
    print('O valor R${:.2f} com 20% de juros fica R${:.2f}'.format(valor, valor20))
    print('E em {}x, cada parcela fica R${:.2f}'.format(parcelas, valor20 / parcelas))
