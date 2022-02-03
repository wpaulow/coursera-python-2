def incomodam(n: int) -> str:
    inco = "incomodam "
    
    if n <= 0:
        return ""
    
    if n == 1:
        return inco
    else:
        return inco + incomodam(n-1)

        
def elefantes(n: int) -> str:
    um = "Um elefante incomoda muita gente\n"
    eles = " elefantes "
    m_mais = "muito mais\n"
    texto = ""

    if n <= 0:
        return ""

    if n == 1:
        return um + texto
    
    if n == 2:
        texto += str(n) + eles + incomodam(n) + m_mais
        return um + texto
    else:
        incomodo = str(n-1) + " elefantes incomodam muita gente\n"
        texto += incomodo + str(n) + eles + incomodam(n) + m_mais
        return elefantes(n-1) + texto
    
