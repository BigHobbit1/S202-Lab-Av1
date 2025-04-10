import pymongo

class Database:
    def __init__(self, database: str, collection: str):
        self.connection_string = "mongodb://localhost:27017"
        self.db = None
        self.collection = None
        self.connect(database, collection)

    def connect(self, database: str, collection: str):
        try:
            self.cluster_connection = pymongo.MongoClient(
                self.connection_string, tlsAllowInvalidCertificates=True
            )
            self.db = self.cluster_connection[database]
            self.collection = self.db[collection]
            print("✅ Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao conectar: {e}")

    def reset_database(self, dataset: list):
        """
        Reseta a coleção atual do banco de dados, removendo todos os documentos e populando com o dataset fornecido.

        :param dataset: Lista de documentos (dicionários) para inserir na coleção após o reset.
        """
        try:
            # Remove todos os documentos da coleção atual
            self.collection.drop()

            # Insere o novo dataset
            if dataset:
                self.collection.insert_many(dataset)
                print("Novo dataset inserido com sucesso!")
            else:
                print("Nenhum dado para inserir na coleção.")

        except Exception as e:
            print(f"❌ Erro ao resetar o banco de dados: {e}")