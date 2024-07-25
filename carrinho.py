import os 
def limpar_tela():
 os.system('cls' if os.name == 'nt' else 'clear')
carrinho = []

def modulo_carrinho():
    limpar_tela()
    total = sum(produto[2] for produto in carrinho)
    print(f"O total no seu carrinho é: {total}")
    finalizar_compra = input("Deseja finalizar a compra?")
    if finalizar_compra.upper() == "S":
        print("Compra finalizada com sucesso!")
        carrinho.clear()
    else:
        print("Compra não finalizada.")
    input("Pressione ENTER para continuar...")
