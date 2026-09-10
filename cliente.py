arquivo = "clientes.txt"

def cadastro_cliente():
    while True:
        try:
            nome = input("Digite seu nome: ")

        except ValueError:
            print("Nome inválido, tente novamente")