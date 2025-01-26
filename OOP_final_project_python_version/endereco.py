class Endereco:
    def __init__(self, rua, numero, complemento, bairro):
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro

    def __str__(self):
        return f"{self.__rua}, {self.__numero} - {self.__complemento} - {self.__bairro}"

    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

