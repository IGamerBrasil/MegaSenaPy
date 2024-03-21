from Repositorios import ApostasBD
from Modelos import Apostas
from faker import Faker

gerador = Faker()

class ServicoApostas:
    def __init__(self):
        self.aBD = ApostasBD.ApostaBD()
        self.vetor_apostas = []

    
    def criacao_de_tabelas(self):
        self.aBD.connectBD()
        #self.aBD.deleteBDs()
        self.aBD.criarTabelas()
        
        
    def registro_usuario(self,cpf,nome):
        aposta = self.aBD.identificacaoUsuario(cpf, nome)
        self.aBD.commitBD()
        return aposta
    
    def registrar_apostadores(self):
        self.vetor_apostas.clear()
        for _ in range(10):
            nome = gerador.name()
            cpf = gerador.numerify(text='###########')
            aposta = self.registro_usuario(cpf,nome)
            self.sist_surpresa(aposta)
            
            
        return self.vetor_apostas
            
        
    def registros_apostadores(self,apostas):
        self.aBD.criarApostadores(apostas)  
        
    def sist_surpresa(self,aposta):
        if isinstance(aposta,Apostas.Aposta):
            self.aBD.surpresinha(aposta)
            self.vetor_apostas.append(aposta)
            self.aBD.commitBD()
            
    def adicao_de_numeros(self,aposta,num):
        if isinstance(aposta,Apostas.Aposta):
            self.aBD.adicionarNumero(aposta, num)

    def salvaNumeros(self, aposta):
        self.aBD.adicionarNumerosBD(aposta)
        self.vetor_apostas.append(aposta)
        self.aBD.commitBD()
            
    def resetar_vetor(self, aposta):
        if isinstance(aposta,Apostas.Aposta):
            self.aBD.resetNumeros(aposta)
        
    def visualizador_numeros_apostados_por_cpf(self, cpf):
        return self.aBD.mostrar_apostas(cpf)
    
    def fechar_banco(self):
        self.aBD.fechaBD()
 