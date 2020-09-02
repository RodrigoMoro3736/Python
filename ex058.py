import random
print('Olá, eu sou o ´cérebro´ do seu computador!\nEsse jogo funciona assim:\nEu vou pensar em um número aleatório inteiro entre 0 e 10 !')
print('E voce vai tentar descobrir!\nVamos lá!')
num = 11
aleatorio = random.randint(0, 10)
contador = 1
while num != aleatorio:
    num = int(input('Tente adivinhar o numero que estou pensando: '))
    if num < 0 or num > 10:
        print('ERRO! Digite um número entre 0 e 10!')
        contador += 1
    elif num != aleatorio:
        if aleatorio > num:
            print('Mais... Tente novamente!')
        else:
            print('Menos... Tente novamente!')
        contador += 1
    else:
        print('==-' * 20)
        print(f'Você acertou! Eu estava pensando no número {aleatorio} !!!\nVocê precisou de {contador} tentativas!')
