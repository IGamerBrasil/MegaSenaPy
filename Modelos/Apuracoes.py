from Apostas import Aposta
from Sorteios import Sorteio
verifaca = False
class Apuracao:
    def __init__(self, sorteio):
        self.numerosSorteados = None
        if isinstance(sorteio,Sorteio):
            self.sorteio = sorteio
        else:
            self.sorteio = None
        self.vencedores = []
        self.rodadas = 0
        
    def verificaVencedor(self, apostas = None):
        if isinstance(apostas,list) and apostas is not None:
            if isinstance(self.sorteio,Sorteio):
                self.sorteio.rodada(self.vencedores, apostas)
    
    def numeroVencedores(self):
        return len(self.vencedores)
    
    def getNumeroDeRodadas(self):
        if self.sorteio is not None:
            return self.sorteio.rodadas
        else:
            return None
    
        