dicMaster = {}
dicMaster['nome'] = str(input('Nome: ')).title()
dicMaster['media'] = float(input(f'Média de {dicMaster["nome"]}: '))
if dicMaster['media'] >= 7.0:
    dicMaster['situacao'] = 'Aprovado'
elif 5 <= dicMaster['media'] < 7:
    dicMaster['situacao'] = 'Recuperação'
else:
    dicMaster['situacao'] = 'Reprovado'
for k, v in dicMaster.items():
        print(f'{k} é igual a {v}')
