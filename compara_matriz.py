def sao_multiplicaveis(matriz_a, matriz_b):
    """
    Para multiplicar duas matrizes o número de linhas de uma precisa ser igual
    ao número de colunas da outra.
    Uma matriz de duas linhas e três colunas multiplica uma matriz de três linhas
    e duas colunas.
    Logo, enquanto para somar duas matrizes basta que tenham dimensões idênticas,
    para multiplicá-las, é necessário que se inverta essa dimensão: as linhas de
    uma são as colunas da outra e as colunas de uma são as linhas da outra.
    """
    
    col1 = 0
    num_lin_b = len(matriz_b)
    num_col_a = len(matriz_a[0])
    
    for i in range(1, len(matriz_a)):
        x = len(matriz_a[i])
        if num_col_a != x:
            return False
            break
        
    col1 = num_col_a
    
    if col1 == num_lin_b:
        return True
    else:
        return False
    
            











            
