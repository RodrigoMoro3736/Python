def mostraLinha():
    print('==-' * 10)
mostraLinha()

def mensagem(msg):
    print('-=-' * 10)
    print(msg)
    print('-=-' * 10)

mensagem('Teste 1 com parametro')

# a = 4
# b = 5
# s = a + b
# print(s)

# a = 8
# b = 9
# s = a + b
# print(s)

# a = 2
# b = 1
# s = a + b
# print(s)

def soma(a, b):
    s = a + b
    print(s)
soma(4, 5)
soma(8, 9)
soma(2, 1)
# funcão soma substituindo todas as linhas acima
# função melhorada:

def soma2(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
soma2(4, 9)
# Pode ser: soma2(a=4, b=5) para especificar o parametro
# ou: soma2(b=5, a=4)
