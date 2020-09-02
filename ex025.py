nome = input('Digite seu nome completo: ').lower().strip()
fnd = nome.find('silva')
if not fnd == -1:
    print('Seu nome contem ´Silva´')
else:
    print('Seu nome não contem ´Silva´')
