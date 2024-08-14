##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
###########################################

class Aposta:
    def __init__(self, nome, cpf, id = 0, numeros=None):
        self.__nome = nome
        self.__cpf = cpf
        
        if numeros is None:
            numeros = []
            
        self.__id = id    
        self.numeros = numeros

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def id(self):
        return self.__id
    
    