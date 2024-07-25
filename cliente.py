import os 
import validador
import pickle

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

clientes = {}
try:
  arq_clientes = open("clientes.dat", "rb")
  clientes = pickle.load(arq_clientes)
except:
  arq_clientes = open("clientes.dat", "wb")
  arq_clientes.close()

def modulo_cliente():
    limpar_tela()
    print("_______________________________________")
    print("_______           Módulo Cliente _______")
    print("_______________________________________")         
    print("____  1 - Cadastrar Cliente       _____")
    print("_____ 2 - Exibir Dados do Cliente  ____")
    print("_____ 3 - Alterar Dados do Cliente ____")
    print("_____ 4 - Excluir Cliente         _____")
    print("_____ 0 - Sair                    _____")
    op_cliente = input("##### Escolha sua opção:  ")
    return op_cliente

def cadastrar_cliente():
    limpar_tela()
    print("____________________________________________")
    print("_____        Cadastrar Cliente         _____")
    print("____________________________________________")
    nome = input("Qual seria o seu nome completo? ")
    while not validador.validar_nome(nome):
        print("Nome inválido. Por favor, insira apenas letras e espaços.")
        nome = input("Qual o seu nome ")
    email = input("Qual o seu e-mail: ")
    while not validador.validar_email(email):
        print("Email inválido. Por favor, digite um email válido.")
        email = input("Qual o seu e-mail: ")
    endereço = input("Qual o seu endereço completo? ")
    while not validador.validar_endereço(endereço):
        print("Endereço inválido. Por favor, insira apenas letras e espaços.")
        endereço = input("Qual o seu endereço? ")
    telefone = input("Qual o seu número de telefone? ")
    while not validador.validar_telefone(telefone):
        print("Telefone inválido. Por favor, insira seu número corretamente (Use o travessão para separar o números)")
        telefone = input("Qual é o seu número de telefone? ")
    produtos_interesse = input("Qual seriam os tipos de produto que seriam de seu interesse? (Temos as opções de roupas, fraldas e brinquedos) ")
    metodo_pagamento = input("Qual seria o método de pagamento desejado? ")
    clientes[email] = [nome, endereço, telefone, produtos_interesse, metodo_pagamento]
    with open("clientes.dat", "wb") as arq_clientes:
        pickle.dump(clientes, arq_clientes)
    print(clientes)

def exibir_cliente():
    limpar_tela()
    print("____________________________________________")
    print("_____         Exibir Dados do Cliente  _____")
    print("____________________________________________")
    email = input("Digite o email do cliente: ")
    if email in clientes:
        print("Nome:", clientes[email][0])
        print("Endereço:", clientes[email][1])
        print("Telefone:", clientes[email][2])
        print("Produtos de Interesse:", clientes[email][3])
        print("Método de Pagamento:", clientes[email][4])
    else:
        print("Cliente não encontrado.")
    input("Pressione ENTER para continuar...")

def alterar_cliente():
    limpar_tela()
    print("____________________________________________")
    print("_____        Alterar Dados do Cliente  _____")
    print("____________________________________________")
    email = input("Digite o email do cliente: ")
    if email in clientes:
        print("Informe os novos dados do(a) cliente: ")
        nome = input("Nome: ")
        while not validador.validar_nome(nome):
            print("Nome inválido. Por favor, insira apenas letras e espaços.")
            nome = input("Qual o seu nome ")
        endereço = input("Endereço: ")
        while not validador.validar_endereço(endereço):
            print("Endereço inválido. Por favor, insira apenas letras e espaços.")
            endereço = input("Qual o seu endereço? ")
        telefone = input("Celular: ")
        while not validador.validar_telefone(telefone):
            print("Telefone inválido. Por favor, insira seu número corretamente (Use o travessão para separar o números)")
            telefone = input("Qual é o seu número de telefone? ")
        produtos_interesse = input("Produtos de interesse: ")
        metodo_pagamento = input("Metodo de pagamento: ")
        clientes[email] = [nome, endereço, telefone, produtos_interesse, metodo_pagamento]
        with open("clientes.dat", "wb") as arq_clientes:
            pickle.dump(clientes, arq_clientes)
        print("Cliente alterado(a) com sucesso!")
    else:
        print("Cliente não encontrado.")
    input("Pressione ENTER para continuar...")

def excluir_cliente():
    limpar_tela()
    print("____________________________________________")
    print("_____        Excluir Cliente           _____")
    print("____________________________________________")
    email = input("Digite o email do cliente que deseja excluir: ")
    if email in clientes:
        del clientes[email]
        with open("clientes.dat", "wb") as arq_clientes:
            pickle.dump(clientes, arq_clientes)
        print("Cliente excluído com sucesso.")
    else:
        print("Cliente não encontrado.")
    input("Pressione ENTER para continuar...")
