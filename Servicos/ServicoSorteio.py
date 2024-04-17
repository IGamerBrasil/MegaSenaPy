from Modelos import Sorteios
from Repositorios import SorteioBD


class ServicoSorteio:
    def __init__(self):
        self.sorteio = Sorteios.Sorteio()
        self.rep_sorteio = SorteioBD.SorteioBD()
        
    def sortear(self):
        self.sorteio.sortearNumeros()
        
    def lista_de_num_sorteados(self):           
         return self.sorteio.numerosSorteados   

    def criar_tabela_sorteio(self):
        self.rep_sorteio.connectSorteioBD() 
        self.rep_sorteio.criar_sorteios_tabela()
    
    def registrar_sorteio(self, num_vencedores):
        self.rep_sorteio.registrarSorteio(num_vencedores, self.sorteio.rodadas)
        
    def delecao_de_tabela_sorteio(self):
        self.rep_sorteio.deleteSorteioBD()