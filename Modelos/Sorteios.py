import random
from Modelos import Apostas

##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

#Classe Modelo para a fase de Sorteio
class Sorteio:
    
    
    def __init__(self):
        self.numerosSorteados = None
        self.rodadas = 0

    def sortearNumeros(self):
        self.numerosSorteados = [1,2,3,4,5]  #random.sample(range(1,51),5)
    
    def rodada(self,ganhadores = None, apostas = None):
        if apostas is not None:
            self.rodadas+=1
            for a in apostas:
                if isinstance(a,Apostas.Aposta):
                    if set(a.numeros).issubset(set(self.numerosSorteados)):
                        if a not in ganhadores:
                            ganhadores.append(a)
                    
                
    def sortearExtra(self):
        rand = random.randrange(1,51)
        while rand in self.numerosSorteados:
            rand = random.randrange(1,51)
        self.numerosSorteados.append(rand)