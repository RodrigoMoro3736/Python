a = float(input('Digite o valor da reta 1 do triangulo: '))
b = float(input('Digite o valor da reta 2 do triangulo: '))
c = float(input('Digite o valor da reta 3 do triangulo: '))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo!')
