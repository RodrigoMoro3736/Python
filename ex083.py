exp = [input('Digite sua expressão: ')]
for c in exp:
    a = c.count('(')
    b = c.count(')')
    if a == b:
        print('Sua expressão está CORRETA!')
    else:
        print('Sua expressão está ERRADA!')
