import random

from Modelos import Apostas
from faker import Faker
from Repositorios import ApostasBD
##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

gerador = Faker()

#Classe para o App.py nao ter acesso direto ao Banco de Dadods
class ServicoApostas:
        def __init__(self):
            self.vetor_apostas = []
            self.__aBD = ApostasBD.ApostaBD()
        
        @property
        def aBD(self):
            return self.__aBD   

        def criacao_de_tabelas(self):
            self.aBD.connectApostaBD()
            self.aBD.criarTabelas()
            self.aBD.criar_indexes_cpf_ids()
        
        #Caso queira excluir os Bancos ponha na ultima linha do App.py, salve, execute e aperte 4           
        def delecao_de_tabelas(self):
            self.aBD.deleteBDs()

        def registro_usuario(self,cpf,nome,id_sorteio):
            aposta = self.aBD.identificacaoUsuario(cpf, nome, id_sorteio)
            self.__commitApostas()
            return aposta
        
        def registro_nao_usuario(self,cpf,nome,id_sorteio):
            aposta = self.aBD.identificacaoNaoUsuario(cpf, nome, id_sorteio)
            self.__commitApostas()
            return aposta

        #Gera Count apostadores para o sorteio
        def registrar_apostadores(self,count,id_sorteio):
            for _ in range(count):
                apostador = self.__gera_apostador()
                for _ in range(apostador[2]):
                    aposta = self.registro_nao_usuario(apostador[0],apostador[1],id_sorteio)
                    self.sist_surpresa(aposta)
            return self.vetor_apostas

        def __gera_apostador(self):
            nome = gerador.name()
            cpf = gerador.numerify(text='###########')
            num_apostas = random.randint(1,6)
            
            return [cpf,nome,num_apostas]
        
        #Metodo do sistema Surpresinha
        def sist_surpresa(self,aposta):
            if self.__verifica_tipo(aposta,Apostas.Aposta):
                self.aBD.surpresinha(aposta)
                self.vetor_apostas.append(aposta)
                self.__commitApostas()

        #Adiciona numero escolhido a aposta
        def adicao_de_numeros(self,aposta,num):
            if self.__verifica_tipo(aposta,Apostas.Aposta):
                self.aBD.adicionarNumero(aposta, num)
                
        #Adiciona todos os numeros escolhido ao banco
        def salvaNumeros(self, aposta):
            self.aBD.adicionarNumerosBD(aposta)
            self.vetor_apostas.append(aposta)
            self.__commitApostas()

        #Metodo que retorna todas as apostas dentro do banco
        def lista_numeros_apostados_por_cpf(self, cpf, id_sorteio):
            return self.aBD.lista_apostas_cpf(cpf, id_sorteio)

        def __verifica_tipo(self, variavel, tipo):
            if isinstance(variavel, tipo):
                return True
            return False
        
        #Metodo para encerrar comunicacao com o banco
        def fechar_banco(self):
            self.aBD.conexao.fechaBD()
            
        def __commitApostas(self):
            self.aBD.conexao.commitBD()
 