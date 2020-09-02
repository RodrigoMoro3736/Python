def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.
    :param num: número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número num
    """
    if show == False:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        f = 1
        for c in range(num, 0, -1):
            f *= c
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        return f
n = int(input('Digite um número: '))
condicao = str(input('Deseja mostrar o processo? [S/N] ')).upper().strip()[0]
if condicao == 'S':
    condicao = True
    print(fatorial(n, condicao))
else:
    condicao = False
    print(f'O fatorial de {n} é: {fatorial(n)}')
