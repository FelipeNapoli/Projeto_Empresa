from rich import print
from rich.panel import Panel
from rich.table import Table
from rich import box

arquivo = "clientes.txt"

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
            nome = input(" ")

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
            email = input(" ")
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
            telefone = input(" ")
            digitos = telefone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

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
    
cadastro_cliente()