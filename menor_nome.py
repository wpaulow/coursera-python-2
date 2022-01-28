def menor_nome(nomes):
    menor = nomes[0].strip()
    for i in range(1, len(nomes)):
        nome = nomes[i].strip()
        if len(nome) < len(menor):
            menor = nome

    return menor.capitalize()

