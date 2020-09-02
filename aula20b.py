# Desenpacotamento de parametros:

def contador(* num):
    # o * sinaliza um desenpacotamento de parametros
    print(num)

contador(2, 1, 4, 6)
contador(4, 9)
contador(5, 6, 2, 7, 0, 9, 6, 7)

print('*' * 30)
print('*' * 30)
# ---------------------------
# outro jeito de imprimir, com for

def contador2(* num2):
    for valor in num2:
        print(f'{valor} ', end='')
    print('Fim')

contador2(2, 1, 4, 6)
contador2(4, 9)
contador2(5, 6, 2, 7, 0, 9, 6, 7)

print('*' * 30)
print('*' * 30)
#---------------------------
# usando len:

def contador3(* num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números!')

contador3(2, 1, 4, 6)
contador3(4, 9)
contador3(5, 6, 2, 7, 0, 9, 6, 7)
