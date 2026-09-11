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
            nome = input(" Digite seu nome: ")

            if not nome:
                raise ValueError

            elif not nome.replace(" ","").isalpha():
                raise ValueError

            else:
                break

        except ValueError:
            print(" Nome inválido, tente novamente")

    print()

    while True:
        try:
            email = input(" Digite o email: ")
            if not "@" in email:
                raise ValueError

            else:
                break

        except ValueError:
            print(" Email inválido")

    print()        

    while True:
        try:
            telefone = input(" Digite seu numero de telefone: ")
            digitos = telefone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

            if not (10 <= len(digitos) <= 12):
                raise ValueError

            else:
                break

        except ValueError:
            print(" Numero de telefone inválido")
    

cadastro_cliente()