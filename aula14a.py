c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
# jeito normal, sabendo o final (9)

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
# Lê os valores até o número 0 ser digitado

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM')
# Contiua a ler o valor para n até o usuário digitar N

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares, e {impar} números ímpares')
# conta qts números pares e ímpares o usuario digitou até digitar 0 e sair

