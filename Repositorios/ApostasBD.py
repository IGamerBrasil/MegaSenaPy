import mysql.connector
import random
from Modelos import Apostas
from faker import Faker
gerador = Faker()

##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

#Classe que mexe diretamente com o Banco
class ApostaBD:
    #Criação do banco de dados
    def __init__(self):
        #id da aposta no banco de dados
        self.id = 1000
        self.db_config = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="dell",
                    password="root"
                    )
        
    #Conexão com o Banco de dados
    def connectBD(self):
        self.cursorAposta = self.db_config.cursor()
        self.cursorNumerosAposta = self.db_config.cursor()
        
    #Criação das Tabela  
    def criarTabelas(self):
        
        #Result é verdadeiro se existir tabela de aposta
        self.cursorAposta.execute("SELECT * FROM information_schema.tables WHERE table_schema = %s AND table_name = %s", (self.db_config.database, "aposta"))
        result = self.cursorAposta.fetchone()
        
        #if para impedir que se crie mais de uma vez a tabela
        if not result:
            self.create_table_query = """
                                CREATE TABLE aposta (
                                    id int PRIMARY KEY NOT NULL,
                                    cpf char(11) NOT NULL,
                                    nome varchar(100) NOT NULL
                                )
                               """
            self.cursorAposta.execute(self.create_table_query)
        else:
            self.verificacao_conteudo()
            
        #Result é verdadeiro se existir tabela de numeros_aposta
        self.cursorNumerosAposta.execute("SELECT * FROM information_schema.tables WHERE table_schema = %s AND table_name = %s", (self.db_config.database, "numeros_aposta"))      
        result = self.cursorNumerosAposta.fetchone()   
        
        #if para impedir que se crie mais de uma vez a tabela 
        if not result:
            self.criarTabelaNumerosApostados()
    
    def criarTabelaNumerosApostados(self):
        self.create_table_query = """
                                CREATE TABLE numeros_aposta (
                                    id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
                                    n1 int,
                                    n2 int,
                                    n3 int,
                                    n4 int,
                                    n5 int,
                                    id_aposta int NOT NULL,
                                    FOREIGN KEY (id_aposta) REFERENCES aposta(id)
                                )
                                """
        self.cursorNumerosAposta.execute(self.create_table_query)
        print("CriadaNumeros")
        
        
    #insercao de dados no banco
    
    def adicionarNumero(self, aposta, num):
        
        #Verifica se num esta no intervalo 1 a 50, juntamente se num não esta na aposta e se a aposta ainda não tem 5 números
        if num in range(1,51) and num not in aposta.numeros and len(aposta.numeros) < 5:
            aposta.numeros.append(num)
            
    #Sistema Surpresinha            
    def surpresinha(self, aposta):
        aposta.numeros = random.sample(range(1,51),5)
        self.adicionarNumerosBD(aposta) 
    
    #Adiciona no Banco e retorna aposta       
    def identificacaoUsuario(self, cpf, nome):
        apostador = Apostas.Aposta(nome, cpf, self.id)
        
        self.cursorAposta.execute("""
                                    INSERT INTO aposta (id, cpf, nome)
                                    VALUES (%s, %s,%s);
                                    """, (self.id, cpf, nome))
        self.id+=1
        return apostador
    
    #Adiciona numeros da aposta no banco      
    def adicionarNumerosBD(self, aposta):
        if aposta.numeros is not None:
           self.cursorNumerosAposta.execute("""
                                            INSERT INTO numeros_aposta (n1,n2,n3,n4,n5,id_aposta)
                                            VALUES (%s, %s, %s, %s, %s, %s);
                                            """,(aposta.numeros[0], aposta.numeros[1], aposta.numeros[2], aposta.numeros[3], aposta.numeros[4], aposta.id))
    #Retorna todas as aposta do cpf específico
    def mostrar_apostas(self, cpf):
        
        #seleciona todas as aposta do cpf específico
        self.cursorNumerosAposta.execute(f"""
                                         SELECT na.id_aposta, na.n1, na.n2, na.n3, na.n4, na.n5 FROM aposta a LEFT JOIN numeros_aposta na ON a.id = na.id_aposta WHERE a.cpf = {cpf}
                                         """)

        return self.cursorNumerosAposta.fetchall()
    
    #Faz com que o primeiro id do sorteio a ser executado seja sequencial de acordo com o banco das apostas
    def verificacao_conteudo(self):
            self.cursorAposta.execute("SELECT * FROM aposta")
            apostas = self.cursorAposta.fetchall()
            if apostas is not None:
                if len(apostas) > 0:
                    self.id = apostas[len(apostas)-1][0]+1
                    
    #Deleta todos as tabela                
    def deleteBDs(self):
        self.cursorNumerosAposta.execute("""
                                    DROP TABLE numeros_aposta
                                    """) 
        self.cursorAposta.execute("""
                                    DROP TABLE aposta
                                      """)    
    #Atualiza o Banco    
    def commitBD(self):
        self.db_config.commit()
    
    #Encerra comunicação com o banco
    def fechaBD(self):
        self.db_config.close()      