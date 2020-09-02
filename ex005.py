num = int(input('Digite um numero: '))
suc = num + 1
ant = num - 1

print('O seu numero é: \033[30m{}\033[m\nseu sucessor é: \033[31m{}\033[m\nseu antecessor é: \033[32m{}\033[m'.format(num, suc, ant))
