# Selection Sort

def ordena(lista):

    for i in range(len(lista)-1):
        posicao_menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[posicao_menor]:
                posicao_menor = j
        lista[i], lista[posicao_menor] = lista[posicao_menor], lista[i]
        
    return lista
