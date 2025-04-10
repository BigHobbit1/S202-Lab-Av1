from database import Database
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

print("Iniciando a conexão com o banco de dados...")
db = Database("Avaliacao","Motoristas")
motorista_dao = MotoristaDAO(db)
  
motoristaCLI = MotoristaCLI(motorista_dao)
print("Bem-vindo ao sistema de gerenciamento de motoristas!")
print("Comandos disponíveis: create, read, update, delete, quit")
motoristaCLI.run()
