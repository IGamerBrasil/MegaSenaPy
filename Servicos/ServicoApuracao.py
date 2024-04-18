from Modelos import Apuracoes
from Modelos import Apostas

from Servicos import ServicoSorteio

##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

class ServicoApuracao():
    def __init__(self, servSorteio):
        self.servSorteio = servSorteio     
        self.apuracao = Apuracoes.Apuracao(self.servSorteio.sorteio)

    #Vê quem ganhou, caso nao tenha ele faz rodadas extra
    def verificarGanhadores(self,vetApostas):
        if vetApostas is not None:
            self.apuracao.verificaGanhador(vetApostas)
            ganhadores_sorteio = self.apuracao.ganhadores
            if not len(ganhadores_sorteio):
                print('Ninguem ganhou, por essa nao esperavamos, por isso daremos mais 25 CHANCES!!')
                print(' ')
                for _ in range(25):
                    self.servSorteio.sorteio.sortearExtra()
                    self.apuracao.verificaGanhador(vetApostas)
                    if len(ganhadores_sorteio) > 0:
                        break
        else:
            return None
        
    #Metodo para armazenar em ordem decrescente os numeros sorteados que mais e menos apareceram
    def maior_ao_menor_num_aparecido(self,apostas):
        dict = {}
        count = 0
        todas_apostas = apostas
        for i in self.servSorteio.lista_de_num_sorteados():
            count = 0
            for a in todas_apostas:
                if isinstance(a,Apostas.Aposta):
                    for n in a.numeros:
                        if n == i:
                            count+=1
                            
            dict.update({i:count})
        return dict
    
    #Ordena em ordem alfabética de acordo com o nome
    def lista_das_apostas_ganhadoras_em_ordem(self):
        return sorted(self.apuracao.ganhadores, key=lambda x: x.nome)
             
            
    

