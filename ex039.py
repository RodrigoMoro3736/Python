from datetime import date
anoNascimento = int(input('Digite o seu ano de nascimento: '))

anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade == 18:
    print('Está na hora de se alistar! Você tem 18 anos!')
elif idade < 18:
    print('Você ainda vai se alistar! faltam {} anos'.format(18 - idade))
else:
    print('Já passou da hora de se alistar! Passaram {} anos!'.format(idade - 18))
