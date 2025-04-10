class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

    def to_dict(self):
        return {
            "nome": self.nome,
            "documento": self.documento
        }
    
class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia 
        self.valor = valor
        self.passageiro = passageiro

    def to_dict(self):
        return {
            "nota": self.nota,
            "distancia": self.distancia,
            "valor": self.valor,
            "passageiro": self.passageiro.to_dict()
        }
    
class Motorista:
    def __init__(self, nome: str, nota: int, corridas: list[Corrida]):
        self.nome = nome
        self.nota = nota
        self.corridas = corridas 

    def to_dict(self):
        return {
            "nome": self.nome,
            "nota": self.nota,
            "corridas": [corrida.to_dict() for corrida in self.corridas]
        }