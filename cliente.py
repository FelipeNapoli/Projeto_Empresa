arquivo = "clientes.txt"

def cadastro_cliente():
    while True:
        try:
            nome = input("Digite seu nome: ")

            if not nome:
                raise ValueError

            elif not nome.replace(" ","").isalpha():
                raise ValueError

            else:
                break

        except ValueError:
            print("Nome inválido, tente novamente")

    while True:
        try:
            email = input("Digite o email: ")
            if not "@" in email:
                raise ValueError

            else:
                break

        except ValueError:
            print("Email inválido")