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
    
<<<<<<< HEAD
    #Vê quem ganhou, caso nao tenha ele faz rodadas extra
    def verificarGanhadores(self,vetApostas):
=======
<<<<<<< HEAD
    #Vê quem ganhou, caso nao tenha ele faz rodadas extra
    def verificarGanhadores(self,vetApostas):
=======
    #Vê quem venceu, caso nao tenha ele faz rodadas extra
    def verificarVencedores(self,vetApostas):
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
        if vetApostas is not None:
            self.apuracao.verificaGanhador(vetApostas)
            ganhadores_sorteio = self.apuracao.ganhadores
            if not len(ganhadores_sorteio):
                print('Ninguem ganhou, por essa nao esperavamos, por isso daremos mais 25 CHANCES!!')
                print(' ')
                for _ in range(25):
                    self.sorteio.sortearExtra()
<<<<<<< HEAD
                    self.apuracao.verificaGanhador(vetApostas)
                    if len(ganhadores_sorteio) > 0:
=======
<<<<<<< HEAD
                    self.apuracao.verificaGanhador(vetApostas)
                    if len(ganhadores_sorteio) > 0:
=======
                    self.apuracao.verificaVencedor(vetApostas)
                    if len(vencs_sorteio) > 0:
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
                        break
        else:
            return None
        
    #Metodo para armazenar em ordem decrescente os numeros sorteados que mais e menos apareceram
    def maior_ao_menor_num_aparecido(self,apostas):
        dict = {}
        count = 0
        todas_apostas = apostas
        for i in self.lista_de_num_sorteados():
<<<<<<< HEAD
            count = 0
=======
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
            for a in todas_apostas:
                if isinstance(a,Apostas.Aposta):
                    for n in a.numeros:
                        if n == i:
                            count+=1
<<<<<<< HEAD
                            
=======
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
            dict.update({i:count})
        return dict
    
    #Ordena em ordem alfabética de acordo com o nome
<<<<<<< HEAD
    def lista_das_apostas_ganhadoras_em_ordem(self):
        return sorted(self.apuracao.ganhadores, key=lambda x: x.nome)
=======
<<<<<<< HEAD
    def lista_das_apostas_ganhadoras_em_ordem(self):
        return sorted(self.apuracao.ganhadores, key=lambda x: x.nome)
=======
    def lista_das_apostas_vencedoras_em_ordem(self):
        return sorted(self.apuracao.vencedores, key=lambda x: x.nome)
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
        
                      
    def lista_de_num_sorteados(self):           
         return self.sorteio.numerosSorteados           
       
        
