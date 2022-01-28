import ordenadores
import time
import random

class ContaTempos:

    def lista_aleatoria(self, n):
        lista = [random.randrange(n+1) for x in range(n+1)]
        return lista
    

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n+1)]
        lista[n//10] = -157
        return lista
    

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]      
        
        ord_list = ordenadores.Ordenador()

        print("Comparando listas desordenadíssimas")
            
        antes = time.time()
        ord_list.selection_sort(lista1)
        depois = time.time()
        print("Selection Sort demorou ", depois - antes)

        antes = time.time()
        ord_list.bubble_sort(lista2)
        depois = time.time()
        print("Bubble Sort demorou ", depois - antes)

        print("\nComparando listas quase ordenadas")
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]      

        antes = time.time()
        ord_list.selection_sort(lista1)
        depois = time.time()
        print("Selection Sort demorou ", depois - antes)

        antes = time.time()
        ord_list.bubble_sort(lista2)
        depois = time.time()
        print("Bubble Sort demorou ", depois - antes)


        
