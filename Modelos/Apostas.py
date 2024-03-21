##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

class Aposta:
    def __init__(self, nome, cpf, id = 0, numeros=None):
        self.nome = nome
        self.cpf = cpf
        
        if numeros is None:
            numeros = []
            
        self.id = id    
        self.numeros = numeros

    
    