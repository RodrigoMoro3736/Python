matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
pares = 0
for c in range(0, 3):
    matriz[c][0] = int(input(f'Digite um valor para [{c}, 0]: '))
    matriz[c][1] = int(input(f'Digite um valor para [{c}, 1]: '))
    matriz[c][2] = int(input(f'Digite um valor para [{c}, 2]: '))
print('==-' * 10)
for p in matriz:
    print(p)
print('==-' * 10)
for par in matriz:
    for y in par:
        if y % 2 == 0:
            pares += y
somaTerCol = (matriz[0][2]) + (matriz[1][2]) + (matriz[2][2])
maiorSegLin = max(matriz[1])
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {somaTerCol}.')
print(f'O maior valor da segunda linha é {maiorSegLin}.')
