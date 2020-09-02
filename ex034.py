salario = float(input('Digite o salário: '))
if salario > 1250:
    print('O salário R${:.2f} + 10% é igual a R${:.2f}'.format(salario, (salario * 0.10) + salario))
else:
    print('O salário R${:.2f} + 15% é igual a R${:.2f}'.format(salario, (salario * 0.15) + salario))
