class Ordenador:
    
    def selection_sort(self, lista):
        fim = len(lista)
        
        for i in range(fim-1):
            posicao_menor = i
            for j in range(i+1, fim):
                if lista[j] < lista[posicao_menor]:
                    posicao_menor = j
            lista[i], lista[posicao_menor] = lista[posicao_menor], lista[i]
            
        return lista


    def bubble_sort(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                break
    
        return lista


    def insertion_sort(self, lista):
        for i in range(1, len(lista)):
            valor_atual = lista[i]
            posicao = i

            while posicao > 0 and lista[posicao-1] > valor_atual:
                lista[posicao] = lista[posicao-1]
                posicao -= 1

            lista[posicao] = valor_atual

        return lista

