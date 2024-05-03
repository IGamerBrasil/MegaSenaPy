from Repositorios import BD

class ServicoConexaoUnica():
    def __init__(self):
        self.bd = BD.BD()
        