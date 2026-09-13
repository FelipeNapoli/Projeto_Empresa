import os
from colorama import Fore, Style, init

init(autoreset=True)

def caixa(texto, cor=Fore.CYAN, largura=50):
    linhas = texto.split("\n")
    print(cor + "┌" + "─" * (largura - 2) + "┐")
    for linha in linhas:
        print(cor + "│" + Style.BRIGHT + linha.center(largura - 2) + Style.NORMAL + cor + "│")
    print(cor + "└" + "─" * (largura - 2) + "┘")


txt = "produtos.txt"    

def cadastro_produto():
    caixa("CADASTRAR PRODUTO", Fore.CYAN)

    while True:
        try:
            nome = input(Fore.MAGENTA + Style.BRIGHT + "\nNome do produto: ").strip().title()

            if not nome:
                raise ValueError
            
            if not nome.replace(" ", "").isalpha():
                raise ValueError
            
            break
        except ValueError:
            print(Fore.RED + "Nome inválido! Digite apenas letras.")

    while True:

        try:
            preco = float(input(Fore.MAGENTA + Style.BRIGHT + "Preço do produto: R$ ").strip().replace("," , "."))

            if preco <= 0:
                raise ValueError

            break

        except ValueError:
            print(Fore.RED + "Preço inválido! Digite somente números.")


    while True:

        try:
            quantidade = int(input(Fore.MAGENTA + Style.BRIGHT +"Informe a quantidade do produto: "))

            if quantidade <= 0:
                raise ValueError

            break

        except ValueError:
            print(Fore.RED + "Quantidade inválida! Digite um número inteiro.")

    try:
        if os.path.exists(txt):
            with open(txt, "r", encoding="utf-8") as arquivo:

                for linha in arquivo:

                    linha = linha.strip()

                    if not linha:
                        raise FileExistsError

                    dados = linha.split(";")

                    if len(dados) != 3:
                        raise FileExistsError

                    nome_cadastrado, _, _ = dados

                    if nome_cadastrado.lower() == nome.lower():
                        raise ValueError

        with open(txt, "a", encoding="utf-8") as arquivo:
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

    if not os.path.exists(txt):
        print(Fore.RED + "Nenhum produto cadastrado.")
        return

    try:
        produtos = []

        with open(txt, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                linha = linha.strip()

                if not linha:
                    raise FileNotFoundError

                dados = linha.split(";")

                if len(dados) != 3:
                    raise ValueError

                nome, preco, quantidade = dados

                preco = float(preco)
                quantidade = int(quantidade)

                produtos.append((nome, preco, quantidade))

            if not produtos:
                raise FileNotFoundError
            
            print(Fore.BLUE + Style.BRIGHT + f"{'NOME':<25} {'PREÇO':<12} {'QUANTIDADE':<12}")
            print(Fore.CYAN + "-" * 48)

            for nome, preco, quantidade in produtos:
                print(
                    Fore.WHITE + Style.BRIGHT + f"{nome:<25}"
                    + Fore.YELLOW + f"R$ {preco:<9.2f}"
                    + Fore.YELLOW + f"{quantidade:<12}"
                )

    except (OSError, ValueError, FileNotFoundError):
        print(Fore.RED + "Não foi possível ler os produtos cadastrados.")

def excluir_produto():

    while True:
        try:
            caixa("EXCLUIR PRODUTO", Fore.CYAN)

            if not os.path.exists(txt):
                raise FileNotFoundError

            nome_excluir = input(Fore.MAGENTA + Style.BRIGHT + "\nDigite o nome do produto que deseja excluir: ").strip().title()

            if not nome_excluir:
                raise ValueError

            elif not nome_excluir.replace(" ", "").isalpha():
                raise ValueError

       
            produtos = []
            encontrado = False

            with open(txt, "r", encoding="utf-8") as arquivo:

                for linha in arquivo:

                    linha = linha.strip()

                    if not linha:
                        raise FileNotFoundError

                    dados = linha.split(";")

                    if len(dados) != 3:
                        raise ValueError

                    nome, _, _ = dados

                    if nome.lower() == nome_excluir.lower():
                        encontrado = True
                        continue

                    produtos.append(linha)

            if not encontrado:
                raise ValueError

            with open(txt, "w", encoding="utf-8") as arquivo:

                for produto in produtos:
                    arquivo.write(produto + "\n")

            caixa("PRODUTO EXCLUÍDO", Fore.GREEN)
            print(Fore.GREEN + "Produto excluído com sucesso!")

            break

        except (OSError, FileNotFoundError, ValueError):
            print("Erro ao excluir produto!")

