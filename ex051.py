pritermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
ultimo = pritermo + (11 - 1) * razao
for c in range(pritermo, ultimo, razao):
    print(c, end=', ')
