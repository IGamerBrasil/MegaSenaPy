from Modelos import Sorteios

##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

#Classe Modelo para a fase de apuração
class Apuracao:
    def __init__(self, sorteio):
        if isinstance(sorteio,Sorteios.Sorteio):
            self.sorteio = sorteio
        else:
            self.sorteio = None
        self.ganhadores = []
        self.rodadas = 0

    
    def verificaGanhador(self, apostas = None):
        if isinstance(apostas,list) and apostas is not None:
            if isinstance(self.sorteio,Sorteios.Sorteio):
                self.sorteio.rodada(self.ganhadores, apostas)
    
    def numeroGanhadores(self):
        return len(self.ganhadores)
    
    
        