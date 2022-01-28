class Triangulo:

    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return "equilátero"
        elif ((self.a == self.b and self.b != self.c) or
              (self.a == self.c and self.a != self.b) or
              (self.b == self.c and self.a != self.c)):
            return "isósceles"
        else:
            return "escaleno"

    def retangulo(self):
        lados = [self.a, self.b, self.c]
        lados.sort()
        if lados[2]**2 == lados[0]**2 + lados[1]**2:
            return True
        else:
            return False

    def semelhantes(self, x):
        lados_t1 = [self.a, self.b, self.c]
        lados_t1.sort()
        lados_t2 = [x.a, x.b, x.c]
        lados_t2.sort()
        a, b = lados_t1, lados_t2
        if a[0] / b[0] == a[1] / b[1] == a[2] / b[2]:
            return True
        else:
            return False

        
        
