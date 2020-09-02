print('Agora você vai digitar quantos números inteiros quiser!\nQuando quiser sair e somar todos esses números, digite 999')
num = []
contador = 1
while contador > 0:
    n = (int(input('Digite um número inteiro: ')))
    if n != 999:
        num.append(n)
        contador += 1
    else:
        break
print('==-' * 10)
print(f'Você digitou {contador - 1} números!')
print(f'A soma desses números é: {sum(num)}')
