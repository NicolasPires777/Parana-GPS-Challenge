from grafo.grafo import Grafo
from algoritmos.aestrela import Aestrela

def main():
    grafo = Grafo()

    aestrela = Aestrela(grafo.curitiba) #O destino é sempre curitiba
    aestrela.buscar(grafo.canoinhas) #Insira aqui a cidade inicial

if __name__ == "__main__":
    main()