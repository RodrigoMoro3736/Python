cidade = str(input('Digite o nome da sua cidade: ')).strip()
sprd = cidade.split()
minus = sprd[0].lower()
if minus == 'santo':
    print('Sua cidade começa com a palavra ´Santo´!!!')
else:
    print('Sua cidade não começa com a palavra ´Santo´!!')
