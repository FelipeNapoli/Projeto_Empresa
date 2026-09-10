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

    while True:
        try:
            telefone = int(input("Digite seu numero de telefone: "))

            if 10 > len(telefone) > 11:
                raise ValueError

            else:
                break

        except ValueError:
            print("Numero de telefone inválido")