#import pytest

def soma_lista(lista):

    if len(lista) == 0:
        return 0
    
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])


##a = [10, 20, 30, 40, 50, 60]    # 210
##b = [1, 2, 3, 4, 5, 6]          # 21
##c = [0, 0, 0, 0, 0, 1]          # 1
##d = [1, 1, 1, 1, 1, 1]          # 6
##e = [-1, 1, 1, 1, 1, 1]         # 4
##f = []
##
##@pytest.mark.parametrize("lista, esperado", [
##    (a, 210),
##    (b, 21),
##    (c, 1),
##    (d, 6),
##    (e, 4),
##    (f, 0)
##    ])
##
##def testa_soma_lista(lista, esperado):
##    assert soma_lista(lista) == esperado
##


