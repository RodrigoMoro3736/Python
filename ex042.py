a = float(input('Digite o valor da reta 1 do triangulo: '))
b = float(input('Digite o valor da reta 2 do triangulo: '))
c = float(input('Digite o valor da reta 3 do triangulo: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Essas retas podem formar um triangulo!')

    if a == b == c:
        print('Seu triangulo é equilátero!')
    elif a == b or b == c or a == c:
        print('Seu triangulo é isóceles!')
    else:
        print('Seu triangulo é escaleno!')

else:
    print('Essas retas não podem formar um triangulo!')
