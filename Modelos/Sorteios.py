import random
from Modelos import Apostas

##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
###########################################

#Classe Modelo para a fase de Sorteio
class Sorteio:
    
    def __init__(self):
        self.numerosSorteados = None
        self.rodadas = 0

    def sortearNumeros(self):
        self.numerosSorteados = random.sample(range(1,51),5)
    
    def rodada(self,ganhadores = None, apostas = None):
        if apostas is not None:
            self.rodadas+=1
            for a in apostas:
                if self.__verifica_tipo(a, Apostas.Aposta):
                    if self.__verifica_interseccao(a.numeros, self.numerosSorteados):
                        if a not in ganhadores:
                            ganhadores.append(a)            
     
    def __verifica_tipo(self, variavel, tipo):
        if isinstance(variavel, tipo):
            return True
        return False 
    
    def __verifica_interseccao(self, lista1, lista2):
        if set(lista1).issubset(set(lista2)):
            return True
        return False
               
    def sortearExtra(self):
        rand = random.randrange(1,51)
        while rand in self.numerosSorteados:
            rand = random.randrange(1,51)
        self.numerosSorteados.append(rand)