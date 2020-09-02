dias = int(input('Qts dias alugados? '))
km = float(input('Qts KM rodados? '))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))
