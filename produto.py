import os

ARQUIVO = "produtos.txt"    

def cadastro_produto():
    print("\n --- CADASTRAR PRODUTO ---")

    while True:

        nome = input("Nome do produto: ").strip()

        if not nome:
            print("Nome inválido. Tente novamente")
            continue

        if not nome.replace(" ", "").isalpha():
            print("Nome inválido. Digite apenas letras.")
            continue

        break

    while True:

        try:
            preco = float(input("Preço do produto: R$ ").strip().replace("," , "."))

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

def listar_produto():
    print("\n --- PRODUTOS CADASTRADOS ---")

    if not os.path.exists(ARQUIVO):
        print("Nenhum produto cadastrado.")
        return

    try:
        produtos = []

        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                linha = linha.strip()

                if not linha:
                    continue

                dados = linha.split(";")

                if len(dados) != 3:
                    print("Existe uma linha inválida no arquivo!")
                    return

                nome, preco, quantidade = dados

                preco = float(preco)
                quantidade = int(quantidade)

                produtos.append((nome, preco, quantidade))

            if not produtos:
                        print("Nenhum produto cadastrado.")
                        return

            print(f"{'NOME':<25} {'PREÇO':<12} {'QUANTIDADE':<12}")
            print("-" * 48)

            for nome, preco, quantidade in produtos:
                print(
                    f"{nome:<25}"
                    f"R$ {preco:<9.2f}"
                    f"{quantidade:<12}"
                )

    except (OSError, ValueError):
        print("Não foi possível ler os produtos cadastrados.")

def excluir_produto():

    print("\n --- EXCLUIR PRODUTO ---")

    if not os.path.exists(ARQUIVO):
        print("Nenhum produto cadastrado.")
        return

    nome_excluir = input("Digite o nome do produto que deseja excluir.").strip()

    if not nome_excluir:
        print("Nome inválido.")
        return

    if not nome_excluir.replace(" ", "").isalpha():
        print("Nome inválido. Digite apenas letras.")
        return

    try:
        produtos = []
        encontrado = False

        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:

                linha = linha.strip()

                if not linha:
                    continue

                dados = linha.split(";")

                if len(dados) != 3:
                    print("Existe uma linha inválida no arquivo!")
                    return

                nome, preco, quantidade = dados

                if nome.lower() == nome_excluir.lower():
                    encontrado = True
                    continue

                produtos.append(linha)

            if not encontrado:
                print("Produto não encontrado.")
                return

            with open(ARQUIVO, "w", encoding = "utf-8") as arquivo:
                for produto in produtos:
                    arquivo.write(produto + "\n")

            print(" === PRODUTO EXCLUÍDO ===")
            print("Produto excluído com sucesso!")

    except OSError:
        print("Não foi possível excluir o produto")