def insertion_sort(lista):
        
    for i in range(1, len(lista)):
        valor_atual = lista[i]
        posicao = i

        while posicao > 0 and valor_atual < lista[posicao-1]:
            lista[posicao] = lista[posicao-1]
            posicao -= 1

        lista[posicao] = valor_atual

    return lista

