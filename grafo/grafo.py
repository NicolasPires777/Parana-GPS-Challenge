from .vertice import Vertice
from .adjacente import Adjacente

class Grafo:
    def __init__(self):
        self.portoUniao = Vertice('Porto União', 203)
        self.pauloFrontin = Vertice('Paulo Frontin', 172)
        self.canoinhas = Vertice('Canoinhas', 141)
        self.tresBarras = Vertice('Três Barras', 131)
        self.saoMateusDoSul = Vertice('São Mateus do Sul', 123)
        self.irati = Vertice('Irati', 139)
        self.curitiba = Vertice('Curitiba', 0)
        self.palmeira = Vertice('Palmeira', 59)
        self.mafra = Vertice('Mafra', 94)
        self.campoLargo = Vertice('Campo Largo', 27)
        self.balsaNova = Vertice('Balsa Nova', 41)
        self.lapa = Vertice('Lapa', 74)
        self.tijucasDoSul = Vertice('Tijucas do Sul', 56)
        self.araucaria = Vertice('Araucária', 23)
        self.saoJoseDosPinhais = Vertice('São José dos Pinhais', 13)
        self.contenda = Vertice('Contenda', 39)

        self._criar_grafo()

    def _criar_grafo(self):
        self.portoUniao.adiciona_adjacente(Adjacente(self.pauloFrontin, 46))
        self.portoUniao.adiciona_adjacente(Adjacente(self.saoMateusDoSul, 87))
        self.portoUniao.adiciona_adjacente(Adjacente(self.canoinhas, 78))

        self.pauloFrontin.adiciona_adjacente(Adjacente(self.portoUniao, 46))
        self.pauloFrontin.adiciona_adjacente(Adjacente(self.irati, 75))

        self.canoinhas.adiciona_adjacente(Adjacente(self.portoUniao, 78))
        self.canoinhas.adiciona_adjacente(Adjacente(self.mafra, 66))
        self.canoinhas.adiciona_adjacente(Adjacente(self.tresBarras, 12))

        self.tresBarras.adiciona_adjacente(Adjacente(self.saoMateusDoSul, 43))
        self.tresBarras.adiciona_adjacente(Adjacente(self.canoinhas, 12))

        self.saoMateusDoSul.adiciona_adjacente(Adjacente(self.portoUniao, 87))
        self.saoMateusDoSul.adiciona_adjacente(Adjacente(self.tresBarras, 43))
        self.saoMateusDoSul.adiciona_adjacente(Adjacente(self.irati, 57))
        self.saoMateusDoSul.adiciona_adjacente(Adjacente(self.palmeira, 77))
        self.saoMateusDoSul.adiciona_adjacente(Adjacente(self.lapa, 60))

        self.irati.adiciona_adjacente(Adjacente(self.palmeira, 75))
        self.irati.adiciona_adjacente(Adjacente(self.pauloFrontin, 75))
        self.irati.adiciona_adjacente(Adjacente(self.saoMateusDoSul, 57))

        self.curitiba.adiciona_adjacente(Adjacente(self.campoLargo, 29))
        self.curitiba.adiciona_adjacente(Adjacente(self.balsaNova, 51))
        self.curitiba.adiciona_adjacente(Adjacente(self.araucaria, 37))
        self.curitiba.adiciona_adjacente(Adjacente(self.saoJoseDosPinhais, 15))

        self.palmeira.adiciona_adjacente(Adjacente(self.irati, 75))
        self.palmeira.adiciona_adjacente(Adjacente(self.campoLargo, 55))
        self.palmeira.adiciona_adjacente(Adjacente(self.saoMateusDoSul, 77))

        self.mafra.adiciona_adjacente(Adjacente(self.tijucasDoSul, 99))
        self.mafra.adiciona_adjacente(Adjacente(self.lapa, 57))
        self.mafra.adiciona_adjacente(Adjacente(self.canoinhas, 66))

        self.campoLargo.adiciona_adjacente(Adjacente(self.palmeira, 55))
        self.campoLargo.adiciona_adjacente(Adjacente(self.balsaNova, 22))
        self.campoLargo.adiciona_adjacente(Adjacente(self.curitiba, 29))

        self.balsaNova.adiciona_adjacente(Adjacente(self.contenda, 19))
        self.balsaNova.adiciona_adjacente(Adjacente(self.curitiba, 51))
        self.balsaNova.adiciona_adjacente(Adjacente(self.campoLargo, 22))

        self.lapa.adiciona_adjacente(Adjacente(self.contenda, 26))
        self.lapa.adiciona_adjacente(Adjacente(self.saoMateusDoSul, 60))
        self.lapa.adiciona_adjacente(Adjacente(self.mafra, 57))

        self.tijucasDoSul.adiciona_adjacente(Adjacente(self.mafra, 99))
        self.tijucasDoSul.adiciona_adjacente(Adjacente(self.saoJoseDosPinhais, 49))

        self.araucaria.adiciona_adjacente(Adjacente(self.curitiba,37))
        self.araucaria.adiciona_adjacente(Adjacente(self.contenda, 18))

        self.saoJoseDosPinhais.adiciona_adjacente(Adjacente(self.tijucasDoSul, 49))
        self.saoJoseDosPinhais.adiciona_adjacente(Adjacente(self.curitiba, 15))

        self.contenda.adiciona_adjacente(Adjacente(self.balsaNova, 19))
        self.contenda.adiciona_adjacente(Adjacente(self.lapa, 26))
        self.contenda.adiciona_adjacente(Adjacente(self.araucaria, 18))