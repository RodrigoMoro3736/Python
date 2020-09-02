def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}  ')
    print('~' * (len(txt) + 4))
texto = str(input('Escreva uma mensagem: '))
escreva(texto)
