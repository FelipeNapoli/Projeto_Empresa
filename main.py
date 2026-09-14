from cliente import *
from produto import *

while True:
    try:
        print(
            Panel(
                "[bright_gray]EMPRESA+[/]",
                border_style = "deep_pink1",
                width = 40,
                padding = (0, 15)
            
            ))
        
        print()
        
        print(Panel(
    """
    [light_goldenrod2][ 1 ] Menu Produtos[/]

    [royal_blue1][ 2 ] Menu Cliente[/]
    """,
                box = box.ROUNDED,
                border_style= "deep_pink1",
                padding= (1, 5),
                width = 40,
                title = "[bright_white]CADASTRO[/]",
                subtitle = "[deep_pink1]Pressione 3 para sair[/]",
                subtitle_align= "right",

    ))

        resp = int(input(" "))


        match resp:
            case 1:
                print()
                menu_produto()
                print()
            case 2:
                print()
                menu_cliente()
                print()

            case 3:
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
