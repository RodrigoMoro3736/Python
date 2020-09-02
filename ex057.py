c = 0
while c == 0:
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        print('Você é do sexo masculino!')
        c += 1
    elif sexo == 'F':
        print('Você é do sexo feminino!')
        c += 1
    else:
        print('ERRO! Digite novamente!')
