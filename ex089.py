listaMaster = []
while True:
    nome = str(input('Nome: ')).title().strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    listaMaster.append([nome, [nota1, nota2], media])
    condicao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if condicao == 'N':
        break
print('==-' * 10)
print('Nº  NOME         MÉDIA')
for i, l in enumerate(listaMaster):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8.1f}')
while True:
    condicao2 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if condicao2 == 999:
        break
    if condicao2 <= len(listaMaster) - 1:
        print(f'Notas de {listaMaster[condicao2][0]} são {listaMaster[condicao2][1]}')
