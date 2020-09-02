cores = {'limpa': '\033[m',
         'fundoAzul': '\033[1;44;30m',
         'fundoRoxo': '\033[1;45;30m',
         'fundoPiscina': '\033[1;46;30m',
         'fundoCinza': '\033[1;47;30m', }

num = int(input('Digite um numero: '))
raiz = round(num ** (1/2), 2)
print('Seu número é: {}{}{}\nO dobro é: {}{}{}\nSeu triplo é: {}{}{}\nA raiz quadrada é: {}{}{}'.format(cores['fundoPiscina'], num, cores['limpa'], cores['fundoCinza'], num * 2, cores['limpa'], cores['fundoAzul'], num * 3, cores['limpa'], cores['fundoRoxo'], raiz, cores['limpa']))
