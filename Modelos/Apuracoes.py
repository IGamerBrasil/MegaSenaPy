from Modelos import Sorteios
verifaca = False

##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

#Classe Modelo para a fase de apuração
class Apuracao:
    def __init__(self, sorteio):
        self.numerosSorteados = None
        if isinstance(sorteio,Sorteios.Sorteio):
            self.sorteio = sorteio
        else:
            self.sorteio = None
        self.ganhadores = []
        self.rodadas = 0

<<<<<<< HEAD
=======
    
    def verificaGanhador(self, apostas = None):
        if isinstance(apostas,list) and apostas is not None:
            if isinstance(self.sorteio,Sorteios.Sorteio):
<<<<<<< HEAD
                self.sorteio.rodada(self.ganhadores, apostas)
    
=======
                self.sorteio.rodada(self.vencedores, apostas)
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
    
    def verificaGanhador(self, apostas = None):
        if isinstance(apostas,list) and apostas is not None:
            if isinstance(self.sorteio,Sorteios.Sorteio):
                self.sorteio.rodada(self.ganhadores, apostas)
    
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
    def numeroGanhadores(self):
        return len(self.ganhadores)
    
    def getNumeroDeRodadas(self):
        if self.sorteio is not None:
            return self.sorteio.rodadas
        else:
            return None
    
        