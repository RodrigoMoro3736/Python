from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
c = 0
menu = 0
azul = '\033[34m'
limpa = '\033[m'
while c == 0:
    menu = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior valor\n[4] Digitar novos números\n[5] Sair do programa\nSua escolha: '))
    if menu == 1:
        print(f'{azul}SOMA: {num1} + {num2} = {num1 + num2}{limpa}')
    if menu == 2:
        print(f'{azul}MULTIPLICAÇÃO: {num1} X {num2} = {num1 * num2}{limpa}')
    if menu == 3:
        if num1 == num2:
            print(f'{azul}Os números digitados são iguais!{limpa}')
        elif num1 > num2:
            print(f'{azul}Entre {num1} e {num2}, O número {num1} é maior!{limpa}')
        else:
            print(f'{azul}Entre {num1} e {num2}, O número {num2} é maior{limpa}')
    if menu == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    if menu == 5:
        c = 1
    if menu < 1 or menu > 5:
        print('Digite um número entre 1 e 5!')
    sleep(3)
    print('==-' * 10)
print('FIM')
