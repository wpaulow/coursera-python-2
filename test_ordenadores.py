import ordenadores
import compara_sorts
import pytest

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenadores.Ordenador()


    @pytest.fixture
    def l_quase(self):
        c = compara_sorts.ContaTempos()
        return c.lista_quase_ordenada(100)


    @pytest.fixture
    def l_aleat(self):
        c = compara_sorts.ContaTempos()
        return c.lista_aleatoria(100)

    
    def esta_ordenada(self, lista):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                return False
        return True


    def test_bubble_aleat(self, o, l_aleat):
        o.bubble_sort(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_selection_aleat(self, o, l_aleat):
        o.selection_sort(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_bubble_quase(self, o, l_quase):
        o.bubble_sort(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selection_quase(self, o, l_quase):
        o.selection_sort(l_quase)
        assert self.esta_ordenada(l_quase)
