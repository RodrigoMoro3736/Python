import math
ang = int(input('Digite um angulo: '))
angulo = math.radians(ang)
cos = math.cos(angulo)
seno = math.sin(angulo)
tan = math.tan(angulo)
print('Cosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}'.format(cos, seno, tan))
