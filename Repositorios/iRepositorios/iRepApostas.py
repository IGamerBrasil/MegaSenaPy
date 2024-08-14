from abc import ABC, abstractmethod

class iRepAposta(ABC):
    
    @abstractmethod
    def connectApostaBD(self):
        pass
    
    @abstractmethod
    def criarTabelas(self):
        pass
    
    @abstractmethod
    def criar_tabela_apostas(self):
        pass
    
    @abstractmethod
    def criar_tabela_numeros_apostados(self):
        pass
    
    @abstractmethod
    def criar_indexes_cpf_ids(self):
        pass
    
    @abstractmethod
    def adicionarNumero(self, aposta, num):
        pass
    
    @abstractmethod
    def surpresinha(self, aposta):
        pass
    
    @abstractmethod
    def identificacaoUsuario(self, cpf, nome, id_sorteio):
        pass
    
    @abstractmethod
    def identificacaoNaoUsuario(self, cpf, nome, id_sorteio):
        pass
    
    @abstractmethod
    def adicionarNumerosBD(self, aposta):
        pass
    
    @abstractmethod
    def lista_apostas_cpf(self, cpf, id_sorteio):
        pass
    
    @abstractmethod
    def verificacao_conteudo(self):
        pass
    
    @abstractmethod
    def deleteBDs(self):
        pass
    