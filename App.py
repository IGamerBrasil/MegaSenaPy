from Servicos import ServicoApostas
from Servicos import ServicoApuracao
from Apostas import Apostas
import re
import os


servAposta = ServicoApostas.ServicoApostas()
servApuracao = ServicoApuracao.ServicoApuracao()

servAposta.criacao_de_tabelas()

def limpar_console():
    print(os.name)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
        
letras_grandes = {
    "A": ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
    "B": ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
    "C": [" CCC ", "C   C", "C    ", "C   C", " CCC "],
    # Adicione mais letras conforme necessário
}

def print_letras_grandes(texto):
    for linha in range(5):  # 5 linhas para cada letra
        linha_grande = ""
        for letra in texto:
            linha_grande += letras_grandes.get(letra.upper(), [""]*5)[linha] + "  "  # Obtém a representação da letra grande
        print(linha_grande)

# Loop do menu

denovo = False
nome = ''
cpf = ''
op = 0
aposta = None
vetor_apostas = []
while True:
    print('----------------------------------------------------------------')
    print('Menu')
    print('1 - Apostar')
    print('2 - Ver minhas apostas')
    print('3 - Finalizar e apurar resultado')
    print('4 - Sair')
    try:
        op = int(input('Opção: '))
    except Exception:
        print('Valor digitado nao eh um numero!')

    if op == 1:
        nome = input('Seu nome: ')
        while not re.match(r'^[a-zA-Z]*$', nome):
            print('Nome invalido!')
            nome = input('Seu nome: ')    
        cpf = input('Seu CPF: ')
        while len(cpf) != 11 or not re.match(r'^[0-9]*$', cpf):
             print('CPF invalido!')
             cpf = input('Seu CPF: ')
        aposta = servAposta.registro_usuario(cpf,nome)
        surpresa = input('Surpresa? (s/n): ').lower()
        if surpresa=='s':
            servAposta.sist_surpresa(aposta)
        elif surpresa=='n':
            for _ in range(5):
                num = int(input('Digite um numero: '))
                servAposta.adicao_de_numeros(aposta, num)
            servAposta.salvaNumeros(aposta)
            vetor_apostas.append(aposta)        
            
        #servAposta.resetar_vetor(aposta)
        limpar_console()
    elif op == 2:
        limpar_console()
        if aposta is not None:
            apostas = servAposta.visualizador_numeros_apostados_por_cpf(aposta.cpf)
            if not apostas:
                print('Não há apostas registradas.')
            else:
                for row in apostas:
                    print(f'Aposta {row[0]} - Numeros: {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}')
    elif op == 3:
        limpar_console()
        print('Execuntando o sorteio! BOA SORTE!')
        print(' ')
        vetor_apostas.append(servAposta.registrar_apostadores())
        servApuracao.sortear()
        servApuracao.verificarVencedores(vetor_apostas)
        if servApuracao.sorteio.rodadas < 15:
            print(f'Sorteio Terminado com {servApuracao.sorteio.rodadas} RODADAS QUE RAPIDO!!')
        else:
            print(f'Desculpe a demora, chegamos no final em {servApuracao.sorteio.rodadas} rodadas')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'Numeros Sorteados: {servApuracao.lista_de_sorteados()}')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        if len(servApuracao.apuracao.vencedores) == 0:
            print('Nao a Vencedores :(')
        else:
            print('VENCEDORES SAO:')
            print(len(servApuracao.apuracao.vencedores))
            for a in servApuracao.apuracao.vencedores:
                if isinstance(a,Apostas.Aposta):
                 print(f'{a.nome}')
            servApuracao.sorteio.rodadas = 0
        break
    elif op == 4:
        break

# Fechar conexão com o banco de dados
servAposta.fechar_banco()


