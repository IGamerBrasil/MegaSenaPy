from Modelos import Apuracoes
from Modelos import Apostas


##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

class ServicoApuracao(Apuracoes.Apuracao):
    def __init__(self, sorteio):
        super().__init__(sorteio)
    

    #Vê quem ganhou, caso nao tenha ele faz rodadas extra
    def verificarGanhadores(self,vetApostas):
        if vetApostas is not None:
            self.verificaGanhador(vetApostas)
            ganhadores_sorteio = self.ganhadores
            if not len(ganhadores_sorteio):
                print('Ninguem ganhou, por essa nao esperavamos, por isso daremos mais 25 CHANCES!!')
                print(' ')
                for _ in range(25):
                    self.sorteio.sortearExtra()
                    self.verificaGanhador(vetApostas)
                    if len(ganhadores_sorteio) > 0:
                        break
        else:
            return None
        
    #Metodo para armazenar em ordem decrescente os numeros sorteados que mais e menos apareceram
    def maior_ao_menor_num_aparecido(self,apostas):
        dict = {}
        count = 0
        todas_apostas = apostas
        for i in self.sorteio.numerosSorteados:
            count = 0
            for a in todas_apostas:
                if self._Apuracao__verifica_tipo(a, Apostas.Aposta):
                    for n in a.numeros:
                        if n == i:
                            count+=1
                            
            dict.update({i:count})
        return dict
    
    #Ordena em ordem alfabética de acordo com o nome
    def lista_das_apostas_ganhadoras_em_ordem(self):
        return sorted(self.ganhadores, key=lambda x: x.nome)
             
            
    

