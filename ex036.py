valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
prazo = int(input('Em quantos anos você quer pagar? : '))

prestacao = valorCasa / (prazo * 12)

if prestacao >= salario * 0.3:
    print('Seu emprestimo não foi aprovado!\nA prestação mensal é maior ou igual a 30% do seu salário.')
else:
    print('Seu emprestimo foi aprovado!\nA prestação mensal vai ficar em R${:.2f}'.format(prestacao))
