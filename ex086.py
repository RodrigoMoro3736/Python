matriz = [['', '', ''],
          ['', '', ''],
          ['', '', '']]
for c in range(0, 3):
    matriz[c][0] = input(f'Digite um valor para [{c}, 0]: ')
    matriz[c][1] = input(f'Digite um valor para [{c}, 1]: ')
    matriz[c][2] = input(f'Digite um valor para [{c}, 2]: ')
print('==-' * 10)
for p in matriz:
    print(p)
