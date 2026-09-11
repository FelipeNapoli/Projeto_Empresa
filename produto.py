import os
from colorama import Fore, Style, init

init(autoreset=True)

def caixa(texto, cor=Fore.CYAN, largura=50):
    linhas = texto.split("\n")
    print(cor + "┌" + "─" * (largura - 2) + "┐")
    for linha in linhas:
        print(cor + "│" + Style.BRIGHT + linha.center(largura - 2) + Style.NORMAL + cor + "│")
    print(cor + "└" + "─" * (largura - 2) + "┘")

ARQUIVO = "produtos.txt"    

def cadastro_produto():
    caixa("CADASTRAR PRODUTO", Fore.CYAN)

    while True:

        nome = input(Fore.MAGENTA + Style.BRIGHT + "\nNome do produto: " + Style.RESET_ALL).strip()

        if not nome:
            print(Fore.RED + "Nome inválido. Tente novamente")
            continue

        if not nome.replace(" ", "").isalpha():
            print(Fore.RED +"Nome inválido. Digite apenas letras.")
            continue

        break

    while True:

        try:
            preco = float(input(Fore.MAGENTA + Style.BRIGHT + "Preço do produto: R$ ").strip().replace("," , "."))

            if preco <= 0:
                print(Fore.RED + "Preço inválido! Tente Novamente.")
                continue

            break

        except ValueError:
            print(Fore.RED + "Preço inválido! Digite somente números.")


    while True:

        try:
            quantidade = int(input(Fore.MAGENTA + Style.BRIGHT +"Informe a quantidade do produto: "))

            if quantidade <= 0:
                print(Fore.RED + "Quantidade inválida! Digite um número inteiro maior que zero.")

                continue

            break

        except ValueError:
            print(Fore.RED + "Quantidade inválida! Digite um número inteiro.")

    try:
        if os.path.exists(ARQUIVO):
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

                for linha in arquivo:

                    linha = linha.strip()

                    if not linha:
                        continue

                    dados = linha.split(";")

                    if len(dados) != 3:
                        print(Fore.RED + "Existe uma linha inválida no arquivo.")
                        return

                    nome_cadastrado, preco_cadastrado, quantidade_cadastrada = dados

                    if nome_cadastrado.lower() == nome.lower():
                        print(Fore.RED +"Esse produto já está cadastrado.")
                        return

        with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome};{preco:.2f};{quantidade}\n")

        caixa("PRODUTO CADASTRADO", Fore.GREEN)
        print(Fore.YELLOW + f"Nome: {Style.BRIGHT}{nome}")
        print(Fore.YELLOW + f"Preço: {Style.BRIGHT}R$ {preco:.2f}")
        print(Fore.YELLOW + f"Quantidade: {Style.BRIGHT}{quantidade}")
        print(Fore.GREEN + "Produto cadastrado com sucesso!")

    except OSError:
        print("Não foi possível cadastrar o produto")

def listar_produto():
    caixa("PRODUTOS CADASTRADOS", Fore.CYAN)

    if not os.path.exists(ARQUIVO):
        print(Fore.RED + "Nenhum produto cadastrado.")
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
                    print(Fore.RED + "Existe uma linha inválida no arquivo!")
                    return

                nome, preco, quantidade = dados

                preco = float(preco)
                quantidade = int(quantidade)

                produtos.append((nome, preco, quantidade))

            if not produtos:
                        print(Fore.RED + "Nenhum produto cadastrado.")
                        return

            print(Fore.BLUE + Style.BRIGHT + f"{'NOME':<25} {'PREÇO':<12} {'QUANTIDADE':<12}")
            print(Fore.CYAN + "-" * 48)

            for nome, preco, quantidade in produtos:
                print(
                    Fore.WHITE + Style.BRIGHT + f"{nome:<25}"
                    + Fore.YELLOW + f"R$ {preco:<9.2f}"
                    + Fore.YELLOW + f"{quantidade:<12}"
                )

    except (OSError, ValueError):
        print(Fore.RED + "Não foi possível ler os produtos cadastrados.")

def excluir_produto():

      while True:

        caixa("EXCLUIR PRODUTO", Fore.CYAN)

        if not os.path.exists(ARQUIVO):
            print(Fore.RED + "Nenhum produto cadastrado.")
            return

        nome_excluir = input(Fore.MAGENTA + Style.BRIGHT + "\nDigite o nome do produto que deseja excluir: ").strip()

        if not nome_excluir:
            print(Fore.RED + "Nome inválido.")
            continue

        if not nome_excluir.replace(" ", "").isalpha():
            print(Fore.RED +"Nome inválido. Digite apenas letras.")
            continue

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
                        print(Fore.RED + "Existe uma linha inválida no arquivo!")
                        return

                    nome, preco, quantidade = dados

                    if nome.lower() == nome_excluir.lower():
                        encontrado = True
                        continue

                    produtos.append(linha)

            if not encontrado:
                print(Fore.RED + "Produto não encontrado.")
                continue

            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

                for produto in produtos:
                    arquivo.write(produto + "\n")

            caixa("PRODUTO EXCLUÍDO", Fore.GREEN)
            print(Fore.GREEN + "Produto excluído com sucesso!")

            break

        except OSError:
            print(Fore.RED + "Não foi possível excluir o produto.")
            break

