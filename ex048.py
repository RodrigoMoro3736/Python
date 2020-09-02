r = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        r += c
print('A soma de todos números ímpares que são\nmultiplos de 3 no intervalo de 1 a 500 é: {}'.format(r))
