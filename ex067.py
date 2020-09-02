cont = tab = 1
while tab > 0:
    tab = int(input('Quer ver a taboada de qual valor? '))
    while tab > 0:
        if cont <= 10:
            print(f'{tab} X {cont} = {tab * cont}')
            cont += 1
        else:
            break
    print('==-' * 10)
    cont = 1
print('FIM')
