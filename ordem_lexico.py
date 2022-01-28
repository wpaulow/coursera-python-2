def primeiro_lex(lista):
    maior = lista[0]
    for i in range(1, len(lista)):
        palavra = lista[i]
        if maior > palavra.lower():
            maior = palavra

    return maior
        
