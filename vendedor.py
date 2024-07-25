from utils import limpar_tela

vendedores = {
    "premium": {"nome": "ANDRÉ BABY IMPORTS", "cargo": "Vendedor Premium", "vendas": "5000+ vendas"},
    "ceo": {"nome": "André Leandro de Medeiros Araújo", "idade": 33, "descricao": "Com mestrado em administração e gestão de negócios, atua no mercado de produtos infantis há 10 anos."}
}

def modulo_vendedor():
    op_vendedor = ''
    while op_vendedor != '0':
        limpar_tela()
        print("_______________________________________")
        print("_______           Módulo Vendedor _____")
        print("_______________________________________")
        print("____   1 - Informações do Vendedor ____")
        print("_____  2 - Informações do CEO     _____")
        print("_____  0 - Sair                   _____")
        op_vendedor = input("##### Escolha sua opção: ")
        
        if op_vendedor == '1':
            info_vendedor()
        elif op_vendedor == '2':
            info_ceo()

def info_vendedor():
    # Código da função aqui...

def info_ceo():
    # Código da função aqui...
