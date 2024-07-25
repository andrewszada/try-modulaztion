import re
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_email(email):
    
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(padrao, email))


def validar_nome(nome):
    # Esta função verifica se o nome contém apenas letras e espaços
    if nome.replace(" ", "").isalpha():
        return True
    else:
        print("Nome inválido. Por favor, insira apenas letras e espaços.")
        return False
    
def validar_endereço(endereço):
    # Esta função verifica se o nome contém apenas letras e espaços
    if endereço.replace(" ", "").isalpha():
        return True
    else:
        print("Endereço inválido. Por favor, insira apenas letras e espaços.")
        return False
    
def validar_telefone(numero):
    # Define o padrão para o número de telefone
    padrao = re.compile(r'^\(\d{2}\) 9\d{4}-\d{4}$')
    
    # Verifica se o número corresponde ao padrão
    if padrao.match(numero):
        return True
    else:
        return False
    
def aceitar_apenas_digitos(*args):
    if not isinstance(int):
        return False
    else:
        return True
    
def acesso_admin():
    login = input("Qual é o login? ")
    senha = input("Qual é a senha? ")
    if login == 'andrews' and senha == 'projeto':
        return True
    else:
        return False
