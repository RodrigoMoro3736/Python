import math
num = int(input('Digite um número de 0 a 9999: '))
u = num % 10
d = math.floor((num % 100)/10)
c = math.floor((num % 1000)/100)
m = math.floor(num/1000)
print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}'.format(u, d, c, m))