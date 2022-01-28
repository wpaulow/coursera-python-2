def maiusculas(frase):
    char_up = ""
    for i in frase:
        for j in range(65, 91):
            if i == chr(j):
                char_up += i

    return char_up
