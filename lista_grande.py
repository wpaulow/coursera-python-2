import random

def lista_grande(n):
    aleatorios = list(range(1,n+1))
    random.shuffle(aleatorios)
    return aleatorios

def lista_grande_better(n):
    lista = [random.randrange(n+1) for x in range(n+1)]
    return lista
