from rich import print
from rich.panel import Panel
from rich.table import Table
from rich import box
import os

arquivo = r"clientes.txt"

def cadastro_cliente():
    print(Panel(
        "Cadastro de Cliente", 
        box= box.DOUBLE, 
        width= 50, 
        padding= (0, 14), 
        border_style="dodger_blue3")
        )

    print()

    while True:
        try:
            print(" [dodger_blue1]Digite seu nome: ")
            nome = input(" ").strip().title()

            if not nome:
                raise ValueError

            elif not nome.replace(" ","").isalpha():
                raise ValueError

            else:
                break

        except ValueError:
            print()
            print(Panel(
                "[dark_red]Nome Inválido[/]", 
                box=box.HORIZONTALS, 
                expand=False, 
                padding=(0, 2),
                border_style="red"
                )
            )
            print()

    print()

    while True:
        try:
            print(" [blue_violet]Digite o email: [/]")
            email = input(" ").lower().strip()
            if not "@" in email:
                raise ValueError

            else:
                break

        except ValueError:
            print()
            print(Panel(
                "[dark_red]Email Inválido[/]", 
                box=box.HORIZONTALS, 
                expand=False, 
                padding=(0, 2),
                border_style="red"
                )
            )
            print()

    print()        

    while True:
        try:
            print(" [medium_violet_red]Digite seu numero de telefone: [/]")
            telefone = input(" ").strip()
            digitos = telefone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

            int(digitos)

            if not (10 <= len(digitos) <= 12):
                raise ValueError

            else:
                break

        except ValueError:
            print()
            print(Panel(
                "[dark_red]Telefone Inválido[/]", 
                box=box.HORIZONTALS, 
                expand=False, 
                padding=(0, 2),
                border_style="red"
                )
            )

    with open(arquivo, "a", encoding="utf-8") as txt:
        txt.write(f"{nome.title()};{email.lower()};{telefone}\n")

    print()
    print()
    print(
        Panel(
            "Cliente Cadastrado com Sucesso", 
            expand= False,
            title_align="center",
            border_style="green3"
        )
    )
    print(f"\n [orange1]Nome:[/] {nome}\n\n [orange1]Email:[/] {email}\n\n [orange1]Telefone:[/] {telefone}")


def listar_clientes():
    try:
        print()
        print()
        print(Panel(
            "CLIENTES CADASTRADOS",
            box = box.DOUBLE,
            border_style = "bright_blue",
            width = 80,
            padding = (0, 29)
        ))

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
        tabela.add_column("EMAIL", justify = "center", style="italic magenta")
        tabela.add_column("TELEFONE", justify = "center", style="yellow")

        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding = "utf-8") as txt:
                clientes = txt.readlines()

            clientes.sort()

            for cliente in clientes:
                dados = cliente.strip().split(";")
                nome = dados[0]
                email = dados[1]
                telefone = dados[2]

                tabela.add_row(nome, email, telefone)

            print(tabela)
            print()

        else:
            raise FileNotFoundError
        
    except FileNotFoundError:
        print(Panel(
            "[dark_red]Nenhum Cliente Cadastrado[/]",
            expand = False,
            title_align= "center",
            border_style= "red",
            width = 80
        ))


def excluir_cliente():
    try:
        print()
        print()
        print(Panel(
            "EXCLUIR CLIENTES",
            box = box.DOUBLE,
            border_style = "bright_red",
            width = 80,
            padding = (0, 31)
        ))

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
        tabela.add_column("EMAIL", justify = "center", style="italic magenta")
        tabela.add_column("TELEFONE", justify = "center", style="yellow")

        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding = "utf-8") as txt:
                clientes = txt.readlines()

        clientes.sort()

        for cliente in clientes:
            dados = cliente.strip().split(";")
            nome = dados[0]
            email = dados[1]
            telefone = dados[2]

            tabela.add_row(nome, email, telefone)

        print(tabela)
        print()

        if os.path.exists(arquivo):
            dados = []
            with open(arquivo, "r", encoding= "utf-8") as txt:
                dados = txt.readlines()

        else:
            raise FileNotFoundError

        while True:
            try:
                nome = input("Digite o nome do aluno para excluí-lo: ").strip().title()

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
                    "[dark_red]Aluno não encontrado[/]",
                    expand = False,
                    title_align= "center",
                    border_style= "red",
                    width = 80
                    ))

        with open(arquivo, "w", encoding = "utf-8") as txt:
            for n in dados:
                if not n.startswith(nome + ";"):
                    txt.write(n)

        print()
        print()
        print(
            Panel(
                "Cliente Excluido com Sucesso", 
                expand= False,
                title_align="center",
                border_style="green3"
            )
        )
                
    except FileNotFoundError:
        print(Panel(
            "[dark_red]Nenhum Cliente Cadastrado[/]",
            expand = False,
            title_align= "center",
            border_style= "red",
            width = 80
        ))
