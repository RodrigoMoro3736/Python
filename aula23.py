# try: (operação)
# except: (se falhou)(`Exception as erro` faz mostrar o erro)
# else: (se deu certo - opcional)
# finally: (se deu certo, ou se falhou, vai executar independentemente - opcional)
# ex:

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Erro encontrado: {erro.__class__}')
except (ValueError, TypeError):
    print('Problema com o tipo de dado digitado')
except ZeroDivisionError:
    print('Não é possivel dividir por zero')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!')
