# escrever `help()` com qqr parametro ou função do python, retorna sua descrição completa
# ex: help(print)

def teste01():
    """
    3 aspas duplas no começo da função serve para documenta-la
    Isso é chamado docstring
    :return:
    """
#-------------------------

def somar(a=0, b=0, c=0): # declarar o valor ( 0 no caso) faz com que o usuario não precise necessariamente
                          # passar 3 valores pra função. Fica como um valor opcional
    s = a + b + c
    return s

# o `retunr s`  joga o valor de `s` dentro das variaveis r1 r2 e r3
# pode ser jogado num print direto tbm
# ex: print(somar(9, 8, 7))

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}!')
