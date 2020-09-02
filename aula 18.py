teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)

#--------------

galera = [['João', 19], ['Ana', 33], ['joaquim', 13], ['Maria', 45]]
print(galera[2][1]) # vai imprimir: 13

# para imprimir de uma forma melhor:
for p in galera:
    print(p)
# ['João', 19]
# ['Ana', 33]
# ['joaquim', 13]
# ['Maria', 45]

# print(p[0]) imprime somente os nomes e [1] as idades

# ou melhor ainda:

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
# joão tem 19 anos de idade # etc

galera3 = []
dado = []
totalMaior = totalMenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear() # deleta tudo na lista
for p in galera3:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totalMaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalMenor += 1
print(f'Temos {totalMaior} maiores de ideda, e {totalMenor} menores')

