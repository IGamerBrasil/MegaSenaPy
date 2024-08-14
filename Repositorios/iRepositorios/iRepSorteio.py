from abc import ABC, abstractmethod

class iRepSorteio(ABC):
    
    @abstractmethod
    def connectSorteioBD(self):
        pass
    
    @abstractmethod
    def criar_sorteios_tabela(self):
        pass

    @abstractmethod
    def registrarSorteio(self, num_vencedores, rodadas, valor_premio):
        pass
    
    @abstractmethod
    def get_sorteio_atual(self):
        pass
    
    @abstractmethod
    def update_sorteio(self, id, numero_vencedores, rodadas, valor_premio):
        pass
    
    @abstractmethod
    def get_sorteios(self):
        pass

    @abstractmethod
    def mostrar_sorteio(self, id):
        pass
    
    @abstractmethod
    def deleteSorteioBD(self):
        pass
    
    