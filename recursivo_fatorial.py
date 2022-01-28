def fatorial(n):
    if n <= 1:               ## base da recursao
        return 1
    else:                   ## chamada recursiva
        return n * fatorial(n-1)

##import pytest
##
##@pytest.mark.parametrize("entrada, esperado", [
##    (0, 1),
##    (1, 1),
##    (2, 2),
##    (3, 6),
##    (4, 24),
##    (5, 120)
##    ])
##
##def testa_fatorial(entrada, esperado):
##    assert fatorial(entrada) == esperado

    
