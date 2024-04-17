from Servicos import ServicoApostas
from Servicos import ServicoApuracao
from Modelos import Apostas
<<<<<<< HEAD
from Modelos import Premiacao

=======
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
import re
import os



##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################

#metodo que deixa mais limpo o terminal
def limpar_console():
    print(os.name)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

<<<<<<< HEAD
def menu():
=======
# Loop do menu

denovo = False
nome = ''
cpf = ''
op = 0
id_inicial = 0
apostaUsuario = None
vetor_apostas = []
<<<<<<< HEAD
usuarioGanha = False
=======
usuarioVence = False
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
# Loop do Menu
while True:
    if op > 4:
        limpar_console()
        print('Digite número de 1 a 4')
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
    print('----------------------------------------------------------------')
    print('Menu')
    print('1 - Apostar')
    print('2 - Ver minhas apostas')
    print('3 - Apuração e Premiação')	
    print('4 - Sair')
    print('5 - Deletar Tabelas')
    
    
servAposta = ServicoApostas.ServicoApostas()
servApuracao = ServicoApuracao.ServicoApuracao()
premiacao = Premiacao.Premiacao()

servAposta.criacao_de_tabelas()

nome = ''
cpf = ''

op = 0
id_inicial = 0
numParticipantes = 100

ja_registrado = False

apostaUsuario = None
vetor_apostas = []

# Loop do Menu
while True:
    if op > 4:
        limpar_console()
        print('Digite número de 0 a 4')
        
    menu()
    
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
        if not ja_registrado:
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
            ja_registrado = True
        apostaUsuario = servAposta.registro_usuario(cpf,nome)
        
            
        #Loop para caso não ponha as informações corretas o usuário não sai ate por corretamente
        while True:
            limpar_console()
            menu()
            surpresa = input('Surpresa? (s/n): ').lower()
            
            if surpresa=='s':
                servAposta.sist_surpresa(apostaUsuario)
<<<<<<< HEAD
                vetor_apostas.append(apostaUsuario)
                
                limpar_console()
                print('APOSTADO!!') 
        
=======
                limpar_console()
                print('APOSTADO!!') 
                
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
                break 
            elif surpresa=='n':
                
                for _ in range(5):
<<<<<<< HEAD
                    while True:
                        try:
                            num = int(input('Digite um numero: '))
                            if num < 1 or num > 50:
                                raise Exception
                        except:
                            print('Digite um numero de 1 a 50')
                        else:
                            servAposta.adicao_de_numeros(apostaUsuario, num)
                            break
                    
                servAposta.salvaNumeros(apostaUsuario)
                
<<<<<<< HEAD
=======
                limpar_console()  
                
=======
                    num = int(input('Digite um numero: '))
                    servAposta.adicao_de_numeros(apostaUsuario, num)
                    
                servAposta.salvaNumeros(apostaUsuario)
                
                vetor_apostas.append(apostaUsuario)
                
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
                limpar_console()  
                   
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
                print('APOSTADO!!')
                break
    #if para mostrar caso tenha alguma aposta guardada no banco de dados  
    elif op == 2:
        limpar_console()
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
        
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
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
<<<<<<< HEAD
        premiacao.digitarValor()

        #If para verificar se apostou
<<<<<<< HEAD
        if len(vetor_apostas) == 0:
            vetor_apostas = servAposta.registrar_apostadores(numParticipantes)
=======
        if len(vetor_apostas) == 0:
            vetor_apostas = servAposta.registrar_apostadores(5)
        else:
            vetor_apostas.extend(servAposta.registrar_apostadores(5))  

        servApuracao.sortear()
        
        #Pega todas as apostas e verifica quem ganhou
        servApuracao.verificarGanhadores(vetor_apostas)
=======
        
        #Caso queira fazer manualmente a inserção de apostadores sem aleatorização apague os itens abaixo
        if len(vetor_apostas) == 0:
            vetor_apostas == servAposta.registrar_apostadores(100)
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
        else:
            vetor_apostas.extend(servAposta.registrar_apostadores(numParticipantes))  

        servApuracao.sortear()
        
<<<<<<< HEAD
        #Pega todas as apostas e verifica quem ganhou
        servApuracao.verificarGanhadores(vetor_apostas)
=======
        #Pega todas as apostas e verifica quem venceu
        servApuracao.verificarVencedores(vetor_apostas)
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
        
        if servApuracao.sorteio.rodadas < 15:
            print(f'Sorteio Terminado com {servApuracao.sorteio.rodadas} RODADAS QUE RAPIDO!!')
        else:
            print(f'Desculpe a demora, chegamos no final em {servApuracao.sorteio.rodadas} rodadas...')
            
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'Numeros Sorteados: {servApuracao.lista_de_num_sorteados()}')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
        #Verifica se a algum ganhador depois das rodadas
        t_apuracao = len(servApuracao.apuracao.ganhadores)
        if t_apuracao == 0:
            print('Nao a Ganhadores :(')
<<<<<<< HEAD
        else:
            print(f'Quantidade de Ganhadores: {t_apuracao}')
=======
        else:
            print(f'Quantidade de Ganhadores: {t_apuracao}')
            print(' ')
            print('Aposta(s) do(s) Ganhador(es): ')
            
            #Imprimi Ganhadores
            l = len(servApuracao.lista_das_apostas_ganhadoras_em_ordem()) 
            for a in servApuracao.lista_das_apostas_ganhadoras_em_ordem():
                if isinstance(a,Apostas.Aposta):                     
                    print(f'Nome: {a.nome} - {a.numeros}')
                    if a == apostaUsuario:
                        premiacao.notficacao_premio(True,l)       
                print(' ')
            #Fase Premiação################################
            premiacao.notficacao_premio(False,l)                        
            ################################################  
        
        #Zera rodadas para o próximo sorteio         
        servApuracao.sorteio.rodadas = 0
=======
        #Verifica se a algum vencedor depois das rodadas
        if len(servApuracao.apuracao.vencedores) == 0:
            print('Nao a Vencedores :(')
        else:
            print(f'Quantidade de Vencedores: {len(servApuracao.apuracao.vencedores)}')
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
            print(' ')
            print('Aposta(s) do(s) Ganhador(es): ')
            
<<<<<<< HEAD
            #Imprimi Ganhadores
            l = len(servApuracao.lista_das_apostas_ganhadoras_em_ordem()) 
            for a in servApuracao.lista_das_apostas_ganhadoras_em_ordem():
                if isinstance(a,Apostas.Aposta):                     
                    print(f'Nome: {a.nome} - {a.numeros}')
=======
            #Imprimi vencedores
            for a in servApuracao.lista_das_apostas_vencedoras_em_ordem():
                if isinstance(a,Apostas.Aposta):
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
                    if a == apostaUsuario:
                        premiacao.notficacao_premio(True,l)       
                print(' ')
<<<<<<< HEAD
            #Fase Premiação################################
            premiacao.notficacao_premio(False,l)                        
            ################################################  
        
        #Zera rodadas para o próximo sorteio         
        servApuracao.sorteio.rodadas = 0
=======
                #Fase Premiação################################
                if usuarioVence:
                    print(f'PARAEBNS!!! VOCE FOI UM DOS SORTUDOS A VENCER NOSSO SORTEIO!!!! ')
                    print(f'Porem como a empresa esta com baixo orcamento e funcionario .... apenas te daremos congratulacoes.')
                else:
                    print(f'ALGUEM VENCEU UM DOS NOSSOS SORTEIOS!!!! ')
                    print(f'Porem como a empresa esta com baixo orcamento e funcionario .... apenas daremos congratulacoes.')
                ################################################  
        
        #Zera rodadas para o próximo sorteio         
        servApuracao.sorteio.rodadas = 0
        
>>>>>>> ad823e647dc7626f514778a57775029a54207a51
>>>>>>> 93286719b22bec5bbdb9e392a7e182bd55bbd23c
        veti = servApuracao.maior_ao_menor_num_aparecido(vetor_apostas)
        
        if isinstance(veti, dict):
            #Ordena em ordem decrecente
            vetf = sorted(veti.items(), key=lambda x: x[1], reverse=True)
        
        print('---------------------------------------')
        print('| Nros Apostados       Qntde de Apostas|')
        for i,j in vetf:
            print(f'|  {i}                            {j}   |') 
        print('------------------------------------')
     
        break
    elif op == 4:
        break
    elif op == 5:
        servAposta.delecao_de_tabelas()
        print('Tabelas deletadas!')
        break

# Fechar conexão com o banco de dados
servAposta.fechar_banco()


