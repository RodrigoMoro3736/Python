from random import randint
from time import sleep
numeros = []
def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        sleep(0.4)
        numeros.append(randint(1, 10))
        print(numeros[c], end=' ')
    print('Pronto!!')
def somaPar():
    pares = 0
    for s in numeros:
        if s % 2 == 0:
            pares += s
    print(f'Somando os valores pares de {numeros}', end=' ')
    print(f'temos {pares}!!')
sorteia()
somaPar()
