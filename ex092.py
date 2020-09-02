import datetime
dataAtual = datetime.date.today().year
dicMaster = {}
dicMaster['nome'] = str(input('Nome: ')).title()
anoNasc = int(input('Ano de Nascimento: '))
dicMaster['idade'] = dataAtual - anoNasc
dicMaster['ctps'] = int(input('Carteira de trabalho (0 = não tem): '))
if dicMaster['ctps'] != 0:
    dicMaster['contratacao'] = int(input('Ano de Contratação: '))
    dicMaster['salario'] = float(input('Salário: R$'))
    calcAposen = (dicMaster['contratacao'] - anoNasc) + 35
    dicMaster['aposentadoria'] = calcAposen
print('==-' * 10)
for k, v in dicMaster.items():
    print(f'{k} tem o valor {v}')
