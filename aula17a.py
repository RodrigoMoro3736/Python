lanche = ['hamburguer', 'suco', 'pizza', 'sorvete']
lanche.append('cookie')
# insere o 'cookie' no final da lista

lanche.insert(0, 'cachorro quente')
# insere o 'cachorro quente' na posição 0 da lista

#para remover:
del lanche[3]
lanche.pop(3) # remove o ultimo elemente se não for indicado nada entre parenteses: lanche.pop()
lanche.remove('pizza') # remove pelo valor, e não pelo numero do indice (remove só o primeiro elemento achado
# na lista, caso haja mais de um

# dica para remover item, se existir na lista:
if 'pizza' in lanche:
    lanche.remove('pizza')

# dia para criar uma lista com numeros dados por um range
valores = list(range(4, 11))
# a lista vai conter 7 números (de 4 a 10) (4 no indice 0) (5 no indice 1) etc

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() # coloca em ordem os números
valores.sort(reverse=True) # coloca em ordem decrescente

# para mostrar os valores da lista de uma forma melhor visualmente:
for v in valores:
    print(f'{v} ', end=' ')

#para mostrar a posição (key ou chave) e o valor:
for c, v in enumerate(valores):
    print(f'posição: {c} temos o valor: {v}')

# para inserir valores na lista com input:
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

# para copiar uma lista em python temos 2 jeitos:
# uma copia e cria uma ligação, assim se vc alterar o valor de uma, altera das duas listas:
a = [1, 2, 3]
b = a # desse jeito cria-se uma ligação, e se b for alterado, a tbm será

b = a[:] # assim cria-se uma cópia, e se b for alterado, a não será
# ou assim:
b = a.copy()

