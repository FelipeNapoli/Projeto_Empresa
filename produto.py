import os
from colorama import Fore, Style, init
from rich import print
from rich.panel import Panel
from rich import box
from rich.table import Table

init(autoreset=True)

txt = "produtos.txt"    

def cadastro_produto():

    print(Panel(
        "Cadastro de Produto", 
        box= box.DOUBLE, 
        width= 50, 
        padding= (0, 14), 
        border_style="green3")
        )

    print()

    while True:
        try:
            nome = input(Fore.MAGENTA + Style.BRIGHT + "\nNome do produto: ").strip().title()

            if not nome:
                raise ValueError
            
            if not nome.replace(" ", "").isalpha():
                raise ValueError
            
            break

        except ValueError:
            print()
            print(Panel(
                "[bright_red]Nome Inválido![/]",
                box=box.ROUNDED,
                expand= False,
                width=80,
                border_style="red",
            ))
            print()
            print()
    print()

    while True:

        try:
            preco = float(input(Fore.MAGENTA + Style.BRIGHT + "Preço do produto: R$ ").strip().replace("," , "."))

            if preco <= 0:
                raise ValueError

            break

        except ValueError:
            print()
            print(Panel(
                "[bright_red]Preço Inválido![/]",
                box=box.ROUNDED,
                expand= False,
                width=80,
                border_style="red",
            ))
            print()
            print()
    print()


    while True:

        try:
            quantidade = int(input(Fore.MAGENTA + Style.BRIGHT +"Informe a quantidade do produto: "))

            if quantidade <= 0:
                raise ValueError

            break

        except ValueError:
            print()
            print(Panel(
                "[bright_red]Quantidade Inválido![/]",
                box=box.ROUNDED,
                expand= False,
                width=80,
                border_style="red",
            ))
            print()
            print()
    print()

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

                    nome_cadastrado, _ , _ = dados

                    if nome_cadastrado.lower() == nome.lower():
                        raise ValueError

        with open(txt, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome};{preco:.2f};{quantidade}\n")

        print(Panel(
            "Produto cadastrado com sucesso", 
            box= box.DOUBLE, 
            width= 50, 
            padding= (0, 8), 
            border_style="bright_green")
        )

        print()
        print(f"[orange3]Nome:[/] {nome}")
        print()
        print(f"[orange3]Preço:[/] R$ {preco:.2f}")
        print()
        print(f"[orange3]Quantidade:[/] {quantidade}")
        print()

    except OSError:
        print()
        print(Panel(
            "[bright_red]Não foi possivel cadastrar o produto![/]",
            box=box.ROUNDED,
            expand= False,
            border_style="red",
        ))
        print()
        print()
    print()

def listar_produto():
    try:
        if os.path.exists(txt):
            with open(txt, "r", encoding = "utf-8") as arquivo:
                produto = arquivo.readlines()

            if produto:   
                produto.sort()

                print(Panel(
                    "Listar Produto", 
                    box= box.DOUBLE, 
                    width= 80, 
                    padding= (0, 32), 
                    border_style="dodger_blue3")
                 )

                print()


                tabela = Table(
                    caption = "EMPRESA+",
                    caption_style= "dim italic #000a9b",
                    title_style = "bold white on dark_blue",
                    border_style="bright_blue",
                    box = box.ROUNDED,
                    style = "cyan",
                    width = 80,
                    show_lines= True
                )

                tabela.add_column("NOME", justify = "center", style="bold white")
                tabela.add_column("PREÇO", justify = "center", style="italic magenta")
                tabela.add_column("QUANTIDADE", justify = "center", style="yellow")

                for prod in produto:
                    dados = prod.strip().split(";")
                    nome, preco, qtd = dados

                    tabela.add_row(nome, preco, qtd)

                print(tabela)
                print()

            else:
                raise FileNotFoundError

        else:
            raise FileNotFoundError
            
    except FileNotFoundError:
        print(Panel(
            "[bright_red]Nenhum Produto Cadastrado[/]",
            expand = False,
            title_align= "center",
            border_style= "red",
            width = 80
        ))

def excluir_produto():

    while True:
        try:
            global txt
            if os.path.exists(txt):
                with open(txt, "r", encoding = "utf-8") as arquivo:
                    produtos = arquivo.readlines()

            if produtos:
                produtos.sort()

                print(Panel(
                    "Exclusão de Produtos", 
                    box= box.DOUBLE, 
                    width= 80, 
                    padding= (0, 28), 
                    border_style="bright_red")
                )

                print()


                tabela = Table(
                        caption = "EMPRESA+",
                        caption_style= "dim italic #000a9b",
                        title_style = "bold white on dark_red",
                        border_style="bright_red",
                        box = box.ROUNDED,
                        style = "bright_red",
                        width = 80,
                        show_lines= True
                    )

                tabela.add_column("NOME", justify = "center", style="bold white")
                tabela.add_column("PREÇO", justify = "center", style="italic magenta")
                tabela.add_column("QUANTIDADE", justify = "center", style="yellow")

                for produto in produtos:
                    dados = produto.strip().split(";")
                    nome, preco, qtd = dados

                    tabela.add_row(nome, preco, qtd)

                print(tabela)
                print()

            else:
                raise FileNotFoundError

            
            dados = []
            with open(txt, "r", encoding= "utf-8") as arquivo:
                dados = arquivo.readlines()

            while True:
                try:
                    nome = input("Digite o nome do produto para excluí-lo: ").strip().title()

                    if not nome.replace(" ", "").isalpha():

                        raise NameError

                    else:
                        for n in dados:
                            if n.startswith(nome + ";"):
                                break

                        else:
                            raise NameError

                        break

                except NameError:
                    print(Panel(
                        "[bright_red]Produto não encontrado[/]",
                        expand = False,
                        title_align= "center",
                        border_style= "red",
                        width = 80
                        ))

            with open(txt, "w", encoding = "utf-8") as arquivo:
                for n in dados:
                    if not n.startswith(nome + ";"):
                        arquivo.write(n)

            print()
            print()
            print(
                Panel(
                    "[bright_green]Produto Excluido com Sucesso[/]", 
                    expand= False,
                    title_align="center",
                    border_style="green3"
                )
            )
            break        
        except FileNotFoundError:
            print(Panel(
                "[bright_red]Nenhum Produto Cadastrado[/]",
                expand = False,
                title_align= "center",
                border_style= "red",
                width = 80
            ))
            break
        
def menu_cliente():
    while True:
        try:
            print(
                Panel(
                    "[bright_gray]PRODUTO[/]",
                    border_style = "gold3",
                    width = 40,
                    padding = (0, 15)
                ))
            print()
            
            print(Panel(
    """
[chartreuse1][ 1 ] Cadastrar Produto[/]

[royal_blue1][ 2 ] Listar Produto[/]

[indian_red1][ 3 ] Excluir Produto[/]
    """,
                box = box.ROUNDED,
                border_style= "gold3",
                padding= (1, 6),
                width = 40,
                title = "[bright_white]CADASTRO[/]",
                subtitle = "[turquese1]Pressione 4 para sair[/]",
                subtitle_align= "right",

        ))

            resp = int(input())

            match resp:
                case 1:
                    cadastro_produto()

                case 2:
                    listar_produto()

                case 3:
                    excluir_produto()

                case 4:
                    break

                case _:
                    raise ValueError
                
        except ValueError:
            print()
            print(Panel(
                "[bright_red]Opção Inválida![/]", 
                box=box.ROUNDED, 
                expand = False, 
                width = 80,
                border_style="red",
                )
            )
            print()
            print()

        
menu_cliente()