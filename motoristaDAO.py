from database import Database
from motorista import Motorista

class MotoristaDAO:
    def __init__(self, database):
        self.database = database

    def criar_motorista(self, motorista: Motorista):
        motorista_dict = motorista.to_dict()
        resultado = self.database.collection.insert_one(motorista_dict)
        return resultado.inserted_id

    def ler_motorista(self, nome: str):
        motorista = self.database.collection.find_one({"nome": nome})
        return motorista

    def atualizar_motorista(self, nome: str, nova_nota: int):
        resultado = self.database.collection.update_one(
            {"nome": nome},
            {"$set": {"nota": nova_nota}}
        )
        return resultado.modified_count

    def deletar_motorista(self, nome: str):
        resultado = self.database.collection.delete_one({"nome": nome})
        return resultado.deleted_count