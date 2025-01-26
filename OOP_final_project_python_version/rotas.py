class Rota:
    __total_rotas = 0

    def __init__(self):
        self.__pontos = []
        Rota.__total_rotas += 1
        self.__id = Rota.__total_rotas

    def adiciona_ponto(self, ponto):
        self.__pontos.append(ponto)

    def calcula_demanda(self):
        demanda = 0
        for ponto in self.__pontos:
            demanda += len(ponto.alunos)
        return demanda

    @staticmethod
    def numero_rotas():
        return Rota.__total_rotas

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def mostrar_dados(self):
        print(f"ID da Rota: {self.id}")
        print("Pontos de Parada:")
        for ponto in self.pontos:
            print(f"  Nome: {ponto.nome}, Latitude: {ponto.latitude}, Longitude: {ponto.longitude}")
            print(f"  Alunos no Ponto: {len(ponto.alunos)}")
            print("-------------------------------------------")    
