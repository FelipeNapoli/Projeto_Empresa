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
            telefone = input("Digite seu numero de telefone: ")
            digitos = telefone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

            if not (10 <= len(digitos) <= 12):
                raise ValueError

            else:
                break

        except ValueError:
            print("Numero de telefone inválido")