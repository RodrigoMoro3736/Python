from datetime import date

anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

print('A categoria de natação para {} anos é:'.format(idade))
if idade < 10:
    print('MIRIN')
elif idade < 15:
    print('INFANTIL')
elif idade < 20:
    print('JUNIOR')
elif idade < 25:
    print('SÊNIOR')
else:
    print('MASTER')
