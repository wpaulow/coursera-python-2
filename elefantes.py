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
        return texto
    
    if n == 1:
        return um + texto
    else:
        texto += str(n) + eles + incomodam(n) + m_mais
        incomodo = str(n) + " elefantes incomodam muita gente\n"
        return elefantes(n-1) + texto + incomodo
    
