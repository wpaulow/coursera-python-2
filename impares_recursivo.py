def encontra_impares(lista):

    # Define a lista que armazenará os números ímpares:
    lis = []

    # Verifica se há elementos na lista:
    ##    if len(lista) > 0:
    if lista:

        # Retira o primeiro elemento da lista:
        numero = lista.pop(0)

        # Verifica se o número é ímpar:
        if numero % 2 != 0:

            # Sim, então adiciona-o à lista de ímpares:
            lis.append(numero)

        # Faz a união do resultado atual com o retorno para o resto da lista:
        lis.extend(encontra_impares(lista))

    # Retorna a lista final:
    return lis
