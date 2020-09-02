total = maisDeMil = maisBarato = 0
maisbaratoNome = ''
while True:
    produto = str(input('Nome do produto: ')).title()
    preco = float(input('Preço: R$'))
    total += preco
    if preco >= 1000:
        maisDeMil += 1
    if maisBarato == 0:
        maisBarato = preco
        maisbaratoNome = produto
    elif preco < maisBarato:
        maisBarato = preco
        maisbaratoNome = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('==-'*10)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisDeMil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi: {maisbaratoNome} que custa R${maisBarato:.2f}')
