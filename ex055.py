print('DIGITE O PESO DE 5 PESSOAS!')
menor = 9999
maior = 0
for c in range(1, 6):
    peso = float(input('Digite o peso em kilos: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'Maior peso: {maior:.2f}KG\nMenor peso: {menor:.2f}KG')
