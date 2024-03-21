from Modelos import Sorteios
from Modelos import Apuracoes
from Modelos import Apostas
from ServicoApostas import ServicoApostas


class ServicoApuracao():
    def __init__(self):
        self.sorteio = Sorteios.Sorteio()
        self.apuracao = Apuracoes.Apuracao(self.sorteio)
    
    def sortear(self):
       self.sorteio.sortearNumeros()
    
    def verificarVencedores(self,vetApostas):
        if vetApostas is not None:
            self.apuracao.verificaVencedor(vetApostas)
            vencs_sorteio = self.apuracao.vencedores
            if not len(vencs_sorteio):
                print('PUTZ!! Ninguem ganhou, por essa nao esperavamos, por isso daremos mais 25 CHANCES!!')
                print(' ')
                for _ in range(25):
                    self.sorteio.sortearExtra()
                    self.sorteio.rodada(vencs_sorteio,vetApostas)
                    if len(vencs_sorteio) > 0:
                        break
        else:
            return None
    
                      
    def lista_de_sorteados(self):           
         return self.sorteio.numerosSorteados           
       
        
