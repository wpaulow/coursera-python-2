def multiplica_matriz(A, B):
    num_lins_A, num_cols_A = len(A), len(A[0])
    num_lins_B, num_cols_B = len(B), len(B[0])
    assert num_cols_A == num_lins_B

    C = []
    for linha in range(num_lins_A):
        # Começando uma nova linha
        C.append([])
        for coluna in range(num_cols_B):
            # Adicionando uma nova coluna na linha
            C[linha].append(0)
            for k in range(num_cols_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]

    return C


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    print(multiplica_matriz(A, B))

