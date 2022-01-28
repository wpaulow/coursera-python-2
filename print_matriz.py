def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)

        matriz.append(linha)

    return matriz


def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return lin, col


def imprime_matriz(matriz):
    for i in range(len(matriz)):
        x = matriz[i]
        for j in range(len(x)-1):
            print(x[j], end=" ")
        print(x[-1])

##def main():
##    lin, col = le_matriz()
##    mat = cria_matriz(lin, col)
##    imprime_matriz(mat)
##
##
##main()
