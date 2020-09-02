nome = input('Digite seu nome completo: ').title().strip()
separado = nome.split()
ultimoNome = separado[len(separado) - 1]
print('Seu primeiro nome é: {}'.format(separado[0]))
print('Seu ultimo nome é: {}'.format(ultimoNome))
