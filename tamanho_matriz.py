def dimensoes(matriz):
    lins = len(matriz)
    cols = 0
    for i in matriz[0]:
        cols += 1

    print(str(lins)+"X"+str(cols))
