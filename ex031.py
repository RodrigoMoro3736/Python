distancia = float(input('Digite a distancia em KM da viagem: '))
passag1 = distancia * 0.5
passag2 = distancia * 0.45
if distancia <= 200:
    print('Sua passagem vai custar R${:.2f}'.format(passag1))
else:
    print('Sua passagem vai custar R${:.2f}'.format(passag2))
