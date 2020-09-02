import math
catOpo = float(input('Digite o cateto oposto do triangulo: '))
catAdj = float(input('Digite o cateto adjacente do triangulo: '))
hipoten = math.hypot(catOpo, catAdj)
print('A hipotenusa desse triangulo é: {:.2f}'.format(hipoten))
