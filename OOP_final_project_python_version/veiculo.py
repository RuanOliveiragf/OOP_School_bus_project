class Veiculo:
    __total_veiculos = 0

    def __init__(self, placa, ano, modelo, capacidade, tipo, num_contrato=None):
        self.__placa = placa
        self.__ano = ano
        self.__modelo = modelo
        self.__capacidade = capacidade
        self.__tipo = tipo
        self.__num_contrato = num_contrato
        Veiculo.__total_veiculos += 1
        self.__num_veiculo = Veiculo.__total_veiculos

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def num_contrato(self):
        return self.__num_contrato

    @num_contrato.setter
    def num_contrato(self, num_contrato):
        if self.tipo == 0:
            print("Método inválido")
            print("Não é possível colocar número de contrato porque o veículo é próprio.")
        else:
            self.__num_contrato = num_contrato

    @property
    def num_veiculo(self):
        return self.__num_veiculo

    def exige_contrato(self):
        if self.tipo == 1 and self.num_contrato is None:
            print("Insira o número do contrato.")
        else:
            self.num_contrato = self.num_contrato

    def verifica_veiculo(self):
        if self.tipo == 0:
            print("O veículo é próprio.")
        else:
            print("O veículo é alugado.")
