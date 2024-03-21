from Servicos import ServicoApostas
from Servicos import ServicoApuracao
from Modelos import Apostas
import re
import os



##########################################
# Programa - Sorteio
# Autor -    Lucas Candemil Chagas
# Data -     03/24/2024
###########################################


servAposta = ServicoApostas.ServicoApostas()
servApuracao = ServicoApuracao.ServicoApuracao()

servAposta.criacao_de_tabelas()

#metodo que deixa mais limpo o terminal
def limpar_console():
    print(os.name)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Loop do menu

denovo = False
nome = ''
cpf = ''
op = 0
id_inicial = 0
apostaUsuario = None
vetor_apostas = []
usuarioVence = False
# Loop do Menu
while True:
    if op > 4:
        limpar_console()
        print('Digite número de 1 a 4')
    print('----------------------------------------------------------------')
    print('Menu')
    print('1 - Apostar')
    print('2 - Ver minhas apostas')
    print('3 - Finalizar e apurar resultado')
    print('4 - Sair')
    
    #Salva primeiro id para quando for mostrar as apostas apenas mostre as do sorteio em execução
    if op == 0:
        id_inicial = servAposta.aBD.id
        
    #Verificação caso não seja um número
    try:
        op = int(input('Opção: '))
    except Exception:
        print('Valor digitado nao eh um numero!')

    #if para pegar as informações do usuário
    if op == 1:
        
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
        apostaUsuario = servAposta.registro_usuario(cpf,nome)
        
        #Loop para caso não ponha as informações corretas o usuário não possa continuar
        while True:
            
            surpresa = input('Surpresa? (s/n): ').lower()
            
            if surpresa=='s':
                servAposta.sist_surpresa(apostaUsuario)
                limpar_console()
                print('APOSTADO!!') 
                
                break 
            elif surpresa=='n':
                
                for _ in range(5):
                    num = int(input('Digite um numero: '))
                    servAposta.adicao_de_numeros(apostaUsuario, num)
                    
                servAposta.salvaNumeros(apostaUsuario)
                
                vetor_apostas.append(apostaUsuario)
                
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
        
        #Caso queira fazer manualmente a inserção de apostadores sem aleatorização apague os itens abaixo
        if len(vetor_apostas) == 0:
            vetor_apostas == servAposta.registrar_apostadores(100)
        else:
            vetor_apostas.extend(servAposta.registrar_apostadores(100))  
        ################################################################################################
        
        servApuracao.sortear()
        
        #Pega todas as apostas e verifica quem venceu
        servApuracao.verificarVencedores(vetor_apostas)
        
        if servApuracao.sorteio.rodadas < 15:
            print(f'Sorteio Terminado com {servApuracao.sorteio.rodadas} RODADAS QUE RAPIDO!!')
        else:
            print(f'Desculpe a demora, chegamos no final em {servApuracao.sorteio.rodadas} rodadas...')
            
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'Numeros Sorteados: {servApuracao.lista_de_num_sorteados()}')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        
        #Verifica se a algum vencedor depois das rodadas
        if len(servApuracao.apuracao.vencedores) == 0:
            print('Nao a Vencedores :(')
        else:
            print(f'Quantidade de Vencedores: {len(servApuracao.apuracao.vencedores)}')
            print(' ')
            print('Aposta(s) do(s) Vencedor(es): ')
            
            #Imprimi vencedores
            for a in servApuracao.lista_das_apostas_vencedoras_em_ordem():
                if isinstance(a,Apostas.Aposta):
                    if a == apostaUsuario:
                        usuarioVence = True
                    print(f'Nome: {a.nome} - {a.numeros}')    
                print(' ')
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

# Fechar conexão com o banco de dados
servAposta.fechar_banco()


