class PontoDeParada:
    _total_pontos = 0  # Atributo de classe para contar o total de pontos de parada

    def __init__(self, nome, latitude, longitude):
        self.__nome = nome
        self.__latitude = latitude
        self.__longitude = longitude
        self.__alunos = []  # Lista para armazenar os alunos associados ao ponto de parada
        PontoDeParada._total_pontos += 1
        self.__id = PontoDeParada._total_pontos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        self.__latitude = latitude

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude):
        self.__longitude = longitude

    @property
    def id(self):
        return self.__id

    @property
    def alunos(self):
        return self.__alunos

    @alunos.setter
    def alunos(self, alunos):
        self.__alunos = alunos

    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)

    @staticmethod
    def numero_pontos():
        return PontoDeParada._total_pontos

    def __str__(self):
        return f"ID: {self.__id}, Nome: {self.__nome}, Latitude: {self.__latitude}, Longitude: {self.__longitude}, Alunos: {self.__alunos}"
