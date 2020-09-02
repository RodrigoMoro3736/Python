alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = alt * lar
tinta = float(area / 2)
print('A área da parede é {}m2\nVocê precisará de {} galões de tinta para pinta-la!'.format(area, tinta))
