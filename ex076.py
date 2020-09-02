lista = (('Lápis', 1.75), ('Boracha', 2), ('Caderno', 15.90), ('Estojo', 25), ('Transferidor', 4.20),
         ('Compasso', 9.99), ('Mochila', 120.32), ('Canetas', 22.30), ('Livro', 34.90))
print('~'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('~'*40)
for a, b in lista:
    print('{:.<30} R${:<.2f}'.format(a, b))
