from time import sleep
def maior(* num):
    print('=~' * 20)
    print('Analisando os valores passados...')
    for c in num:
        print(c, end=', ')
        sleep(0.3)
    if len(num) > 0:
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print('Nenhum valor foi informado!')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
