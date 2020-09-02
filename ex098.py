from time import sleep
def linha():
    print('=*=' * 20)
def contador(inicio, fim, passo):
    if fim > inicio and passo > 0:
        for c in range(inicio, fim + 1, passo):
            print(f'{c} ', end='')
            sleep(0.2)
        print('Fim')
    if inicio > fim and passo > 0:
        for c in range(inicio, fim - 1, -passo):
            print(f'{c} ', end='')
            sleep(0.2)
        print('Fim')
    if inicio > fim and passo < 0:
        for c in range(inicio, fim - 1, passo):
            print(f'{c} ', end='')
            sleep(0.2)
        print('Fim')
    if inicio < fim and passo == 0:
        print('ERRO! O passo não pode ser 0. Assumindo passo 1 automaticamente.')
        for c in range(inicio, fim - 1, 1):
            print(f'{c} ', end='')
            sleep(0.2)
        print('Fim')
    if inicio > fim and passo == 0:
        print('ERRO! O passo não pode ser 0. Assumindo passo 1 automaticamente.')
        for c in range(inicio, fim - 1, -1):
            print(f'{c} ', end='')
            sleep(0.2)
        print('Fim')
linha()
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
linha()
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
inicioPers = int(input('Início: '))
fimPers = int(input('Fim: '))
passoPers = int(input('Passo: '))
linha()
print(f'Contagem de {inicioPers} até {fimPers} de {passoPers} em {passoPers}')
contador(inicioPers, fimPers, passoPers)
linha()
