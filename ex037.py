num = int(input('Digite um numero: '))
conversao = int(input('Deseja converter esse numero para:\n1 - Binario\n2 - Octal\n3 - Hexadecimal\nDigite o numero desejado: '))

if conversao < 1 or conversao > 3:
    print('ERRO! Você não digitou o numero 1 ou 2 ou 3!')
elif conversao == 1:
    print('O numero {} em binario: {}'.format(num, bin(num)[2:]))
elif conversao == 2:
    print('O numero {} em octal: {}'.format(num, oct(num)[2:]))
else:
    print('O numero {} em hexadecimal: {}'.format(num, hex(num)[2:]))
