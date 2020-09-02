saque = int(input('Que valor você quer sacar? R$'))
nota50 = int(saque / 50)
nota20 = int((saque - (nota50 * 50)) / 20)
nota10 = int(((saque - (nota50 * 50)) - (nota20 * 20)) / 10)
nota1 = int((((saque - (nota50 * 50)) - (nota20 * 20)) - nota10 * 10) / 1)
if nota50 != 0:
    print(f'Total de {nota50} cédulas de R$50,00')
if nota20 != 0:
    print(f'Total de {nota20} cédulas de R$20,00')
if nota10 != 0:
    print(f'Total de {nota10} cédulas de R$10,00')
if nota1 != 0:
    print(f'Total de {nota1} cédulas de R$1,00')
