from motorista import Corrida
from motorista import Motorista
from motorista import Passageiro

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_dao):
        super().__init__()
        self.motorista_dao = motorista_dao
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        print("\n=== Crie um Novo Motorista ===")
        nome = input("Digite o nome do motorista: ")
        nota = int(input("Digite a nota do motorista: "))

        corridas = []
        while True:
            print("\nAdicionando uma nova Corrida...")
            nota_corrida = int(input("Digite a avaliação da corrida: "))
            distancia = float(input("Digite a distancia da corrida: "))
            valor = float(input("Digite o valor cobrado na corrida: "))

            nome_passageiro = input("Digite o nome do passageiro: ")
            documento_passageiro = input("Digite o documento do passageiro: ")
            passageiro = Passageiro(nome_passageiro, documento_passageiro)

            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            corridas.append(corrida)

            continuar = input("Você gostaria de adicionar uma nova Corrida? (sim/nao): ").lower()
            if continuar != "sim":
                break

        motorista = Motorista(nome, nota, corridas)
        motorista_id = self.motorista_dao.criar_motorista(motorista)
        print(f"Motorista criado com o ID: {motorista_id}")

    def read_motorista(self):
        print("\n=== Dados do Motorista ===")
        nome = input("Digite o nome do motorista: ")
        motorista = self.motorista_dao.ler_motorista(nome)
        if motorista:
            print(f"Motorista encontrado: {motorista}")
        else:
            print("Motorista nao encontrado!")

    def update_motorista(self):
        print("\n=== Update um Motorista ===")
        nome = input("Digite o nome do motorista para dar update: ")
        nova_nota = int(input("Digite a nova avaliação para o motorista: "))
        result = self.motorista_dao.atualizar_motorista(nome, nova_nota)
        if result > 0:
            print("Motorista atualizado com sucesso!")
        else:
            print("Motorista não encontrado ou não realizou o update!")

    def delete_motorista(self):
        print("\n=== Delete um Motorista ===")
        nome = input("Digite o nome de um motorista para deletar: ")
        result = self.motorista_dao.deletar_motorista(nome)
        if result > 0:
            print("Motorista deletado com sucesso!")
        else:
            print("Motorista não encontrado!")

    def run(self):
        print("Bem vindo ao Motorista CLI!")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()