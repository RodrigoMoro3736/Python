pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items(): # faz a função do enumerate para dicionario
    print(f'{k} = {v}')

pessoas['nome'] = 'Leandro' # para alterar o valor da key 'nome' no caso

pessoas['peso'] = 98.5 # adiciona a key 'peso' no final do dicionario já com o valor 98.5
#----------------------------------------------------------------------------------------
print('==-' * 10)
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)

# ou

print('==-' * 10)
for testePrint in brasil:
    print(testePrint)

# ou melhor ainda (mais bonito)

print('==-' * 10)
for testePrint2 in brasil:
    for key, valor in testePrint2.items():
        print(f'O campo {key} tem o valor {valor}.')

# ou:
print('==-' * 10)
for testePrint3 in brasil:
    for valor2 in testePrint3.values():
        print(valor2, end=' ')
        print()
