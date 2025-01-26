class Pessoa:
    def __init__(self, nome_oficial, cpf_cnpj, endereco, telefone):
        self._nome_oficial = nome_oficial
        self.__cpf_cnpj = cpf_cnpj
        self.__endereco = endereco  
        self.__telefone = telefone

    def apresentar_dados(self):
        print("Nome: " + self.nome_oficial)
        print("CPF/CNPJ: " + self.cpf_cnpj)
        print("Endereço: " + str(self.endereco))  # imprimir o endereço como uma string
        print("Telefone: " + self.telefone)

    def verificar_tipo(self):
        return "Pessoa"

    @property
    def nome_oficial(self):
        return self._nome_oficial

    @nome_oficial.setter
    def nome_oficial(self, nome_oficial):
        self._nome_oficial = nome_oficial

    @property
    def cpf_cnpj(self):
        return self.__cpf_cnpj

    @cpf_cnpj.setter
    def cpf_cnpj(self, cpf_cnpj):
        self.__cpf_cnpj = cpf_cnpj

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
