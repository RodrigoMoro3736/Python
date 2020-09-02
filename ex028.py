import random
aleatorio = random.randint(0, 5)
print('Olá, eu sou o ´cérebro´ do seu computador!\nEsse jogo funciona assim:\nEu vou pensar em um número aleatório inteiro entre 0 e 5 !')
print('E voce vai tentar descobrir!\nVamos lá!')
num = int(input('Tente adivinhar o numero que estou pensando: '))
if num < 0 or num > 5:
    print('Você não digitou um número entre 0 e 5 !')
elif num == aleatorio:
    print('VOCÊ ACERTOU!')
else:
    print('Você errou! O número que eu pensei foi: {} ! Tente outra vez!'.format(aleatorio))
