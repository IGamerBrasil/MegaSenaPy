import random
from Apostas import Aposta
class Sorteio:
    
    
    def __init__(self):
        self.numerosSorteados = None
        self.apostas = None
        self.rodadas = 0
        
    def adicionarApostaParaSoteio(self, aposta):
        if self.apostas is None:
            self.apostas = []
        if isinstance( aposta,Aposta ):
            aposta.numeros = random.sample(range(1,51),5)
            self.apostas.append(aposta)
        
        
        
    def sortearNumeros(self):
        self.numerosSorteados = [1,2,3,4,5]#random.sample(range(1,51),5)
    
    def rodada(self,vencedores = None, apostas = None):
        if apostas is not None:
            self.rodadas+=1
            for a in apostas:
                if isinstance(a,Aposta):
                    if set(a.numeros).issubset(set(self.numerosSorteados)):
                        if a not in vencedores:
                            vencedores.append(a)
                    
                
    def sortearExtra(self):
        rand = random.randrange(1,51)
        while rand in self.numerosSorteados:
            rand = random.randrange(1,51)
        self.numerosSorteados.append(rand)