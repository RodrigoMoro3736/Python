import os
try:
    ping = os.system('ping -n 1 pudim.com.br > NUL')
    if ping == 0:
        print('\033[33mO site Pudim está online!\033[m')
    else:
        print('\033[31mO site Pudim está offline!\033[m')
except Exception as erro:
    print(f'ERRO! {erro}')
