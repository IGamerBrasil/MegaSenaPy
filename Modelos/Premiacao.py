class Premiacao():
    def __init__(self):
        self.valor = 0

    def digitarValor(self):
        while True:
            try:
                self.valor = int(input('Digite o valor que o sortudo ira GANHAR!!'))
            except ValueError:
                print('Valor Invalido!!')
            else:
                break
    def notficacao_premio(self,usuarioGanha,s):
        if usuarioGanha:
            if s == 1:
                print(f'PARABENS!!! VOCE FOI O SORTUDO A VENCER NOSSO SORTEIO E GANHOU R${self.valor}!!!! ')
            else:
             print(f'PARABENS!!! VOCE FOI UM DOS SORTUDOS A VENCER UM DOS NOSSOS SORTEIOS E GANHOU R${self.valor/s}')
        else:
             if s == 1:
                 print(f'ALGUEM VENCEU UM DOS NOSSOS SORTEIOS  E GANHOU R${self.valor}!!!! ')
             else:
                print(f'VARIAS PESSOAS GANHARAM UM DOS NOSSOS SORTEIOS E CADA UM GANHOU R${self.valor/s}!!!! ')