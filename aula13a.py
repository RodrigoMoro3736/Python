for c in range(0, 6):
    print('oi')
# escreve 'oi' 6 vezes (o python ignora o ultimo numero)

for c in range(6, 0, -1):
    print(c)
# o -1 é o passo (contagem regressiva)

for c in range(1, 10, 2):
    print(c)
# de 1 a 9 com passo 2 (até 9 pq o python ignora o ultimo numero)

comeco = int(input('Digite o começo: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
for c in range(comeco, fim + 1, passo):
    print(c)
# usuario decide as paradas ai (fim + 1 pq o python ignora o ultimo numero)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio de todos os valores foi {}'.format(s))
# soma os 4 valores digitados pelo usuario

