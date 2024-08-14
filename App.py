from Servicos import ServicoApostas
from Servicos import ServicoApuracao
from Servicos import ServicoSorteio

from Modelos import Apostas
from Modelos import Premiacao

import re
import os



##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
###########################################
__servSorteio = ServicoSorteio.ServicoSorteio()
__servAposta = ServicoApostas.ServicoApostas()
__servApuracao = ServicoApuracao.ServicoApuracao(__servSorteio)
__premiacao = Premiacao.Premiacao()

__servSorteio.criar_tabela_sorteio()
__servAposta.criacao_de_tabelas()

nome = ''
cpf = ''

op = 0
id_inicial = 0
num_participantes = 5

apostaUsuario = None
vetor_apostas = []

ja_registrado = False
sorteio_registrado = False

#metodo que deixa mais limpo o terminal
def limpar_console():
    print(os.name)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu(id):
    print('----------------------------------------------------------------')
    print(f'Sorteio {id} da MegaSena')
    print('----------------------------------------------------------------')
    print('Menu')
    print('1 - Apostar')
    print('2 - Ver minhas apostas')
    print('3 - Ver sorteios')
    print('4 - Buscar sorteio')
    print('5 - Apuração e Premiação')	
    print('6 - Sair')
    #print('7 - Deletar Tabelas')
    

# Loop do Menu
while True:
    if op > 6:
        limpar_console()
        print('Digite número de 1 a 6')
    
    #Impedi que nao registre mais de uma vez o mesmo sorteio
    if not sorteio_registrado:
        sorteio_registrado = True
        __servSorteio.registrar_sorteio(0, 0, 0)
        id_sorteio = __servSorteio.get_sorteio_atual()[0]
        
    menu(id_sorteio)
    
    #Salva primeiro id para quando for mostrar as apostas apenas mostre as do sorteio em execução
    if op == 0:
        id_inicial = __servAposta.aBD.id
        
    #Verificação caso não seja um número
    try:
        op = int(input('Opção: '))
        if re.match(r'^[a-zA-Z]+[a-zA-Z\s]*$', op):
            raise Exception
    except Exception:
        limpar_console()
        print('Valor digitado não é um número!')

    match op:
        case 1:
            #case para pegar as informações do usuário
            limpar_console()
            if not ja_registrado:
                nome = input('Seu nome: ')

                while not re.match(r'^[a-zA-Z]+[a-zA-Z\s]*$', nome):
                    print('Nome invalido!')
                    nome = input('Seu nome: ')

                cpf = input('Seu CPF: ')

                #Loop para verificação de autenticação de CPF
                while len(cpf) != 11 or not re.match(r'^[0-9]*$', cpf):
                    print('CPF invalido!')
                    cpf = input('Seu CPF: ')
                ja_registrado = True

            #Pega as informações do usuário e armazena no Banco de Dados
            apostaUsuario = __servAposta.registro_usuario(cpf,nome,id_sorteio)

            #Loop para caso não ponha as informações corretas o usuário não possa continuar
            while True:
                limpar_console()
                menu(id_sorteio)

                surpresa = input('Surpresa? (s/n): ').lower()

                if surpresa=='s':
                    __servAposta.sist_surpresa(apostaUsuario)
                    vetor_apostas.append(apostaUsuario)
                    print('Inserido')

                    limpar_console()
                    print('APOSTADO!!') 

                    break 
                elif surpresa=='n':

                    for _ in range(5):
                        while True:
                            try:
                                num = int(input('Digite um numero: '))
                                if(num < 1 or num > 50):
                                    raise ValueError
                            except:
                                print('Digite um numero de 1 a 50')
                            else:
                                __servAposta.adicao_de_numeros(apostaUsuario, num)
                                break
                            
                    __servAposta.salvaNumeros(apostaUsuario)

                    limpar_console()  

                    print('APOSTADO!!')
                    break
        case 2:
            #case para mostrar caso tenha alguma aposta guardada no banco de dados  
            limpar_console()
            if apostaUsuario is not None:

                apostas = __servAposta.lista_numeros_apostados_por_cpf(apostaUsuario.cpf, id_sorteio)

                if not apostas:
                    print('Não há apostas registradas.')
                else:
                    print('Apostas do Sorteio atual:')

                    for row in apostas:
                        if row[0] != None:
                            if isinstance(row[0], int):
                                if row[0] >= id_inicial:
                                    print(f'Aposta {row[0]} - Numeros: {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}')
        case 3:
            #case para visualizar todos os sorteios
            limpar_console()
            print('Sorteios: ')
            for row in __servSorteio.get_sorteios():
                print(f'Sorteio {row[0]}: Numero de Vencedores: {row[1]}, Rodadas: {row[2]}')
        case 4:
            #case para visualizar um sorteio especifico
            limpar_console()
            quant_sorteios = len(__servSorteio.get_sorteios())
            while True:
                try:
                    sorteio_id = int(input(f'Digite um id de 1 ate {quant_sorteios-1}: '))
                    if(sorteio_id < 1 or sorteio_id >= quant_sorteios):
                        raise Exception
                except:
                    print(f'Id Invalida!! {sorteio_id}')
                else:
                    break
            sorteio = __servSorteio.get_sorteio(sorteio_id)
            print(f'Sorteio {sorteio_id}: Numero de Vencedores: {sorteio[1]}, Rodadas: {sorteio[2]}')  
            pass
        case 5:
            #case da Apuração e Premiação
            #Fase Apuração
            limpar_console()
            print('Execuntando o sorteio! BOA SORTE!')
            print(' ')
            __premiacao.digitarValor()

            #If para verificar se apostou
            if len(vetor_apostas) == 0:
                vetor_apostas = __servAposta.registrar_apostadores(num_participantes,id_sorteio)
            else:
                vetor_apostas.extend(__servAposta.registrar_apostadores(num_participantes,id_sorteio))  
            __servSorteio.sortear()

            #Pega todas as apostas e verifica quem ganhou
            __servApuracao.verificarGanhadores(vetor_apostas)

            if __servSorteio.getNumeroDeRodadas() < 15:
                print(f'Sorteio {id_sorteio} Terminado com {__servSorteio.getNumeroDeRodadas()} RODADAS QUE RAPIDO!!')
            else:
                print(f'Desculpe a demora, chegamos no final em {__servSorteio.getNumeroDeRodadas()} rodadas...')

            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            print(f'Numeros Sorteados: {__servSorteio.lista_de_num_sorteados()}')
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

            #Verifica se a algum ganhador depois das rodadas
            num_ganhadores = len(__servApuracao.ganhadores)
            if num_ganhadores == 0:
                print('Nao a Ganhadores :(')
            else:
                print(f'Quantidade de Ganhadores: {num_ganhadores}')
                print(' ')
                print('Aposta(s) do(s) Ganhador(es): ')

                #Imprimi Ganhadores
                for a in __servApuracao.lista_das_apostas_ganhadoras_em_ordem():
                    if isinstance(a,Apostas.Aposta):                     
                        print(f'Nome: {a.nome} - {a.numeros}')
                        if a == apostaUsuario:
                            __premiacao.notficacao_premio(True,num_ganhadores)       
                    print(' ')

                #Fase Premiação################################
                __premiacao.notficacao_premio(False,num_ganhadores)                       
                ################################################  

            __servSorteio.update_sorteio(id_sorteio, num_ganhadores, __servSorteio.getNumeroDeRodadas(), __premiacao.valor)        

            #Zera rodadas para o próximo sorteio         
            __servSorteio.rodadas = 0
            veti = __servApuracao.maior_ao_menor_num_aparecido(vetor_apostas)

            if isinstance(veti, dict):
                #Ordena em ordem decrecente
                vetf = sorted(veti.items(), key=lambda x: x[1], reverse=True)

            print('---------------------------------------')
            print('| Nros Apostados       Qntde de Apostas|')
            for i,j in vetf:
                print(f'|  {i}                            {j}   |') 
            print('------------------------------------')
            sorteio_registrado = False
            break
        case 6:
            break
        #case 7:
        #    __servAposta.delecao_de_tabelas()
        #    __servSorteio.delecao_de_tabela_sorteio()
        #    limpar_console()
        #    break

# Fechar conexão com o banco de dados
__servAposta.fechar_banco()


