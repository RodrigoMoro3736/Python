times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
        'Atlético', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
        'Bahia', 'Corinthians', 'Fluminense', 'Vasco', 'Ceará-SC',
        'Chapecoense', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
print(f'20 times na ordem de colocação:\n{times}')
print(f'5 primeiros: {times[:5]}')
print(f'Ultimos 4: {times[-4:]}')
print(f'Ordem alfabetica: {sorted(times)}')
print(f'O chapecoense está na {times.index("Chapecoense") + 1}ª posição')
