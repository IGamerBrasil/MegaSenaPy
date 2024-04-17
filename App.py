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
# Data -     03/24/2024
###########################################


servSorteio = ServicoSorteio.ServicoSorteio()
servAposta = ServicoApostas.ServicoApostas()
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

ja_registrado = True
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
    print('3 - Apuração e Premiação')	
    print('4 - Sair')
    print('5 - Deletar Tabelas')

# Loop do Menu
while True:
    if op > 5:
        limpar_console()
        print('Digite número de 1 a 5')
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

    #if para pegar as informações do usuário
    if op == 1:
        limpar_console()
        nome = input('Seu nome: ')
        
        while not re.match(r'^[a-zA-Z]*$', nome):
            print('Nome invalido!')
            nome = input('Seu nome: ')
                
        cpf = input('Seu CPF: ')
        
        #Loop para verificação de autenticação de CPF
        while len(cpf) != 11 or not re.match(r'^[0-9]*$', cpf):
             print('CPF invalido!')
             cpf = input('Seu CPF: ')
             
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
                        except:
                            print('Digite um numero de 1 a 50')
                        else:
                            servAposta.adicao_de_numeros(apostaUsuario, num)
                            break
                    
                servAposta.salvaNumeros(apostaUsuario)
                
                limpar_console()  
                
                print('APOSTADO!!')
                break
    #if para mostrar caso tenha alguma aposta guardada no banco de dados  
    elif op == 2:
        limpar_console()
        if apostaUsuario is not None:
            
            apostas = servAposta.visualizador_numeros_apostados_por_cpf(apostaUsuario.cpf)
            
            if not apostas:
                print('Não há apostas registradas.')
            else:
                print('Apostas do Sorteio atual:')
                
                for row in apostas:
                    if row[0] != None:
                        if isinstance(row[0], int):
                            if row[0] >= id_inicial:
                                print(f'Aposta {row[0]} - Numeros: {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}')
    #if da Apuração e Premiação
    elif op == 3:
        #Fase Apuração
        limpar_console()
        print('Execuntando o sorteio! BOA SORTE!')
        print(' ')
        premiacao.digitarValor()

        #If para verificar se apostou
        if len(vetor_apostas) == 0:
            print('nao apostou')
            vetor_apostas = servAposta.registrar_apostadores(100,id_sorteio)
        else:
            print('apostou')
            vetor_apostas.extend(servAposta.registrar_apostadores(100,id_sorteio))  

        servSorteio.sortear()
        print(f'Len de Serv numerosSorteados {len(servSorteio.sorteio.numerosSorteados)}')
        
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

        print(f'ID sorteio {id_sorteio}')
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
    elif op == 4:
        break
    elif op == 5:
        servAposta.delecao_de_tabelas()
        servSorteio.delecao_de_tabela_sorteio()
        limpar_console()
        break

# Fechar conexão com o banco de dados
servAposta.fechar_banco()


