class Triangulo:

    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return "equilátero"
        elif ((self.a == self.b and self.b != self.c) or
            (self.a == self.c and self.a != self.b) or
            (self.b == self.c and self.a != self.c)):
            return "isósceles"
        else:
            return "escaleno"



    
