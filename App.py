from Servicos import ServicoApostas
from Servicos import ServicoApuracao
from Servicos import ServicoSorteio
from Servicos import ServicoConexaoUnica


from Modelos import Apostas
from Modelos import Premiacao

import re
import os



##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

connector = ServicoConexaoUnica.ServicoConexaoUnica()
servSorteio = ServicoSorteio.ServicoSorteio(connector.bd.db_config)
servAposta = ServicoApostas.ServicoApostas(connector.bd.db_config)
servApuracao = ServicoApuracao.ServicoApuracao(servSorteio)
premiacao = Premiacao.Premiacao()

servSorteio.criar_tabela_sorteio()
servAposta.criacao_de_tabelas()

nome = ''
cpf = ''

op = 0
id_inicial = 0

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

def menu():
    print('----------------------------------------------------------------')
    print('Menu')
    print('1 - Apostar')
    print('2 - Ver minhas apostas')
    print('3 - Ver sorteios')
    print('4 - Buscar sorteio')
    print('5 - Apuração e Premiação')	
    print('6 - Sair')
    #print('5 - Deletar Tabelas')

# Loop do Menu
while True:
    if op > 6:
        limpar_console()
        print('Digite número de 1 a 6')
    menu()
    
    if not sorteio_registrado:
        sorteio_registrado = True
        servSorteio.registrar_sorteio(0, 0)
        id_sorteio = servSorteio.get_sorteio_atual()[0]
    
    #Salva primeiro id para quando for mostrar as apostas apenas mostre as do sorteio em execução
    if op == 0:
        id_inicial = servAposta.aBD.id
        
    #Verificação caso não seja um número
    try:
        op = int(input('Opção: '))
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
            apostaUsuario = servAposta.registro_usuario(cpf,nome,id_sorteio)

            #Loop para caso não ponha as informações corretas o usuário não possa continuar
            while True:
                limpar_console()
                menu()

                surpresa = input('Surpresa? (s/n): ').lower()

                if surpresa=='s':
                    servAposta.sist_surpresa(apostaUsuario)
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
                                servAposta.adicao_de_numeros(apostaUsuario, num)
                                break
                            
                    servAposta.salvaNumeros(apostaUsuario)

                    limpar_console()  

                    print('APOSTADO!!')
                    break
        case 2:
            #case para mostrar caso tenha alguma aposta guardada no banco de dados  
            limpar_console()
            if apostaUsuario is not None:

                apostas = servAposta.visualizador_numeros_apostados_por_cpf(apostaUsuario.cpf, id_sorteio)

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
            limpar_console()
            print('Sorteios: ')
            for row in servSorteio.get_sorteios():
                print(f'Sorteio {row[0]}: Numero de Vencedores: {row[1]}, Rodadas: {row[2]}')
        case 4:
            limpar_console()
            quant_sorteios = len(servSorteio.get_sorteios())
            while True:
                try:
                    sorteio_id = int(input(f'Digite um id de 1 ate {quant_sorteios-1}: '))
                    if(sorteio_id < 1 or sorteio_id >= quant_sorteios):
                        raise Exception
                except:
                    print(f'Id Invalida!! {sorteio_id}')
                else:
                    break
            sorteio = servSorteio.get_sorteio(sorteio_id)
            print(f'Sorteio {sorteio_id}: Numero de Vencedores: {sorteio[1]}, Rodadas: {sorteio[2]}')  
        case 5:
            #case da Apuração e Premiação
            #Fase Apuração
            limpar_console()
            print('Execuntando o sorteio! BOA SORTE!')
            print(' ')
            premiacao.digitarValor()

            #If para verificar se apostou
            if len(vetor_apostas) == 0:
                vetor_apostas = servAposta.registrar_apostadores(100,id_sorteio)
            else:
                vetor_apostas.extend(servAposta.registrar_apostadores(100,id_sorteio))  

            servSorteio.sortear()

            #Pega todas as apostas e verifica quem ganhou
            servApuracao.verificarGanhadores(vetor_apostas)

            if servSorteio.getNumeroDeRodadas() < 15:
                print(f'Sorteio Terminado com {servSorteio.getNumeroDeRodadas()} RODADAS QUE RAPIDO!!')
            else:
                print(f'Desculpe a demora, chegamos no final em {servSorteio.getNumeroDeRodadas()} rodadas...')

            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            print(f'Numeros Sorteados: {servSorteio.lista_de_num_sorteados()}')
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

            #Verifica se a algum ganhador depois das rodadas
            num_ganhadores = len(servApuracao.apuracao.ganhadores)
            if num_ganhadores == 0:
                print('Nao a Ganhadores :(')
            else:
                print(f'Quantidade de Ganhadores: {num_ganhadores}')
                print(' ')
                print('Aposta(s) do(s) Ganhador(es): ')

                #Imprimi Ganhadores
                for a in servApuracao.lista_das_apostas_ganhadoras_em_ordem():
                    if isinstance(a,Apostas.Aposta):                     
                        print(f'Nome: {a.nome} - {a.numeros}')
                        if a == apostaUsuario:
                            premiacao.notficacao_premio(True,num_ganhadores)       
                    print(' ')

                #Fase Premiação################################
                premiacao.notficacao_premio(False,num_ganhadores)                       
                ################################################  

            servSorteio.update_sorteio(id_sorteio, num_ganhadores, servSorteio.getNumeroDeRodadas())        

            #Zera rodadas para o próximo sorteio         
            servSorteio.sorteio.rodadas = 0
            veti = servApuracao.maior_ao_menor_num_aparecido(vetor_apostas)

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
    #elif op == 5:
    #    servAposta.delecao_de_tabelas()
    #    servSorteio.delecao_de_tabela_sorteio()
    #    limpar_console()
    #    break

# Fechar conexão com o banco de dados
servAposta.fechar_banco()


