arquivo = "clientes.txt"

def cadastro_cliente():
    while True:
        try:
            nome = input("Digite seu nome: ")

            if not nome:
                raise ValueError

            elif not nome.replace(" ","").isalpha():
                raise ValueError

        except ValueError:
            print("Nome inválido, tente novamente")