import mysql.connector
import random

class SorteioBD:
    #Criação do banco de dados
    def __init__(self):
        self.db_config = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="dell",
                    password="root"
                    )
            
    #Conexão com o Banco de dados
    def connectSorteioBD(self):
        #mexe com a tabela dos sorteios realizados
        self.cursorSorteios = self.db_config.cursor()
    
    def criar_sorteios_tabela(self):
        self.cursorSorteios.execute("SELECT * FROM information_schema.tables WHERE table_schema = %s AND table_name = %s", (self.db_config.database, "sorteios"))
        
        #Result é verdadeiro se existir tabela de aposta
        result = self.cursorSorteios.fetchone()
        
        if not result:
            self.create_table_query = """
                                CREATE TABLE sorteios (
                                    id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
                                    numero_vencedores int NOT NULL,
                                    rodadas int NOT NULL
                                );
                               """
            self.cursorSorteios.execute(self.create_table_query)
    
    
    def registrarSorteio(self, num_vencedores, rodadas):
        self.cursorSorteios.execute("""
                                    INSERT INTO sorteios (numero_vencedores, rodadas)
                                    VALUES (%s, %s);
                                    """, (num_vencedores, rodadas))

        
    def get_sorteio(self):
        self.cursorSorteios.execute("SELECT * FROM sorteios;")
        list = self.cursorSorteios.fetchall()[-1]
        return list
    
    def update_sorteio(self, id, numero_vencedores, rodadas):
        self.cursorSorteios.execute("""
                                    UPDATE sorteios
                                    SET numero_vencedores = %s 
                                    WHERE id = %s
                                    """,(numero_vencedores,id))
        
        self.cursorSorteios.execute("""
                                    UPDATE sorteios
                                    SET rodadas = %s 
                                    WHERE id = %s
                                    """,(rodadas,id))
        
    def deleteSorteioBD(self):
        self.cursorSorteios.execute("SELECT * FROM information_schema.tables WHERE table_schema = %s AND table_name = %s", (self.db_config.database, "sorteios"))
        
        #Result é verdadeiro se existir tabela de aposta
        result = self.cursorSorteios.fetchone()
        if result:
            self.cursorSorteios.execute("""
                                    DROP TABLE sorteios
                                      """)  
        else:
            print('Tabela nao existe')
            
    #Atualiza o Banco    
    def commitBD(self):
        self.db_config.commit()
        
    def fechaBD(self):
        self.db_config.close()   