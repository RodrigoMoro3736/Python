dado = input('Digite algo: ')
tipo = type(dado)
print('vc digitou um dado tipo: \033[35m{}'.format(tipo))
if dado.isalpha():
    print('\033[36mAlpha')
if dado.isalnum():
    print('\033[36mAlphaNum')
if dado.isnumeric():
    print('\033[36mNumerico')
if dado.isprintable():
    print('\033[36mPrintavel')
if dado.isupper():
    print('\033[36mUpper')
if dado.islower():
    print('\033[36mMinusculo')