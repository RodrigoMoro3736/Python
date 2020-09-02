num = str(input('Digite 3 números: ')).strip()
if len(num) != 3:
    print('ERRO! POR FAVOR DIGITE 3 NÚMEROS!')
else:
    if num[0] >= num[1] and num[0] >= num[2]:
        print('O maior número é o {}'.format(num[0]))
    elif num[1] >= num[0] and num[1] >= num[2]:
        print('O maior número é o {}'.format(num[1]))
    else:
        print('O maior número é o {}'.format(num[2]))

    if num[0] <= num[1] and num[0] <= num[2]:
        print('O menor número é o {}'.format(num[0]))
    elif num[1] <= num[0] and num[1] <= num[2]:
        print('O menor número é o {}'.format(num[1]))
    else:
        print('O menor número é o {}'.format(num[2]))
