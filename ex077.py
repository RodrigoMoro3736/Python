palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
vogais = "aeiouAEIOU"
somenteVogais = ""
print('CONTADOR DE VOGAIS')
for c in range(0, len(palavras)):
    for i in palavras[c]:
        if i in vogais:
            somenteVogais += i
    print(f'Na palavra "{palavras[c]}" temos "{somenteVogais}"')
    somenteVogais = ""
