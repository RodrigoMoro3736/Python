def area(a, b):
    tot = a * b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {tot:.1f}m2')
print('  Controle de terrenos')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
