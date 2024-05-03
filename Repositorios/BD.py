import mysql.connector

class BD:
     def __init__(self):
        #id da aposta no banco de dados
        self.db_config = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="dell",
                    password="root"
                    )