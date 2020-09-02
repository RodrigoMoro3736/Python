import time
anoAtual = time.localtime().tm_year
maior = 0
menor = 0
anoNascimento = 0

for c in range(1, 8):
    anoNascimento = int(input('Digite o ano de nascimento: '))
    if (anoAtual - anoNascimento) >= 21:
        maior += 1
    elif (anoAtual - anoNascimento) < 21:
        menor += 1

print(f'{menor} pessoas são menores de 21 anos!\n{maior} pessoas são maiores de 21 anos!')
