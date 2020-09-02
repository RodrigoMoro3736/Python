valores = [7, 2, 5, 0, 4]

# função para dobrar os valores:
def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1
    print(lista)

dobra(valores)
# Tudo que a função dobra fizer, vai interferir na lista valores definitivamente
print(valores)

print('*' * 30)
print('*' * 30)

# Somando valores:
def soma(* numeros):
    s = 0
    for num in numeros:
        s += num
    print(f'Somando os valores {numeros} temos {s}')

soma(5, 2)
soma(2, 9, 4)
