def leiaInt(num):
    while True:
        x = input(num).strip()
        if x == '':
            print('\033[31mUsuário preferiu não digitar um número.\033[m')
            return 0
            break
        else:
            try:
                int(x)
                return x
                break
            except:
                print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
def leiaFloat(num):
    while True:
        x = input(num).replace(',', '.').strip()
        if x == '':
            print('\033[31mUsuário preferiu não digitar um número.\033[m')
            return 0
            break
        else:
            try:
                float(x)
                return x.replace('.', ',')
                break
            except:
                print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
i = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')
print(f'Valor inteiro digitado foi {i} e o real foi {f}')
