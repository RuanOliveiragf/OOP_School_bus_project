from pessoa import Pessoa
from endereco import Endereco

class PessoaFisica(Pessoa):
    def __init__(self, nome, mae, pai, naturalidade, data_nascimento, nome_oficial, cpf_cnpj, endereco, telefone):
        super().__init__(nome_oficial, cpf_cnpj, endereco, telefone)
        self.__nome = nome
        self.__mae = mae
        self.__pai = pai
        self.__naturalidade = naturalidade
        self.__data_nascimento = data_nascimento

    

    @property
    def nome_oficial(self):
        return super().nome_oficial

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def mae(self):
        return self.__mae

    @mae.setter
    def mae(self, mae):
        self.__mae = mae

    @property
    def pai(self):
        return self.__pai

    @pai.setter
    def pai(self, pai):
        self.__pai = pai

    @property
    def naturalidade(self):
        return self.__naturalidade

    @naturalidade.setter
    def naturalidade(self, naturalidade):
        self.__naturalidade = naturalidade

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def cpf(self):
        return super().cpf_cnpj

    def apresentar_dados_pessoa_fisica(self):
        print("==== Dados da Pessoa Física ====")
        print("Nome: " + self.nome_oficial)
        print("CPF: " + self.cpf_cnpj)
        print("Endereço: " + str(self.endereco))
        print("Telefone: " + self.telefone)
        print("Data de Nascimento: " + str(self.data_nascimento))
        print("Naturalidade: " + self.naturalidade)
        print("Nome da Mãe: " + self.mae)
        print("Nome do Pai: " + self.pai)
        print("=================================")
