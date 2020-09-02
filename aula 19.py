# dicionarios pode ser declarados com chaves {}
# ex: teste = {}
# dicionarios tem indices personalizados
# ex: teste = {'nome':'Pedro'}
# 'nome' é o indice
# 'Pedro' é o valor no indice 'nome'
# print(dados['nome'] imprime 'Pedro'

# append não funciona
# para adicionar um elemento:
# dados['sexo'] = 'M'

# para remover um elemento:
# del dados['idade']
# deleta o indice e o valor no indice

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
}
print(filme.values()) # imprime os valores
print(filme.keys()) # imprime os indices, chaves (keys)
print(filme.items()) # imprime os dois (indice e valor)

for keys, values in filme.items():
    print(f'O {keys} é {values}')
# imprime:
# O titulo é Star Wars
# O ano é 1977
# O diretor é George Lucas

filme2 = {'titulo':'Avengers',
          'ano':2012,
          'diretor':'Joss Whedon'
}
filme3 = {'titulo':'Matrix',
          'ano':1999,
          'diretor':'Wachowski'
}
locadora = []
locadora.append(filme.copy())
locadora.append(filme2.copy())
locadora.append(filme3.copy())
print('==-' * 10)
print(locadora)
print('==-' * 10)
for teste01 in locadora:
    print(teste01)
