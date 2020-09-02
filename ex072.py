numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um número entre 0 e 20: '))
    while num not in range(0, 21):
        num = int(input('ERRO! Digite um número entre 0 e 20: '))
        if 0 > num < 20:
            break
    print(f'Você digitou o número {numeros[num]}')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
