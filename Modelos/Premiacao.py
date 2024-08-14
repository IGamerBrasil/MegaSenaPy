##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
###########################################

class Premiacao():
    def __init__(self):
        self.valor = 0

    def digitarValor(self):
        while True:
            try:
                self.valor = int(input('Digite o valor que o sortudo ira GANHAR!! R$'))
            except ValueError:
                print('Valor Invalido!!')
            else:
                break
            
    def notficacao_premio(self,usuarioGanha,s):
        if usuarioGanha:
            if s == 1:
                print(f'PARABÉNS!!! VOCÊ FOI O SORTUDO A GANHAR NOSSO SORTEIO E GANHOU R${self.valor:.2f}!!!! ')
            else:
                print(f'PARABÉNS!!! VOCÊ FOI UM DOS SORTUDOS A GANHAR UM DOS NOSSOS SORTEIOS E GANHOU R${self.valor/s:.2f}!!')
        else:
             if s == 1:
                print(f'ALGUEM GANHOU UM DOS NOSSOS SORTEIOS E RECEBEU R${self.valor:.2f}!!!! ')
             else:
                print(f'AS PESSOAS ACIMA GANHARAM UM DOS NOSSOS SORTEIOS E CADA UM RECEBEU R${self.valor/s:.2f}!!!! ')
                