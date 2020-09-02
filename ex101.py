def voto(num = 1):
    import datetime
    anoAtual = datetime.date.today().year
    idade = anoAtual - num
    if num == 1:
        return print('ERRO! Tente novamente!')
    else:
        if idade < 16:
            return print(f'Você tem {idade} anos, e ainda não pode votar!')
        elif idade < 18 or idade > 64:
            return print(f'Você tem {idade} anos, e seu voto é opcional!')
        else:
            return print(f'Você tem {idade} anos, e seu voto é obrigatório!')
voto(int(input('Digite o seu ano de nascimento: ')))
