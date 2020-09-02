velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Você está dentro do limite de velocidade!')
else:
    print('Você ultrapassou o limite de velocidade!\nSeu carro estava a {:.2f}KM/h\nAmulta é de R$7,00 por cada KM acima do limite de 80KM/h'.format(velocidade))
    print('Sua multa vai ficar em R${:.2f}'.format(multa))
