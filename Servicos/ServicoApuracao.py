from Modelos import Sorteios
from Modelos import Apuracoes
from Modelos import Apostas

##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

class ServicoApuracao():
    def __init__(self):
        self.sorteio = Sorteios.Sorteio()
        self.apuracao = Apuracoes.Apuracao(self.sorteio)
    
    def sortear(self):
       self.sorteio.sortearNumeros()
    
    #Vê quem venceu, caso nao tenha ele faz rodadas extra
    def verificarVencedores(self,vetApostas):
        if vetApostas is not None:
            self.apuracao.verificaVencedor(vetApostas)
            vencs_sorteio = self.apuracao.vencedores
            if not len(vencs_sorteio):
                print('PUTZ!! Ninguem ganhou, por essa nao esperavamos, por isso daremos mais 25 CHANCES!!')
                print(' ')
                for _ in range(25):
                    self.sorteio.sortearExtra()
                    self.apuracao.verificaVencedor(vetApostas)
                    if len(vencs_sorteio) > 0:
                        break
        else:
            return None
        
    #Metodo para armazenar em ordem decrescente os numeros sorteados que mais e menos apareceram
    def maior_ao_menor_num_aparecido(self,apostas):
        dict = {}
        count = 0
        todas_apostas = apostas
        for i in self.lista_de_num_sorteados():
            for a in todas_apostas:
                if isinstance(a,Apostas.Aposta):
                    for n in a.numeros:
                        if n == i:
                            count+=1
            dict.update({i:count})
        return dict
    
    #Ordena em ordem alfabética de acordo com o nome
    def lista_das_apostas_vencedoras_em_ordem(self):
        return sorted(self.apuracao.vencedores, key=lambda x: x.nome)
        
                      
    def lista_de_num_sorteados(self):           
         return self.sorteio.numerosSorteados           
       
        
