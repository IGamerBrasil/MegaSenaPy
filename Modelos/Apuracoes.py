from Modelos import Sorteios

##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
###########################################

#Classe Modelo para a fase de apuração
class Apuracao:
    def __init__(self, sorteio):
        if self.__verifica_tipo(sorteio, Sorteios.Sorteio):
            self.sorteio = sorteio
        else:
            self.sorteio = None
        self.ganhadores = []
        self.rodadas = 0

    def __verifica_tipo(self, variavel, tipo):
        if isinstance(variavel, tipo):
            return True
        return False
    
    def __valida_lista(self, lista):
        if isinstance(lista,list) and lista is not None:
            return True
        return False
    
    def verificaGanhador(self, apostas = None):
        if self.__valida_lista(apostas):
            if self.__verifica_tipo(self.sorteio,Sorteios.Sorteio):
                self.sorteio.rodada(self.ganhadores, apostas)
    
    def numeroGanhadores(self):
        return len(self.ganhadores)
    
    
        