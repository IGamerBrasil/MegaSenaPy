from Repositorios import ApostasBD
from Modelos import Apostas
from faker import Faker

##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

gerador = Faker()

#Classe para o App.py nao ter acesso direto ao Banco de Dadods
class ServicoApostas:
        def __init__(self):
            self.aBD = ApostasBD.ApostaBD()
            self.vetor_apostas = []

        def criacao_de_tabelas(self):
            self.aBD.connectBD()
            self.aBD.criarTabelas()
        
        #Caso queira excluir os Bancos ponha na ultima linha do App.py, salve, execute e aperte 4           
        def delecao_de_tabelas(self):
            self.aBD.deleteBDs()

        def registro_usuario(self,cpf,nome):
            aposta = self.aBD.identificacaoUsuario(cpf, nome)
            self.aBD.commitBD()
            return aposta

        #Gera Count apostadores para o sorteio
        def registrar_apostadores(self,count):
            for _ in range(count):
                nome = gerador.name()
                cpf = gerador.numerify(text='###########')
                aposta = self.registro_usuario(cpf,nome)
                self.sist_surpresa(aposta)
                

            return self.vetor_apostas

        #Metodo do sistema Surpresinha
        def sist_surpresa(self,aposta):
            if isinstance(aposta,Apostas.Aposta):
                self.aBD.surpresinha(aposta)
                self.vetor_apostas.append(aposta)
                self.aBD.commitBD()

        #Adiciona numero escolhido a aposta
        def adicao_de_numeros(self,aposta,num):
            if isinstance(aposta,Apostas.Aposta):
                self.aBD.adicionarNumero(aposta, num)
                
        #Adiciona todos os numeros escolhido ao banco
        def salvaNumeros(self, aposta):
            self.aBD.adicionarNumerosBD(aposta)
            self.vetor_apostas.append(aposta)
            self.aBD.commitBD()

        #Metodo que retorna todas as apostas dentro do banco
        def visualizador_numeros_apostados_por_cpf(self, cpf):
            return self.aBD.mostrar_apostas(cpf)

        #Metodo para encerrar comunicacao com o banco
        def fechar_banco(self):
            self.aBD.fechaBD()
 