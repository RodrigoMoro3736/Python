frase = str(input('Digite uma frase para ver se ela é um PALÍNDROMO! : ')).strip().lower().replace(' ', '')
invertido = frase[::-1]

if frase == invertido:
    print('A sua frase é SIM um PALÍNDROMO!')
else:
    print('A sua frase NÃO é um PALÍNDROMO!')
