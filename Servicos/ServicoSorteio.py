from Modelos import Sorteios
from Repositorios import SorteioBD


##########################################
# Programa - ServicoSorteio
# Autor -    Lucas Candemil Chagas
###########################################

class ServicoSorteio(Sorteios.Sorteio):
    def __init__(self):
        super().__init__()
        self.__rep_sorteio = SorteioBD.SorteioBD()
    
    @property
    def rep_sorteio(self):
        return self.__rep_sorteio
       
    def sortear(self):
        self.sortearNumeros()
        
    def lista_de_num_sorteados(self):           
         return self.numerosSorteados   

    def criar_tabela_sorteio(self):
        self.rep_sorteio.connectSorteioBD() 
        self.rep_sorteio.criar_sorteios_tabela()
    
    def registrar_sorteio(self, num_vencedores, rodadas, valor_premio):
        self.rep_sorteio.registrarSorteio(num_vencedores, rodadas, valor_premio)
        self.__commitSorteios()
    
    def update_sorteio(self, id, num_vencedores, rodadas, valor_premio):
        self.rep_sorteio.update_sorteio(id, num_vencedores, rodadas, valor_premio)
        self.__commitSorteios()
        
    def get_sorteio_atual(self):
        return self.rep_sorteio.get_sorteio_atual()
    
    def get_sorteios(self):
        return self.rep_sorteio.get_sorteios()

    def get_sorteio(self, id):
        return self.rep_sorteio.mostrar_sorteio(id)
    
    def getNumeroDeRodadas(self):
        return self.rodadas
          
    def delecao_de_tabela_sorteio(self):
        self.rep_sorteio.deleteSorteioBD()
        
    def __commitSorteios(self):
        self.rep_sorteio.conexao.commitBD()