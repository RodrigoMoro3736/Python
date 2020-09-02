lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# Varial composta tupla
# Tuplas são imutáveis

for cont in range(0, len(lanche)):
    print(lanche[cont], ' posição ', cont)

for comida in lanche:
    print(comida)

for pos, comida in enumerate(lanche):
    print(comida, ' posição ', pos)

print(sorted(lanche))
# sorted ordena a tupla em ordem alfabetica

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
# resultado: (2, 5, 4, 5, 8, 1, 2)

print(c.count(2))
# resultado: 2
# conta quantas vezes o numero 2 aparece em c

print(c.index(4))
# mostra a posição do numero 4 (somente o primeiro numero 4 caso haja mais numeros 4)

print(c.index(5, 1))
# mostra a posição do num 5, começando a contar pela posição 1

pessoa = ('Rodrigo', 29, 'M', 70)
# tuplas podem conter numeros e texto

del(pessoa)
# apaga a tupla inteira (não pode ser apagado um item somente) (somente a tupla inteira pode ser apagada)
