import os

ARQUIVO = "produtos.txt"    

def cadastro_produto():
    print("\n --- CADASTRAR PRODUTO---")

    while True:

        nome = input("Nome do produto: ").strip()

        if not nome:
            print("Nome inválido. Tente novamente")
            continue

        if not nome.isalpha():
            print("Nome inválido. Digite apenas letras.")
            continue

        break