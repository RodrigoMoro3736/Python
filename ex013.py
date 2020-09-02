salario = float(input('Digite seu salário: R$'))
newSal = round((salario * 0.15) + salario, 2)
print('Seu salário R${} mais 15% fica: R${}'.format(salario, newSal))
