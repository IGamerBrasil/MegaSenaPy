from Modelos import Sorteios
from Repositorios import SorteioBD


class ServicoSorteio:
    def __init__(self,connector):
        self.sorteio = Sorteios.Sorteio()
        self.rep_sorteio = SorteioBD.SorteioBD(connector)
        
    def sortear(self):
        self.sorteio.sortearNumeros()
        
    def lista_de_num_sorteados(self):           
         return self.sorteio.numerosSorteados   

    def criar_tabela_sorteio(self):
        self.rep_sorteio.connectSorteioBD() 
        self.rep_sorteio.criar_sorteios_tabela()
    
    def registrar_sorteio(self, num_vencedores, rodadas, valor_premio):
        self.rep_sorteio.registrarSorteio(num_vencedores, rodadas, valor_premio)
        self.rep_sorteio.commitBD()
    
    def update_sorteio(self, id, num_vencedores, rodadas, valor_premio):
        self.rep_sorteio.update_sorteio(id, num_vencedores, rodadas, valor_premio)
        self.rep_sorteio.commitBD()
        
    def get_sorteio_atual(self):
        return self.rep_sorteio.get_sorteio_atual()
    
    def get_sorteios(self):
        return self.rep_sorteio.get_sorteios()

    def get_sorteio(self, id):
        return self.rep_sorteio.mostrar_sorteio(id)
    
    def getNumeroDeRodadas(self):
        if self.sorteio is not None:
            return self.sorteio.rodadas
        else:
            return 0  
          
    def delecao_de_tabela_sorteio(self):
        self.rep_sorteio.deleteSorteioBD()