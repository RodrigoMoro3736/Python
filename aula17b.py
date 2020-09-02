dados = ['Pedro', 25]
# uma lista normal

pessoas = []
pessoas.append(dados[:])
# criou uma copia (copia por causa do [:]) de dados dentro de pessoas
# ['Pedro', 25] está no indice 0 de pessoas

# outro exemplo:
pessoas2 = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas2[0][0])
# imprime: 'Pedro'

print(pessoas2[1])
# imprime: ['Maria', 19]

