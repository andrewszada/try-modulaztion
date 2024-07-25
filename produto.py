import os 
import validador
import pickle


def limpar_tela():
 os.system('cls' if os.name == 'nt' else 'clear')

produtos = {}
try:  
  arq_produtos = open("produtos.dat", "rb")
  produtos = pickle.load(arq_produtos)
except:
  arq_produtos = open("produtos.dat", "wb")
  arq_produtos.close()

def modulo_produto():
    op_produto = ''
    while op_produto != '0':
        limpar_tela()
        print("_______________________________________")
        print("_______           Módulo Produto_______")
        print("_______________________________________")         
        print("____  1 - Cadastrar Produto       _____")
        print("_____ 2 - Exibir Dados do Produto _____")
        print("_____ 3 - Alterar Dados do Produto ____")
        print("_____ 4 - Excluir Produto         _____")
        print("_____ 0 - Sair                    _____")
        op_produto = input("##### Escolha sua opção: ")
        
        if op_produto == '1':
            cadastrar_produtos()
        elif op_produto == '2':
            exibir_produtos()
        elif op_produto == '3':
            alterar_produtos()
        elif op_produto == '4':
            excluir_produtos()

def cadastrar_produtos():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____        Cadastrar Produto         _____")
    print("____________________________________________")
    print()
    id = len(produtos) + 1
    nome_do_produto = input("Qual é o nome do produto desejado? ")
    while not validador.validar_nome(nome_do_produto):
        print("Nome de produto inválido. Por favor, insira apenas letras e espaços.")
        nome_do_produto = input("Qual o nome do produto ")
    else:
        print("Nome válido")
    
    quantidade_do_produto = input("Qual a quantidade do produto desejada: ")
    while not validador.aceitar_apenas_digitos(quantidade_do_produto):
        print("Nome de produto inválido, digite novamente")
        quantidade_do_produto = input("Qual a quantidade do produto desejada? ")
    else:
        print("Nome de produto válido")
    
    valor_produto = input("Qual será o valor desse produto? ")
    while not validador.aceitar_apenas_digitos(valor_produto):
        print("Digite apenas números")
        valor_produto = input("Qual será o valor desse produto ")
    else:
        print("Valor válido")

    produtos[id] = [nome_do_produto, quantidade_do_produto, valor_produto]

def exibir_produtos():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____         Exibir Dados do Produtos  _____")
    print("____________________________________________")
    print()
    id = input("Digite o id do produto: ")
    if id in produtos:
        print("Nome:", produtos[id][0])
        print("Endereço:", produtos[id][1])
        print("Telefone:", produtos[id][2])
        print("Produtos de Interesse:", produtos[id][3])
        print("Método de Pagamento:", produtos[id][4])
    else:
        print("Cliente não encontrado.")
    input("Pressione ENTER para continuar...")

def alterar_produtos():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____        Alterar Dados do Produto  _____")
    print("____________________________________________")
    print()
    id = input("Digite o id do cliente: ")
    if id in produtos:
        print("Informe os novos dados do(a) produto: ")
        nome_do_produto = input("Nome do produto : ")
        while not validador.validar_nome(nome_do_produto):
            print("Nome inválido. Por favor, insira apenas letras e espaços.")
            nome_do_produto = input("Qual o nome do produto?")
        else:
            print("Nome válido")
        print()
        quantidade_do_produto = input("Qual a quantidade do produto desejada: ")
        while not validador.aceitar_apenas_digitos(quantidade_do_produto):
            print("Nome de produto inválido, digite novamente")
            quantidade_do_produto = input("Qual a quantidade do produto desejada? ")
        else:
           print("Nome de produto válido")

        valor_produto = input("Qual será o valor desse produto? ")
        while not validador.aceitar_apenas_digitos(valor_produto):
            print("Digite apenas números")
            valor_produto = input("Qual será o valor desse produto ")
        else:
            print("Valor válido")
        produtos[id] = [nome_do_produto, quantidade_do_produto, valor_produto]
        print ("Informações de produto alterados com sucesso ")    

def excluir_produtos():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____        Excluir Produto           _____")
    print("____________________________________________")
    print()
    id = input("Digite o id do produto que deseja excluir: ")
    if id in produtos:
        del produtos[id]
        print("Produto excluído com sucesso.")
    else:
        print("Produto não encontrado.")
    input("Pressione ENTER para continuar...")   

arq_produtos = open("produtos.dat", "wb")
pickle.dump(produtos, arq_produtos)  
arq_produtos.close()
