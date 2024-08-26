from .vetor_ordenado import VetorOrdenado

class Aestrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False
        self.distancia_total = 0
    
    def buscar(self, atual):
        print('==========')
        print('Atual: {}'.format(atual.rotulo))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado=True
            print(f'Distância total percorrida: {self.distancia_total} quilometros')
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] is not None:
                self.distancia_total += vetor_ordenado.valores[0].custo
                self.buscar(vetor_ordenado.valores[0].vertice)
        