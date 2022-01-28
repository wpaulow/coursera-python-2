def conta_letras(frase, contar="vogais"):
    frase.lower()
    nLetras = 0
    vogais = ["a", "e", "i", "o", "u"]
    consoantes = ["b", "c", "d", "f",
                  "g", "h", "j", "k",
                  "l", "m", "n", "p",
                  "q", "r", "s", "t",
                  "v", "x", "w", "y", "z"]
    if contar == "vogais":
        for j in vogais:
            nLetras += frase.count(j)
        
    if contar == "consoantes":
        for j in consoantes:
            nLetras += frase.count(j)

    return nLetras
