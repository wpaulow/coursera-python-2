def dimensoes(matriz):
    lins = len(matriz)
    cols = 0
    for i in matriz[0]:
        cols += 1

    return [lins, cols]


def soma_matrizes(m1, m2):
    dim_m1 = dimensoes(m1)
    dim_m2 = dimensoes(m2)
    m3 = []
    if dim_m1 != dim_m2:
        return False
    else:
        for i in range(dim_m1[0]):
            linha_m1 = m1[i]
            linha_m2 = m2[i]
            linha_m3 = []
            for j in range(len(linha_m1)):
                linha_m3.append(linha_m1[j] + linha_m2[j])
            m3.append(linha_m3)
        return m3
