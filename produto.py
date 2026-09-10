import os

ARQUIVO = "produtos.txt"    

def cadastro_produto():
    print("\n --- CADASTRAR PRODUTO---")

    while True:

        nome = input("Nome do produto: ").strip()

        if nome == "":
            print("O nome não pode ficar vazio.")
            continue

        if not nome:
            print("Nome inválido. Tente novamente")
            continue

        if not nome.isalpha():
            print("Nome inválido. Digite apenas letras.")
            continue

        break

    while True:

        try:
            preco = float(input("Preço do produto: R$")).strip().replace("," , ".")

            if preco <= 0:
                print("Preço inválido! Tente Novamente.")
                continue

            break

        except ValueError:
            print("Preço inválido! Digite somente números.")


    while True:

        try:
            quantidade = int(input("Informe a quantidade do produto: "))

            if quantidade <= 0:
                print("Quantidade inválida! Digite um número inteiro maior que zero.")

                continue

            break

        except ValueError:
            print("Quantidade inválida! Digite um número inteiro.")

    try:
        if os.path.exists(ARQUIVO):
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

                for linha in arquivo:

                    linha = linha.strip()

                    if not linha:
                        continue

                    dados = linha.split(";")

                    if len(dados) != 3:
                        print("Existe uma linha inválida no arquivo.")
                        return

                    nome_cadastrado, preco_cadastrado, quantidade_cadastrada = dados

                    if nome_cadastrado.lower() == nome.lower():
                        print("Esse produto já está cadastrado.")
                        return

        with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome};{preco:.2f};{quantidade}\n")

        print("== PRODUTO CADASTRADO ==")
        print("Produto cadastrado com sucesso!")

    except OSError:
        print("Não foi possível cadastrar o produto")