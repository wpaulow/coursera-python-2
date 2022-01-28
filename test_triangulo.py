import Triangulo
import pytest

class TestTriangulo:

    @pytest.fixture
    def tri(self):
        return Triangulo.Triangulo()

    @pytest.mark.parametrize("a, b, c, esperado", [
        (1, 1, 1, "equilátero"),
        (1, 2, 2, "isósceles"),
        (2, 1, 2, "isósceles"),
        (2, 2, 1, "isósceles"),
        (1, 2, 3, "escaleno"),
        (3, 2, 1, "escaleno"),
        (1, 5, 7, "escaleno")
        ])

    def testa_tipo(self, tri, a, b, c, esperado):
        assert tri.tipo_lado(a, b, c) == esperado


    @pytest.mark.parametrize("a, b, c, esperado", [
        (1, 1, 1, False),
        (1, 2, 3, False),
        (2, 1, 2, False),
        (3, 2, 1, False),
        (3, 4, 5, True),
        (5, 12, 13, True),
        (7, 24, 25, True),
        (17, 15, 8, True)
        ])

    def testa_retangulo(self, tri, a, b, c, esperado):
        assert tri.retangulo(self, a, b, c) == esperado
