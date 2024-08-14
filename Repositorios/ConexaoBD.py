import mysql.connector
from Repositorios.iRepositorios.iRepConexaoBD import iRepConexaoBD


##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
###########################################

class ConexaoBD(iRepConexaoBD):
   def __init__(self):
      #id da aposta no banco de dados
      self.__db_config = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  database="dell",
                  password="root"
                  )
      
   @property
   def db_config(self):
       return self.__db_config
    
   #Atualiza o Banco    
   def commitBD(self):
      self.db_config.commit()
    
   def fechaBD(self):
      self.db_config.close() 
   
   