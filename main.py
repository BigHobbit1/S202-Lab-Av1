from database import Database
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

def main():
    # Configuração do banco de dados
    print("Iniciando a conexão com o banco de dados...")
    db = Database("Avaliacao","Motoristas")
    motorista_dao = MotoristaDAO(db)

    # Inicializando o CLI
    motoristaCLI = MotoristaCLI(motorista_dao)
    print("Bem-vindo ao sistema de gerenciamento de motoristas!")
    print("Comandos disponíveis: create, read, update, delete, quit")
    motoristaCLI.run()

if __name__ == "__main__":
    main()