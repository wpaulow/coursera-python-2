def encontra_impares(lista):
    odds = []

    if lista:
        n = lista.pop(0)

        if n % 2 != 0:
            odds.append(n)

        odds.extend(encontra_impares(lista))

    return odds

