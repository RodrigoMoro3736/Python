maior18 = homens = mulherMenor20 = fim = 0
while fim == 0:
    print('CADASTRE UMA PESSOA!')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 17:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulherMenor20 += 1
    continuar = str(input('QUER CONTINUAR? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        fim += 1
print(f'{maior18} pessoa(s) cadastrada(s) maior(es) de 18 anos')
print(f'{homens} homen(s) cadastrado(s)')
print(f'{mulherMenor20} mulher(es) cadastrada(s) menor(es) de 20 anos')
