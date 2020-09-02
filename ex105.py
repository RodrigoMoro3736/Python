def notas(* n, sit=False):
    """
    => Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (acita várias)
    :param sit: (opcional) Mostra a situação do aluno
    :return: Dicionário com várias informações sobre a situação da turma
    """
    dicMaster = {}
    s = ''
    dicMaster["total"] = len(n)
    dicMaster["maior"] = max(n)
    dicMaster["menor"] = min(n)
    dicMaster["media"] = sum(n) / len(n)
    if sit == True:
        if dicMaster["media"] < 6:
            s = 'RUIM'
        elif dicMaster["media"] < 7:
            s = 'RAZOAVEL'
        else:
            s = 'BOA'
        dicMaster["situacao"] = s
    return dicMaster
resp = notas(3.5, 2, 10, 6.5, sit=True)
print(resp)
help(notas)
