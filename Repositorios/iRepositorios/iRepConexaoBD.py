from abc import ABC, abstractmethod

class iRepConexaoBD(ABC):
    
    @abstractmethod
    def commitBD(self):
       pass
    
    @abstractmethod
    def fechaBD(self):
        pass
       