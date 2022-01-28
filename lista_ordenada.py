def esta_ordenada(lista):

    for i in range(len(lista)-1):
        posicao_menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[posicao_menor]:
                return False
    return True


def esta_ordenada_better(lista):

    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True
