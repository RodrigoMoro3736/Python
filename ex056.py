idade = 0
homemMaisVelho = ''
homemMaisVelhoIdade = 0
mulheresMenor20 = 0

for c in range(1, 5):
    nome2 = str(input('Digite o nome: ')).title()
    idade2 = int(input('Digite a idade: '))
    sexo2 = str(input('Digite o sexo: ')).strip().lower()
    print('*=' * 10)
    if idade2 > 0:
        idade += idade2
    if sexo2 == 'feminino' or sexo2 == 'fem' or sexo2 == 'f' and idade2 < 20:
        mulheresMenor20 += 1
    if sexo2 == 'masculino' or sexo2 == 'masc' or sexo2 == 'm' and idade2 > homemMaisVelhoIdade:
        homemMaisVelho = nome2
        homemMaisVelhoIdade = idade2

print(f'A média de idade dessas 4 pessoas é {idade / 4} anos!')
if homemMaisVelho != '':
    print(f'O homem mais velho é o {homemMaisVelho} com {homemMaisVelhoIdade} anos!')
else:
    print('As 4 pessoas são mulheres!')
print(f'Tem {mulheresMenor20} mulher(es) menor(es) de 20 anos!')
